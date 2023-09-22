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

class m050_leastsq( Scene ):
    def construct( self ):

        title = Text( "Least squares using calculus." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        # s/\\B\(.\)/{{ \\mathbf{\1} }}/g
        eq = [ cMathTex( r"\mbox{Let:}\quad \epsilon = ({{ \mathbf{c} }} - {{ \mathbf{a} }} x - {{ \mathbf{b} }} y){}^2" ),
               cMathTex( r"0 = { {\partial \epsilon} \over {\partial x} } = 2 ({{ \mathbf{c} }} - {{ \mathbf{a} }} x - {{ \mathbf{b} }} y) \cdot (-{{ \mathbf{a} }})" ),
               cMathTex( r"0 = { {\partial \epsilon} \over {\partial y} } = 2 ({{ \mathbf{c} }} - {{ \mathbf{a} }} x - {{ \mathbf{b} }} y) \cdot (-{{ \mathbf{b} }})" ),
               MathTex( r"0 = \begin{bmatrix}  \mathbf{a} {}^2 &  \mathbf{a}  \cdot  \mathbf{b}  \\  \mathbf{a}  \cdot  \mathbf{b}  &  \mathbf{b} {}^2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix}  \mathbf{a}  \cdot  \mathbf{c}  \\  \mathbf{b}  \cdot  \mathbf{c}  \\ \end{bmatrix}" ) ]

        eq[0].shift( 2.00 * UP + 0.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.00 * LEFT
            if i == 1:
                sh += 0.50 * DOWN + 0.00 * LEFT
            if i == 2:
                sh += 0.50 * DOWN + 0.00 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eq2 = [ MathTex( r"x = { { \mathbf{b}^2 ( \mathbf{a} \cdot \mathbf{c} ) - ( \mathbf{a} \cdot \mathbf{b} ) ( \mathbf{b} \cdot \mathbf{c} ) } \over { \mathbf{a}^2 \mathbf{b}^2 - ( \mathbf{a} \cdot \mathbf{b} ){}^2 } }" ),
                MathTex( r"y = { { \mathbf{a}^2 ( \mathbf{b} \cdot \mathbf{c} ) - ( \mathbf{a} \cdot \mathbf{b} ) ( \mathbf{a} \cdot \mathbf{c} ) } \over { \mathbf{a}^2 \mathbf{b}^2 - ( \mathbf{a} \cdot \mathbf{b} ){}^2 } }" ) ]
    
        eqx = [ MathTex( r" = { {( \mathbf{a} \wedge \mathbf{b} ) \cdot ( \mathbf{b} \wedge \mathbf{c} ) } \over { -( \mathbf{a} \wedge \mathbf{b} ){}^2 } }" ),
                MathTex( r" = {1 \over {\mathbf{a} \wedge \mathbf{b}} } \cdot ( \mathbf{c} \wedge \mathbf{b} )" ) ]

        eq2[0].move_to( eq[0] ).shift( 0.50 * DOWN + 3.50 * LEFT )
        eq2[1].move_to( eq2[0] ).shift( 0.00 * DOWN + 7.00 * RIGHT )
        self.play( ReplacementTransform( VGroup(*eq), VGroup(*eq2) ) )
        self.wait( 5 )

        sh = 0.42 * RIGHT + 1.40 * DOWN
        write_aligned( self, eq2[0], eqx[0], sh, None )
        self.wait( 5 )
        sh = 0.00 * RIGHT + 1.40 * DOWN
        write_aligned( self, eqx[0], eqx[1], sh, None )
        self.wait( 5 )

        eqy = [ MathTex( r" = { -{( \mathbf{a} \wedge \mathbf{b} ) \cdot ( \mathbf{a} \wedge \mathbf{c} ) } \over { -( \mathbf{a} \wedge \mathbf{b} ){}^2 } }" ),
                MathTex( r" = {1 \over {\mathbf{a} \wedge \mathbf{b}} } \cdot ( \mathbf{a} \wedge \mathbf{c} )" ) ]

        sh = 0.42 * RIGHT + 1.40 * DOWN
        write_aligned( self, eq2[1], eqy[0], sh, None )
        self.wait( 5 )
        sh = 0.00 * RIGHT + 1.40 * DOWN
        write_aligned( self, eqy[0], eqy[1], sh, None )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
