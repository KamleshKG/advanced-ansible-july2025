# Day 5

## Lab - Setting  MFA with LDAP in Ansible Automation Platform

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

#### Let's create a LDAP Server

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

Select 
