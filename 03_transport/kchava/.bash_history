gcloud services enable pubsub.googleapis.com
gcloud auth application-default login
gcloud projects add-iam-policy-binding PROJECT_ID --member="user:EMAIL_ADDRESS" --role=ROLE
gcloud projects add-iam-policy-binding project-k-420718 --member="user:kchava@pdx.edu" --role=roles/pubsub.admin
pip install --upgrade google-cloud-pubsub
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-sub --topic my-topic
from google.cloud import pubsub_v1
# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"
publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)
for n in range(1, 10):
print(f"Published messages to {topic_path}.")
sudo apt-get update
sudo apt-get install python3
python3 --version
nano kkc1.py
ls
python3 kkc1.py
ls
nano bcsample.json
nano kkc_pub.py
python3 kkc_pub.py
nano kkc_pub.py
python3 kkc_pub.py
nano kkc_sub.py
python3 kkc_sub.py 
nano kkc_sub.py
python3 kkc_sub.py 
nano kkc_sub.py
python3 kkc_sub.py 
nano kkc_pub.py
python3 kkc_sub.py 
nano kkc_sub.py
pythond3 kkc_sub.py
python3 kkc_sub.py
nano kkc_pub.py
python3 kkc_pub.py
nano kkc_pub.py
python3 kkc_pub.py
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
kchava@cloudshell:~ (project-k-420718)$ nano kkc_pub.py                                                                                                    
kchava@cloudshell:~ (project-k-420718)$ python3 kkc_sub.py 
Listening for messages on projects/project-k-420718/subscriptions/my-sub..
KeyboardInterrupt
kchava@cloudshell:~ (project-k-420718)$ nano kkc_sub.py                                                                                                    
kchava@cloudshell:~ (project-k-420718)$ pythond3 kkc_sub.py                                                                                                
-bash: pythond3: command not found
kchava@cloudshell:~ (project-k-420718)$ python3 kkc_sub.py                                                                                                 
Listening for messages on projects/project-k-420718/subscriptions/my-sub..
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
}.
Received Message {
nano kkc1_pub.py
nano kkc_pub.py
python3 kkc_pub.py
nano kkc_sub.py
python3 kkc_sub.py
python3 kkc_pub.py
python3 kkc_sub.py
python3 kkc_pub.py
nano kkc_sub.py
nano topic_clean.py
python3 kkc_pub.py
python3 kkc_sub.py
nano kkc_sub.py
python3 kkc_sub.py
