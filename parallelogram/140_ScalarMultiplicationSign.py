from helper import *

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
