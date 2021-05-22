k8s installation on multi-node cluster
------

Ref: https://phoenixnap.com/kb/install-kubernetes-on-ubuntu

# Install packages
```
sudo apt-get update
sudo apt-get install docker.io
docker -v
sudo systemctl enable docker
sudo systemctl status docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt-get install kubeadm kubelet kubectl
sudo apt-mark hold kubeadm kubelet kubectl
kubeadm version
```

# Disable swap
```
# sudo swapoff –a
sudo vi /etc/fstab # Comment out swap & restart
```

# Create master
```
# sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Note down the join section
sudo kubeadm init --apiserver-advertise-address="192.168.50.10" --apiserver-cert-extra-sans="192.168.50.10"  --node-name k8s-master --pod-network-cidr=192.168.0.0/16

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl get pods --all-namespaces
```

# Join worker nodes
```
kubeadm join 192.168.50.10:6443 --token 6pa62p.mtme5awdrxotq1lw \
        --discovery-token-ca-cert-hash sha256:5ac372bfef0b6d65f8de383c426dc1568e0d7b0a54bbcfd2099c01e0299cafdf
```
# Check if nodes are available in master
```
kubectl get nodes
```
