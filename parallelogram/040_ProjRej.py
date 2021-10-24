from helper import *

class ProjRej( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )

        labels = DrawVectorsAndProjRej( self, 0 )

        eq = MathTex( concat( vecv, r' &= ', vecv, r'\times 1', l.newline ),
                      concat( r' &= ', vecv, l.lr( vecu, invu ), l.newline ),
                      concat( r' &= ', l.lr( vecv, vecu ), invu, l.newline ),
                      concat( r' &= ', l.lr( l.add( vdotu, vwedgeu ) ), invu, l.newline ),
                      concat( r' &= ', l.add( proj, rej ), l.newline ) )

        eq.shift( 2 * RIGHT )
        for item in eq:
           self.play( Write( item ) )
           self.wait( 7 )
        self.wait( 1 )

        o = np.array( [ -4, -2, 0 ] )
        p1 = dv_p1
        p2 = dv_p2

        ulen = np.linalg.norm( p1 )
        ucap = p1 / ulen
        n_udotv = np.dot( p1, p2 )
        uinverse = ucap / ulen

        a_u = Arrow( start = o, end = o + p1, buff = 0, color = PURPLE )
        l_u = MathTex( vecu )
        l_u.move_to( a_u, LEFT )
        l_u.shift( 0.6 * LEFT + 0.8 * DOWN )
        l_u.set_color( PURPLE )
        self.play( AnimationGroup( Write( a_u ), Write( l_u ) ) )
        self.wait( 2 )

        a_ucap = Arrow( start = o, end = o + ucap, buff = 0, color = PURPLE )
        l_ucap = MathTex( hatu )
        l_ucap.move_to( l_u )
        l_ucap.set_color( PURPLE )
        g1 = VGroup( a_u, l_u )
        g2 = VGroup( a_ucap, l_ucap )
        self.play( ReplacementTransform( g1, g2 ) )
        self.wait( 2 )

        a_uinverse = Arrow( start = o, end = o + uinverse, buff = 0, color = PURPLE )
        l_uinverse = MathTex( l.inv( vecu ) )
        l_uinverse.move_to( l_u )
        l_uinverse.set_color( PURPLE )
        g3 = VGroup( a_uinverse, l_uinverse )
        self.play( ReplacementTransform( g2, g3 ) )
        self.wait( 2 )

        v_proj = uinverse * n_udotv
        a_proj = Arrow( start = o, end = o + v_proj, buff = 0, color = PURPLE )
        l_proj = MathTex( proj )
        l_proj.move_to( l_u )
        l_proj.shift( LEFT )
        l_proj.set_color( PURPLE )
        g4 = VGroup( a_proj, l_proj )
        self.play( ReplacementTransform( g3, g4 ) )
        self.wait( 2 )
        projl = MathTex( proj )
        projl.set_color( PURPLE )
        projl.move_to( labels[ 0 ] )
        self.play( ReplacementTransform( VGroup( labels[0] ) + g4, projl ) )
        self.wait( 7 )

        o2 = o + DOWN + RIGHT
        a_uinverse2 = Arrow( start = o2, end = o2 + uinverse, buff = 0, color = GREEN )
        l_uinverse2 = MathTex( l.inv( vecu ) )
        l_uinverse2.move_to( a_uinverse2 )
        l_uinverse2.set_color( GREEN )
        l_uinverse2.shift( LEFT )
        g3p = VGroup( a_uinverse2, l_uinverse2 )

        self.play( AnimationGroup( Write( a_uinverse2 ), Write( l_uinverse2 ) ) )
        self.wait( 1 )
        v_rej = p2 - v_proj
        a_rej = Arrow( start = o2, end = o2 + v_rej, buff = 0, color = GREEN )
        l_rej = MathTex( rej )
        l_rej.move_to( a_rej )
        l_rej.shift( LEFT + DOWN )
        l_rej.set_color( GREEN )
        g5 = VGroup( a_rej, l_rej )
        self.play( ReplacementTransform( g3p, g5 ) )
        self.wait( 2 )
        rejl = MathTex( rej )
        rejl.set_color( GREEN )
        rejl.move_to( labels[ 1 ] )
        rejl.shift( 0.5 * RIGHT )
        self.play( ReplacementTransform( VGroup( labels[1] ) + g5, rejl ) )
        self.wait( 3 )



# vim: et sw=4 ts=4
