# Install python client library
pip install --upgrade google-cloud-vision 

# Download Google Cloud SDK
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-147.0.0-linux-x86_64.tar.gz 

# Uncompress it: 
tar -xvf google-cloud-sdk-147.0.0-linux-x86_64.tar.gz 

# Install the SDK
./google-cloud-sdk/install.sh

# Check version and update
gcloud version
gcloud components update

# Initialize the SDK, log in and select project 
gcloud init
gcloud auth application-default login 





