from mycolors import *

class m050_reciprocalbasis( Scene ):
    def construct( self ):

        title = Text( "Reciprocal basis." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }}^{i} \cdot {{ \mathbf{x} }}_{j} = {\delta^i}_j, \textrm{where}\, {{ \mathbf{x} }}^{i} \in \textrm{span}\{ {{ \mathbf{x} }}_{1}, {{ \mathbf{x} }}_{2}, \cdots \}" ),
               cMathTex( r"\textrm{Theorem: Given}\, {{ \mathbf{x} }}_1, {{ \mathbf{x} }}_2" ),
               cMathTex( r"{{ \mathbf{x} }} {}^1 = {{ \mathbf{x} }}_2 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1}" ),
               cMathTex( r"{{ \mathbf{x} }} {}^2 = -{{ \mathbf{x} }}_1 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1}." ) ]

        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        eq[1].move_to( eq[0] ).shift( 1.00 * DOWN + 0 * RIGHT )
        self.play( Write( eq[1] ) )
        self.wait( 1 )
        eq[2].move_to( eq[1] ).shift( 1.00 * DOWN + 0 * RIGHT )
        self.play( Write( eq[2] ) )
        self.wait( 1 )
        eq[3].move_to( eq[2] ).shift( 1.00 * DOWN + 0 * RIGHT )
        self.play( Write( eq[3] ) )
        self.wait( 1 )

        g = VGroup( eq[1], eq[2], eq[3] )
        self.play( g.animate.shift(4.00 * LEFT), run_time=1, rate_func=linear )
        self.wait( 8 )

        eq2 = [ cMathTex( r"{{ \mathbf{x} }}_1 \cdot {{ \mathbf{x} }}^1 = \bigl\langle {{ \mathbf{x} }}_1 \Bigl( {{ \mathbf{x} }}_2 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \Bigr) \bigr\rangle" ),
                cMathTex( r"= \bigl\langle {{ \mathbf{x} }}_1 {{ \mathbf{x} }}_2 \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= \bigl\langle ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= 1" ) ]
        eq2[0].move_to( eq[2] ).shift( 0.00 * UP + 6.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.75 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 1.42 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )
        self.wait( 3 )
        self.play( FadeOut( *eq2 ) )
        self.wait( 1 )

        eq3 = [ cMathTex( r"{{ \mathbf{x} }}_2 \cdot {{ \mathbf{x} }}^1 = \bigl\langle {{ \mathbf{x} }}_2 \Bigl( {{ \mathbf{x} }}_2 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \Bigr) \bigr\rangle" ),
                cMathTex( r"= \bigl\langle {{ \mathbf{x} }}_2 {{ \mathbf{x} }}_2 \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= \bigl\langle \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= 0" ) ]
        eq3[0].move_to( eq[2] ).shift( 0.00 * UP + 6.00 * RIGHT )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.75 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 1.42 * LEFT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 1 )
        self.wait( 3 )
        self.play( FadeOut( *eq3 ) )
        self.wait( 1 )

        eq4 = [ cMathTex( r"{{ \mathbf{x} }}_1 \cdot {{ \mathbf{x} }}^2 = - \bigl\langle {{ \mathbf{x} }}_1 \Bigl( {{ \mathbf{x} }}_1 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \Bigr) \bigr\rangle" ),
                cMathTex( r"= - \bigl\langle {{ \mathbf{x} }}_1 {{ \mathbf{x} }}_1 \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= -\bigl\langle \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= 0" ) ]
        eq4[0].move_to( eq[2] ).shift( 0.00 * UP + 6.00 * RIGHT )
        self.play( Write( eq4[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.75 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 1.42 * LEFT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 1 )
        self.wait( 3 )
        self.play( FadeOut( *eq4 ) )
        self.wait( 1 )

        eq5 = [ cMathTex( r"{{ \mathbf{x} }}_2 \cdot {{ \mathbf{x} }}^2 = - \bigl\langle {{ \mathbf{x} }}_2 \Bigl( {{ \mathbf{x} }}_1 \cdot \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \Bigr) \bigr\rangle" ),
                cMathTex( r"= - \bigl\langle {{ \mathbf{x} }}_2 {{ \mathbf{x} }}_1 \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= \bigl\langle ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \bigl( {{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 } \bigr) {}^{-1} \bigr\rangle" ),
                cMathTex( r"= 1." ) ]
        eq5[0].move_to( eq[2] ).shift( 0.00 * UP + 6.00 * RIGHT )
        self.play( Write( eq5[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.75 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            #if i == 3:
            #    sh += 0.00 * DOWN + 1.42 * LEFT
            write_aligned( self, eq5[i], eq5[i+1], sh, None )
            self.wait( 1 )
        self.wait( 3 )
        self.play( FadeOut( *eq5 ) )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
