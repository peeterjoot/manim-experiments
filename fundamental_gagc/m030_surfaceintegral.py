from mycolors import *

class m030_surfaceintegral( Scene ):
    def construct( self ):

        title = Text( "Surface integrals." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }} (a_1, a_2)" ),
               cMathTex( r"{{ \mathbf{x} }}_1 = {\partial {{ \mathbf{x} }} \over \partial a_1},\quad {{ \mathbf{x} }}_2 = {\partial {{ \mathbf{x} }} \over \partial a_2}" ),
               cMathTex( r"d^2{{ \mathbf{x} }} = {{ \mathbf{x} }}{}_1 \wedge {{ \mathbf{x} }}{}_1\, da_1 da_2" ),
               cMathTex( r"\int F d^2{{ \mathbf{x} }} G" ) ]

        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.98 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.54 * LEFT
            if i == 2:
                sh += 1.00 * DOWN + 1.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )

        g = VGroup( *eq )
        self.play( g.animate.shift(4.00 * LEFT), run_time=1, rate_func=linear )
        self.wait( 8 )

        title2 = Text( "Surface integrals: example." )
        title2.move_to( title ).shift( 0 * LEFT )
        title2.set_color( BLUE )
        self.play( AnimationGroup( FadeOut( *g ), ReplacementTransform( title, title2 ) ) )

        eq2 = [ cMathTex( r"{{ \mathbf{x} }}(r,\phi) = r \mathbf{e}_1 e^{i\phi}, \quad i = \mathbf{e}_{12}" ),
                cMathTex( r"{{ \mathbf{x} }}_1 = \mathbf{e}_1 e^{i\phi}, \quad {{ \mathbf{x} }}_2 = r \mathbf{e}_2 e^{i\phi}" ),
                cMathTex( r"d^2 {{ \mathbf{x} }} = r \mathbf{e}_{12} dr d\phi,\quad F = \mathbf{e}_1 + \mathbf{e}_{13} , \quad G = \mathbf{e}_{21}" ),
                cMathTex( r"\int_{r = 0}^R \int_{\phi = 0}^{\pi} F d^2 x G =" ),
                cMathTex( r"\int_{r = 0}^R \int_{\phi = 0}^{\pi} ( \mathbf{e}_1 + \mathbf{e}_{13} ) r \mathbf{e}_{12} dr d\phi \mathbf{e}_{21}" ),
                cMathTex( r"\int_{r = 0}^R \int_{\phi = 0}^{\pi} ( \mathbf{e}_1 + \mathbf{e}_{13} ) r dr d\phi" ),
                cMathTex( r"{ {\pi R^2 \mathbf{e}_1 } \over 2 } ( 1 + \mathbf{e}_{3} )" ) ]

        eq2[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.5 * LEFT
            if i == 0:
                sh += 0.00 * DOWN + 0.20 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.00 * LEFT
            if i == 2:
                sh += 0.20 * DOWN + 2.00 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )

        eq2[4].move_to( eq2[3] ).shift( 5.60 * RIGHT )
        self.play( Write( eq2[4] ) )
        self.wait( 1 )
        for i in range(5, 7):
            sh = 0.00 * LEFT
            print("i = {}".format( i ))
            if i == 5:
                sh += 0.60 * LEFT
            if i == 6:
                sh += 1.10 * LEFT
            eq2[i].move_to( eq2[4] ).shift( sh )
            self.play( ReplacementTransform( eq2[i-1], eq2[i] ) )
            self.wait( 1 )

        self.wait( 5 )
        fadeall( self )


# vim: et sw=4 ts=4
