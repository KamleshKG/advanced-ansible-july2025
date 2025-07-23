# Day 2

## Demo - Installing ansible core in Ubuntu
````
wget -O- "https://keyserver.ubuntu.com/pks/lookup?fingerprint=on&op=get&search=0x6125E2A8C77F2818FB7BD15B93C4A3FD7BB9C367" | sudo gpg --dearmour -o /usr/share/keyrings/ansible-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/ansible-archive-keyring.gpg] http://ppa.launchpad.net/ansible/ansible/ubuntu $UBUNTU_CODENAME main" | sudo tee /etc/apt/sources.list.d/ansible.list

sudo apt update && sudo apt install ansible
````

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

## Info - Ansible High Level Architecture
![ansible](AnsibleHighLevelArchitecture.png)

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
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/7099e555-10b5-4044-92b2-6f625d78df47" />

## Lab - Building Custom Rocky Ansible Node container image

```
cd ~\advanced-ansible-july2025
git pull
cd Day2/custom-container-images/rocky
cat Dockerfile
cp ~/.ssh/id_ed25519.pub authorized_keys
podman build -t tektutor/rocky-ansible-node:1.0 .
podman images | grep rocky-ansible
```

Expected output
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/b265e1ef-f203-43a8-82c0-92f06302f961" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/397f232d-8e07-4b5e-8c5a-557771275d64" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/35cc2158-4247-4225-94ae-34ba9963375c" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/1c23d89e-d9c8-49e0-89e9-f468ba80c882" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/09e92a11-4e66-4ea6-8a4e-c8ddc1210429" />

## Lab - Creating ubuntu ansible node containers and testing it
Let's list the custom images
```
podman images
```

Let's create couple of ubuntu ansible node containers
```
podman run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ubuntu-ansible-node:1.0
podman run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ubuntu-ansible-node:1.0
```

List and check if ubuntu1 and ubuntu2 ansible node containers are running
```
podman ps
```

SSH into ubuntu1 and ubuntu2 containers and check if it is allowing you to login without prompting for password
```
ssh -p 2001 root@localhost
exit
ssh -p 2002 root@localhost
exit
```
Expected output
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/19bc6899-c5f7-4959-bd78-0797a4d914f7" />
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/1a1353c5-9d98-4417-98b6-d031960763cc" />

## Lab - Ansible ping ad-hoc command
```
cd ~/advanced-ansible-july2025
git pull
cd Day2/ansible
ansible -i inventory all -m ping
ansible -i inventory ubuntu1 -m setup
ansible -i inventory all -m shell -a "hostname -i"
```

## Lab - Writing a simple ansible playbook
```
cd ~/advanced-ansible-july2025
git pull
cd Day2/ansible/playbooks
ansible-playbook -i ../inventory ping-playbook.yml 
```
<img width="1891" height="1057" alt="image" src="https://github.com/user-attachments/assets/35063515-2e92-4751-982f-143ad0db10e9" />


## Lab - Running the install nginx playbook

```
cd ~/advanced-ansible-july2025
git pull
cd Day2/ansible/playbooks
ansible-playbook -i ../inventory install-nginx-playbook.yml 
```

If all goes well, you may test it as shown
```
podman ps | grep tektutor
curl http://localhost:<your-container1-port>
curl http://localhost:<your-container2-port>
```

Expected output
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/dc337c26-69f1-40b7-8416-f8af18a58e5d" />

## Lab - Conditional installation in ansible playbook
Let's create couple of rocky ansible node containers
```
# List our custom images
podman images | grep tektutor

# Create two rocky ansible node containers using our custom podman image
podman run -d --name rocky1 --hostname rocky1 -p 2003:22 -p 8003:80 tektutor/rocky-ansible-node:1.0
podman run -d --name rocky2 --hostname rocky2 -p 2004:22 -p 8004:80 tektutor/rocky-ansible-node:1.0

## List all the running containers
podman ps
```

Let's test if SSH works in rocky1 and rocky2
```
ssh -p 2003 root@localhost
exit
ssh -p 2004 root@localhost
exit
```

<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2fffb6d0-1454-4f86-b676-a32b1aa01711" />

We need to add the rocky container details in our inventory, the updated inventory should look as shown below
<pre>
[all]
ubuntu1 ansible_port=2001
ubuntu2 ansible_port=2002
rocky1  ansible_port=2003
rocky2  ansible_port=2004

[all:vars]
ansible_user=root
ansible_host=localhost
ansible_private_key_file=~/.ssh/id_ed25519  
</pre>
<img width="1242" height="439" alt="image" src="https://github.com/user-attachments/assets/23f7f3bc-ed62-4dc4-8e19-66701d2bfb9f" />

Check if you are able to ping all nodes
```
ansible all -m ping
```

<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/be780851-c46e-405d-bae4-278ac0756ec2" />

Now run the install-nginx-playbook.yml and observe the output
```
cat ansible.cfg
ansible-playbook install-nginx-playbook.yml
```
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/d60c9f99-2424-4984-81b1-ce69d909fcfb" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/13c93b8e-f784-4da0-ae5d-5331d0941acc" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/efed7c30-5a32-4d25-954c-c22528f9adc4" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/38b7721f-33ec-4c2a-b40e-584207cb93d7" />

## Lab - Running the refactored playbook
```
cd ~/advanced-ansible-july2025
git pull
cd Day2/ansible/playbooks/refactored
ansible-playbook install-nginx-playbook.yml 
```

<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/36d3b0c5-68c9-457f-8fca-c2b22a530059" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/1ddfb127-3399-43b1-aedf-ac091f83dfaf" />
