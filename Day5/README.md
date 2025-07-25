# Day 5

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
ldapsearch -x \
> -D "uid=jegan,ou=users,dc=palmeto,dc=org" \
> -w "palmeto@123" \
> -b "dc=palmeto,dc=org" \
> "(uid=jegan)"
```


## Info - Keycloak Overview
<pre>
- an opensource Identiy and Access Management (IAM) solution designed for modern application and services
- helps us manage who can access your applications, what they can do with your applications
- Mainly used for Single Sign-on(SSO)
- handles the porcess of verifying an user's identify
- supports below of authentication
  - login with username & password
  - Multi-factor Authentication (MFA)
    - OTP
    - Social Media Logins
      - Facebook
      - Twitter
      - Gmail
      - GitHub, etc
- provides a centralized user management
</pre>

## Info - OpenLDAP 
<pre>
- is an opensource software commonly used in Linux distributions
- LDAP - Lightweight Directory Access Protocol
- distributed directory informaiton services over IP
- Supports Centralized User and Identity Management
  - User Authentication
    - User and respective credentials will be stored in LDAP server
    - When we attempt to login to some software with LDAP Integration, the LDAP server will verify login and authenticates
  - Authorization
    - LDAP stores information about user's roles and group mememberships
    - LDAP determines what permission a user has 
    - RBAC - Role-Based Access Control
  - Single Sign-ON(SSO)
</pre>

## Lab - Setting up MFA with LDAP in Ansible Automation Platform

#### Let's create a Keycloak Podman container
```
podman run -d --name keycloak \
  -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:24.0.2 \
  start-dev
```

You may access the keycloak Dashboard
<pre>
http://localhost:8080  
</pre>

Login Credentials
<pre>
username: admin
password: admin
</pre>

#### Let's create a LDAP Server ( This can be skipped as we already installed OpenLDAP in our lab servers )

```
podman run --name my-openldap -d \
  -p 389:389 -p 636:636 \
  -e LDAP_ORGANISATION="Palmeto" \
  -e LDAP_DOMAIN="palmeto.org" \
  -e LDAP_ADMIN_PASSWORD="palmeto@123" \
  osixia/openldap:1.5.0
```

Test your LDAP server
```
ldapsearch -x -H ldap://localhost:389 -D "cn=admin,dc=palmeto,dc=org" -w palmeto@123 -b "dc=palmeto,dc=org"
```

#### Create a Realm for AAP in keycloak

Navigate to keycload admin console
<pre>
http://localhost:8080  
</pre>

keycloak combo box on the left side, click on "Create realm" button
<pre>
realm name:  aap-realm 
</pre>
Click "Create" button

On the left side menu, at the bottom you will see "User fedaration" click that

On the center of the screen, click on "Add Ldap providers"
We need to type in the below details
<pre>
UI Display name: jegan-ldap
Vendor: Other ( as we don't see OpenLDAP there )
Under "Connection and authentication settings"
Connection URL: ldap://192.168.10.200:389
Bind DN: cn=admin,dc=palmeto,dc=org
Bind Credential: palmeto@123
Users DN: ou=users,dc=palmeto,dc=org
Username LDAP attribute: uid
RDN LDAP attribute: uid  
</pre>

#### Enabling MFA with keycloak
In Keycloak webconsole, navigate to Authentication --> Flows --> Copy "Browse" Flow
Name it Browser + MFA
Need to add a new step, Actions --> Add Execution
Choose OTP Form
Set requirement to Required

Go to Authentications --> Bindings
Set Browser Flow to Browser + MFA
