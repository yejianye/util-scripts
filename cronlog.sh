#!/bin/sh
# A simple script to print out command executing result along with timestamp.
# STDERR of the original command will be redirect to STDOUT.
# Especially useful to debug cronjob and performance testing
# Usage:
#	cronlog.sh [any command]

echo "[`date`] Start executing $1"
$@ 2>&1 | sed -e "s/\(.*\)/[`date`] \1/"
echo "[`date`] End executing $1"
