from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex2 import *

l = latex2( )
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
lr_vdotu   = l.lr( vdotu )
lr_vwedgeu = l.lr( vwedgeu )

def write_aligned( s, ref, new, sh, m, what = '=' ):
    where = ref.get_part_by_tex( what )
    new.move_to( where, LEFT )
    new.shift( sh )
    new.set_color_by_tex_to_color_map( m )
    s.play( Write( new ) )

# vim: et sw=4 ts=4
