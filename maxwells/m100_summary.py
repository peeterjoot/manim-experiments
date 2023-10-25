from mycolors import *

class m100_summary( Scene ):
    def construct( self ):

        title = Text( "Summary." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 0.25 )

        eq = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - { \partial {{ \mathbf{B} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + { \partial {{ \mathbf{D} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{D} }} = \rho" ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{B} }} = \rho_{\mathrm{m}}" ),
               cMathTex( r"\eta = \sqrt{\mu/\epsilon},\, c = 1/\sqrt{\mu \epsilon}" ),
               cMathTex( r"{{ \mathbf{D} }} = \epsilon {{ \mathbf{E} }},\, {{ \mathbf{B} }} = \mu {{ \mathbf{H} }}" ) ]
        eq[0].shift( 2.00 * UP + 3.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        for i in range(5):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.70 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 3:
                sh += 0.00 * DOWN + 2.00 * LEFT
                self.wait( 1 )
            if i == 4:
                self.wait( 7 )
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 0.25 )
        #self.play( FadeOut( VGroup( *eq ) ) )
        self.wait( 3 )

        eqEH = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - \mu { \partial {{ \mathbf{H} }} \over \partial t } " ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + \epsilon { \partial {{ \mathbf{E} }} \over \partial t } " ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{E} }} = \rho/\epsilon" ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{H} }} = \rho_{\mathrm{m}}/\mu" ) ]

        for i in range(4):
            eqEH[i].move_to(eq[i])

        self.play( AnimationGroup(
                ReplacementTransform( eq[0], eqEH[0] ),
                ReplacementTransform( eq[1], eqEH[1] ),
                ReplacementTransform( eq[2], eqEH[2] ),
                ReplacementTransform( eq[3], eqEH[3] ) ) )
        self.wait( 7 )
 
        eq2 = [ cMathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over \partial t } \Bigr) {{ F }} = J" ),
                cMathTex( r"{{ F }} = {{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}" ),
                cMathTex( r"J = \eta( c \rho - {{ \mathbf{J} }} ) + I ( c \rho_{\mathrm{m}} - {{ \mathbf{M} }} )" ) ]
        eq2[0].move_to( eq[0] ).shift( 6.00 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(2):
            sh = 1.15 * DOWN
            if i == 0:
                sh += 0.15 * DOWN + 3.00 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 2.00 * LEFT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
