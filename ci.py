#!/usr/bin/python3

###
# DO NOT EDIT THIS FILE
###

#Import Settings
from settings import VERSIONS, REPO_NAME, CODE_PATH, CI_COMMAND

# Import Libs
import os
import subprocess
import itertools

service_names = sorted(VERSIONS.keys());
service_versions = list()

for service in service_names:
    service_versions.append(VERSIONS[service])

for combination in list(itertools.product(*service_versions)):
    env = "CODE_PATH=" + CODE_PATH + " "
    for x in range(len(combination)):
        env = env + "VERSION_%s=%s " % (service_names[x].upper(), combination[x])

    cmd = "docker-compose -f docker-compose.yml run php " + CI_COMMAND
    
    returned_value = subprocess.call(env + cmd, shell=True)
    # Exit if Error Occurs
    if(returned_value > 0):
        exit(returned_value)