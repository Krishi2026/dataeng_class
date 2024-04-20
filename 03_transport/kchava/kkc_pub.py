import json
from google.cloud import pubsub_v1

# Function to publish messages to Pub/Sub
def publish_messages(project_id, topic_name, filename):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    with open(filename, 'r') as f:
        messages = json.load(f)

    # Initialize the count
    published_count = 0

    for message in messages:
        data = json.dumps(message).encode('utf-8')
        future = publisher.publish(topic_path, data=data)
        future.result()  # Wait for message to be published
        published_count += 1  # Increment the count after successful publish

    # Print the total count of published messages
    print(f"Total messages published: {published_count}")

if __name__ == "__main__":
    project_id = "project-k-420718"
    topic_name = "my-topic"
    filename = "bcsample.json"
    publish_messages(project_id, topic_name, filename)
