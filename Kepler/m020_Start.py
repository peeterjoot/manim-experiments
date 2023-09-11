from helper import *

class m020_Start( Scene ):
    def construct( self ):

        title = MathTex( r"\mbox{Starting point:}\, \mathbf{\hat{r}'\, \mbox{derivative}" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} \mathbf{r} \wedge \mathbf{p}" ),
        #MathTex( r"\mathbf{p} = \mathbf{p} \cdot \mathbf{\hat{r}} \mathbf{\hat{r}} + {1 \over r} \mathbf{\hat{r}} L" )
        eq = [ MathTex( r"\mathbf{\hat{r}}' = {1 \over r} \mathbf{\hat{r}} ( \mathbf{\hat{r}} \wedge \mathbf{v} )" ),
               MathTex( r"                  = {1 \over {r^2 m} } \mathbf{\hat{r}} ( \mathbf{x} \wedge \mathbf{p} )" ),
               MathTex( r"                  = {1 \over {m} } {\mathbf{\hat{r}} \over r^2} L" ),
               MathTex( r"                  = -{1 \over {G m M} } {d \mathbf{v} \over {dt} } L" )
             ]
        eq[0].shift( 1.50 * UP + 1.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( r"\mathbf{p} = m \mathbf{v}" ),
                MathTex( r"\mathbf{x} = r \mathbf{\hat{r}}" ),
                MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ),
                MathTex( r"m {d \mathbf{v} \over {dt} } = - G m M {\mathbf{\hat{r}} \over r^2}" ) ]
        eq2[0].move_to( eq[0] ).shift( 0.10 * DOWN + 5.50 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        i = 0
        sh = 1.00 * DOWN + 0.00 * RIGHT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 5 )

        i = 0
        sh = 1.30 * DOWN + 0.50 * RIGHT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )

        i = 1
        sh = 1.00 * DOWN + 0.00 * RIGHT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 5 )

        i = 1
        sh = 1.30 * DOWN + 0.00 * RIGHT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )

        i = 2
        sh = 1.00 * DOWN + 0.80 * LEFT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 5 )

        i = 2
        sh = 1.30 * DOWN + 0.00 * RIGHT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )


        eq3 = [ MathTex( r"{ d \mathbf{\hat{r}} \over {dt } } = -{1 \over {G m M} } {d \mathbf{v} \over {dt} } L" ),
                MathTex( r"                                   = -{1 \over {G m M} } {d (\mathbf{v} L) \over {dt} } - {d L \over {dt} }" ),
                MathTex( r"                                   = -{1 \over {G m M} } {d (\mathbf{v} L) \over {dt} }" ),
                MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m M} } \mathbf{v} L - \mathbf{e}" ) ]
        eq3[0].move_to( eq[0] )
        self.play( AnimationGroup( FadeOut( eq2[3] ),
                                   ReplacementTransform( VGroup(*eq), eq3[0] ) ) )
        self.wait( 5 )

        for i in range(3):
            sh = 1.30 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.75 * RIGHT
            if i == 2:
                sh += 0.00 * DOWN + 0.41 * LEFT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
