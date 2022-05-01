#! /bin/bash

#q='-q h'
#p='-p'

../bin/build $q $p Coordinates_005.py
../bin/build $q $p Basis_008.py
../bin/build $q $p VisualizeDerivatives_009.py
../bin/build $q $p VisualizeDerivatives_009b.py
../bin/build $q $p GADecoding_010.py
../bin/build $q $p Velocity_and_acceleration_020.py
../bin/build $q $p Circular_025.py
../bin/build $q $p Finale_150.py

ffmpeg -f concat -safe 0 -i concat.in -c copy circular_all.mp4
