#! /bin/bash

#q='-q h'
#p='-p'

./clean.sh

../bin/build $q $p Coordinates_10.py
../bin/build $q $p Basis_20.py
../bin/build $q $p GADecoding_30.py
../bin/build $q $p VisualizeDerivatives_40.py
# script:
../bin/build $q $p VisualizeDerivatives_50.py
../bin/build $q $p Velocity_and_acceleration_60.py
../bin/build $q $p General_70.py
../bin/build $q $p Circular_80.py
../bin/build $q $p Finale_90.py

ffmpeg -f concat -safe 0 -i concat.in -c copy circular_all.mp4
