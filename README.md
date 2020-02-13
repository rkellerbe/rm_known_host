rm_known_host
========

CLI for removing host from ~/.ssh/known_hosts

## Usage

Pass in a hostname or IP and remove matching lines from the known_host file.

hostname example:
```
$ rm_known_host.sh rtp1-pod6-gw1
Removing rtp1-pod6-gw1 from known_hosts
```

IP example:
```
$ rm_known_host.sh 192.168.1.15
Removing 192.168.1.15 from known_hosts
```

Removal with backup example
```
$ rm_known_host.sh -b rtp1-pod6-gw1
Backing up known_hosts to known_hosts.old
Removing rtp1-pod7-gw1 from known_hosts
```

Removal Prompt example:
```
$ rm_known_host.sh -i 173.37.150.2
173.37.150.2 ssh-rsa AAAAB3NzaC1yc2EAAAAB......
Removing 173.37.150.2 from known_hosts
Remove host(s)? y/n(y) n
Exiting without change!
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:
```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone https://github.com/rkellerbe/rm_known_host`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
