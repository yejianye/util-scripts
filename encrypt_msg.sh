#!/bin/bash
openssl rsautl -encrypt -pubin -inkey <(ssh-keygen -e -f $1 -m PKCS8)
