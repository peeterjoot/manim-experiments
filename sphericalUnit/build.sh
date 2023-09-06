#! /bin/bash

if [ 1 -eq 0 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m010_Intro.py
#../bin/build $q $p m025_Lemma.py
#../bin/build $q $p m030_Simple.py
../bin/build $q $p m040_Sneaky.py
#../bin/build $q $p mxx_test.py
#echo done
