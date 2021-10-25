#! /usr/local/bin/python3

from sys import *
path.append( '../bin' )
from mylatex2 import *

l          = latex( )
vecu       = l.vec( 'u' )
invu       = l.inv( vecu )
hatu       = l.hat( vecu )
vecv       = l.vec( 'v' )
vec_v1     = concat( l.vec( 'v' ), '_1' )
vec_v2     = concat( l.vec( 'v' ), '_2' )
vec_e1     = concat( l.vec( 'e' ), '_1' )
vec_e2     = concat( l.vec( 'e' ), '_2' )
vec_e3     = concat( l.vec( 'e' ), '_3' )
vec_f1     = concat( l.vec( 'f' ), '_1' )
vec_f2     = concat( l.vec( 'f' ), '_2' )
vec_e12    = concat( l.vec( 'e' ), '_{12}' )
vec_e13    = concat( l.vec( 'e' ), '_{13}' )
vec_e23    = concat( l.vec( 'e' ), '_{23}' )
uu         = l.sq( vecu )
vv         = l.sq( vecv )
uwedgev    = l.wedge( vecu, vecv )
vwedgeu    = l.wedge( vecv, vecu )
udotv      = l.dot( vecu, vecv )
vdotu      = l.dot( vecv, vecu )
lr_uwedgev = l.lr( uwedgev )
lr_vwedgeu = l.lr( vwedgeu )
lr_udotv   = l.lr( udotv )
lr_vdotu   = l.lr( vdotu )
detuivj    = l.det22( 'u_i', 'v_i', 'u_j', 'v_j' )
normu      = l.norm( vecu )
#uvcolors   = { l.vec('u'): RED, l.vec('v'): YELLOW }

squ        = l.norm2( vecu )
sqv        = l.norm2( vecv )
vdotuhatsq = l.lrsq( l.dot( vecv, hatu ) )
rej        = l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) )
vdotuhatsq_dist = l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) )

#eq0 = [ l.text( 'Area' ), ' = ', l.text( 'base' ), r' \times ', l.text( 'height' ) ]
#eq1 = [ l.sq( l.text( 'Area' ) ), ' = ', squ, l.norm2( rej ) ]
#eq2 = [ '= ', squ, l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ) ]
#eq3 = [ '= ', squ, l.lr( l.sub( sqv, vdotuhatsq ) ) ]
#eq4 = [ '= ', l.sub( l.mult( squ, sqv ), l.mult( squ, vdotuhatsq ) ) ]
#eq5 = [ '= ', l.sub( l.mult( squ, sqv ), vdotuhatsq_dist ) ]
#eq6 = [ '= ', l.sub( l.mult( squ, sqv ), l.lrsq( vdotu ) ) ]
eq0 = [ r'{{ \text{Area} }}', 
        ' = ',
        r'{{ \text{base} }} \times {{ \text{height} }}' ]
eq1 = [ r'{{ \text{Area} }} {}^2',
        ' = ',
        r'\lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} - ( {{ \mathbf{v} }} \cdot {{ \hat{\mathbf{u} } }} ) {{ \hat{\mathbf{u} } }} \rVert {}^2' ]

eq2 = [ '= ',
        r' \lVert {{\mathbf{u} }} \rVert {}^2', r'\Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 + ( {{ \mathbf{v} }} \cdot {{ \hat{\mathbf{u} } }} ) {}^2 - 2 ( {{ \mathbf{v} }} \cdot {{ \hat{\mathbf{u} } }} ){}^2 \Bigr)' ]

eq3 = [ '= ',
        r' \lVert {{\mathbf{u} }} \rVert {}^2 \Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \hat{\mathbf{u} } }} ){}^2 \Bigr)' ]

eq4 = [ '= ',
        r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \lVert {{ \mathbf{u} }} \rVert {}^2 ( {{ \mathbf{v} }} \cdot {{ \hat{\mathbf{u} } }} ){}^2' ]
eq5 = [ '= ',
        r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \Bigl( {{ \mathbf{v} }} \cdot ( \lVert {{ \mathbf{u} }} \rVert {{ \hat{\mathbf{u} } }} ) \Bigr){}^2' ]
eq6 = [ '= ',
        r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{u} }} ){}^2' ]

print( eq0 )
print( eq1 )
print( eq2 )
print( eq3 )
print( eq4 )
print( eq5 )
print( eq6 )
