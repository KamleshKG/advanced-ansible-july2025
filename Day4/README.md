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
pip install ansible-runner
pip install ansible-builder

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
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/90c570ad-649b-416e-ab13-b1f392c3c256" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/3ee6d9a3-c641-4af6-b309-0fa0d0744fdd" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8c548eaa-e70d-4ce1-8c9a-3b32f3ca2256" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/062939bc-0953-4427-af6d-c568ce53a86a" />
