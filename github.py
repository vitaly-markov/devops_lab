import requests
import argparse
import getpass
parser = argparse.ArgumentParser()
parser.add_argument('-login', nargs=1, help="write github username", required=True)
parser.add_argument('-user', nargs=1, help="write github username", required=True)
parser.add_argument('-repo', nargs=1, help="write name of repo", required=True)
parser.add_argument('-num', nargs=1, help="write number of pull request", required=True)
parser.add_argument('-showlogin', help="write flag for show login", action='store_true')
parser.add_argument('-id', help="write flag for show id", action='store_true')
parser.add_argument('-title', help="write flag for show title", action='store_true')
parser.add_argument('-v', action='version', version='version 1.0')
parser.add_argument('--version', action='version', version='version 1.0')

args = parser.parse_args()
password = getpass.getpass()
b = requests.get(
    'https://api.github.com/repos/' + args.user[0] + '/' + args.repo[0] + '/pulls/' + args.num[0],
    auth=(args.login[0], password))
if args.id:
    print(b.json()['id'])
elif args.title:
    print(b.json()['title'])
elif args.login:
    print(b.json()['user']['login'])
else:
    print('bad argument')
