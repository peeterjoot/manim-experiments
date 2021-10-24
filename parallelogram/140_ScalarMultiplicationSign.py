from helper import *
from OrientedPolygon import *
import enum # IntFlag


def int2str( v ):
    if v == 1:
        vstr = ''
    elif v == -1:
        vstr = '-'
    else:
        vstr = str( v )
    return vstr


class vsflags( enum.IntFlag ):
    default = 0
    braces = 1
    signed = 2



def vecstr( l, v, e, flags ):
    vs = str( v )
    if v == 1:
        if flags & vsflags.signed:
            vstr = concat( '+', e )
        else:
            vstr = e
    else:
        if v == -1:
            if flags & vsflags.braces:
                vstr = l.lr( '-', e )
            else:
                vstr = concat( '-', e )
        else:
            if flags & vsflags.braces:
                if (flags & vsflags.signed) and (v > 0):
                    vstr = l.lr( '+', vs, e )
                else:
                    vstr = l.lr( vs, e )
            else:
                if (flags & vsflags.signed) and (v > 0):
                    vstr = concat( '+', vs, e )
                else:
                    vstr = concat( vs, e )
    return vstr



def OrientedPolygon2( *vertices, c0, c1, c2, f, s1, s2, r ):
    n = len( vertices )

    poly = Polygon( *vertices, color = c0, fill_opacity = f )

    s1str = vecstr( l, s1, vec_e1, vsflags.default )
    s2str = vecstr( l, s2, vec_e2, vsflags.default )

    v1 = MathTex( s1str )
    v1.set_color( c1 )
    v2 = MathTex( s2str )
    v2.set_color( c2 )
    g = VGroup( poly, v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            v1.move_to( (vertices[0] + vertices[1])/2 - np.sign( s2 ) * UP/2 )
            a.set_color( c1 )
        elif i == 1:
            v2.move_to( (vertices[2] + vertices[1])/2 - np.sign( s1 ) * LEFT/2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g




def write_area_products( self, n1, n2, ar, o ):
    p = n1 * n2
    an1 = abs( n1 )
    an2 = abs( n2 )
    rect1   = Rectangle( color = GREEN_B, width = an1, height = an2, fill_opacity = 0.5 )
    rect1.move_to( RIGHT * n1/2 + UP * n2/2 )

    absp = abs( p )
    prod_string = int2str( p )

    n1vec = vecstr( l, n1, vec_e1, vsflags.braces )
    n2vec = vecstr( l, n2, vec_e2, vsflags.braces )
    prodvec = vecstr( l, n1 * n2, l.mult( vec_e1, vec_e2 ), vsflags.signed )
    pp2 = MathTex( n1vec, n2vec, ' = ', prodvec )
    pp2[0].set_color( RED )
    pp2[1].set_color( BLUE )
    pp2[3].set_color( GREEN_B )

    v1 = np.array( [ n1, 0, 0 ] )
    v2 = np.array( [ 0, n2, 0 ] )
    pts = [ o, o + v1, o + v1 + v2, o + v2 ]
    rect2 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = n1, s2 = n2, r = ar )
    pp2.move_to( 3 * DOWN )

    tog = VGroup( rect2, pp2 )
    self.play( Write( tog ) )
    self.wait( 2 )

    return rect2, pp2



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

        #title = Text( 'Geometry of scalar multiplication signs.' )
        #self.play( Write( title ) )
        #self.wait( )
        #self.play( FadeOut( title ) )

        number_plane = NumberPlane(
            x_range = [ -10, 10, 1 ],
            y_range = [ -10, 10, 1 ],

            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )

        plus = MathTex( '+' )
        minus = MathTex( '-' )

        self.play( Write( number_plane ) )
        self.wait( )
        t = write_area_products( self, 2, 3, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        t = write_area_products( self, 3, 2, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        x = 1
        y = 1
        t = write_area_products( self, x, y, 0.2, ORIGIN )
        g = t[0] + t[1]

        o = np.array( 1 * (RIGHT + UP) )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        rect1 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = x, s2 = y, r = 0.2 )
        plus.move_to( 1.5 * (RIGHT + UP) )
        g1 = rect1 + plus
        self.play( ReplacementTransform( g, g1 ) )
        self.wait( )


        t = write_area_products( self, -2, 3, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        t = write_area_products( self, -3, 2, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        x = -1
        t = write_area_products( self, x, y, 0.2, ORIGIN )
        g = t[0] + t[1]

        o = np.array( 1 * (LEFT + UP) )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        rect2 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = x, s2 = y, r = 0.2 )
        minus.move_to( 1.5 * (LEFT + UP) )
        g2 = rect2 + minus
        self.play( ReplacementTransform( g, g2 ) )
        self.wait( )

        o = np.array( 1 * (LEFT + DOWN) )
        y = -1
        t = write_area_products( self, x, y, 0.2, o )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        plus2 = plus.copy( )
        plus2.move_to( 1.5 * (LEFT + DOWN) )
        self.play( FadeOut( t[1] ), Write( plus2 ) )
        self.wait( )

        o = np.array( 1 * (RIGHT + DOWN) )
        x = 1
        t = write_area_products( self, x, y, 0.2, o )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        minus2 = minus.copy( )
        minus2.move_to( 1.5 * (RIGHT + DOWN) )
        self.play( FadeOut( t[1] ), Write( minus2 ) )
        self.wait( )



# vim: et sw=4 ts=4
