from mycolors import *

class m020_lineintegral( Scene ):
    def construct( self ):

        title = Text( "Line integrals." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }} (a_1)" ),
               cMathTex( r"{{ \mathbf{x} }}_1 = {\partial {{ \mathbf{x} }} \over \partial a_1}" ),
               cMathTex( r"d^1{{ \mathbf{x} }} = {{ \mathbf{x} }}{}_1\, da_1" ),
               cMathTex( r"\int F d^1{{ \mathbf{x} }} G" ) ]

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

        title2 = Text( "Line integrals: examples." )
        title2.move_to( title ).shift( 0 * LEFT )
        title2.set_color( BLUE )
        self.play( AnimationGroup( FadeOut( *g ), ReplacementTransform( title, title2 ) ) )

        eq2 = [ cMathTex( r"{{ \mathbf{x} }}(a) = (1/2) a^2 \mathbf{e}_2" ),
                cMathTex( r"{{ \mathbf{x} }}_1 = a \mathbf{e}_2" ),
                cMathTex( r"d^1 {{ \mathbf{x} }} = a \mathbf{e}_2 da,\quad F = \mathbf{e}_1, \quad G = \mathbf{e}_3" ),
                cMathTex( r"\int_0^{A} F d^1 x G =" ),
                cMathTex( r"\int_0^{A} \mathbf{e}_1 a \mathbf{e}_2 da \mathbf{e}_3" ),
                cMathTex( r"\mathbf{e}_{123} \int_0^{A} a da" ),
                cMathTex( r"{A \mathbf{e}_{123} \over 2}" ) ]

        eq2[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.5 * LEFT
            if i == 0:
                sh += 0.00 * DOWN + 0.60 * RIGHT
            if i == 1:
                sh += 0.00 * DOWN + 1.00 * LEFT
            if i == 2:
                sh += 0.20 * DOWN + 0.00 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )
        eq2[4].move_to( eq2[3] ).shift( 3.20 * RIGHT )
        self.play( Write( eq2[4] ) )
        self.wait( 1 )
        for i in range(5, 7):
            #print("i = {}".format( i ))
            sh = 0.00 * RIGHT
            #if i == 5:
            #    sh = 1.25 * LEFT
            if i == 6:
                sh = 0.75 * LEFT
            eq2[i].move_to( eq2[4] ).shift( sh )
            self.play( ReplacementTransform( eq2[i-1], eq2[i] ) )
            self.wait( 1 )
        self.play( FadeOut( VGroup( eq2[0], eq2[1], eq2[2], eq2[3], eq2[6] ) ) )
        self.wait( 5 )

        eq3 = [ cMathTex( r"{{ \mathbf{x} }}(\phi) = \mathbf{e}_1 e^{i\phi}, \quad i = \mathbf{e}_{12}" ),
                cMathTex( r"{{ \mathbf{x} }}_1 = \mathbf{e}_2 e^{i\phi}" ),
                cMathTex( r"d^1 {{ \mathbf{x} }} = \mathbf{e}_2 e^{i\phi} d\phi,\quad F = e^{i\phi}, \quad G = \mathbf{e}_3" ),
                cMathTex( r"\int_0^{\pi} F d^1 x G =" ),
                cMathTex( r"\int_0^{\pi} e^{i\phi} \mathbf{e}_2 e^{i\phi} \mathbf{e}_3 d\phi" ),
                cMathTex( r"\int_0^{\pi} \mathbf{e}_2 e^{-i \phi} e^{i\phi} \mathbf{e}_3 d\phi" ),
                cMathTex( r"\int_0^{\pi} \mathbf{e}_{23} d\phi" ),
                cMathTex( r"{ \pi \mathbf{e}_{23} }" ) ]

        eq3[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.5 * LEFT
            if i == 0:
                sh += 0.00 * DOWN + 0.20 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.00 * LEFT
            if i == 2:
                sh += 0.20 * DOWN + 0.00 * LEFT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 1 )
        eq3[4].move_to( eq3[3] ).shift( 3.70 * RIGHT )
        self.play( Write( eq3[4] ) )
        self.wait( 1 )
        for i in range(5, 8):
            sh = 0.00 * LEFT
            if i == 6:
                sh = 0.75 * LEFT
            if i == 7:
                sh = 1.50 * LEFT
            eq3[i].move_to( eq3[4] ).shift( sh )
            self.play( ReplacementTransform( eq3[i-1], eq3[i] ) )
            self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
