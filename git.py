import requests
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="version script", version="ver. 0.1", action="version")
parser.add_argument("-u", "--user", help="user", action="store_true")
parser.add_argument("-o", "--open", help="How long pull request are opening", action="store_true")
parser.add_argument("-l", "--label", help="Label of this pull request", action="store_true")
parser.add_argument("-r", "--repo", help="Repository", action="store_true")
parser.add_argument("-d", "--update", help="When the pullrequest was updated", action="store_true")
parser.add_argument("-b", "--base", help="Base repository for forking", action="store_true")

args = parser.parse_args()
u = input("Enter login: ", )
t = input("Enter token: ", )
repo = input("Enter repository: ", )
n = input("Enter pull request's number: ", )

repo_url = requests.get("https://api.github.com/repos/" + u + "/" + repo + "/pulls/" + n)
gh_session = requests.Session()
gh_session.auth = (u, t)
url = repo_url.json()

if args.user:
    print(url["user"]["login"])

if args.open:
    date = url["created_at"]
    day = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    k = datetime.datetime.now() - day
    print(k)

if args.label:
    print(url["head"]["label"])

if args.repo:
    print(url["repo"]["name"])

if args.update:
    date = url["updated_at"]
    day = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    up = datetime.datetime.now() - day
    print(up)

if args.base:
    print(url["base"]["html_url"])
