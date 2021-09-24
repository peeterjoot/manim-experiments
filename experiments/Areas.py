class Areas(Scene):
    def construct(self):

        square = Square(color = MAROON_A, fill_opacity = 0.5)

        hexwidth = np.sqrt( 2 * np.sqrt(3) ) * 2/3
        hexagon = RegularPolygon( n = 6, start_angle = 30 * DEGREES, color = GREEN, fill_opacity = 0.5)
        hexagon.scale( hexwidth )

        r = 1/np.sqrt( math.pi )
        #circle = Circle( color = RED, fill_opacity = 0.5)
        #circle.scale( circlewidth )
        circle = Ellipse( width = 2*r, height = 2*r, color = RED, fill_opacity = 0.5 )
        circle.scale( 2 ) # why?

        a = 1.3/np.sqrt( math.pi )
        b = 1/( math.pi * a )
        ellipse = Ellipse( width = 2*a, height = 2*b, color = BLUE_B, fill_opacity = 0.5 )
        ellipse.scale( 2 ) # why?

        o = np.array( [0, 0, 0] )
        p1 = np.array( [1, 1/3, 0] )
        p2 = np.array( [1/3, 1, 0] )

        p1cap = p1/ np.linalg.norm( p1 )
        cross = np.cross( p2, p1cap )

        p1 = p1cap / np.linalg.norm( cross )
        op1 = o + p1
        op2 = o + p2

        ppoints = [ o, op1, op1 + p2, op2 ]
        parallelogram = Polygon( *ppoints, color = PURPLE, fill_opacity = 0.5 )
        parallelogram.scale( 2 )
        parallelogram.shift( 1.0 * DOWN + 1.0 * LEFT )
        #self.add( parallelogram )
        #self.wait( )

        rest = [ parallelogram, hexagon, circle, ellipse ]
        ac = CurvedArrow( [r, 0, 0], [0, r, 0] )
        ac.move_to( square )
        ac.shift( 0.1 * DOWN + 0.1 * LEFT )
        g = VGroup( square, ac )
        self.play( Write( g ) )
        self.wait( )
        last=square
        for item in rest:
            self.play( FadeOut( ac ) )
            self.play( ReplacementTransform( last, item ) )
            self.play( FadeIn( ac ) )
            self.wait( )
            last=item
