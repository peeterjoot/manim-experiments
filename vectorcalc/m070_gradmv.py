from mycolors import *

class m070_gradmv( Scene ):
    def construct( self ):

        title = Text( "Gradient of products." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq0 = cMathTex( r"A \in \bigwedge^k" )
        eq0.next_to( title, DOWN )
        self.play( Write( eq0 ) )

        eq1 = [ [ cMathTex( r"\boldsymbol{\nabla} (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\spacegrad f)A + f (\spacegrad A)" ) ] ]
        eq2 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\spacegrad f) \cdot A + f (\spacegrad \cdot A)" ) ] ]
        eq3 = [ [ cMathTex( r"\boldsymbol{\nabla} \wedge (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\spacegrad f) \wedge A + f (\spacegrad \wedge A)" ) ] ]
        eq4 = [ [ cMathTex( r"\boldsymbol{\nabla} \cross (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\spacegrad f) \cross A + f (\spacegrad \cross A)" ) ] ]

        aligned( self, eq1, eq0, 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq2, eq1[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq3, eq2[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq4, eq3[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
