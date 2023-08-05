from helper import *

class m05_position( ThreeDScene ):
    def construct( self ):

        text3d = Text("Rotation bivector")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)

        axes = ThreeDAxes()
        self.set_camera_orientation( phi = 75 * DEGREES, theta = (90 -60) * DEGREES, zoom = 3 )

        o = ORIGIN
        #s = 2
        t = math.pi/4
        p = math.pi/3
        x  = np.array( [ math.sin(t) * math.cos(p), math.sin(t) * math.sin(p), math.cos(t) ] )
        e1 = np.array( [ 1, 0, 0 ] )
        e2 = np.array( [ 0, 1, 0 ] )
        e3 = np.array( [ 0, 0, 1 ] )
        ve1 = Arrow( start = o, end = e1, buff = 0, color = BLUE )
        ve2 = Arrow( start = o, end = e2, buff = 0, color = BLUE )
        ve3 = Arrow( start = o, end = e3, buff = 0, color = BLUE )
        vx  = Arrow( start = o, end = x, buff = 0, color = WHITE )
        #e1t = MathTex( vec_e1 )
        #e1t.move_to( e1 )
        #e2t = MathTex( vec_e2 )
        #e2t.move_to( e2 )
        #e3t = MathTex( vec_e3 )
        #e3t.move_to( e3 )
        bases = VGroup( ve1, ve2, ve3, vx )
        #, e1t, e2t, e3t )
        #ul = MathTex( vecu )
        #ul.move_to( s * p1 )
        #vl = MathTex( vecv )
        #vl.move_to( o + s* (p1 + p2) )

        #sq1 = [ o, o + s * p1, o + s *( p1 + p2), o + s * p2 ]
        #s1 = OrientedPolygon( *sq1, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )

        #p = -np.arccos( math.sqrt( 2/5 ) )
        g = bases + VGroup( axes )
        self.add( g )
        self.wait( 5 )

        projx = np.array( [ math.sin(t) * math.cos(p), math.sin(t) * math.sin(p), 0 ] )
        projxdir = np.array( [ math.cos(p), math.sin(p), 0 ] )
        proj = Line3D( start = o, end = projxdir, color = RED )
        le3 = Line3D( start = o, end = e3, color = GREEN )
        rej  = Line( start = projx, end = x, color = BLUE )
        #e1l = Line( start = o, end = e3, buff = 0 )
        #a = Angle( e1l, proj, radius = 1 )
        self.play( AnimationGroup( Write( proj ), Write( rej ) ) )
        #self.add(a)   
        t2 = MathTex( concat( vec_e1, r'e^{i\theta}' ) )
        t2.move_to(text3d).shift( 1.0 * DOWN ).set_color( RED )
        self.add_fixed_in_frame_mobjects( t2 )
        self.wait( 5 )

        self.play( Write( le3 ) )
        t3 = MathTex( concat( vec_e3 ) )
        t3.move_to(t2).shift( 1.0 * DOWN ).set_color( GREEN )
        self.add_fixed_in_frame_mobjects( t3 )
        self.wait( 5 )

        le4 = Arrow( start = e3, end = np.array( [ math.cos(p), math.sin(p), 1 ] ), color = BLUE, buff = 0 )
        le5 = Arrow( start = np.array( [ math.cos(p), math.sin(p), 1 ] ), end = projxdir, color = BLUE, buff = 0 )
        self.play( AnimationGroup( Write( le4 ), Write( le5 ) ) )
        self.wait( 5 )

        t4 = MathTex( concat( r'j = ', vec_e3, vec_e1, r'e^{i\phi}' ) )
        t4.move_to(t3).shift( 2.0 * DOWN ).set_color( BLUE )
        self.add_fixed_in_frame_mobjects( t4 )
        self.wait( 5 )

        self.begin_ambient_camera_rotation( rate = 1.0 )
        self.wait( 4 )
        self.stop_ambient_camera_rotation( )
        self.wait( 5 )

        fadeall( self )
