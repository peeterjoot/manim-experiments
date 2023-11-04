from mycolors import *

class m040_volumeintegral( Scene ):
    def construct( self ):

        title = Text( "Volume integrals." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }} (a_1, a_2, a_3)" ),
               cMathTex( r"{{ \mathbf{x} }}_1 = {\partial {{ \mathbf{x} }} \over \partial a_1},\, {{ \mathbf{x} }}_2 = {\partial {{ \mathbf{x} }} \over \partial a_2},\, \cdots" ),
               cMathTex( r"d^3{{ \mathbf{x} }} = {{ \mathbf{x} }}{}_1 \wedge {{ \mathbf{x} }}{}_2 \wedge {{ \mathbf{x} }}{}_3 \, da_1 da_2 da_3" ),
               cMathTex( r"\int F d^3{{ \mathbf{x} }} G" ) ]

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

        #g = VGroup( *eq )
        #self.play( g.animate.shift(4.00 * LEFT), run_time=1, rate_func=linear )
        #self.wait( 8 )

        title2 = Text( "Volume integrals: example." )
        title2.move_to( title ).shift( 0 * LEFT )
        title2.set_color( BLUE )
        self.play( AnimationGroup( FadeOut( *eq ), ReplacementTransform( title, title2 ) ) )

        eq2 = [ cMathTex( r"{{ \mathbf{x} }}(r, \phi, z) = r \mathbf{e}_1 e^{i\phi} + z \mathbf{e}_3, \quad i = \mathbf{e}_{12}" ),
                cMathTex( r"{{ \mathbf{x} }}_1 = \mathbf{e}_1 e^{i\phi}, \quad {{ \mathbf{x} }}_1 = r \mathbf{e}_2 e^{i\phi}, \quad {{ \mathbf{x} }}_3 = \mathbf{e}_3" ),
                cMathTex( r"d^3 {{ \mathbf{x} }} = r^2 \mathbf{e}_{123}\, dr d\phi dz,\quad F = \mathbf{e}_1, \quad G = z \mathbf{e}_4" ),
                cMathTex( r"\int_{r=0}^{R} \int_{\phi=0}^{\phi} \int_{z=0}^{Z} F d^3 x G =" ),
                cMathTex( r"\int_{r=0}^{R} \int_{\phi=0}^{\phi} \int_{z=0}^{Z} r^2 \mathbf{e}_{234} dr d\phi z dz" ),
                cMathTex( r"{1 \over 6} \mathbf{e}_{234} R^3 \pi Z^2" ) ]

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
                sh += 0.20 * DOWN + 2.00 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )
        eq2[4].move_to( eq2[3], RIGHT ).shift( 6.00 * RIGHT )
        self.play( Write( eq2[4] ) )
        self.wait( 1 )
        i=5
        sh = 0.00 * RIGHT
        eq2[i].move_to( eq2[4], LEFT ).shift( sh )
        self.play( ReplacementTransform( eq2[i-1], eq2[i] ) )
        #self.wait( 1 )
        #self.play( FadeOut( VGroup( eq2[0], eq2[1], eq2[2], eq2[3], eq2[5] ) ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
