from mycolors import *

class m050_vectorderivative( Scene ):
    def construct( self ):

        title = Text( "Reciprocal basis, and vector derivative." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }} (a_1, a_2, \cdots, a_k)" ),
               cMathTex( r"{{ \mathbf{x} }}_{i} = {\partial {{ \mathbf{x} }} \over \partial a_i}" ),
               cMathTex( r"I^k = {{ \mathbf{x} }}{}_{1} \wedge {{ \mathbf{x} }}{}_{2} \cdots \wedge {{ \mathbf{x} }}{}_{k},\quad d^k {{ \mathbf{x} }} = I^k \, da_1 da_2 \cdots da_k" ),
               cMathTex( r"{{ \mathbf{x} }}^{i} \cdot {{ \mathbf{x} }}_{j} = {\delta^i}_j, \textrm{where}\, {{ \mathbf{x} }}^{i} \in \textrm{span}\{ {{ \mathbf{x} }}_{1}, {{ \mathbf{x} }}_{2}, \cdots \}" ),
               cMathTex( r"\boldsymbol{\partial} = \sum_{i = 0}^k {{ \mathbf{x} }}^{i} {\partial \over \partial a_i} = \boldsymbol{\nabla} \cdot I^k {1 \over I^k}" ) ]

        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        for i in range(4):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.62 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 3.00 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.00 * RIGHT
            if i == 3:
                sh += 0.30 * DOWN + 0.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )

        #g = VGroup( *eq )
        #self.play( g.animate.shift(4.00 * LEFT), run_time=1, rate_func=linear )
        #self.wait( 8 )

        fadeall( self )

# vim: et sw=4 ts=4
