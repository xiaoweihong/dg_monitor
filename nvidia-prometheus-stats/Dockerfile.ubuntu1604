
FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y wget git python python-pip python3-dev python-dev
RUN git clone https://github.com/BonsaiAI/nvidia-prometheus-stats
WORKDIR nvidia-prometheus-stats
RUN pip install nvidia-ml-py pyinstaller prometheus_client
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
RUN dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
RUN apt-get update -y
RUN apt-get install -y cuda
RUN pyinstaller nvidia-prometheus-stats.py 
