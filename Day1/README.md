# Day 1

## Info - Installing Podman in Ubuntu
```
sudo apt update
sudo apt-get -y install podman
```

## Lab - Check if podman is installed in your lab machine
```
podman --version
podman images
```

## Info - Container Engine
<pre>
- it is a high-level software that manages container images and containers
- highly user-friendly, abstracts lots of complex internal implementation details nicely,while providing user-friendly commands
- internally Container Engines depends on Container Runtime
- examples
  - Docker
    - internally depends on containerd, which in turn depends on runC Container Runtime
  - Podman
    - internally depends on CRI-O Container Runtime
</pre>

## Info - Container Runtime
<pre>
- is a low-level software that manages container images and containers
- not so user-friendly, hence no end-users normally uses this directly
- examples
  - CRI-O Container Runtime
  - runC Container Runtime
</pre>

## Info - Container Images
<pre>
- Container Images are similar to Operating System ISO files we download from microsoft, ubuntu, etc.,
- technically it is possible to have more than one applicaiton per Container Image, but that is the best practice
- as per industry best practices, only one application per container is allowed
- is a blueprint of a running container
- all the necessary softwares can be installed while creating a image
- using container image, we can create containers
- every container image has an unique ID and name
- it is broken down into many image layers
- one container image may refer one or more image layers
- each image layer has an unique ID
- the image layers can be shared by container images
</pre>

## Info - Containers
<pre>
- is running instance of a Container Image
- one application along with it all its dependencies
- it is an application process that runs in its own namespace
- Linux kernels supports 2 features which enables the container technology
  - Namespace
    - is used to isolate one container from the other
  - Control Groups ( CGroups )
- it gets 
  - it own IP Address
  - it own Filesystem 
  - network namespace
    - network stack
    - software defined network card ( NIC )
  - its own port range ( 0 - 65535 )
</pre>

## Docker Overview
<pre>
- is developed in Golang by a company called Docker Inc
- it follows client-server Architecture
  - client tool (docker)
  - server tool (dockerd - which runs a service)
- docker images are stored in local registry folder /var/lib/docker
- if any one user has downloaded a particular image, it is stored in the /var/lib/docker folder
- when other users attempt to list the images, they will see all the images under /var/lib/docker
- the containers created by one user will be visible to other users in the same linux machine
</pre>

## Podman Overview
<pre>
- is an open source product 
- primarily maintained by Red Hat
- it creates root-less containers ( meaning no admin/root user created within container images )
- Red Hat acquired a company called CoreOS
- The organization CoreOS had 2 interesting products
  1. CoreOS - Operating System optimized & Secured for Container Orchestration Platforms like Kubernetes/Openshift
  2. Container Runtime called rkt(pronounced as rocket)
- Red Hat developed Podman Container Engine and CRI-O Container Runtime
- The ideas from rkt were in created CRI-O
- Starting from Red Hat Openshift 4.x, Openshift stopped support for Docker, they moved to Podman instead
- Podman stores container images for every user (isolated by users)
- Podman containers created by one user is not visible to other users (isolated by users)
</pre>

## Pod Overview
<pre>
- a logical group of many containers is called a Pod
- all the containers that belongs to a single Pod, they get the same IP address
- all the containers that belongs to a single Pod, they get to share the same Port Range ( 0 - 655535 )
</pre>

## Lab - Creating a container in Podman
For downloading nginx image
```
podman pull docker.io/library/nginx:latest
```

To create and run a container
```
podman run -d --name nginx --hostname nginx docker.io/library/nginx:latest
```

To list the running containers
```
podman ps
```

## Lab - Podman image listing
Podman images is the default 
<pre>
podman images
</pre>

List podman images with just the image ids
```
podman image ls --quiet
```

List all images without the heading
```
podman images --noheading
```

List all images with full image id
```
podman image list --no-tunc
```

Finding more details about a container image
```
podman image inspect <name of the container image>
podman image inspect docker.io/library/nginx:latest
```

## Lab - Create a container
```
podman run registry.fedoraproject.org/fedora:latest echo hello
```

Listing the running containers, you are not supposed to see the 
```
podman ps
```

If you wish to see all containers even the ones which isn't running
```
podman ps -a
```

## Lab - Getting inside a running container shell
```
# Type this on your lab machine i.e ubuntu terminal
podman ps
podman exec -it nginx /bin/sh

# Type thes commands inside the container shell
ls
hostname
hostname -i

# To come out of the container shell
exit
```
