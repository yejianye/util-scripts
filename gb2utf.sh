#!/usr/bin/env bash
cp "$1" "$1-backup"
for encode in 'GBK' 'GB18030' 'GB2312'
do
	iconv -f $encode -t UTF-8 "$1-backup" > "$1"
	if [ $? = 0 ]; then
		rm "$1-backup"
		echo "Decode: $encode. Success!"
		exit
	fi
done

