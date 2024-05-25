from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.cloud import storage
import json
import os
from datetime import datetime

# Configuration settings
GCP_PROJECT_ID = "project-k-420718"
PUBSUB_SUBSCRIPTION_ID = "data-sub"
LISTEN_TIMEOUT = 300.0  # Time in seconds for the subscriber to listen for messages
GCS_BUCKET_NAME = "vehicle-records"  # Replace with your bucket name

# Set up Google Cloud credentials
CREDENTIALS_PATH = '/home/kchava/.config/gcloud/application_default_credentials.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH

# Initialize the Google Cloud Pub/Sub client
pubsub_client = pubsub_v1.SubscriberClient()
subscription_path = pubsub_client.subscription_path(GCP_PROJECT_ID, PUBSUB_SUBSCRIPTION_ID)

# Initialize the Google Cloud Storage client
gcs_client = storage.Client()
gcs_bucket = gcs_client.bucket(GCS_BUCKET_NAME)

# List to hold all messages
accumulated_messages = []
# Counter for the total number of messages received
message_counter = 0

def upload_messages_to_gcs(messages):
    """Upload accumulated messages to a Google Cloud Storage bucket as a single JSON file."""
    if messages:
        blob = gcs_bucket.blob("vehicle_messages.json")
        blob.upload_from_string(json.dumps(messages, indent=4))
        print(f"Successfully uploaded {len(messages)} messages to {blob.name}")
        messages.clear()

def process_message(message: pubsub_v1.subscriber.message.Message) -> None:
    """Process and accumulate incoming Pub/Sub messages."""
    global message_counter

    # Parse the JSON data in the 'data' field
    message_content = json.loads(message.data.decode('utf-8'))

    formatted_message = {
        "message_id": message.message_id,
        "data": message_content,
    }

    # Add the formatted message to the list
    accumulated_messages.append(formatted_message)
    message_counter += 1  # Increment the message count
    print(f"Received and stored message with ID: {message.message_id}")
    message.ack()

def listen_for_pubsub_messages():
    """Listen for messages on the specified Pub/Sub subscription."""
    streaming_pull_future = pubsub_client.subscribe(subscription_path, callback=process_message)
    print(f"Started listening for messages on {subscription_path}...")

    with pubsub_client:
        try:
            streaming_pull_future.result(timeout=LISTEN_TIMEOUT)
        except TimeoutError:
            print("Listening period has ended due to timeout.")
        finally:
            if accumulated_messages:  # Ensure any remaining messages are uploaded
                upload_messages_to_gcs(accumulated_messages)
            print(f"Total number of messages received and processed: {message_counter}")

if __name__ == "__main__":
    listen_for_pubsub_messages()
