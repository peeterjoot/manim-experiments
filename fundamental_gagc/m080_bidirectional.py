from mycolors import *

class m080_bidirectional( Scene ):
    def construct( self ):

        title = Text( "Bidirectional differential operators." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"F {\stackrel{ \leftrightarrow }{\boldsymbol{\partial}}} G = \textrm{?}" ) ]

        eq[0].shift( 2.00 * UP + 0.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        self.play( FadeOut( eq[0] ) )
        self.wait( 1 )
        defin = Text( "Definition:" )
        defin.move_to( eq[0] ).shift( 0.50 * DOWN + 5.00 * LEFT )
        self.play( Write( defin ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"F {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = F \Bigl( \sum_i {{ \mathbf{x} }}^i { {\stackrel{ \leftrightarrow }{\partial} \over { \partial u_i } } \Bigr) G" ),
                cMathTex( r"= \sum_i \Bigl( { { \partial F } \over { \partial u_i } } \Bigr) {{ \mathbf{x} }}^i G + F {{ \mathbf{x} }}^i \Bigl( { { \partial G } \over { \partial u_i } } \Bigr)" ),
                cMathTex( r"= \sum_i { { \partial } \over { \partial u_i } } \Bigl( F {{ \mathbf{x} }}^i G \Bigr) - F \Bigl( { { \partial {{ \mathbf{x} }}^i } \over { \partial u_i } } \Bigr) G" ) ]
        eq2[0].move_to( defin ).shift( 0.00 * DOWN + 5.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        i = 0
        sh = 1.40 * DOWN
        sh += 0.00 * DOWN + 0.00 * LEFT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 1 )
        i = i + 1
        sh = 1.40 * DOWN
        sh += 0.00 * DOWN + 0.00 * LEFT
        write_aligned( self, eq2[i], eq2[i+1], sh, None )
        self.wait( 1 )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
