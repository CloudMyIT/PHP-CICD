#!/usr/bin/python3

REPO_NAME="cloudmyit/php-cicd"

VERSIONS={
    'php': [
        '7.2',
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
        if os.path.exists('services/' + server + "/Dockerfile-" + version):
            dockerfile = 'services/' + server + "/Dockerfile-" + version
        else:
            dockerfile = 'services/' + server + "/Dockerfile"
        # Build the Image
        cmd = 'docker build services/' + server + ' -f ' + dockerfile + ' --build-arg VERSION=' + version + ' -t ' + REPO_NAME + ':' + server + '-' + version
        
        if(float(max(VERSIONS[server])) == float(version)):
            cmd = cmd + ' -t ' + REPO_NAME + ':' + server + '-latest'
        
        returned_value = subprocess.call(cmd, shell=True)
        
        # Exit if Error Occurs
        if(returned_value > 0):
            exit()

