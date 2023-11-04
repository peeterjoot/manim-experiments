from mycolors import *
import random

class m003_theorem( Scene ):
    def construct( self ):

        title = Text( "Fundamental theorem of geometric calculus." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^k {{ \mathbf{x} }} \boldsymbol{\partial} G = \int_{\partial V} F d^{k-1} {{ \mathbf{x} }} G" ),
               cMathTex( r"\int_V d^k {{ \mathbf{x} }} \cdot (\boldsymbol{\partial} \wedge F) = \int_{\partial V} d^{k-1} {{ \mathbf{x} }} \cdot F" ),
               cMathTex( r"\int_{u_0}^{u_1} d {{ \mathbf{x} }} \cdot (\boldsymbol{\nabla} \mathbf{f}(u) ) = f(u_1) - f(u_0)" ),
               cMathTex( r"\int_S d^2 {{ \mathbf{x} }} \cdot (\boldsymbol{\nabla} f) = \ointctrclockwise_{\partial S} d {{ \mathbf{x} }} f" ),
               cMathTex( r"\int_S dA \hat{\mathbf{n}} \times \boldsymbol{\nabla} f = \ointclockwise_{\partial S} d {{ \mathbf{x} }} f" ),
               cMathTex( r"\int_S dA \hat{\mathbf{n}} \cdot ( \boldsymbol{\nabla} \times \mathbf{f} ) = \ointclockwise_{\partial S} d {{ \mathbf{x} }} \cdot \mathbf{f}" ),
               cMathTex( r"\int_S dx dy \Bigl( {\partial P \over \partial y} - { \partial Q \over \partial x } \Bigr) = \ointctrclockwise_{\partial S} P dx + Q dy" ),
               cMathTex( r"\int_V dV \boldsymbol{\nabla} f = \int_{\partial V} dA \hat{\mathbf{n}} f" ),
               cMathTex( r"\int_V dV \boldsymbol{\nabla} \times \mathbf{f} = \int_{\partial V} dA \hat{\mathbf{n}} \times \mathbf{f}" ),
               cMathTex( r"\int_V dV \boldsymbol{\nabla} \cdot lmathbf{f} = \int_{\partial V} dA \hat{\mathbf{n}} \cdot \mathbf{f}" ) ]

        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        for i in range(1, 9):
            xrand = random.uniform( -3, 3 )
            yrand = random.uniform( 1.8, 5 )
            eq[i].move_to( eq[0] ).shift( xrand * RIGHT + yrand * DOWN )
            if i > 1:
                self.play( AnimationGroup( FadeOut( eq[i-1] ), Write( eq[i] ) ) )
            else:
                self.play( Write( eq[i] ) )
            self.wait( 1 )

        fadeall( self )

# vim: et sw=4 ts=4
