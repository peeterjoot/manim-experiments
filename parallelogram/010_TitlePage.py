from helper import *

class TitlePage( ThreeDScene ):
    def construct( self ):
        t = Text( "Geometric algebra: wedge products and area." )
        t.shift( 3 * DOWN )

        self.add_fixed_in_frame_mobjects( t )
        #self.wait( )
        #self.play( FadeOut( t ) )

        #t2 = t.copy()
        #self.play( ReplacementTransform( t, t2 ) )
        #self.remove( t2 )
        #self.add_fixed_in_frame_mobjects( t2 )

        axes = ThreeDAxes( )

        o0 = np.array( [ -2, -2, -1 ] )
        p1 = np.array( [ 1, 1, 1 ] )
        p2 = np.array( [ -1, 1, 0.5 ] )
        sq1 = unitParallelogram( o0, p1, p2, 4 )
        s1 = OrientedPolygon( *sq1, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )

        o1 = np.array( [ 0, 0, -1 ] )
        q1 = np.array( [ 1, -1, 1 ] )
        q2 = np.array( [ 0, 1, 1 ] )
        sq2 = unitParallelogram( o1, q1, q2, 2 )
        s2 = OrientedPolygon( *sq2, c0 = RED, c1 = RED, c2 = RED, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.2 )

        o2 = np.array( [ 0, 0, -2 ] )
        r1 = np.array( [ 1, -0.5, 0 ] )
        r2 = np.array( [ 0, -0.5, 1 ] )
        sq3 = unitParallelogram( o2, r1, r2, 3 )
        s3 = OrientedPolygon( *sq3, c0 = GREEN, c1 = GREEN, c2 = GREEN, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.2 )

        self.set_camera_orientation( phi = 75 * DEGREES, theta = 0 * DEGREES )
        self.add( axes, s1, s2, s3 )
        self.begin_ambient_camera_rotation( rate = 0.5 )
        self.wait( 8 ) # how long to animate the motion.
        # This results in a zippy move at the very end of the smooth rotation:
        #self.move_camera( phi = 75 * DEGREES, theta = 360 * DEGREES )
        self.stop_ambient_camera_rotation( )
        self.wait( 1 )


# vim: et sw=4 ts=4
