#!/bin/bash
FILE=$1

if [ -f "brb.tag" ];
then
   rm brb.tag
   mv status.html brb.html
   mv status_backup.html status.html 
else
   touch brb.tag
   mv status.html status_backup.html
   mv brb.html status.html
fi

git add -A *.html
git add -A brb.tag
git commit -a -m "push"
git push
