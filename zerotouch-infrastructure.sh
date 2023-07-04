#! /bin/bash


#ENV=production
ENV=staging
#ENV=develop

ansible-playbook master.yml -i ${ENV}/hosts -k 
