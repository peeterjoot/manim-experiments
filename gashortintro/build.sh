#! /bin/bash

if [ 0 -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m010_GAvectorProduct.py
../bin/build $q $p m020_Multivector.py
#../bin/build $q $p Finale_110.py && \
#echo done
