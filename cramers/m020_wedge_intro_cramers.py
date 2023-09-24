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

class m020_wedge_intro_cramers( Scene ):
    def construct( self ):

        eq = [ cMathTex( r"x = { { \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} } \over \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} } }" ),
               cMathTex( r"y = { { \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} } \over \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} } }" ) ]
        eq[0].shift( LEFT * 2.00 )
        eq[1].move_to( eq[0] ).shift( RIGHT * 4.00 )
        self.play( Write( VGroup( *eq ) ) )
        self.wait( 2 )

        fadeall( self )

# vim: et sw=4 ts=4
