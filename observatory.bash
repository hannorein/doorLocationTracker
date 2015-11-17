#!/bin/bash
FILE=$1

if [ -f "observatory.tag" ];
then
   rm observatory.tag
   mv status.html observatory.html
   mv status_backup.html status.html 
else
   touch observatory.tag
   mv status.html status_backup.html
   mv observatory.html status.html
fi

git add -A *.html
git add -A observatory.tag
git commit -a -m "push"
git push
