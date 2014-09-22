#!/bin/bash
FILE=$1

if [ -f "officehours.tag" ];
then
   rm officehours.tag
   mv status.html officehours.html
   mv status_backup.html status.html 
else
   touch officehours.tag
   mv status.html status_backup.html
   mv officehours.html status.html
fi

git add -A *.html
git add -A officehours.tag
git commit -a -m "push"
git push
