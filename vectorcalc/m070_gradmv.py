from mycolors import *

class m070_gradmv( Scene ):
    def construct( self ):

        title = Text( "Gradient of products." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq0 = cMathTex( r"A \in \bigwedge {}^k" )
        eq0.next_to( title, DOWN )
        self.play( Write( eq0 ) )

        eq1 = [ [ cMathTex( r"\boldsymbol{\nabla} (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} f)A + f (\boldsymbol{\nabla} A)" ) ] ]
        eq2 = [ [ cMathTex( r"\boldsymbol{\nabla} \cdot (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} f) \cdot A + f (\boldsymbol{\nabla} \cdot A)" ) ] ]
        eq3 = [ [ cMathTex( r"\boldsymbol{\nabla} \wedge (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} f) \wedge A + f (\boldsymbol{\nabla} \wedge A)" ) ] ]
        eq4 = [ [ cMathTex( r"\boldsymbol{\nabla} \times (f A)" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} f) \times A + f (\boldsymbol{\nabla} \times A)" ) ] ]

        aligned( self, eq1, eq0, 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq2, eq1[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )
        aligned( self, eq3, eq2[0][1], 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )

        eq5 = cMathTex( r"{{ \mathbf{a} }} \in \mathbb{R}^3,\quad {{ \mathbf{b} }} \wedge {{ \mathbf{c} }} = I( {{ \mathbf{b} }} \times {{ \mathbf{c} }})" )
        eq5.next_to( eq4[0][1], DOWN )
        self.play( Write( eq5 ) )
        self.wait( 1 )

        eq6 = [ [ cMathTex( r"\boldsymbol{\nabla} \times (f {{ \mathbf{a} }})" ),
                  cMathTex( r"=" ),
                  cMathTex( r"(\boldsymbol{\nabla} f) \times {{ \mathbf{a} }} + f (\boldsymbol{\nabla} \times {{ \mathbf{a} }})" ) ] ]
        aligned( self, eq6, eq5, 0.0 * LEFT + 0.2 * DOWN, 0.3 * DOWN, 1, 1 )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
