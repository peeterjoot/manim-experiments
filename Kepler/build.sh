#! /bin/bash

production=0
#production=1

if [ $production -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m010_Intro.py
../bin/build $q $p m020_Start.py
#../bin/build $q $p m060_Summary.py
#echo done
