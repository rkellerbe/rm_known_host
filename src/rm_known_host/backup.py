import os
from shutil import copy

def backup_function():
    home_dir = os.environ['HOME']
    ssh_location = '.ssh'
    file_name = 'known_hosts'
    backup_name = 'known_hosts.bak'

    infile = os.path.join(home_dir, ssh_location, file_name)
    outfile = os.path.join(home_dir, ssh_location, backup_name)

    copy(infile, outfile)
    print(f"Backup file {backup_name} created.")
