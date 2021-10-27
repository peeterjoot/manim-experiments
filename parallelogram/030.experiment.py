from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex2 import *

l          = latex( )
#invu       = l.inv( vecu )
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
#uu         = l.sq( vecu )
#vv         = l.sq( vecv )
#uwedgev    = l.wedge( vecu, vecv )
#vwedgeu    = l.wedge( vecv, vecu )
#udotv      = l.dot( vecu, vecv )
#vdotu      = l.dot( vecv, vecu )
#lr_uwedgev = l.lr( uwedgev )
#lr_vwedgeu = l.lr( vwedgeu )
#lr_udotv   = l.lr( udotv )
#lr_vdotu   = l.lr( vdotu )
#detuivj    = l.det22( 'u_i', 'v_i', 'u_j', 'v_j' )

#vdotuhatsq = l.lrsq( l.dot( vecv, hatu ) )
#rej        = l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) )
#vdotuhatsq_dist = l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) )


# new:
#    ' = ', 'stuff'
def write_aligned( s, ref, new, sh, m ):
    where = ref.get_part_by_tex( '=' )
    new.move_to( where, LEFT )
    new.shift( sh )
    new.set_color_by_tex_to_color_map( m )
    s.play( Write( new ) )


class foo( Scene ):
    def construct( self ):

        uvcolors = { l.hat('u'): PURPLE, l.vec('u'): RED, l.vec('v'): YELLOW }
        acolors = { 'Area': BLUE, 'base': RED, 'height': GREEN }

        t_area = l.doublebr( l.text( 'Area' ) )
        t_base = l.doublebr( l.text( 'base' ) )
        t_height = l.doublebr( l.text( 'height' ) )

        vecu  = l.doublebr( l.vec( 'u' ) )
        vecv  = l.doublebr( l.vec( 'v' ) )
        squ   = l.norm2( vecu )
        sqv   = l.norm2( vecv )
        hatu  = l.doublebr( l.hat( 'u' ) )
        normu = l.norm( vecu )

        #ar_a  = [ r'{{ \text{Area} }}', '=', r'{{ \text{base} }} \times {{ \text{height} }}' ]
        ar_a = [ t_area, '=', t_base, r' \times ', t_height ]
        #ar_0 = [ r'{{ \text{Area} }} {}^2', '=', r'{{ \text{base} }} {}^2 \times {{ \text{height} }} {}^2' ]
        ar_0 = [ l.sq( t_area ), '=', l.sq( t_base ), r' \times ', l.sq( t_height ) ]

        ar_1 = [ '=', squ, l.norm2( l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) ) ) ]
        eq2 = [ '=', squ, l.lr( l.add( sqv, l.lrsq( l.dot( vecv, hatu ) ) ), l.neg( l.mult( '2', l.lrsq( l.dot( vecv, hatu ) ) ) ) ) ]
        eq3 = [ '=', squ, l.lr( l.sub( sqv, l.lrsq( l.dot( vecv, hatu ) ) ) ) ]
        eq4 = [ '=', l.sub( l.mult( squ, sqv ), l.mult( squ, l.lrsq( l.dot( vecv, hatu ) ) ) ) ]
        eq5 = [ '=', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) ) ) ]

        #ar_1  = [ '=',
        #          r'\lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} - ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ) {{ \mathbf{\hat{u} } }} \rVert {}^2' ]
        ar_2 = [ '=',
                r' \lVert {{\mathbf{u} }} \rVert {}^2 \Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 + ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ) {}^2 - 2 ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2 \Bigr)' ]
        ar_3 = [ '=',
                r' \lVert {{\mathbf{u} }} \rVert {}^2 \Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2 \Bigr)' ]

        ar_4 = [ '=',
                r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \lVert {{ \mathbf{u} }} \rVert {}^2 ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2' ]
        ar_5 = [ '=',
                r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \Bigl( {{ \mathbf{v} }} \cdot ( \lVert {{ \mathbf{u} }} \rVert {{ \mathbf{\hat{u} } }} ) \Bigr){}^2' ]
        ar_6 = [ '=',
                r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{u} }} ){}^2' ]
        #ar_6 = [ '=', l.sub( l.mult( squ, sqv ), l.lrsq( vdotu ) ) ]

        eq_area_text = MathTex( *ar_a )
        eq_area_text.set_color_by_tex_to_color_map( acolors )
        eq_area_text.shift( 2 * UP )

        eq_area_squared_text = MathTex( *ar_0 )
        eq_area_squared_text.set_color_by_tex_to_color_map( acolors )
        eq_area_squared_text.shift( 2 * UP )

        eq_sq_norms = MathTex( *ar_1 )
        eq_2 = MathTex( *ar_2 )
        eq_3 = MathTex( *ar_3 )
        eq_4 = MathTex( *ar_4 )
        eq_5 = MathTex( *ar_5 )
        eq_6 = MathTex( *ar_6 )

        self.play( Write( eq_area_text ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_area_text, eq_area_squared_text ) )
        self.wait( )
        write_aligned( self, eq_area_squared_text, eq_sq_norms, 0.75 * DOWN, uvcolors )
        self.wait( )
        write_aligned( self, eq_sq_norms, eq_2, 0.75 * DOWN, uvcolors )
        self.wait( )

        eq_3.move_to( eq_2, LEFT )
        eq_3.set_color_by_tex_to_color_map( uvcolors )
        eq_4.move_to( eq_3, LEFT )
        eq_4.set_color_by_tex_to_color_map( uvcolors )
        eq_5.move_to( eq_4, LEFT )
        eq_5.set_color_by_tex_to_color_map( uvcolors )
        eq_6.move_to( eq_5, LEFT )
        eq_6.set_color_by_tex_to_color_map( uvcolors )
        self.play( TransformMatchingTex( eq_2, eq_3 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_3, eq_4 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_4, eq_5 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_5, eq_6 ) )
        self.wait( )


# vim: et sw=4 ts=4
