#! /bin/bash

production=0
production=1

if [ $production -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m003_theorem.py
#../bin/build $q $p m005_vectorderivative.py
#../bin/build $q $p m020_lineintegral.py
#../bin/build $q $p m030_surfaceintegral.py
#../bin/build $q $p m040_volumeintegral.py
#../bin/build $q $p m050_reciprocalbasis.py
#../bin/build $q $p m055_reciprocal_orthogonal.py
#../bin/build $q $p m060_gradient.py
#../bin/build $q $p m070_gradientexamples.py
#../bin/build $q $p m080_bidirectional.py
#../bin/build $q $p m090_oneparameter.py
#../bin/build $q $p m100_twoparameters.py
../bin/build $q $p m105_d1xboundary.py
#../bin/build $q $p x.py
#../bin/build $q $p m110_threeparameters.py
#../bin/build $q $p m200_summary.py
#echo done
