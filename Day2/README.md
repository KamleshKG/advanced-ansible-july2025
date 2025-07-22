# Day 2

## Info - Configuration Management Tools Overview
<pre>
- Configuration Management Tools helps us automate system administrative activities
- it is one of the DevOps tools
- With Configuration Management Tools
  - given a machine with some OS pre-installed
  - we can remotely using these tools to further install/uninstall,configure, update/upgrade softwares, manage users, manage networks etc on that machine 
- examples
  - Puppet ( oldest - developed and maintained by Perforce )
  - Chef
  - Salt/Saltstack
  - Ansible
</pre>

## Info - Ansible Overview
<pre>
- ansible is developed by Michael Deehan 
- Michael Deehan started a company called Ansible Inc
- ansible can only be installed in Linux distros, no Windows
- the machine where Ansible is installed is called Ansible Controller Machine(ACM)
- the machines/servers that ansible is going to manage are called Ansible Nodes
- Ansible Nodes
  - are containers or servers, could be physical server or virtual machine, or ec2 instances running in public cloud
  - it could be Server with Linux or Unix or Windows or Mac OS-X, Router, Switch, etc.,
  - Unix/Linux/Mac
    - required softwares
      1. SSH Server should be there
      2. Python should be there
  - Windows
    1. WinRM should be there
    2. Powershell should be supported
- ansible comes in 3 flavours
  1. Ansible Core - open source, CLI only
  2. AWX 
     - open source 
     - supports Webconsole GUI
     - developed on top of Ansible core
     - user management
     - supports many additional features on top of Ansible core
  3. Ansible Automation Platform 
    - formerly called Ansible Towers
    - developed on top of opensource AWX
    - all the features supported by AWX are supported in Ansible Tower or Ansible Automation Platform
    - you get support from Red Hat
- installing ansible is very easy
- Ansible Modules
  - are Python scripts in case the node happens to be an Unix/Linux/Mac OS
  - are Powershell scrips in case the node is a Windows machine
  - Ansible comes with many ansible modules
    - there is a module called copy to copy files from controller machine to node or vice versa
    - there is a windows called win_copy to copy files from controller machine to node or vice versa
    - file modules helps us create empty files, directories with specific permissions and owernship
    - apt module to install/uninstall/upgrade softwares in Debain(Ubuntu, Raspberry, Kali like OS )
    - yum module to install/uninstall/upgrade softwares in Red Hat Linux family (CentOS stream, Fedora, RHEL )
- Playbook (YAML File )
  - playbook invokes one or more ansible modules sequentially one after the other 
  - DSL is YAML
</pre>

## Lab - Clone this training repository
```
cd ~
git clone https://github.com/tektutor/advanced-ansible-july2025.git
cd advanced-ansible-july2025
```

## Lab - Building Custom Ubuntu Ansible Node container image
```
# Generate key-pair, accept all default by hitting enter whenever it prompts for something
cd ~
ssh-keygen

cd ~\advanced-ansible-july2025
git pull
cd Day2/custom-container-images/ubuntu
cat Dockerfile
cp ~/.ssh/id_ed25519.pub authorized_keys
podman build -t tektutor/ubuntu-ansible-node:1.0 .
podman images | grep ubuntu-ansible
```

Expected output
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/bb589c41-6e67-4005-b6a1-15b814c1a7b9" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/649a5053-2396-4fe7-9af0-7974ea047e27" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/d79ecfc8-f7cf-4ced-8e57-94902abf1928" />

