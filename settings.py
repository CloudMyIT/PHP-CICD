#!/usr/bin/python3

CODE_PATH="./"

CI_COMMANDS=[
    "pwd",
    "ls -al",
    # "pwd",
    # "ls -al",
    #"php -v"
]

REPO_NAME="cloudmyit/php-cicd"

PUSH_ON_BUILD=False

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