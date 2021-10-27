from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex2 import *

def write_aligned( s, ref, new, sh, m ):
    where = ref.get_part_by_tex( '=' )
    new.move_to( where, LEFT )
    new.shift( sh )
    new.set_color_by_tex_to_color_map( m )
    s.play( Write( new ) )

class foo( Scene ):
    def construct( self ):

        l = latex( )
        acolors = { 'Area': BLUE, 'base': RED, 'height': GREEN, l.hat('u'): PURPLE, l.vec('u'): RED, l.vec('v'): YELLOW }

        t_area = l.doublebr( l.text( 'Area' ) )
        t_base = l.doublebr( l.text( 'base' ) )
        t_height = l.doublebr( l.text( 'height' ) )

        vecu  = l.doublebr( l.vec( 'u' ) )
        vecv  = l.doublebr( l.vec( 'v' ) )
        squ   = l.norm2( vecu )
        sqv   = l.norm2( vecv )
        hatu  = l.doublebr( l.hat( 'u' ) )
        normu = l.norm( vecu )

        eq2 = MathTex( concat( t_base, '&=', normu, l.newline ),
                       concat( t_height, '&= ', l.norm( l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) ) ), l.newline ) )
        eq2.set_color_by_tex_to_color_map( acolors )
        eq2.move_to( 2.5 * DOWN + 2 * LEFT )
        self.play( Write( eq2 ) )
        self.wait( )
        #return


        #ar_a  = [ r'{{ \text{Area} }}', '=', r'{{ \text{base} }} \times {{ \text{height} }}' ]
        ar_a = [ t_area, '=', t_base, r' \times ', t_height ]
        #ar_0 = [ r'{{ \text{Area} }} {}^2', '=', r'{{ \text{base} }} {}^2 \times {{ \text{height} }} {}^2' ]
        ar_0 = [ l.sq( t_area ), '=', l.sq( t_base ), r' \times ', l.sq( t_height ) ]

        #ar_1  = [ '=',
        #          r'\lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} - ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ) {{ \mathbf{\hat{u} } }} \rVert {}^2' ]
        ar_1 = [ '=', squ, l.norm2( l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) ) ) ]
        #ar_2 = [ '=',
        #        r' \lVert {{\mathbf{u} }} \rVert {}^2 \Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 + ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ) {}^2 - 2 ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2 \Bigr)' ]
        ar_2 = [ '=', squ, l.lr( l.add( sqv, l.lrsq( l.dot( vecv, hatu ) ) ), l.neg( l.mult( '2', l.lrsq( l.dot( vecv, hatu ) ) ) ), big = 1 ) ]
        #ar_3 = [ '=',
        #        r' \lVert {{\mathbf{u} }} \rVert {}^2 \Bigl( \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2 \Bigr)' ]
        ar_3 = [ '=', squ, l.lr( l.sub( sqv, l.lrsq( l.dot( vecv, hatu ) ) ), big = 1 ) ]
        #ar_4 = [ '=',
        #        r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \lVert {{ \mathbf{u} }} \rVert {}^2 ( {{ \mathbf{v} }} \cdot {{ \mathbf{\hat{u} } }} ){}^2' ]
        ar_4 = [ '=', squ, sqv, '-', squ, l.lrsq( l.dot( vecv, hatu ) ) ]

        #ar_5 = [ '=',
        #        r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - \Bigl( {{ \mathbf{v} }} \cdot ( \lVert {{ \mathbf{u} }} \rVert {{ \mathbf{\hat{u} } }} ) \Bigr){}^2' ]
        #ar_5 = [ '=', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) ) ) ]

        ar_6 = [ '=',
                r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{u} }} ){}^2' ]
        #ar_6 = [ '=', l.sub( l.mult( squ, sqv ), l.lrsq( vdotu ) ) ]

        eq_a = MathTex( *ar_a )
        eq_a.set_color_by_tex_to_color_map( acolors )
        eq_a.shift( 2 * UP )

        eq_0 = MathTex( *ar_0 )
        eq_0.set_color_by_tex_to_color_map( acolors )
        eq_0.shift( 2 * UP )

        eq_1 = MathTex( *ar_1 )
        eq_2 = MathTex( *ar_2 )
        eq_3 = MathTex( *ar_3 )
        eq_4 = MathTex( *ar_4 )
        #eq_5 = MathTex( *ar_5 )
        eq_6 = MathTex( *ar_6 )

        self.play( Write( eq_a ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_a, eq_0 ) )
        self.wait( )
        write_aligned( self, eq_0, eq_1, 0.75 * DOWN, acolors )
        self.wait( )
        write_aligned( self, eq_1, eq_2, 0.75 * DOWN, acolors )
        self.wait( )

        eq_3.move_to( eq_2, LEFT )
        eq_3.set_color_by_tex_to_color_map( acolors )
        eq_4.move_to( eq_3, LEFT )
        eq_4.set_color_by_tex_to_color_map( acolors )
        #eq_5.move_to( eq_4, LEFT )
        #eq_5.set_color_by_tex_to_color_map( acolors )
        eq_6.move_to( eq_4, LEFT )
        eq_6.set_color_by_tex_to_color_map( acolors )
        self.play( TransformMatchingTex( eq_2, eq_3 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_3, eq_4 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_4, eq_6 ) )
        self.wait( )




# vim: et sw=4 ts=4
