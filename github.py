import requests
import argparse
token = 'fbhjb'
parser = argparse.ArgumentParser()
parser.add_argument('-user', nargs=1, help="write github username", required=True)
parser.add_argument('-repo', nargs=1, help="write name of repo", required=True)
parser.add_argument('-param', nargs=1, help="write argument likes id, title etc...", required=True)
parser.add_argument('-num', nargs=1, help="write number of pull request", required=True)
parser.add_argument('-login', help="write flag for show login", action='store_true')
parser.add_argument('-v', action='version', version='version 1.0')
parser.add_argument('--version', action='version', version='version 1.0')

args = parser.parse_args()

b = requests.get('https://api.github.com/repos/' + args.user[0] +
                 '/' + args.repo[0] + '/pulls/' + args.num[0], auth=('vvvvmmm', token))
dd = b.json()
if args.param[0]:
    print(b.json()[args.param[0]])
else:
    print('bad argument')
if args.login:

    print(b.json()['user']['login'])
