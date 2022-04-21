from helper import *

waittime = 2

class Rejvisualization( ThreeDScene ):
    def construct( self ):

        axes = ThreeDAxes( )

        #o = [ -3.0, -2.0, 0 ]
        o = 0.5 * np.array( [ 1, 1, 1 ] )
        du = np.array( [ 3, 1, 0 ] )
        dv = np.array( [ 1, 3, 0 ] )
        ou = o + du
        ov = o + dv

        ucapdir = du/ np.linalg.norm( du )
        oucap = o + ucapdir
        proj = np.dot( dv, ucapdir ) * ucapdir
        oproj = o + proj

        rej = dv - proj
        rejdir = rej/ np.linalg.norm( rej )

        cross1 = np.cross( dv, ucapdir )
        cross1len = np.linalg.norm( cross1 )
        cross1cap = cross1 / cross1len

        orejcap = o + rejdir
        orej = o + rej
        ocross1cap = o + cross1cap
        ocross1 = o + cross1
        #print( "dump" )
        #print( rejdir )
        #print( cross1cap )

        vrej    = Arrow( start = oproj, end = ov, color = GREEN, buff = 0 )
        au      = Arrow( start = o, end = ou, buff = 0, color = RED )
        aucap   = Arrow( start = o, end = oucap, buff = 0, color = RED )
        arejcap = Arrow( start = o, end = orejcap, buff = 0, color = GREEN )
        av      = Arrow( start = o, end = ov, buff = 0, color = YELLOW )
        arej    = Arrow( start = o, end = orej, buff = 0, color = GREEN )
        an1     = Arrow( start = o, end = ocross1cap, buff = 0, color = GREEN )
        an2     = Arrow( start = o, end = ocross1, buff = 0, color = GREEN )

        all = VGroup( axes, au, av, vrej )

        self.set_camera_orientation( phi = 45 * DEGREES, theta = -60 * DEGREES )
        self.add( all )
        self.wait( 18 )

        aucap2 = aucap.copy()
        self.play( ReplacementTransform( au, aucap ) )
        self.wait( 24/4 )
        self.add( aucap2 )
        self.play( ReplacementTransform( aucap2, an1 ) )
        self.wait( 24/4 )
        self.play( ReplacementTransform( an1, an2 ) )
        self.wait( 24/4 )
        self.play( ReplacementTransform( an2, arej ) )
        self.wait( 24/4 )


# vim: et sw=4 ts=4
