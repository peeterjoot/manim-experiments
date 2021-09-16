#! /usr/local/bin/python3

import numpy as np

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'
def mknorm2(v):
    return r'{\left\lVert{' + v + r'}\right\rVert}^2'
def lr(v):
    return r'\left( ' + v + r' \right)'
def lrsq(v):
    return r'{\left( ' + v + r' \right)}^2'

vecu = r'\vec{u}'
uhat = r'\hat{u}'
vecv = r'\vec{v}'
nsqu = mknorm2(vecu)
nsqv = mknorm2(vecv)

#eq2_text= '${}{}$'.format( nsqu, mknorm2(r'{} - \left({} \cdot {} \right){}'.format(vecv, vecv, uhat, uhat)) )
#print( eq2_text )

vdotusq = lrsq( r'\vec{v} \cdot \hat{u}' )
#eq3_text = '$' + nsqu + r'\left(' + nsqv + ' + {} - 2 {}'.format( vdotusq, vdotusq ) + r'\right) $'
eq3_text = [ r'$\,$', '$=$', '$' + nsqu + r'\left(' + nsqv + ' + {} - 2 {}'.format( vdotusq, vdotusq ) + r'\right) $' ]
print( eq3_text )
