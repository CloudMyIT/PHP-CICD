#!/usr/bin/python3

VERSIONS={
    'php': [
        '7.2.5',
        '7.3',
        '7.4',
        '8.0'
    ],
    'mysql': [
        '5.6',
        '5.7',
        '8.0'
    ],
    'postgresql': [
        '9.6',
        '10',
        '11',
        '12',
        '13'
    ]
}

###
# DO NOT EDIT BELOW THIS LINE!
###

# Import Libs
import os
import subprocess

# Go though each server type
for server in VERSIONS.keys():
    # And each version for said server type
    for version in VERSIONS[server]:
        # Check if a custom docker imge file exists
        if os.path.exists(server + "/Dockerfile-" + version):
            dockerfile = server + "/Dockerfile-" + version
        else:
            dockerfile = server + "/Dockerfile"
        # Build the Image
        returned_value = subprocess.call('docker build ' + server + ' -f ' + dockerfile + ' --build-arg VERSION=' + version, shell=True)
        
        # Exit if Error Occurs
        if(returned_value > 0):
            exit()

