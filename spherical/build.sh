#! /bin/bash

if [ 1 -eq 1 ] ; then
q='-q h'
else
p='-p'
fi

#./clean.sh
#../bin/build $q $p m05_position.py
#../bin/build $q $p m10_spherical.py
#../bin/build $q $p m20_dr.py
#../bin/build $q $p m30_dt.py
#../bin/build $q $p m40_dp.py
#../bin/build $q $p m50_radial_expansion.py
../bin/build $q $p m55_polar_expansion.py
#../bin/build $q $p m60_azimuthal_expansion.py
#../bin/build $q $p Finale_110.py && \
#echo done
