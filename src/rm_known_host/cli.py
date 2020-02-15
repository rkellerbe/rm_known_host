"""
A Command line program to remove unwanted host from ~/.ssh/known_hosts

>>> parser = create_parser()

>>> args = parser.parse_args(['-b', 'example.com'])
>>> args
Namespace(backup=True, hostname='example.com', interactive=False)

>>> args = parser.parse_args(['-i', 'example2.com'])
>>> args
Namespace(backup=False, hostname='example2.com', interactive=True)

>>> args = parser.parse_args(['--backup', 'example3.com'])
>>> args
Namespace(backup=True, hostname='example3.com', interactive=False)

>>> args = parser.parse_args(['--interactive', 'example4.com'])
>>> args
Namespace(backup=False, hostname='example4.com', interactive=True)

>>> args = parser.parse_args(['-ib', 'example5.com'])
>>> args
Namespace(backup=True, hostname='example5.com', interactive=True)

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
                        help="Backs up known_hosts to known_hosts.old",
                        action='store_true',
                        required=False)
    parser.add_argument("hostname", help="Hostname to be removed")
    return parser


def main():
    # from rm_known_host import backup

    args = create_parser().parse_args()

    print(f"Interactive Flag is: {args.interactive}")
    print(f"Backup Flag is: {args.backup}")
    print(f"The hostname is {args.hostname}")
