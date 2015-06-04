#!/bin/sh
if [ -f keys/keyfile ]; then
  rm keys/keyfile
fi
for name in keys/*.key; do ssh-keygen -l -f $name >> keys/keyfile; done
echo -n "Total keys: "
wc -l keys/keyfile
sort -n keys/keyfile | cut -f1,4 -d' ' | sort -k 2 | uniq -c
./dowkd.pl file keys/*.key
