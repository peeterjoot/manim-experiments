from helper import *

class m020_Multivector ( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra: The multivector.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = AcolorsMathTex( concat( r'M = \alpha ', '+ a ', vec_e1, ' + b ', vec_e2, r' + \beta', vec_e1, vec_e2 ) );
        eq.move_to( UP * 2.0 )
        self.play( Write( eq ) )
        self.wait( 5 )

        eq2 = [ AcolorsMathTex( concat( l.gpgradezero('M'), '= ', l.gpgrade('M', n = 0), r' = \alpha' ) ),
                AcolorsMathTex( concat( l.gpgradeone('M'), '= a ', vec_e1, ' + b ', vec_e2 ) ),
                AcolorsMathTex( concat( l.gpgradetwo('M'), r'=\beta', vec_e1, vec_e2 ) ) ]
        eq2[0].shift( 1.0 * UP + 1.5 * LEFT )

        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(2):
            write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )
        self.play( FadeOut( VGroup(*eq2) ) )
        #eq2p = eq2.copy()
        #eq2p[0].shift( 0.0 * UP + 3 * LEFT )
        #eq2p[1].shift( 0.0 * UP + 3 * LEFT )
        #eq2p[2].shift( 0.0 * UP + 3 * LEFT )
        #self.play( ReplacementTransform( VGroup(*eq2), VGroup(*eq2p) ) )
        #self.wait( 5 )

        eqp = [ AcolorsMathTex( concat( r'M = ', l.gpgradezero('M'), '+', l.gpgradeone('M'), '+', l.gpgradetwo('M') ) ),
                AcolorsMathTex( concat( r'N = ', l.gpgradezero('N'), '+', l.gpgradeone('N'), '+', l.gpgradetwo('N') ) ) ]
        eqp[0].move_to( eq[0] )
        #eqp[0].shift( 1.0 * RIGHT )
        self.play( ReplacementTransform( eq, eqp[0] ) )
        self.wait( 5 )

        for i in range(0,1):
            write_aligned( self, eqp[i], eqp[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )

        eq3 = AcolorsMathTex( concat( r'\textrm{Let}\quad M_r = ', l.gpgrade('M', n = 'r'), r',\quad N_s = ', l.gpgrade('N', n = 's') ) )
        self.play( Write( eq3 ) )
        self.wait( 5 )
    
        eq4 = [ AcolorsMathTex( concat( r'M_r \cdot N_s \equiv', l.gpgrade( 'M_r N_s', n = r'\lvert {r - s} \rvert' ) ) ),
                AcolorsMathTex( concat( r'M_r \wedge N_s \equiv', l.gpgrade( 'M_r N_s', n = 'r + s' ) ) ) ]

        eq4[0].shift( 1.0 * DOWN + 0.0 * LEFT )
        self.play( Write( eq4[0] ) )
        self.wait( 5 )
        eq4[1].shift( 2.0 * DOWN + 0.0 * LEFT )
        self.play( Write( eq4[1] ) )
        self.wait( 5 )
        eq4p0 = eq4[0].copy().shift( 3.0 * LEFT + 1.5 * UP )
        eq4p1 = eq4[1].copy().shift( 3.0 * RIGHT + 2.5 * UP )
        self.play( FadeOut( eq3 ) )
        self.play( ReplacementTransform( VGroup(*eq4), VGroup(eq4p0, eq4p1) ) )
        eqpp = AcolorsMathTex( concat( r'M = \sum_k ', l.gpgrade('M', n = 'k'), r' = \sum_k M_k', 
                                       r',\quad N = \sum_k ', l.gpgrade('N', n = 'k'), r' = \sum_k N_k' ) )
        eqpp.move_to( eqp[0] ).shift( 0.0 * LEFT + 0.5 * DOWN )
        self.play( ReplacementTransform( VGroup(*eqp), eqpp ) )
        self.wait( 5 )

        #eq5 = [ AcolorsMathTex( concat( l.gpgradezero( 'M N' ), ' = ', 

        fadeall( self )

# vim: et sw=4 ts=4
