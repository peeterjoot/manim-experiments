from helper import *

mycolors    = { l.vec('a'): GREEN, l.vec('b'):RED, l.vec('c'): BLUE }

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

class m030_approximation_intro( Scene ):
    def construct( self ):

        eq = [ cMathTex( r"{{ \mathbf{a} }} x + {{ \mathbf{b} }} y = {{ \mathbf{c}_\parallel }}" ),
                cMathTex( r"x = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } ({{ \mathbf{c}_\parallel }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r" = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c}_\parallel }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r"= { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }}) - { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c}_\perp }} \wedge {{ \mathbf{b} }})" ),
                cMathTex( r"= { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }})" ) ]
        eq[0].shift( 2.50 * UP ) 
        self.play( Write( eq[0] ) )
        self.wait( 2 )
        for i in range(4):
            sh = 1.50 * DOWN
            if i == 0:
                sh += 0.50 * UP + 4.00 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.40 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 2 )

        fadeall( self )

# vim: et sw=4 ts=4
