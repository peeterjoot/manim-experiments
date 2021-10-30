from manim import *
import numpy as np
import math
from sys import *
sys.path.append( '../bin' )
#from mylatex import *
from mylatex2 import *

#l          = latex( )
l          = latex2( )
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

dv_p1 = np.array( [ 3, 1, 0 ] )
dv_p2 = np.array( [ 1, 3, 0 ] )

acolors = { 'Area': BLUE, 'base': RED, 'height': GREEN, l.hat('u'): PURPLE, l.vec('u'): RED, l.vec('v'): YELLOW }

vecu  = l.doublebr( l.vec( 'u' ) )
vecv  = l.doublebr( l.vec( 'v' ) )
squ   = l.norm2( vecu )
sqv   = l.norm2( vecv )
hatu  = l.doublebr( l.hat( 'u' ) )
normu = l.norm( vecu )
invu  = l.doublebr( l.inv( l.vec( 'u' ) ) )

uwedgev    = l.wedge( vecu, vecv )
vwedgeu    = l.wedge( vecv, vecu )
udotv      = l.dot( vecu, vecv )
vdotu      = l.dot( vecv, vecu )
lr_udotv   = l.lr( udotv )
lr_vdotu   = l.lr( vdotu )
lr_vwedgeu = l.lr( vwedgeu )
lr_uwedgev = l.lr( uwedgev )

uu         = l.sq( vecu )
vv         = l.sq( vecv )

t_area = l.doublebr( l.text( 'Area' ) )
t_base = l.doublebr( l.text( 'base' ) )
t_height = l.doublebr( l.text( 'height' ) )


def align_it( s, ref, new, sh, m, what = '=' ):
    where = ref.get_part_by_tex( what )
    new.move_to( where, LEFT )
    new.shift( sh )
    new.set_color_by_tex_to_color_map( m )

def write_aligned( s, ref, new, sh, m, what = '=' ):
    align_it( s, ref, new, sh, m, what = what )
    s.play( Write( new ) )

def tx_aligned( s, ref, new, sh, m, what = '=' ):
    align_it( s, ref, new, sh, m, what = what )
    s.play( ReplacementTransform( ref, new ) )



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



# vim: et sw=4 ts=4
