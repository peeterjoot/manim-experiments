#! /bin/bash

if [ 0 -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p GAFundamentals_025.py && \
#echo done
#../bin/build $q $p GAIntro_030.py && \
../bin/build $q $p GAvectorProduct_035.py
##../bin/build $q $p Imaginary_040.py && \
#../bin/build $q $p Finale_110.py && \
#echo done
