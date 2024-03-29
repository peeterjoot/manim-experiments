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

class m020_wedge( Scene ):
    def construct( self ):

        title = Text( "Wedge product solutions, and Cramer's rule." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ cMathTex( r"{{ \mathbf{a} }} x + {{ \mathbf{b} }} y = {{ \mathbf{c} }}" ),
               cMathTex( r"({{ \mathbf{a} }} x + {{ \mathbf{b} }} y) \wedge {{ \mathbf{b} }} = {{ \mathbf{c} }} \wedge {{ \mathbf{b} }}" ),
               cMathTex( r"({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) x + ({{ \mathbf{b} }} \wedge {{ \mathbf{b} }}) y = {{ \mathbf{c} }} \wedge {{ \mathbf{b} }}" ),
               cMathTex( r"({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) x = {{ \mathbf{c} }} \wedge {{ \mathbf{b} }}" ),
               cMathTex( r"x = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } ({{ \mathbf{c} }} \wedge {{ \mathbf{b} }})" ) ]
        eq[0].shift( 2.00 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 10 )

        for i in range(4):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 3.00 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 4.40 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 3:
                sh += 0.00 * DOWN + 1.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 10 )

        eq2 = eq[4].copy()
        eq2.move_to( eq[1] ).shift( 3.00 * LEFT )
        self.play( ReplacementTransform( VGroup(eq[1], eq[2], eq[3], eq[4]), eq2 ) )
        self.wait( 10 )

        eq3 = [ cMathTex( r"{{ \mathbf{a} }} \wedge ({{ \mathbf{a} }} x + {{ \mathbf{b} }} y) = {{ \mathbf{a} }} \wedge {{ \mathbf{c} }}" ),
                cMathTex( r"({{ \mathbf{a} }} \wedge {{ \mathbf{a} }}) x + ({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) y = {{ \mathbf{a} }} \wedge {{ \mathbf{c} }}" ),
                cMathTex( r"({{ \mathbf{a} }} \wedge {{ \mathbf{b} }}) y = {{ \mathbf{a} }} \wedge {{ \mathbf{c} }}" ),
                cMathTex( r"y = { 1 \over {{ \mathbf{a} }} \wedge {{ \mathbf{b} }} } ({{ \mathbf{a} }} \wedge {{ \mathbf{c} }})" ) ]
        eq3[0].move_to( eq2 ).shift( 6 * RIGHT )
        self.play( Write( eq3[0] ) )
        self.wait( 10 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 3.70 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.30 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.20 * LEFT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 10 )

        eq4 = eq3[3].copy().move_to( eq2 ).shift( 6.00 * RIGHT )
        self.play( ReplacementTransform( VGroup(eq3[0], eq3[1], eq3[2], eq3[3]), eq4 ) )
        self.wait( 10 )

        eq5 = [ cMathTex( r"{{ \mathbf{a} }} \wedge {{ \mathbf{b} }} = \sum_{i < j} \begin{vmatrix} a_i & b_i \\ a_j & b_j \end{vmatrix} \mathbf{e}_i \mathbf{e}_j" ),
                cMathTex( r"= \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} \mathbf{e}_1 \mathbf{e}_2\quad \mbox{($\mathbb{R}^2$})" ),
                cMathTex( r"x = { { \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} } \over \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} } }" ),
                cMathTex( r"y = { { \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} } \over \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} } }" ) ]
        eq5[0].move_to( eq4 ).shift( 6.50 * LEFT + 1.50 * DOWN )
        eq5[1].move_to( eq5[0] ).shift( 6.00 * RIGHT )
        eq5[2].move_to( eq5[0] ).shift( 0.00 * LEFT + 1.00 * DOWN )
        eq5[3].move_to( eq5[2] ).shift( 6.00 * RIGHT + 0.00 * DOWN )
        self.play( Write( eq5[0] ) )
        self.wait( 10 )
        self.play( Write( eq5[1] ) )
        self.wait( 10 )
        self.play( FadeOut( VGroup( eq5[0], eq5[1] ) ) )
        self.play( Write( eq5[2] ) )
        self.wait( 10 )
        self.play( Write( eq5[3] ) )
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
