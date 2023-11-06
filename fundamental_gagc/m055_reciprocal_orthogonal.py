from mycolors import *
import random

class m055_reciprocal_orthogonal( Scene ):
    def construct( self ):

        title = Text( "Reciprocal basis: orthogonal case." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\textrm{Theorem: If}\, {{ \mathbf{x} }}_i \cdot {{ \mathbf{x} }}_j = 0,\, \textrm{for}\, i \ne j" ),
               cMathTex( r"{{ \mathbf{x} }}^i = { 1 \over { {{ \mathbf{x} }}_i } }" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        eq[1].move_to( eq[0] ).shift( 1 * DOWN )
        self.play( Write( eq[1] ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) {}^2 = ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \cdot ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2)" ),
                cMathTex( r"= {{ \mathbf{x} }}_1 \cdot ({{ \mathbf{x} }}_2 \cdot ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2))" ),
                cMathTex( r"= {{ \mathbf{x} }}_1 \cdot (-{{ \mathbf{x} }}_1 ({{ \mathbf{x} }}_2){}^2 )" ),
                cMathTex( r"= -{{ \mathbf{x} }}_1 {}^2 {{ \mathbf{x} }}_2 {}^2" ) ]
        eq2[0].move_to( eq[1] ).shift( 1 * DOWN )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.69 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )
        self.wait( 2 )
        self.play( FadeOut( *eq2 ) )

        eq3 = [ MathTex( r"( \mathbf{x}_1 \wedge  \mathbf{x}_2 ){}^{-1} =  \mathbf{x}_1 \wedge  \mathbf{x}_2 \Bigl({ -1 \over {  \mathbf{x}_1 {}^2  \mathbf{x}_2 {}^2 } }\Bigr)" ),
                MathTex( r"= { {  \mathbf{x}_2 } \over {  \mathbf{x}_2 {}^2 } } \wedge { {  \mathbf{x}_1 } \over {  \mathbf{x}_1 {}^2 } }" ),
                MathTex( r"= { 1 \over {  \mathbf{x}_2 } } \wedge { 1 \over {  \mathbf{x}_1 } }" ) ]
        eq3[0].move_to( eq[1] ).shift( 1.40 * DOWN )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.30 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 2.65 * RIGHT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 1 )
        self.wait( 2 ) 
        self.play( FadeOut( *eq3 ) )
        self.wait( 5 ) 

        eq4 = [ MathTex( r"\mathbf{x}^1 = \mathbf{x}_2 \cdot ( \mathbf{x}_1 \wedge  \mathbf{x}_2 ){}^{-1}" ),
                MathTex( r"= \mathbf{x}_2 \cdot \Bigl( { 1 \over {  \mathbf{x}_2 } } \wedge { 1 \over {  \mathbf{x}_1 } } \Bigr)" ),
                MathTex( r"= \Bigl( \mathbf{x}_2 \cdot { 1 \over \mathbf{x}_2 }\Bigr) { 1 \over {  \mathbf{x}_1 } } - \Bigl( \mathbf{x}_2 \cdot { 1 \over \mathbf{x}_1 }\Bigr) { 1 \over {  \mathbf{x}_2 } }" ),
                MathTex( r"= { 1 \over { \mathbf{x}_1 } }" ) ]
        eq4[0].move_to( eq[1] ).shift( 1.20 * DOWN )
        self.play( Write( eq4[0] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.10 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.66 * RIGHT
            if i == 1:
                sh += 0.30 * DOWN + 0.00 * RIGHT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 1 )
        eq4[3].move_to( eq4[2], LEFT )
        self.play( ReplacementTransform( eq4[2], eq4[3] ) )
        #self.wait( 2 ) 
        #self.play( FadeOut( *eq4 ) )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
