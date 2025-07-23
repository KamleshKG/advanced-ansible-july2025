# Day 4

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
- What is the benefit?
  - Job Segmentation
  - Location Awareness
  - Tenant Isolation
  - Scalability & Load Distribution
</pre>
