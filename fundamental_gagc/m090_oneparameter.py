from mycolors import *
import random

class m090_oneparameter( Scene ):
    def construct( self ):

        title = Text( "Fundamental theorem of GC: 1 parameter." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^1 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = F G {\vert}_{\Delta V}" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"\int_{u = u_0}^{u_1} F(u) {{ \mathbf{x} }}_1 du\, {{ \mathbf{x} }}^1 { {\stackrel{ \leftrightarrow }{ \partial } } \over { \partial u } } G(u) = \int_{u = u_0}^{u_1} {\partial F(u)G(u) \over {\partial u}}\, du" ),
                cMathTex( r"= F(u_1)G(u_1) - F(u_0)G(u_0)" ) ]
        eq2[0].move_to( eq[0] ).shift( 2.50 * DOWN + 1.00 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 1.30 * DOWN + 5.26 * RIGHT
            #if i == 0:
            #    sh += 0.30 * DOWN + 0.00 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )

        fadeall( self )

# vim: et sw=4 ts=4
