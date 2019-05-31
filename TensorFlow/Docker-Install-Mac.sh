# Install Docker CE for MacOS
# https://hub.docker.com/editions/community/docker-ce-desktop-mac 

docker pull tensorflow/tensorflow 

docker run -it -p 8888:8888 tensorflow/tensorflow  # Start a Jupyter notebook server

