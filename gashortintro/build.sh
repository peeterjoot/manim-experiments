#! /bin/bash

if [ 0 -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p GAvectorProduct_035.py
../bin/build $q $p Multivector_40.py
#../bin/build $q $p Finale_110.py && \
#echo done
