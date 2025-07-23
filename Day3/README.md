<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/3dbae23f-af87-4903-949a-2852feb3c756" /># Day 3

## Info - Ansible Automation Platform Overview
<pre>
- Red Hat’s enterprise solution for automating IT tasks across infrastructure, applications, networks, security, and cloud environments 
- built around Ansible, the popular open-source automation tool
- supports enterprise-grade features like:
  - A web UI (Automation Controller)
  - RBAC (Role-Based Access Control)
  - Logging & analytics
  - Execution environments
  - Certified content and collections
  - Integration with source control (Git), ticketing systems, and more    
</pre>

#### Automation Controller
<pre>
- Manages, schedules, and runs Ansible playbooks. UI + REST API (formerly AWX/Ansible Tower)   
</pre>

#### Execution Environments (EE)
<pre>
- Containerized environments where automation runs 
- All automation in Red Hat Ansible Automation Platform runs on container images called automation execution environments
- Execution environments are consistent and shareable container images that serve as Ansible control nodes 
- Execution environments reduce the challenge of sharing Ansible content that has external dependencies 
- execution environment makes it easy to replicate the developer’s environment, 
- thereby enabling you to reproduce and scale the automation content that the developer has written 
- In this way, execution environments make it easier for you to implement automation in a range of environments
</pre>

#### Automation Hub
<pre>
- Internal or Red Hat-hosted repository of certified and custom content (collections, roles, plugins)   
</pre>

#### Automation Analytics
<pre>
- Dashboard that shows usage, trends, job status, and recommendations. Hosted by Red Hat    
</pre>

#### Automation Mesh
<pre>
- Connects distributed execution nodes across data centers, clouds, and edge   
</pre>

#### Ansible Content Collections
<pre>
- Modular bundles of roles, playbooks, plugins, and docs. Used inside playbooks.   
 </pre>

#### RBAC & Credentials
<pre>
- Secure control over who can do what and access which systems   
</pre>

## Info - Ansible Automation Platform - High Level Architecture
![architecture](aap-architecture.png)

## Lab - Getting help about any ansible module
```
ansible-doc service
ansible-doc shell
ansible-doc apt
ansible-doc yum
ansible-doc template
ansible-doc file
ansible-doc command
```

## Lab - Finding total number of ansible modules supported by your ansible
```
ansible-doc -l | wc
```

## Lab - Finding the status of service
```
podman exec <your-container-name> service nginx status
ansible -i hosts -m shell -a "service nginx status"
```

## Lab - Creating a Project in Ansible Automation Platform (AAP)
Navigate to AAP Webconsole
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/60d0c6ec-0b5f-488f-9a03-66a06b4d7b83" />

Navigate to Automation Execution --> Projects
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/e7651f8a-f4f2-443a-8f7b-21457b404c84" />
Click "Create Project"
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/32168cb7-d3f5-4fd0-80f0-3b7e02cbeaf2" />
<pre>
Name - TekTutor Training Repository
Organization - Default
Execution environment - Default Execution environment
Source control type - Git
Source control url - https://github.com/tektutor/advanced-ansible-july2025.git
Source control branch/tag/commit - main
Options --> Update revision on launch(selected)
</pre>  
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/16745a9c-af17-4308-8d26-05f1ad16b52b" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/0184582b-fc89-48b1-b8b6-3342b50f890b" />
Click "Create Project"
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/4103e20d-bde2-4cff-9f40-8ea307c4f632" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/b5312420-d96a-4359-a1d1-b3cad51612ae" />
Click on "Success"
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/a6d28920-0fab-4e6e-b558-40ad8de2d7e1" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/04057f6c-1301-4308-9af7-9994b2d2bdb4" />
Click on "Projects" on the left side
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/db75cccd-644e-4e7e-b25b-aa0ea9ab3da4" />


## Lab - Creating Credentials in Ansible Automation Platform (AAP)
Navigate to AAP Webconsole
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/60d0c6ec-0b5f-488f-9a03-66a06b4d7b83" />

Navigate to Automation Execution --> Infrastructure --> Credentials
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/139d0c33-4474-4798-928c-c6ae88eff25c" />
Click "Create Credential"
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/7fd1a77f-8bd7-47ba-b085-084ec2b56f87" />
<pre>
Name - Jegan - Private key
Organization - Default
Credential type - Machine
SSH Private key - <From your lab machine terminal, cat ~/.ssh/id_ed25519 and copy/paste entire key including begin, end with hypens, etc>
</pre>
<img width="1122" height="341" alt="image" src="https://github.com/user-attachments/assets/b85c032b-93ae-43a5-b41e-cffe127c315d" />
<img width="1122" height="341" alt="image" src="https://github.com/user-attachments/assets/ad6f31ab-1c13-46d0-9a3a-7dea8212955b" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8414b13e-58fb-4e3e-a289-bbfb8ca02294" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b547bda6-ebf8-4a92-b663-b6be0d5dbcb2" />
Click "Create Credential"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/6f5fdc92-890e-457c-bf3f-f2ad1b03c26d" />
Click "Credentials" on the left side menu
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/d049bcbc-5652-462a-bc20-3c16f73a2c2e" />

## Lab - Create Inventroy with 4 hosts in AAP
Check if your ansible node containers ubuntu1, ubuntu2, rocky1 and rocky2 are running
```
podman ps
```
<img width="1686" height="241" alt="image" src="https://github.com/user-attachments/assets/1c07c869-97d6-4fee-9677-93f238ff958b" />

We need to create an inventory first, navigate to Automation Execution --> Infrastructure --> Inventories
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/d0c7952d-d3d9-4659-8e18-4525b089f350" />

Click "Create Inventory"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/ecae90b2-4ee4-4f42-a7d2-eb7056e24bbb" />
Select the first option "Create Inventory"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/795f88bf-f0d9-40a3-a2db-8d4c0690855c" />
<pre>
Name - Jegan - Docker Inventory
Organization - Default
</pre>
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/680ecb9e-f44e-42f2-8b16-d52193349694" />
Click "Create Inventory"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2b8e42f8-1390-47ed-aa0e-892aca3535aa" />

Within the inventory you created, locate the Hosts Tab and click it
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/0d2865ac-9f14-4c90-8616-bd86b68394f0" />
Click "Create Host"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/271c8f10-d5bf-4283-86bd-faa29b41e7a5" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/01108432-4036-4d18-9f8e-0151eb82102d" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/f5f9661a-05f4-4043-967d-4880189336fc" />
You need to find the port you published on your ubuntu lab server which is set to forward traffic to port 22 on your ubuntu1 container. Also make sure you give either 192.168.10.200 or 192.168.10.201 depending on which server you have working on in the training environment.
<pre>
ansible_port: 2001
ansible_user: root
ansible_host: 192.168.1.104
host_key_checking: false
</pre>
Click "Create host"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/5bea833d-2dc7-4aab-9d2c-78a374c52957" />
Go back to Hosts tab within your Inventory
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/0c04094a-6439-44b3-8f52-428b4532f0d6" />
Repeat this procedure and add Ubuntu1, Rocky1 and Rocky2 Hosts
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/c66746a3-6f0d-4a28-8f95-d3b696dead97" />

Let's test if Ansible Automation Platform is able to ping the hosts we added in our inventory.
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/f410a08c-52d8-437f-9856-1616d5060cce" />
Click "Run command"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/522c41e4-5f5e-4284-8d8a-55bdaf2212a9" />
<pre>
Module - ping
</pre>
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/146380c9-3c78-47a9-b0d6-0f7664e268ab" />
Select Execution environment - Default execution environment
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/29a78305-a4e4-4554-83fe-6aa58c53f826" />
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8288cb97-b2e0-4d4b-8d5b-fe73beb6f4b8" />
Select your Private key
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/56dfbe9a-8b3c-4948-835e-42e1ff2cb987" />
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/24dc49ea-7bcb-4d7f-bd40-63694c0a9ad0" />
Click "Finish"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b11a4d65-544a-4d56-870a-86583a12e106" />

## Lab - Creating a Job Template to run a playbook from AAP
Navigate to Automation Execution --> Templates
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/bd52aa47-b145-44c1-a8a2-e592d7c72aea" />
Click "Create template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/4b2faeef-b7c0-471a-804b-b1e6588a53f8" />
Select "Create job template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/420f4439-bd78-49eb-8d02-799092116ff0" />
<pre>
Name - Invoke Install Nginx Playbook
Job Type - Run
Inventory - Select the Inventory you created in AAP
Project - Select the Project you created in AAP
Playbook - Day2/ansible/playbooks/refactored/install-nginx-playbook.yml
Execution environment - Default execution environment
Credentials - Select the Private key you saved as Credentials in AAP
</pre>
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/9411fd81-30d1-40bb-a3ef-3763093140e3" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/442e44c4-8caf-4c88-981b-74cc043a4e4b" />
Click "Create job template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/50353f73-a853-43a9-9979-34ea72e1db58" />
Click "Launch template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/75778cca-bc22-4877-93c4-12d6defd16b3" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/4b000582-c0b8-4448-8584-f78ff4747673" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/0990ce29-aa0a-4ad4-8b35-f7f22867be4f" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/ef4d19bc-1bdd-4804-b7f4-2fc03558519c" />

Click on Automation Execution --> Jobs on the left side menu
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/aba5b6a8-b850-407e-aa39-36d7a4f5c113" />

## Lab - Creating Ansible workflow
Navigate to Automation Execution --> Templates
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/85be4d01-f81f-417a-821a-ef2240d4e53d" />
Click "Create template" button
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/7bb592a6-5622-41a6-84b1-0b94c5ed4f52" />
Select "Create workflow template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2b88e20f-63e6-49ea-a544-df46aa9fd5eb" />
<pre>
Name - Jegan - Workflow demo
Organization - Default
Inventory - Select your inventory from AAP
</pre>
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/e819b037-c383-4bac-a231-13beae1dcf78" />
Click "Create workflow job template"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/1d7abe64-9b4b-4a7c-9f78-376a0abb5510" />
Click "Add step" button
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2a424d42-5441-42a7-b4f1-bfe26f608973" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/bda391b0-74ea-48de-b506-781c412524e8" />
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/126ef2d6-a7c0-4aa3-b86f-038dc25557d2" />
Click "Finish"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/18a80a90-73a2-4989-80dd-d037790d2c76" />
Click "Add step"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/a6e248de-36bb-4d66-b84f-27b06041eedb" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/d108b51c-a000-4471-b1f1-8a3600b0ace4" />
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/82e191af-3b97-498b-9e8c-5d72af2c0bd6" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b1728e62-f946-43ea-84ab-ae76b7bd032a" />
Click "Finish"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/3ce8c5f0-b44e-4ff1-9bb9-f52a7852bc66" />
Click "Invoke Install Nginx Playbook"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b68be074-b21f-48f5-8f25-ce4d76cd368b" />
Click "Edit" and Remove the step
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b7c204a7-6a9e-46f2-86be-40d0c9d2a2ba" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8181eac0-9b46-4811-9e1d-96e7308f952f" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/db25bf42-2bee-4bcd-85c5-48c3bb959cc1" />
Click "Remove step"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/e17eb041-a404-4149-bdd7-f7feb8720fd7" />
Now click on "Tektutor Training Repository" vertical 3 dots
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/8a9793e8-e37f-41a9-9546-45cab4a962b1" />
Select "Add step and link"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/9d60ae11-31fd-4bd4-90b7-10fac0b3dbd6" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/61102a2b-4393-4c7f-ad5b-2ee1d8a8fdf3" />
Click "Next"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/2d0d690b-a634-4f83-a052-8f8bd8d29ae7" />
Click "Finish"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/d9ba7dbe-3375-4b6a-b618-e5bd60b890a1" />
Click "Save"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/34288f55-3d3b-4f73-9640-2eac01453410" />
Click "Launch workflow"
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/90b263b3-5419-4597-8c30-807d06f49144" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/a5ae0b0e-d182-4fcb-81e5-8ffb35523afc" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/f8c28e9d-20b1-402a-ae5e-713b80e6cbf8" />
<img width="1920" height="1168" alt="image" src="https://github.com/user-attachments/assets/b6e8ac3a-0bc2-4a2f-acad-ec9ac4c1fc01" />




## Demo - Install OpenLDAP in Ubuntu (Just for your reference, please don't attempt this in our lab environment )
```
sudo apt update
sudo apt install slapd ldap-utils -y
```


Configuring LDAP Server
<pre>
sudo dpkg-reconfigure slapd  
</pre>

How to respond when the above commands prompts your response
<pre>
Omit OpenLDAP server configuration?	No
DNS domain name?	palmeto.org
Organization name?	Palmeto
Administrator password?	palmeto@123
Database backend?	MDB
Remove database when slapd is purged?	No
Move old database?	Yes
</pre>

Check if LDAP Server is running
```
sudo systemctl status slapd
sudo ss -tulnp | grep :389
```

Check if LDAP search works
```
ldapsearch -x -LLL -H ldap://localhost -b dc=palmeto,dc=org
```

Create a file named base.ldif
<pre>
dn: ou=users,dc=palmeto,dc=org
objectClass: organizationalUnit
ou: users

dn: ou=groups,dc=palmeto,dc=org
objectClass: organizationalUnit
ou: groups  
</pre>

Apply the above configuration
```
ldapadd -x -D "cn=admin,dc=palmeto,dc=org" -W -f base.ldif
```

Add LDAP users, creat a file named users.ldif
<pre>
dn: uid=jegan,ou=users,dc=palmeto,dc=org
objectClass: inetOrgPerson
uid: jegan
sn: Swaminathan
cn: Jeganathan Swaminathan
mail: jegan@tektutor.org
userPassword: palmeto@123

dn: cn=admins,ou=groups,dc=palmeto,dc=org
objectClass: groupOfNames
cn: admins
member: uid=jegan,ou=users,dc=palemto,dc=org  
</pre>

Create the user
```
ldapadd -x -D "cn=admin,dc=palmeto,dc=org" -W -f users.ldif
```

Search users
```
ldapsearch -x -LLL -b "ou=users,dc=palmeto,dc=org"
```

Search groups
```
ldapsearch -x -LLL -b "ou=groups,dc=palmeto,dc=org"
```

Configure Ubuntu firewall to allow LDAP
```
sudo ufw allow 389
```

LDAP Server details
<pre>
Base DN : dc=palmeto,dc=org
Admin DN: cn=admin,dc=palmeto,dc=org
User DN	: uid=jegan,ou=users,dc=palmeto,dc=org
Group DN: cn=admins,ou=groups,dc=palmeto,dc=org
Password: palmeto@123
</pre>

Script to extract existing linux users and add them as users in LDAP server
```
#!/bin/bash

# Hashed value of "palmeto@123" using slappasswd
LDAP_PASS="{SSHA}Xky2OjkOZt5U4eebv9rWsk9VUYR6Fa9Z"

# Output LDIF file
OUTPUT_FILE="palmeto-ldap-users.ldif"
> "$OUTPUT_FILE"

for user in $(ls -l /home | awk '{print $3}' | sort -u); do
    # Get user details from /etc/passwd
    IFS=':' read -r username _ uid gid full home shell <<< "$(getent passwd "$user")"

    # Skip if user not found
    [ -z "$username" ] && continue

    # Set default values for cn and sn
    if [ -z "$full" ]; then
        cn="$username"
        sn="user"
    else
        cn=$(echo "$full" | cut -d' ' -f1)
        sn=$(echo "$full" | cut -d' ' -f2)
        [ -z "$cn" ] && cn="$username"
        [ -z "$sn" ] && sn="user"
    fi

    # Set email from username
    email="${username}@palmeto.org"

    cat <<EOF >> "$OUTPUT_FILE"
dn: uid=$username,ou=users,dc=palmeto,dc=org
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
cn: $cn
sn: $sn
uid: $username
uidNumber: $uid
gidNumber: $gid
homeDirectory: $home
loginShell: $shell
mail: $email
userPassword: $LDAP_PASS

EOF
done

echo "LDIF file generated: $OUTPUT_FILE"
```

In case you wish to delete existing users from LDAP server before adding the below users
```
ldapsearch -LLL -x -D "cn=admin,dc=palmeto,dc=org" -w 'palmeto@123' -b "ou=users,dc=palmeto,dc=org" "(objectClass=inetOrgPerson)" dn \
  | grep '^dn:' \
  | sed 's/^dn: //' \
  | xargs -n1 ldapdelete -x -D "cn=admin,dc=palmeto,dc=org" -w 'palmeto@123'
```

Let's add the ldap users now
```
ldapadd -x -D "cn=admin,dc=palmeto,dc=org" -W -f palmeto-ldap-users.ldif
```

Let's create an openshift secret
```
oc create secret generic ldap-secret \
  --from-literal=bind_dn='cn=admin,dc=palmeto,dc=org' \
  --from-literal=bind_password='palmeto@123' \
  -n aap
```

Login in to Ansible Automation Platform Admin UI
Settings --> Authentication --> LDAP --> Add LDAP Source

Paste the below LDAP configuration
<pre>
LDAP Server URI: ldap://ldap.palmeto.org
StartTLS: false
Bind DN: cn=admin,dc=palmeto,dc=org
Bind Password: palmeto@123
User Search Base: ou=People,dc=palmeto,dc=org
User Search Filter: (uid=%(user)s)
Group Search Base: ou=Groups,dc=palmeto,dc=org
Group Object Class: groupOfNames
Group Type: MemberDNGroupType
Group Member Attribute: member
Require Group: <optional LDAP group DN>
User DN Template: uid=%(user)s,ou=People,dc=palmeto,dc=org    
</pre>

Test Login
```
oc logs deployment/automationcontroller -n aap
```
