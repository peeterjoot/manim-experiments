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

class m040_justify_last_step( Scene ):
    def construct( self ):

        title = Text( "That last step." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        # UN65MU7600F

        eq = [ cMathTex( r"- { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } \cdot ({{ \mathbf{c}_\perp }} \wedge {{ \mathbf{b} }}) \propto ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }} ) \cdot ({{ \mathbf{c}_\perp }} \wedge {{ \mathbf{b} }})" ),
               cMathTex( r"= {{ \mathbf{a} }} \cdot ({{ \mathbf{b} }} \cdot ({{ \mathbf{c}_\perp }} \wedge {{ \mathbf{b} }}))" ),
               cMathTex( r"= {{ \mathbf{a} }} \cdot (({{ \mathbf{b} }} \cdot {{ \mathbf{c}_\perp }}) {{ \mathbf{b} }} - {{ \mathbf{b}^2 }} {{ \mathbf{b}_\perp }} )" ) ]
        eq[0].shift( 2.00 * UP + 0.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        #for i in range(1):
        #    sh = 1.00 * DOWN
        #    #if i == 0:
        #    #    sh += 0.00 * DOWN + 8.00 * LEFT
        #    #if i == 1:
        #    #    sh += 0.00 * DOWN + 2.00 * LEFT
        #    #if i == 2:
        #    #    sh += 0.60 * DOWN + 0.40 * RIGHT
        #    #if i == 3:
        #    #    sh += 0.60 * DOWN + 0.00 * RIGHT
        #    write_aligned( self, eq[i], eq[i+1], sh, None )
        #    self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
