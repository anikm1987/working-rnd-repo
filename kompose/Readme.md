# Kompose - reference (https://github.com/kubernetes/kompose)
#### kompose is a tool to help users who are familiar with docker-compose move to Kubernetes.
- Tested with rundeck docker compose file 
- Command 
  - kompose convert -f docker-compose.yaml

##### Installation -
- Linux
curl -L https://github.com/kubernetes/kompose/releases/download/v1.21.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose