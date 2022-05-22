#! /bin/bash

if [ 1 -eq 1 ] ; then
q='-q h'
concat=concat.in
else
p='-p'
concat=concat.low.in
fi

#./clean.sh
../bin/build $q $p GAIntro_030.py 
#../bin/build $q $p GAFundamentals_025.py 

#../bin/build $q $p Coordinates_010.py && \
#../bin/build $q $p Basis_020.py && \
#../bin/build $q $p GAFundamentals_025.py && \
#../bin/build $q $p GAIntro_030.py && \
#../bin/build $q $p Imaginary_040.py && \
#../bin/build $q $p Exponential_050.py && \
#../bin/build $q $p VisualizeDerivatives_060.py && \
#../bin/build $q $p VisualizeDerivatives_070.py && \
#../bin/build $q $p Velocity_and_acceleration_080.py && \
#../bin/build $q $p General_090.py && \
#../bin/build $q $p Circular_100.py && \
#../bin/build $q $p Finale_110.py && \
#ffmpeg -f concat -safe 0 -i concat.in -c copy circular_all.mp4
