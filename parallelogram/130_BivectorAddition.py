from helper import *

class BivectorAddition( Scene ):
    def construct( self ):
        number_plane = NumberPlane(
            x_range = [ -10, 10, 1 ],
            y_range = [ -10, 10, 1 ],

            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )

        o = np.array( [ 0, 0, 0 ] )
        p1 = [ np.array( [ 1, 1/3, 0 ] ), np.array( [ -1/4, 1, 0 ] ), np.array( [ -1, -1/2, 0 ] ),  np.array( [ 1/4, -1, 0 ] ) ]
        p2 = [ np.array( [ 1/3, 1, 0 ] ), np.array( [ -0.8, 1/3, 0 ] ), np.array( [ -1/2, -1.25, 0 ] ), np.array( [ 1, -2/7, 0 ] ) ]

        self.add( number_plane )
        v1 = MathTex( vec_v1 )
        v2 = MathTex( vec_v2 )
        e1 = MathTex( vec_e1 )
        e2 = MathTex( vec_e2 )
        p = MathTex( vec_v1, r' \wedge ', vec_v2, ' = 4', vec_e1, vec_e2 )
        p[ 0 ].set_color( RED )
        p[ 2 ].set_color( BLUE )

        dir1 = ( RIGHT, UP, LEFT, DOWN )
        dir2 = ( RIGHT + 0.5 * UP, LEFT, LEFT + 0.25 * DOWN, DOWN + 0.25 * RIGHT )
        shift = 4
        pos = ( shift * LEFT, shift * RIGHT, shift * RIGHT, shift * LEFT )

        for i in range( 4 ):
            ppoints = unitParallelogram( o, p1[ i ], p2[ i ], 2 )
            pg = OrientedPolygon( *ppoints, c0 = PURPLE, c1 = RED, c2 = BLUE, f = 0.5, d1 = dir1[ i ], d2 = dir2[ i ], tex = 1, r = 0.1 )

            p.move_to( pg )
            p.shift( pos[ i ] )
            totx = VGroup( pg, p )
            if i == 0:
                self.play( Write( totx ) )
                self.wait( )
            else:
                self.play( ReplacementTransform( fromtx, totx ) )
                self.wait( )

            fromtx = totx

        i = 3
        add1 = OrientedPolygon( *ppoints, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )
        self.play( ReplacementTransform( fromtx, add1 ) )
        p1 = MathTex( vec_v1, r' \wedge ', vec_v2, ' = 4', vec_e1, vec_e2 )
        p1.move_to( add1 )
        p1.shift( 4 * LEFT )
        self.play( ReplacementTransform( p, p1 ) )
        self.wait( )

        add2 = add1.copy( );
        add2.shift( 2 * UP )
        self.play( FadeOut( p1 ) )
        self.play( Write( add2 ) )
        p2 = MathTex( r'2 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 8', vec_e1, vec_e2 )
        p2.move_to( VGroup( add1, add2 ) )
        p2.shift( 4 * LEFT + 2 * UP )
        self.play( Write( p2 ) )
        self.wait( )

        add3 = add1.copy( );
        add3.shift( 2 * LEFT + 0.55 * UP )
        self.play( FadeOut( p2 ) )
        self.play( Write( add3 ) )
        p3 = MathTex( '3 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 12 ', vec_e1, vec_e2 )
        p3.move_to( add2 )
        p3.shift( 4 * LEFT + 1 * UP )
        self.play( Write( p3 ) )
        self.wait( )

        add4 = add3.copy( );
        add4.shift( 2 * UP )
        self.play( FadeOut( p3 ) )
        self.play( Write( add4 ) )
        p4 = MathTex( '4 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 16 ', vec_e1, vec_e2 )
        p4.move_to( VGroup( add2, add4 ) )
        p4.shift( 1.8 * UP + 3 * RIGHT )
        self.play( Write( p4 ) )
        self.wait( )

        o2 = np.array( [ -2, -2, 0 ] )
        p1s = np.array( [ 1, 0, 0 ] )
        p2s = np.array( [ 0, 1, 0 ] )
        sqpts = unitParallelogram( o2, p1s, p2s, 4 )
        sq = OrientedPolygon( *sqpts, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )
        p5 = MathTex( '16 ', vec_e1, vec_e2 ).scale( 2 )
        p5.move_to( sq )
        p5.shift( 2 * UP + 4 * RIGHT )
        g = VGroup( sq, p5 )
        self.play( ReplacementTransform( VGroup( add1, add2, add3, add4, p4 ), g ) )

        pentwidth = np.sqrt( 2/( 5 * math.sin( 2 * math.pi / 5 ) ) )
        pentagon = OrientedRegularPolygon( 5, pentwidth, PURPLE, 0.5 )
        pentagon.scale( 4 )
        pentagon.shift( 2 * LEFT * pentwidth )
        self.play( ReplacementTransform( sq, pentagon ) )
        self.wait( )

        hexwidth = np.sqrt( 2 * np.sqrt( 3 ) ) * 2/3
        hexagon = OrientedRegularPolygon( 6, hexwidth, PURPLE, 0.5 )
        hexagon.scale( 2 )
        hexagon.shift( 2 * LEFT * hexwidth )
        self.play( ReplacementTransform( pentagon, hexagon ) )
        self.wait( )

        r = 1/np.sqrt( math.pi )
        circle = Ellipse( width = 2*r, height = 2*r, color = PURPLE, fill_opacity = 0.5 )
        circle.scale( 4 )
        ac = CurvedArrow( [ 2 * r, 0, 0 ], [ 0, 2 * r, 0 ] )
        ac.move_to( circle )
        ac.set_color( PURPLE )
        self.play( ReplacementTransform( hexagon, circle ) )
        self.add( ac )
        self.wait( )

        a = 1.3/np.sqrt( math.pi )
        b = 1/( math.pi * a )
        ellipse = Ellipse( width = 2*a, height = 2*b, color = PURPLE, fill_opacity = 0.5 )
        ellipse.scale( 4 )
        self.play( ReplacementTransform( circle, ellipse ) )
        self.wait( )


# vim: et sw=4 ts=4
