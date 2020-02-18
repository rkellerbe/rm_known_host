"""
A Command line program to remove unwanted host from ~/.ssh/known_hosts

>>> parser = create_parser()

>>> args = parser.parse_args(['-b', 'example.com'])
>>> args
Namespace(backup=True, hostname='example.com', interactive=False, verbose=False)

>>> args = parser.parse_args(['-i', 'example2.com'])
>>> args
Namespace(backup=False, hostname='example2.com', interactive=True, verbose=False)

>>> args = parser.parse_args(['--backup', 'example3.com'])
>>> args
Namespace(backup=True, hostname='example3.com', interactive=False, verbose=False)

>>> args = parser.parse_args(['--interactive', 'example4.com'])
>>> args
Namespace(backup=False, hostname='example4.com', interactive=True, verbose=False)

>>> args = parser.parse_args(['-ib', 'example5.com'])
>>> args
Namespace(backup=True, hostname='example5.com', interactive=True, verbose=False)

"""

from argparse import Action, ArgumentParser


class OptionsActions(Action):
    def __call__(self, values, hostname):
        options = values
        hostname = hostname


def create_parser():
    parser = ArgumentParser(
        description='Removes stale hostnames from ~/.ssh/known_hosts')
    parser.add_argument('-i', '--interactive',
                        help="prompt before changing file",
                        action='store_true',
                        required=False)
    parser.add_argument('-b', '--backup',
                        help="Backs up known_hosts to known_hosts.bak",
                        action='store_true',
                        required=False)
    parser.add_argument('-v', '--verbose',
                        help="Verbose. Display the hostname, and argument flags",
                        action='store_true',
                        required=False)
    parser.add_argument("hostname", help="Hostname to be removed")
    return parser


def main():
    import os
    from rm_known_host.rm_host import delete_line
    import rm_known_host.backup as backup

    home_dir = os.environ['HOME']
    ssh_location = '.ssh'
    file_name = 'known_hosts'

    fname = os.path.join(home_dir, ssh_location, file_name)
    fdir = os.path.join(home_dir, ssh_location)


    args = create_parser().parse_args()

    if args.verbose:
        print(f"Interactive Flag is: {args.interactive}")
        print(f"Backup Flag is: {args.backup}")
        print(f"Verbose Flag is {args.verbose}")
        print(f"The hostname is {args.hostname}\n")

    if args.backup:
        backup.backup_function()
    

    delete_line(args.hostname, fname, args.interactive)
