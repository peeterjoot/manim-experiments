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
#../bin/build $q $p m025_Lemma.py
#../bin/build $q $p m030_Simple.py
#../bin/build $q $p m040_Sneaky.py
#../bin/build $q $p m050_3d.py
#../bin/build $q $p m060_Summary.py
#../bin/build $q $p mxx_test.py
#echo done
