#! /bin/bash

production=0
#production=1

if [ $production -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m010_intro.py
../bin/build $q $p m020_simple.py
#../bin/build $q $p m200_summary.py
#echo done
