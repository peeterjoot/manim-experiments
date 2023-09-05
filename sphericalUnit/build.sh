#! /bin/bash

if [ 1 -eq 0 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
../bin/build $q $p m010_Intro.py
#echo done
