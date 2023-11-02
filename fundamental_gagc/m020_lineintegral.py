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

        fadeall( self )

# vim: et sw=4 ts=4
