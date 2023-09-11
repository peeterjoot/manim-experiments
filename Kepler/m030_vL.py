from helper import *

class m030_vL( Scene ):
    def construct( self ):

        title = MathTex( r"\mbox{What is this}\, \mathbf{v} L\, \mbox{multivector?}" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m M} } \mathbf{v} L - \mathbf{e}" ),
               MathTex( r"m \mathbf{v} L = \mathbf{p} (\mathbf{x} \wedge \mathbf{p}) " ),
               MathTex( r"             = \mathbf{p} \cdot (\mathbf{x} \wedge \mathbf{p}) + \mathbf{p} \wedge (\mathbf{x} \wedge \mathbf{p}) " ),
               MathTex( r"             = \mathbf{p} \cdot (\mathbf{x} \wedge \mathbf{p})" ),
               MathTex( r"             = (\mathbf{p} \cdot \mathbf{x}) \mathbf{p} - (\mathbf{p} \cdot \mathbf{p}) \mathbf{x}" ) ]
        eq[0].shift( 1.50 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ),
                MathTex( r"\mathbf{x} = r \mathbf{\hat{r}}" ) ]
        eq2[0].move_to( eq[0] ).shift( 0.10 * DOWN + 5.50 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        for i in range(4):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.30 * DOWN + 0.90 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.24 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 0.41 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} \mathbf{r} \wedge \mathbf{p}" ),
        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} L" )
        #eq3 = [ MathTex( r"m \mathbf{v} L = \mathbf{p} L" ),
        #        MathTex( r"               = (\mathbf{\hat{r}} (\mathbf{\hat{r}} \cdot \mathbf{p}) + \mathbf{\hat{r}} (\mathbf{\hat{r}} \wedge \mathbf{p})) L" ) ]
        #        MathTex( r"               = {1 \over r^2} (\mathbf{x} (\mathbf{x} \cdot \mathbf{p}) + \mathbf{x} (\mathbf{x} \wedge \mathbf{p})) L" ),
        #        MathTex( r"               = {1 \over r^2} (\mathbf{x} (\mathbf{x} \cdot \mathbf{p}) + \mathbf{x} L) L" ) ]
        #eq3[0].move_to( eq[1] ).shift( 0.60 * LEFT )
        #self.play( ReplacementTransform( VGroup(eq[1], eq[2], eq[3], eq[4]), eq3[0] ) )
        #self.wait( 5 )

        #i = 0
        #sh = 1.00 * DOWN + 1.20 * RIGHT
        #write_aligned( self, eq3[i], eq3[i+1], sh, None )
        #self.wait( 5 )

        #i = 0
        #sh = 1.00 * DOWN + 0.00 * RIGHT
        #write_aligned( self, eq2[i], eq2[i+1], sh, None )
        #self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
