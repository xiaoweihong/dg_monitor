# nvidia-prometheus-stats

Want to scrape Memory & GPU utilization metrics using NVML & exposes them to Prometheus through a simple HTTP server and/or a push gateway- All in a Docker container???? Then you have come to the right place.

# Pre-requisite

- Install NVIDIA-DOCKER
- A System with GPGPU Card.

<h1>Detail Steps:</h1>

# Building up Prometheus Container:

Execute the script `start.sh` as shown below:

```
sh start_containers.sh
```

The above command will start pushgateway, prometheus & Grafana in sequence

## Pushing the GPU metrics to Prometheus

```
python gpu_metrics_exporter.py
```


