#!/usr/bin/env python2
from pygithub3 import Github
from urllib2 import urlopen, Request
from json import loads
from time import sleep
from os import getenv
from sys import exit, argv

TOKEN=getenv("GITHUB_TOKEN")
if not TOKEN:
    print "Set GITHUB_TOKEN to your token as created at https://github.com/settings/tokens"
    exit(1)
if len(argv < 1):
    print "usage: get_keys.py <orgname>"
    print "orgname should be the name of your organisation, i.e. alphagov"
    exit(1)

GITHUB_API=getenv("GITHUB_API", "https://api.github.com")

org = argv[0]
gh = Github(token=TOKEN)
r = gh.orgs.members.list(org)

for user in r.iterator():
    req = Request( "%s/users/%s/keys" % (GITHUB_API, user.login), headers={"Authorization": "token "+TOKEN})
    url = urlopen( req)
    keys = loads(url.readlines()[0])
    for key in keys:
        f = open("keys/%s%s.key" % (user.login, key['id']), "w")
        f.write(key['key'])
        f.close()
    sleep(0.1)
