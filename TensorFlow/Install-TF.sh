# Install python pip and TF virtualenv
sudo apt-get install python-pip python-dev python-virtualenv 

# Create TF virtualenv in TF folder
virtualenv --system-site-packages TF 

# Activate the virtual env. 
source ~/TF/bin/activate 
# (use command deactivate to deactivate the env.)

# Install TensorFlow in this virtualenv
pip install --upgrade tensorflow 


