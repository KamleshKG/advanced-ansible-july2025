#!/bin/bash

mkdir -p /runner/.ssh
if [ ! -f /runner/.ssh/id_rsa ]; then
    ssh-keygen -q -t rsa -N "" -f /runner/.ssh/id_rsa
fi

ansible-playbook /runner/push-key-playbook.yml
