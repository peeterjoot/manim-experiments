#! /bin/bash

production=0
production=1

if [ $production -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m010_Intro.py
#../bin/build $q $p m020_wedge_intro.py
#../bin/build $q $p m020_wedge_intro_cramers.py
#../bin/build $q $p m030_approximation_intro.py
#../bin/build $q $p m050_leastsq_intro.py

#../bin/build $q $p m020_wedge.py
#../bin/build $q $p m030_approximation.py
#../bin/build $q $p m050_leastsq.py
../bin/build $q $p m100_summary.py
#echo done
