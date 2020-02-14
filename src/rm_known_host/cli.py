from argparse import Action, ArgumentParser


class OptionsActions(Action):
    def __call__(self, values, hostname):
        options = values
        hostname = hostname


def create_parser():
    parser = ArgumentParser(
        description='Removes stale hostnames from ~/.ssh/known_hosts')
    parser.add_argument('-i', '--interactive',
                        help="requires confirmation before deletion",
                        action='store_true',
                        required=False)
    parser.add_argument('-b', '--backup',
                        help="Backs up known_hosts to known_hosts.old",
                        action='store_true')
    parser.add_argument("hostname", help="Hostname to be removed")
    return parser
