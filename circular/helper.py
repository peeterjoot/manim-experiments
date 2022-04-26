from manim import *
import numpy as np
import math
from sys import *
sys.path.append( '../bin' )
from mylatex2 import *

l = latex2( )

vec_e1     = concat( l.vec( 'e' ), '_1' )
vec_e2     = concat( l.vec( 'e' ), '_2' )
acolors    = { l.vec('x'): GREEN, l.vec('a'): GREEN, l.vec('r'): GREEN , l.vec('v'): GREEN, l.hat(l.vec('r')): RED, l.hat(r'\boldsymbol{\theta}'): YELLOW }

vec_x      = l.doublebr( l.vec( 'x' ) )
vec_r      = l.doublebr( l.vec( 'r' ) )
vec_v      = l.doublebr( l.vec( 'v' ) )
vec_a      = l.doublebr( l.vec( 'a' ) )
hat_r      = l.doublebr( l.hat( l.vec('r') ) )
hat_theta  = l.doublebr( l.hat( r'\boldsymbol{\theta}' ) )

class AcolorsMathTex(MathTex):
    def __init__(
        self,
        *tex_strings,
        arg_separator = " ",
        **kwargs,
    ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        super().__init__(
                arg_separator.join( tex_strings ),
                tex_template = myTemplate,
                **kwargs,
            )
        self.set_color_by_tex_to_color_map( acolors )

def align_it( s, ref, new, sh, m, what ):
    where = ref.get_part_by_tex( what )
    new.move_to( where, LEFT )
    new.shift( sh )
    if m != None:
        new.set_color_by_tex_to_color_map( m )

def write_aligned( s, ref, new, sh = 0 * DOWN, m = None, what = '=' ):
    align_it( s, ref, new, sh = sh, m = m, what = what )
    s.play( Write( new ) )

def tx_aligned( s, ref, new, sh = 0 * DOWN, m = None, what = '=' ):
    align_it( s, ref, new, sh = sh, m = m, what = what )
    s.play( ReplacementTransform( ref, new ) )

def tx_matching( s, ref, new, sh = 0 * DOWN, m = None, what = '=' ):
    align_it( s, ref, new, sh = sh, m = m, what = what )
    s.play( TransformMatchingTex( ref, new ) )

def prime(v):
    return concat( v, "'" )

def dprime(v):
    return concat( v, "''" )

r_prime    = prime('r')
dr_prime   = dprime('r')
rhat_prime = prime(hat_r)

# vim: et sw=4 ts=4
