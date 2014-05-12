#!/bin/bash
FILE=$1

if [ -f "dnd.tag" ];
then
   rm dnd.tag
   mv status.html dnd.html
   mv status_backup.html status.html 
else
   touch dnd.tag
   mv status.html status_backup.html
   mv dnd.html status.html
fi

git add -A *.html
git add -A dnd.tag
#git commit -a -m "push"
#git push
