#!/usr/bin/python3

###
# Build Settings
###
PUSH_ON_BUILD=False

###
# CI Settings
###
CODE_PATH="/srv/samba/sda/CloudMyIT/PHP-CICD/"
CI_COMMANDS=[
    "pwd",
    "ls -al",
]
CI_EXIT_ON_FAIL=True
CI_ENV_BADGES=True
CI_ENV_BADGE_PATH="./badges"

###
# General Settings
###
REPO_NAME="cloudmyit/php-cicd"

# Currently we generate 96 Environments 
# count(environments) = count(php) * count(mysql) * count(postgresql) * ...

VERSIONS={
    # PHP can only have x.x versions because it does not have a "latest-fpm" tag
    'php': [
        '7.2',
        '7.3',
        '7.4',
        '8.0' # This will tag as latest as well as it is the largest number in the list
    ],
    'mysql': [
        '5.6',
        '5.7',
        '8.0',
        'latest'
    ],
    'postgresql': [
        '9.6',
        '10',
        '11',
        '12',
        '13',
        'latest'
    ]
}