#! /bin/bash

production=0
production=1

if [ $production -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
../bin/build $q $p m010_Intro.py
../bin/build $q $p m020_isotropic.py
../bin/build $q $p m030_divcurl.py
../bin/build $q $p m040_maxwells.py
../bin/build $q $p m050_recover.py
../bin/build $q $p m100_summary.py
#echo done
