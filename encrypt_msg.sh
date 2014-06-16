#!/bin/bash
openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pem
