-++++++++++++++++++++# Day 5

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
