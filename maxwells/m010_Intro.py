from mycolors import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( "Maxwell's equation in geometric algebra." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - { \partial {{ \mathbf{B} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + { \partial {{ \mathbf{D} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{D} }} = \rho" ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{B} }} = \rho_{\mathrm{m}}" ),
               cMathTex( r"{{ \mathbf{B} }} = \mu {{ \mathbf{H} }}"),
               cMathTex( r"{{ \mathbf{D} }} = \epsilon {{ \mathbf{E} }}") ]
        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.70 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 2:
                sh += 0.00 * DOWN + 1.40 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )

        eq[4].move_to(eq[0]).shift( 5.00 * RIGHT )
        self.play( Write( eq[4] ) )
        self.wait( 1 )
        i = 4
        sh = 1.00 * DOWN + 0.60 * LEFT
        write_aligned( self, eq[i], eq[i+1], sh, None )
        self.wait( 1 )

        eqEH = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - \mu { \partial {{ \mathbf{H} }} \over \partial t } " ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + \epsilon { \partial {{ \mathbf{E} }} \over \partial t } " ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{E} }} = \rho/\epsilon" ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{H} }} = \rho_{\mathrm{m}}/\mu" ) ]
        for i in range(4):
            eqEH[i].move_to( eq[i] )

        self.play( AnimationGroup( ReplacementTransform( eq[0], eqEH[0] ),
                                   ReplacementTransform( eq[1], eqEH[1] ),
                                   ReplacementTransform( eq[2], eqEH[2] ),
                                   ReplacementTransform( eq[3], eqEH[3] ),
                                   FadeOut( VGroup( eq[4], eq[5] ) ) ) )
        self.wait( 1 )

        gradEH = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{E} }} + I ({{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }}) = \rho/\epsilon -I {{ \mathbf{M} }} - I \mu { \partial {{ \mathbf{H} }} \over \partial t } " ),
                 cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{H} }} + I ({{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }}) = \rho_{\mathrm{m}}/\mu + I {{ \mathbf{J} }} + I \epsilon { \partial {{ \mathbf{E} }} \over \partial t }" ) ]
        gradEH[0].move_to( eq[0] )
        gradEH[1].move_to( eq[2] ).shift( 0.85 * RIGHT )

        self.play( AnimationGroup( ReplacementTransform( VGroup( eqEH[0], eqEH[2] ), gradEH[0] ),
                                   ReplacementTransform( VGroup( eqEH[1], eqEH[3] ), gradEH[1] ) ) )
        self.wait( 1 )

        gradEH2 = [ cMathTex( r"{{ \boldsymbol{\nabla} }} {{ \mathbf{E} }} = \rho/\epsilon -I {{ \mathbf{M} }} - I \mu { \partial {{ \mathbf{H} }} \over \partial t } " ),
                    cMathTex( r"{{ \boldsymbol{\nabla} }} {{ \mathbf{H} }} = \rho_{\mathrm{m}}/\mu + I {{ \mathbf{J} }} + I \epsilon { \partial {{ \mathbf{E} }} \over \partial t }" ) ]
        gradEH2[0].move_to( gradEH[0] ).shift( 1.60 * RIGHT )
        gradEH2[1].move_to( gradEH[1] ).shift( 1.60 * RIGHT )
        self.play( AnimationGroup( ReplacementTransform( gradEH[0], gradEH2[0] ),
                                   ReplacementTransform( gradEH[1], gradEH2[1] ) ) )
        self.wait( 1 )

        etac = cMathTex( r"\eta = \sqrt{ \mu / \epsilon },\qquad c = 1/\sqrt{\mu\epsilon}" )
        etac.move_to( gradEH[1] ).shift( 2.00 * DOWN )
        self.play( Write( etac ) )
        self.wait( 1 )

        gradEH3 = [ cMathTex( r"{{ \boldsymbol{\nabla} }} {{ \mathbf{E} }} = \rho/\epsilon -I {{ \mathbf{M} }} - {\mu \over \eta} { I \eta \partial {{ \mathbf{H} }} \over \partial t } " ),
                    cMathTex( r"I \eta {{ \boldsymbol{\nabla} }} {{ \mathbf{H} }} = I \eta \rho_{\mathrm{m}}/\mu - \eta {{ \mathbf{J} }} -  \eta \epsilon { \partial {{ \mathbf{E} }} \over \partial t }" ) ]
        gradEH3[0].move_to( gradEH2[0] ).shift( 0.00 * RIGHT )
        gradEH3[1].move_to( gradEH2[1] ).shift( 0.00 * RIGHT )
        self.play( AnimationGroup( ReplacementTransform( gradEH2[0], gradEH3[0] ),
                                   ReplacementTransform( gradEH2[1], gradEH3[1] ) ) )
        self.wait( 1 )

        gradEH4 = [ cMathTex( r"{{ \boldsymbol{\nabla} }} {{ \mathbf{E} }} = \eta c \rho -I {{ \mathbf{M} }} - {1 \over c} { \partial I \eta {{ \mathbf{H} }} \over \partial t } " ),
                    cMathTex( r"{{ \boldsymbol{\nabla} }} I \eta {{ \mathbf{H} }} = I c \rho_{\mathrm{m}} - \eta {{ \mathbf{J} }} -  {1 \over c } { \partial {{ \mathbf{E} }} \over \partial t }" ) ]
        gradEH4[0].move_to( gradEH3[0] ).shift( 0.00 * RIGHT )
        gradEH4[1].move_to( gradEH3[1] ).shift( 0.00 * RIGHT )
        self.play( AnimationGroup( ReplacementTransform( gradEH3[0], gradEH4[0] ),
                                   ReplacementTransform( gradEH3[1], gradEH4[1] ) ) )
        self.wait( 1 )

        gradEH5 = [ cMathTex( r"{{ \boldsymbol{\nabla} }} ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }} ) = \eta c \rho -I {{ \mathbf{M} }} - {1 \over c} { \partial ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}) \over \partial t } + I c \rho_{\mathrm{m}} - \eta {{ \mathbf{J} }}" ) ]
        gradEH5[0].move_to( gradEH4[0] ).shift( 1.50 * LEFT )
        self.play( AnimationGroup( ReplacementTransform( VGroup( gradEH4[0], gradEH4[1]), gradEH5[0] ),
                                   FadeOut( etac ) ) )
        self.wait( 1 )

        gradEH6 = [ cMathTex( r"\Bigl({{ \boldsymbol{\nabla} }} + {1 \over c } {\partial \over \partial t }\Bigr) ({{ \mathbf{E} }} + I \eta {{ \mathbf{H} }} ) = \eta ( c \rho - {{ \mathbf{J} }} ) + I ( c \rho_{\mathrm{m}} - {{ \mathbf{M} }} )" ) ]
        gradEH6[0].move_to( gradEH5[0] ).shift( 0.00 * LEFT )
        self.play( ReplacementTransform( gradEH5[0], gradEH6[0] ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over \partial t } \Bigr) F = J" ),
                cMathTex( r"F = {{ \mathbf{E} }} + I \eta {{ \mathbf{H} }}" ),
                cMathTex( r"J = \eta( c \rho - {{ \mathbf{J} }} ) + I ( c \rho_{\mathrm{m}} - {{ \mathbf{M} }} )" ) ]
        eq2[0].move_to( eq[0] ).shift( 0.00 * RIGHT )
        eq2[1].move_to( eq[1] ).shift( 0.50 * RIGHT + 0.50 * DOWN )
        eq2[2].move_to( eq[2] ).shift( 1.00 * RIGHT + 0.80 * DOWN )
        self.play( AnimationGroup( ReplacementTransform( gradEH6[0], VGroup( *eq2 ) ) ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
