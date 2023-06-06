#!/usr/bin/env python3
import sys
import argparse
from classes.FtpCli import FtpCli
import dateutil.parser

parser = argparse.ArgumentParser(description='submit FTP command')
parser.add_argument('path', help='file path on the server')
parser.add_argument('--list', action='store_true', help='LIST')
parser.add_argument('--ls', action='store_true', help='ls')
parser.add_argument('-t', '--time', action='store_true', help='print datetime')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
args = parser.parse_args()

path = args.path.replace('ftp://', '')
pos = path.find('/')
server = path[0:pos]
path = path[pos:]

if args.verbose:
    print(f'server: {server}', file=sys.stderr)
    print(f'path: {path}', file=sys.stderr)

cli = FtpCli(server)

if args.list:
    status = cli.print_list(path)
    if status:
        print(status, file=sys.stderr)
elif args.ls:
    list = cli.get_list(path)
    print("\n".join(list))
elif args.time:
    print(cli.get_remote_datetime(path))

cli.close()
