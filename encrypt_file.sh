#!/bin/bash
# encrypt_file.sh [file] [pubkey]

openssl rand 192 -out $1.key
openssl aes-256-cbc -in $1 -out $1.enc -pass file:$1.key
openssl rsautl -encrypt -pubin -inkey <(ssh-keygen -e -f $2 -m PKCS8) -in $1.key -out $1.key.enc
tar -zcvf $1.tgz $1.enc $1.key.enc
rm $1.key $1.enc $1.key.enc
