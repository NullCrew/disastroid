#!/bin/sh

a=0
GIT=`which git`
echo Commit message:
read message
while [ $a -lt 2 ]
do
   touch test.txt
	${GIT} add --all .
	${GIT} commit -m "$message"
	${GIT} push
	rm test.txt
   a=`expr $a + 1`
done
