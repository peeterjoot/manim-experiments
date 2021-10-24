from helper import *

class WedgeChangeOfBasisPartI( ThreeDScene ):
    def construct( self ):
        axes = ThreeDAxes()
        self.set_camera_orientation( phi = 70 * DEGREES, theta = 90 * DEGREES )

        o = ORIGIN
        s = 2
        p1 = np.array( [ 1, 1, 0 ] )
        p2 = np.array( [ 0, 1, 1 ] )
        e1 = np.array( [ 1, 0, 0 ] )
        e2 = np.array( [ 0, 1, 0 ] )
        e3 = np.array( [ 0, 0, 1 ] )
        ve1 = Arrow( start = o, end = e1, buff = 0, color = RED )
        ve2 = Arrow( start = o, end = e2, buff = 0, color = GREEN )
        ve3 = Arrow( start = o, end = e3, buff = 0, color = BLUE )
        e1t = MathTex( vec_e1 )
        e1t.move_to( e1 )
        e2t = MathTex( vec_e2 )
        e2t.move_to( e2 )
        e3t = MathTex( vec_e3 )
        e3t.move_to( e3 )
        bases = VGroup( ve1, ve2, ve3, e1t, e2t, e3t )
        ul = MathTex( vecu )
        ul.move_to( s * p1 )
        vl = MathTex( vecv )
        vl.move_to( o + s* (p1 + p2) )

        sq1 = [ o, o + s * p1, o + s *( p1 + p2), o + s * p2 ]
        s1 = OrientedPolygon( *sq1, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )

        p = -np.arccos( math.sqrt( 2/5 ) )
        g = bases + s1 + VGroup( axes )
        self.add( g )
        self.begin_ambient_camera_rotation( rate = 1.0 )
        self.wait( 4 )
        self.stop_ambient_camera_rotation( )
        self.wait( 1 )
        self.play( FadeOut( g ) )


# vim: et sw=4 ts=4
