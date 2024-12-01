#!/bin/bash

# cat $1 |\
html=$(echo "$1" | hexdump -ve '1/1 "%.2x"')
plaintext=$2
echo "set the clipboard to {text:\"${plaintext}\", «class HTML»:«data HTML${html}»}" | osascript -
