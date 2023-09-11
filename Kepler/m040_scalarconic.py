from helper import *

class m040_scalarconic( Scene ):
    def construct( self ):

        title = Text( r"Conic equation, polar form." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m^2 M} } \mathbf{p} L - \mathbf{e}" ),
               MathTex( r"\mathbf{x} \cdot \mathbf{\hat{r}} = -{1 \over {G m^2 M} } \mathbf{x} \cdot (\mathbf{p} L) - \mathbf{x} \cdot \mathbf{e}" ),
               MathTex( concat( r"                                r = -{1 \over {G m^2 M} }", l.gpgradezero( " \mathbf{x} \mathbf{p} L " ), r" - r e \cos\theta" ) ),
               MathTex( concat( r"                                r = -{1 \over {G m^2 M} }", l.gpgradezero( " (\mathbf{x} \cdot \mathbf{p} + \mathbf{x} \wedge \mathbf{p}) L " ), r" - r e \cos\theta" ) ) ]
        eq[0].shift( 1.50 * UP + 0.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( r"\mathbf{x} = r \mathbf{\hat{r}" ),
                MathTex( concat( r"\mathbf{a} \cdot \mathbf{b} = ", l.gpgradezero(r"\mathbf{a}", r"\mathbf{b}") ) ),
                MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ) ]
        eq2[0].move_to( eq[0] ).shift( 0.10 * DOWN + 5.50 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        i = 0
        sh = 1.30 * DOWN + 0.62 * LEFT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )

        i = 0
        sh = 1.00 * DOWN + 0.62 * LEFT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 5 )

        i = 1
        sh = 1.30 * DOWN + 0.00 * LEFT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )

        i = 2
        sh = 1.30 * DOWN + 0.00 * LEFT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 5 )

        i = 1
        sh = 1.00 * DOWN + 0.00 * LEFT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 5 )

        eq4 = [ MathTex( concat( r" r = -{1 \over {G m^2 M} }", l.gpgradezero( " (\mathbf{x} \cdot \mathbf{p} + \mathbf{x} \wedge \mathbf{p}) L " ), r" - r e \cos\theta" ) ),
                MathTex( concat(    r"= -{1 \over {G m^2 M} }", l.gpgradezero( " (\mathbf{x} \wedge \mathbf{p}) L " ), r" - r e \cos\theta" ) ),
                MathTex(            r"= -{L^2 \over {G m^2 M} } - r e \cos\theta" ) ]
        #eq4s = [ MathTex( r"L = \mathbf{x} \wedge \mathbf{p}" ) ]
        eq4[0].move_to( eq[0] ).shift( 0.20 * DOWN + 2.00 * RIGHT )
        #eq4s[0].move_to( eq4[0] )
        self.play( ReplacementTransform( VGroup(*eq), VGroup(eq4[0]) ) )
        #self.play( ReplacementTransform( VGroup(*eq, *eq4), VGroup(eq4s[0], eq4[0]) ) )
        self.wait( 5 )

        for i in range(2):
            sh = 1.30 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.40 * RIGHT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 5 )

        eq5 = [ MathTex( r"r (1 + e \cos\theta) = -{L^2 \over {G m^2 M} }" ),
                MathTex( r"                     = e d" ) ]
        eq5[0].move_to( eq4[0] ).shift( 2.00 * LEFT )
        self.play( AnimationGroup( FadeOut( VGroup(*eq2) ),
                                   ReplacementTransform( VGroup(*eq4), eq5[0] ) ) )
        self.wait( 5 )

        i = 0
        sh = 1.00 * DOWN + 2.90 * RIGHT
        write_aligned( self, eq5[i], eq5[i+1], sh, None )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
