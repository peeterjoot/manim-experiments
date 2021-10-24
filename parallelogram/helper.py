from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *
#from mylatex2 import *
import enum # IntFlag

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
uvcolors   = { l.vec('u'): RED, l.vec('v'): YELLOW }

vec_v1, r' \wedge ', vec_v2

dv_p1 = np.array( [ 3, 1, 0 ] )
dv_p2 = np.array( [ 1, 3, 0 ] )

def DrawVectorsAndProjRej( self, prlabels ):

    o = np.array( [ 0, -2, 0 ] )
    dv_p1 = np.array( [ 3, 1, 0 ] )
    dv_p2 = np.array( [ 1, 3, 0 ] )
    op1 = o + dv_p1
    op2 = o + dv_p2

    p1cap = dv_p1/ np.linalg.norm( dv_p1 )
    proj = np.dot( dv_p2, p1cap ) * p1cap
    oproj = o + proj

    vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
    if prlabels:
        vprojl = MathTex( concat( lr_vdotu, invu ) )
    else:
        vprojl = Text( 'Proj' )
    vprojl.set_color( PURPLE )
    vprojl.next_to( vproj, DOWN )

    rej = dv_p2 - proj
    vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
    if prlabels:
        vrejl = MathTex( concat( lr_vwedgeu, invu ) )
    else:
        vrejl = Text( 'Rej' )
    vrejl.set_color( GREEN )
    vrejl.next_to( vrej, 0.2 * RIGHT )

    v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
    v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
    v1l = MathTex( vecu )
    v1l.set_color( RED )
    v1l.next_to( v1, RIGHT )
    v1l.shift( 0.5 * LEFT )
    v2l = MathTex( vecv )
    v2l.set_color( YELLOW )
    v2l.next_to( v2, UP )
    v2l.shift( 0.5 * DOWN )

    all = VGroup( v1, v1l, v2, v2l, vproj, vrej, vprojl, vrejl )

    move = ( -6.5, 2, 0 )
    all.shift( move )

    self.add( all )

    return ( vprojl, vrejl )


def OrientedPolygon( *vertices, c0, c1, c2, f, d1, d2, tex, r ):
    n = len( vertices )

    #print( vertices )

    poly = Polygon( *vertices, color = c0 , fill_opacity = f )
    g = VGroup( poly )

    if tex:
        v1 = MathTex( vec_v1 )
        v1.set_color( c1 )
        v2 = MathTex( vec_v2 )
        v2.set_color( c2 )
        g = g + VGroup( v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            if tex:
                v1.next_to( a, d1 )
            a.set_color( c1 )
        elif i == 1:
            if tex:
                v2.next_to( a, d2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g




def unitParallelogram( o, v1, v2, scale ):
    v1cap = v1/ np.linalg.norm( v1 )
    cross = np.cross( v2, v1cap )

    v1 = scale * v1cap / np.linalg.norm( cross )
    v2 = scale * v2
    ov1 = o + v1
    ov2 = o + v2
    ov12 = ov1 + v2

    ppoints = [ o, ov1, ov12, ov2 ]

    return ppoints



# vim: et sw=4 ts=4
