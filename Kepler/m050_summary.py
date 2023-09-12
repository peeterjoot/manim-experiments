from helper import *

class m050_summary( Scene ):
    def construct( self ):

        title = Text( r"Summary." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{x} = r \mathbf{\hat{r}}" ),
               MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ),
               MathTex( r"e d = -{L^2 \over {G m^2 M} }" ) ]

        eq2 = [ MathTex( r"\mathbf{\hat{r}}' = {1 \over m} {\mathbf{\hat{r}} \over r^2} L" ),
               MathTex( r"d \mathbf{v} \over {dt}} = -G M {\mathbf{\hat{r}} \over r^2}" ),
               MathTex( r"{ d \mathbf{\hat{r}} \over {dt } } = -{1 \over {G m M} } {d (\mathbf{v} L) \over {dt} }" ),
               MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m^2 M} } \mathbf{p} L - \mathbf{e}" ),
               MathTex( r"r (1 + e \cos\theta) = e d" ) ]
        eq[0].shift( 2.00 * UP + 5.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(1):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.10 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.10 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eq2[0].move_to( eq[0] ).shift( 6.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.00 * DOWN
            if i < 3:
                sh += 0.30 * DOWN
            if i == 0:
                sh += 0.30 * LEFT
            if i == 1:
                sh += 0.10 * RIGHT
            if i == 2:
                sh += 0.35 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        i = 1
        sh = 1.00 * DOWN + 0.10 * LEFT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 15 )

        fadeall( self )

# vim: et sw=4 ts=4
