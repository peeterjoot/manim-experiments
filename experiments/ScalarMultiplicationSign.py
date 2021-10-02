from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *

def writeproducts( self, n1, n2 ):
    dotn1 = Dot( n1 * RIGHT )
    dotn1.set_color( RED )
    linen1 = Line( start = ORIGIN, end = n1 * RIGHT, color = RED )

    dotn2 = Dot( n2 * RIGHT )
    dotn2.set_color( BLUE )
    linen2 = Line( start = ORIGIN, end = n2 * RIGHT, color = BLUE )

    p = n1 * n2
    dot_prod = Dot( p * RIGHT )
    dot_prod.set_color( GREEN_B )
    line_prod = Line( start = ORIGIN, end = p * RIGHT, color = GREEN_B )

    absp = abs( p )
    if p > 0:
        prod_string = '+{}'.format( p )
    else:
        prod_string = '-{}'.format( -p )

    if n2 > 0:
        n2str = '{}'.format( n2 )
    else:
        n2str = '({})'.format( n2 )

    pp = MathTex( str(n1), r'\times', n2str, ' = ', prod_string ).scale( 2 )
    pp.set_color_by_tex_to_color_map( { str(n1): RED, str(n2): BLUE, str(absp): GREEN_B } )
    pp.shift( 2 * UP )

    g2 = VGroup( pp[0], linen1, dotn1 )
    self.play( Write( g2 ) )
    self.play( Write( pp[1] ) )

    g3 = VGroup( pp[2], linen2, dotn2 )
    self.play( Write( g3 ) )
    self.play( Write( pp[3] ) )

    g6 = VGroup( pp[4], line_prod, dot_prod )
    self.play( FadeOut( linen1, linen2 ) )
    self.play( Write( g6 ) )
    self.wait( )

    return VGroup( pp, dotn1, dotn2, line_prod, dot_prod )


def OrientedPolygon2( *vertices, c0, c1, c2, f, s1, s2, r ):
    n = len( vertices )
    l = latex( )

    poly = Polygon( *vertices, color = c0, fill_opacity = f )

    v1 = MathTex( concat( str(s1), '{ ', l.vec( 'e' ), ' }_1' ) )
    v1.set_color( c1 )
    v2 = MathTex( concat( str(s2), '{ ', l.vec( 'e' ), ' }_2' ) )
    v2.set_color( c2 )
    g = VGroup( poly, v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            v1.move_to( vertices[1]/2 - np.sign( s2 ) * UP/2 )
            a.set_color( c1 )
        elif i == 1:
            v2.move_to( (vertices[2] + vertices[1])/2 - np.sign( s1 ) * RIGHT/2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g



def write_area_products( self, n1, n2 ):
    p = n1 * n2
    linen1 = Line( start = ORIGIN, end = n1 * RIGHT, color = RED )
    linen2 = Line( start = n1 * RIGHT, end = n1 * RIGHT + n2 * UP, color = BLUE )
    an1 = abs( n1 )
    an2 = abs( n2 )
    rect1   = Rectangle( color = GREEN_B, width = an1, height = an2, fill_opacity = 0.5 )
    rect1.move_to( RIGHT * n1/2 + UP * n2/2 )

    absp = abs( p )
    if p > 0:
        prod_string = '+{}'.format( p )
    else:
        prod_string = '-{}'.format( -p )

    if n2 > 0:
        n2str = '{}'.format( n2 )
    else:
        n2str = '({})'.format( n2 )

    pp = MathTex( str(n1), r'\times', n2str, ' = ', prod_string ).scale( 2 )
    pp.set_color_by_tex_to_color_map( { str(n1): RED, str(n2): BLUE, str(absp): GREEN_B } )
    pp.shift( n1 * LEFT/2 + n2 * DOWN/2 )

    l = latex( )
    e1 = concat( l.vec( 'e' ), r'_1' )
    e2 = concat( l.vec( 'e' ), r'_2' )
    pp2 = MathTex( concat( '{', str(n1), '}', e1 ), r'\times', concat( '{', n2str, '}', e2 ), ' = ', concat( prod_string, e1, e2 ) ).scale( 2 )
    pp2[0].set_color( RED )
    pp2[2].set_color( BLUE )
    pp2[4].set_color( GREEN_B )
    #pp2.set_color_by_tex_to_color_map( '{}{}{}'.format( '{', str(n1), '}' ): RED,  '{}{}{}'.format( '{', str(n2), '}' ): BLUE, str(absp): GREEN_B } )
    pp2.shift( n1 * LEFT/2 + n2 * DOWN/2 )

    g2 = VGroup( pp[0], linen1 )
    self.play( Write( g2 ) )
    self.play( Write( pp[1] ) )

    g3 = VGroup( pp[2], linen2 )
    self.play( Write( g3 ) )
    self.play( Write( pp[3] ) )

    pp[4].move_to( n1 * RIGHT/2 + n2 * UP/2 )
    gp = VGroup( pp[4], rect1 )
    self.play( Write( gp ) )
    self.wait( )

    o = np.array( [ 0, 0, 0 ] )
    v1 = np.array( [ n1, 0, 0 ] )
    v2 = np.array( [ 0, n2, 0 ] )
    pts = [ o, v1, v1 + v2, v2 ]
    rect2 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = n1, s2 = n2, r = 0.1 )

    fromg = VGroup( rect1, linen1, linen2, pp )
    tog = VGroup( rect2, pp2 )
    self.play( ReplacementTransform( fromg, tog ) )
    self.wait( 2 )

    return VGroup( pp2, rect2 )


class ScalarMultiplicationSign( Scene ):
    def construct( self ):
        number_line = NumberLine(
            x_range = [-7, 7, 1],
            length = 14,
            color = TEAL,
            include_numbers = True,
            label_direction = UP,
            stroke_width = 4,
            stroke_opacity = 0.4,
        )

        title = Text( 'Geometry of scalar multiplication signs.' )
        self.play( Write( title ) )
        self.wait( )
        self.play( FadeOut( title ) )

        self.play( Write( number_line ) )
        g = writeproducts( self, 2, 3 )
        self.play( FadeOut( g ) )
        g = writeproducts( self, -2, 3 )
        self.play( FadeOut( g ) )
        g = writeproducts( self, 2, -3 )
        self.play( FadeOut( g ) )
        g = writeproducts( self, -2, -3 )
        self.play( FadeOut( g ), FadeOut( number_line ) )

        number_plane = NumberPlane(
            x_range = [ -10, 10, 1 ],
            y_range = [ -10, 10, 1 ],

            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )

        self.play( Write( number_plane ) )
        self.wait( )
        g = write_area_products( self, 2, 3 )
        self.play( FadeOut( g ) )
        g = write_area_products( self, -2, 3 )
        self.play( FadeOut( g ) )
        g = write_area_products( self, 2, -3 )
        self.play( FadeOut( g ) )
        g = write_area_products( self, -2, -3 )
        #self.play( FadeOut( g ) )



def foo():
    if 0:
        sh = 3 * DOWN
        number_line.shift( sh )

        doto = Dot( ORIGIN + sh )
        dot2 = Dot( 2 * RIGHT + sh )
        dot2.set_color( RED )
        dot3 = Dot( 3 * RIGHT + sh )
        dot3.set_color( ORANGE )

        #g = VGroup( number_line, doto, dot2, dot3 )
        self.play( Write( number_line ) )
        self.play( Write( number_line ) )
        self.wait( )

        l = latex( )

        #scalar_products = MathTex( r'2 \times 3 &= + 6 \\', 
        #                           r'2 \times (-3) &= - 6 \\', 
        #                           r'-2 \times 3 &= - 6 \\', 
        #                           r'-2 \times (-3) &= + 6 \\' ).scale( 2 )
        #for m in scalar_products:
        #    self.play( Write( m ) )
        #    self.wait( 0.25 )
        #self.wait( )
        #self.play( FadeOut( scalar_products ) )
        #self.play( Write( number_line ) )




# vim: et sw=4 ts=4
