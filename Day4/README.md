# Day 4
## Info - AAP Default Execution Environment
<pre>
registry.redhat.io/ansible-automation-platform-2/ee-supported-rhel8:latest    
</pre>    

## Info - Ansible Automation Platform - Control Node Overview
<pre>
- The system that runs the automation playbooks.
- It has Ansible Core installed.
- It connects to managed nodes (hosts) via SSH or other protocols (e.g., WinRM).
- It uses Execution Environments (containers) to run automation jobs.
- Starting from AAP 2.x, the Automation Controller (formerly known as Tower) delegates 
    execution to Execution Nodes, but it is still considered a Control Node 
    because it manages the automation workflows.  
- Receives API/UI requests
- Queues and schedules automation jobs
- Delegates execution to Execution Nodes
- Maintains inventory, projects, credentials, job templates
- Collects job results and logs.
- Communicates with the database and Redis (for async tasks)
</pre>

## Info - Ansible Automation Platform - Execution Node Overview
<pre>
- Execution Nodes are specialized nodes designed only to run automation jobs 
- They provide scalable and isolated execution environments
- especially useful in large or distributed deployments  
- Executes automation jobs delegated from the Control Node (Automation Controller).
- Runs jobs in containerized Execution Environments (EEs).
- Does not manage inventory, credentials, or job templates—those reside on the Control Node
- Is designed to scale out automation horizontally
</pre>

## Info - Ansible Automation Platofrm - Node Groups
<pre>
- Node Groups are logical groupings of nodes (control, execution, or hybrid) 
- used to control where jobs are executed
- provide a flexible and scalable way to assign specific workloads or 
  inventories to designated parts of your infrastructure
- A named collection of one or more AAP nodes (usually execution nodes)
- Used by job templates, inventories, or organizations to route jobs to specific sets of nodes.
- A key feature in multi-node AAP deployments
- Node groups do not manage load balancing
- AAP automatically selects an available node within the group
- Jobs won't run if no healthy node exists in the assigned group
- You can assign default node groups per org or inventory for better management
- What is the benefit?
  - Job Segmentation
  - Location Awareness
  - Tenant Isolation
  - Scalability & Load Distribution
</pre>

## Demo - Installed ansible-builder & ansible-runner
```
sudo apt install -y python3-pip python3-ansible-runner
pip install ansible-runner
pip install ansible-builder --break-system-packages
pip3 install ansible-dev-tools
pip3 install https://github.com/ansible/ansible-builder/archive/devel.zip

ansible-runner --version
ansible-builder --version
```
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8a9fad37-b499-4d76-827a-021974877cf1" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/55ed26af-bc31-4793-87ae-6b6c968dff4b" />

## Lab - Build your custom Ansible Automation Platform Execution Environment
```
cd ~/advanced-ansible-july2025
git pull
cd Day4/my-app-execution-env
tree

ansible-builder create

podman build -f context/Containerfile -t jegan-aap-ee:latest context
podman run -it jegan-aap-ee:latest bash
ansible-runner run . -p myplaybook.yml --container-image jegan-aap-ee:latest
podman tag jegan-aap-ee:latest docker.io/tektutor/jegan-aap-ee:latest
podman login docker.io
podman push docker.io/tektutor/jegan-aap-ee:latest
```
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/900a1c54-09b8-49bc-abd0-03ef2ff577c5" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/bcd14bee-b56b-4ae4-8202-27a9b6879693" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/3ee6d9a3-c641-4af6-b309-0fa0d0744fdd" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8c548eaa-e70d-4ce1-8c9a-3b32f3ca2256" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/062939bc-0953-4427-af6d-c568ce53a86a" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/c6e46284-d5d8-4c42-97ac-623aad35ba9d" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/4905d9ab-c08b-4339-89f0-43661867e5ee" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/c8aac32c-7f61-499d-af09-65509265463d" />

## Lab - Running your playbook with your custom AAP Execution Environment Image locally
```
cd ~/advanced-ansible-july2025
git pull
cd Day4/my-app-execution-env
tree

ansible-runner run . -p ping-playbook.yml --container-image tektutor/jegan-app-ee:1.0
```

Expected output
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/0f633327-ecdc-42b6-aedf-612c8c253ca6" />

## Lab - Running your playbook with your custom AAP Execution Environment Image using Podman
```
podman run -it --rm \
  -v $PWD:/runner:Z \
  tektutor/jegan-app-ee:1.0 \
  ansible-playbook ping-playbook.yml
```

Expected output
<img width="1942" height="717" alt="image" src="https://github.com/user-attachments/assets/064bb229-80a1-4b79-b0e4-39c7db057012" />
<img width="1942" height="997" alt="image" src="https://github.com/user-attachments/assets/2fa65468-85ce-4c8f-ac87-12693be057c2" />

## Lab - Using Custom AAP EE Image in Ansible Automation Platform running within Openshift

Login to Openshift from CLI
```
oc login --token=... --server=https://api.cluster.local:6443
```

Tag your image form Openshift internal registry
```
# Get the internal image registry route (for OpenShift 4.x+)
REGISTRY=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')

# Tag your image to match the OpenShift internal registry path
podman tag tektutor/jegan-aap-ee:1.0 $REGISTRY/aap/jegan-aap-ee:1.0
```

Login to Openshift internal registry using Podman
```
podman login -u $(oc whoami) -p $(oc whoami -t) $REGISTRY
```

Push the image into Openshift Internal image registry
```
podman push $REGISTRY/aap/jegan-aap-ee:1.0
```

Grant image pull permission
```
oc policy add-role-to-user system:image-puller \
  system:serviceaccount:aap:default \
  --namespace=aap
```

Open the AAP webconsole, Navigate to Templates --> Add --> Job Template --> 
Set the below
<pre>
Inventory

Project
    
Playbook
    
Execution Environment: Select Jegan AAP EE    
</pre>
