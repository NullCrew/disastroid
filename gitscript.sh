#!/bin/sh

GIT=`which git`
echo Commit message:
read message
${GIT} add --all .
${GIT} commit -m "$message"
${GIT} push 
