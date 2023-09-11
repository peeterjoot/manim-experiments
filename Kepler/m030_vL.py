from helper import *

class m030_vL( Scene ):
    def construct( self ):

        title = MathTex( r"\mbox{What is this}\, \mathbf{v} L\, \mbox{multivector?}" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m M} } \mathbf{v} L - \mathbf{e}" ),
               MathTex( r"\mathbf{v} L = \mathbf{v} (\mathbf{x} \wedge \mathbf{p}) " ),
               MathTex( r"             = \mathbf{v} \cdot (\mathbf{x} \wedge \mathbf{p}) + m \mathbf{v} \wedge (\mathbf{x} \wedge \mathbf{v}) " ),
               MathTex( r"             = \mathbf{v} \cdot (\mathbf{x} \wedge \mathbf{p})" ),
               MathTex( r"             = (\mathbf{v} \cdot \mathbf{x}) \mathbf{p} - (\mathbf{v} \cdot \mathbf{p}) \mathbf{x}" ) ]
        eq[0].shift( 1.50 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} \mathbf{r} \wedge \mathbf{p}" ),
        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} L" )
        eq2 = [ MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ) ]
        eq2[0].move_to( eq[0] ).shift( 0.10 * DOWN + 5.50 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        for i in range(4):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.30 * DOWN + 0.40 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.80 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 0.41 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
