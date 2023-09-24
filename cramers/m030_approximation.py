from helper import *

mycolors    = { l.vec('a'): GREEN, l.vec('b'):RED, l.vec('c'): BLUE }

hat_theta  = l.doublebr( l.hat( r'\boldsymbol{\theta}' ) )

class cMathTex(MathTex):
    def __init__(
        self,
        *tex_strings,
        arg_separator = " ",
        **kwargs,
    ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        super().__init__(
                arg_separator.join( tex_strings ),
                tex_template = myTemplate,
                **kwargs,
            )
        self.set_color_by_tex_to_color_map( mycolors )

class m030_approximation( Scene ):
    def construct( self ):

        title = Text( "Approximate solutions." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ cMathTex( r"\mbox{May not be able to solve:}\quad {{ \mathbf{a} }} x + {{ \mathbf{b} }} y = {{ \mathbf{c} }}" ),
               cMathTex( r"i = {{ \mathbf{a} }} \wedge {{ \mathbf{b} }}" ),
               cMathTex( r"{{ \mathbf{c}_\parallel }} = i^{-1} (i \cdot {{ \mathbf{c} }})" ),
               cMathTex( r"{{ \mathbf{c}_\perp }} = i^{-1} (i \wedge {{ \mathbf{c} }})" ),
               cMathTex( r"{{ \mathbf{c} }} = {{ \mathbf{c}_\parallel }} + {{ \mathbf{c}_\perp }}" ) ]

        eq[0].shift( 2.00 * UP + 0.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(4):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 9.00 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.34 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 0.76 * LEFT
            if i == 3:
                sh += 0.00 * DOWN + 0.40 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )
        self.wait( 30 )

        eq2 = [ cMathTex( r"\mbox{Can solve:}\quad {{ \mathbf{a} }} x + {{ \mathbf{b} }} y = {{ \mathbf{c}_\parallel }}" ),
                cMathTex( r"x = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } ({{ \mathbf{c}_\parallel }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r" = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c}_\parallel }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r"= { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }}) - { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c}_\perp }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r"= { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }})" ) ]
        self.play( FadeOut( VGroup( *eq ) ) )
        eq2[0].move_to( eq[0] ).shift( 0.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.50 * DOWN
            if i == 0:
                sh += 0.50 * UP + 4.00 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.40 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )
        self.wait( 30 )

        eq3 = [ cMathTex( r"{{ \mathbf{a} }} x + {{ \mathbf{b} }} y = {{ \mathbf{c}_\parallel }}" ),
                cMathTex( r"x = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r"y = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{a} }} \wedge {{ \mathbf{c} }})" ) ]
        eq3[0].move_to( eq2[0] ).shift( 1.00 * DOWN )
        eq3[1].move_to( eq3[0] ).shift( 1.50 * DOWN )
        eq3[2].move_to( eq3[1] ).shift( 1.50 * DOWN )
        self.play( ReplacementTransform( VGroup(*eq2), VGroup(*eq3) ) )
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
