# Github SSH Key Checker

This tool downloads all of the public keys for your organisation on github and can test those keys against known blacklists and also generates an overview of key strength for the keys.

It does not at the moment identify which keys are bad, it leaves that up to the user.

# Usage

```
$ export GITHUB_TOKEN=abc123...
$ ./setup.sh
$ ./test.sh
Total keys: 594 keys/keyfile
15 1024 (DSA)
2 256 (ED25519)
1 1023 (RSA)
10 1024 (RSA)
546 2048 (RSA)
1 2064 (RSA)
1 3072 (RSA)
18 4096 (RSA)
keys/xxxxxx123456.key:1: warning: unparsable line
summary: keys found: 589, weak keys: 0
```

Note that the unparsable line in this case means that it's one of the ED25519 keys
