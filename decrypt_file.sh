#!/bin/bash
# decrypt_file.sh [file]

tar -xzvf $1.tgz
openssl rsautl -decrypt -ssl -inkey ~/.ssh/id_rsa -in $1.key.enc -out $1.key
openssl aes-256-cbc -d -in $1.enc -out $1 -pass file:$1.key
rm $1.enc $1.key.enc $1.key
