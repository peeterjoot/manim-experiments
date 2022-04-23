from helper import *



class ProjRej( Scene ):
    def construct( self ):

        o = np.array( [ 0, -2, 0 ] )
        dv_p1 = np.array( [ 3, 1, 0 ] )
        dv_p2 = np.array( [ 1, 3, 0 ] )
        op1 = o + dv_p1
        op2 = o + dv_p2

        p1cap = dv_p1/ np.linalg.norm( dv_p1 )
        proj = np.dot( dv_p2, p1cap ) * p1cap
        oproj = o + proj

        vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
        vprojl = Text( 'Proj' )
        vprojl.set_color( PURPLE )
        vprojl.next_to( vproj, DOWN )

        rej = dv_p2 - proj
        vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
        vrejl = Text( 'Rej' )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, 0.2 * RIGHT )

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
        v1l = MathTex( vecu )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v1l.shift( 0.5 * LEFT )
        v2l = MathTex( vecv )
        v2l.set_color( YELLOW )
        v2l.next_to( v2, UP )
        v2l.shift( 0.5 * DOWN )

        all = VGroup( v1, v1l, v2, v2l, vproj, vrej, vprojl, vrejl )

        move = ( -6.5, 2, 0 )
        all.shift( move )

        self.add( all )


        title = Text( 'Projective and rejective split.' )
        #.scale(0.75)
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )
        self.play( Indicate( VGroup( v2, v2l ) ) ) # v
        self.wait( 5 )
        self.play( Indicate( VGroup( v1, v1l ) ) ) # u
        self.wait( 5 )
        self.play( Indicate( VGroup( vproj, vprojl ) ) )
        self.wait( 5 )
        self.play( Indicate( VGroup( vrej, vrejl ) ) )
        self.wait( 5 )

        projr       = l.mult( invu, lr_udotv )
        rejr        = l.mult( invu, lr_uwedgev )
        eq2 = [ AcolorsMathTex( concat( vecv, r' = 1 \times ', vecv, l.newline ) ),
                AcolorsMathTex( concat( ' = ', l.lr( invu, vecu, big = 1 ), vecv, l.newline ) ),
                AcolorsMathTex( concat( ' = ', invu, l.lr( vecu, vecv ), l.newline ) ),
                AcolorsMathTex( concat( ' = ', invu, l.lr( l.add( udotv, uwedgev ) ), l.newline ) ),
                AcolorsMathTex( concat( ' = ', l.add( projr, rejr ), l.newline ) ) ]
        delays1 = [ 8, 5, 7, 4, 4 ]
        #delays2 = [ 0, 0, 0, 0, 0 ]

        eq2[0].shift( 0 * RIGHT + 2.0 * UP )
        i = 0
        self.play( Write( eq2[i]) )
        self.wait( delays1[i] )
        for i in range(4):
           write_aligned( self, eq2[i], eq2[i+1], 1.15 * DOWN, None )
           self.wait( delays1[i+1] )

        self.wait( 4 )
        self.play( FadeOut( *eq2 ) )
        self.wait( 4 )


        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        eq = [ AcolorsMathTex( concat( vecv, ' = ', vecv, r'\times 1', l.newline ) ),
               AcolorsMathTex( concat( ' = ', vecv, l.lr( vecu, invu, big = 1 ), l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.lr( vecv, vecu ), invu, l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.lr( l.add( vdotu, vwedgeu ) ), invu, l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.add( proj, rej ), l.newline ) ) ]

        i = 0
        eq[0].move_to( eq2[0] )
        i = 0
        self.play( Write( eq[i]) )
        #self.wait( delays2[i] )
        for i in range(4):
           write_aligned( self, eq[i], eq[i+1], 1.15 * DOWN, None )
           #self.wait( delays2[i+1] )

        self.wait( 14 )

# vim: et sw=4 ts=4
