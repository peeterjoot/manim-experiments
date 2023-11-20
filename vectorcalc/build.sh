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
#../bin/build $q $p m020_simple.py
#../bin/build $q $p m030_curlcurl.py
#../bin/build $q $p m040_curlbivector.py
#../bin/build $q $p m050_graddot.py
#../bin/build $q $p m060_curlcross.py
../bin/build $q $p m070_gradmv.py
#../bin/build $q $p m200_summary.py
#echo done
