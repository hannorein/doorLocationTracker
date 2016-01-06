#!/bin/bash
FILE=$1

if [ -f "teaching.tag" ];
then
   rm teaching.tag
   mv status.html teaching.html
   mv status_backup.html status.html 
else
   touch teaching.tag
   mv status.html status_backup.html
   mv teaching.html status.html
fi

git add -A *.html
git add -A teaching.tag
git commit -a -m "push"
git push
