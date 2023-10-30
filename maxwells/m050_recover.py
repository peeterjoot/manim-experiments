from mycolors import *

class m050_recover( Scene ):
    def construct( self ):

        title = Text( "Check: Recovering Maxwell's equations" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ MathTex( r"\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} ) = \Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H})" ),
               MathTex( r"\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle = \Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H}){\Bigr\rangle}_0" ),
               MathTex( r"\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle = \Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H}){\Bigr\rangle}_1" ),
               MathTex( r"\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle = \Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H}){\Bigr\rangle}_2" ),
               MathTex( r"\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle = \Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H}){\Bigr\rangle}_3" ) ]
        eq[0].shift( 2.00 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.30 * DOWN + 0.00 * LEFT
            if i == 0:
                sh += 0.34 * LEFT
            #if i == 1:
            #    sh += 0.00 * DOWN + 4.90 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 0.00 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 8 )
        self.play( FadeOut( VGroup( eq[1], eq[2], eq[3], eq[4] ) ) )
        self.wait( 8 )

        eqs = [ MathTex( r"\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle = \Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H})\Bigr\rangle" ),
                MathTex( r"\eta c \rho = \langle \boldsymbol{\nabla} \mathbf{E} \rangle" ),
                MathTex( r"\rho/\epsilon = \boldsymbol{\nabla} \cdot \mathbf{E}" ) ]
        eqs[0].move_to( eq[1] )
        self.play( Write( eqs[0] ) )
        self.wait( 5 )
        for i in range(2):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            #if i == 0:
            #    sh += 0.50 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.00 * DOWN + 4.90 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN + 0.00 * RIGHT
            write_aligned( self, eqs[i], eqs[i+1], sh, None )
            self.wait( 5 )
        self.play( FadeOut( VGroup( *eqs ) ) )
        self.wait( 5 )

        eq2 = [ MathTex( r"{\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle}_1 = {\Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H})\Bigr\rangle}_1" ),
                MathTex( r"- \eta \mathbf{J} = { 1 \over c } { \partial \mathbf{E} \over { \partial t } } + \eta {\langle I \boldsymbol{\nabla} \mathbf{H} \rangle}_1" ),
                MathTex( r"- \eta \mathbf{J} = { 1 \over c } { \partial \mathbf{E} \over { \partial t } } + \eta I^2 (\boldsymbol{\nabla} \times \mathbf{H})" ),
                MathTex( r"\mathbf{J} + \epsilon { \partial \mathbf{E} \over { \partial t } } = \boldsymbol{\nabla} \times \mathbf{H}" ) ]
        eq2[0].move_to( eq[1] )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.40 * DOWN + 4.90 * RIGHT
            if i == 1:
                sh += 0.50 * DOWN + 0.00 * RIGHT
            if i == 2:
                sh += 0.00 * DOWN - 1.00 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        self.play( FadeOut( VGroup( *eq2 ) ) )
        self.wait( 5 )

        eq3 = [ MathTex( r"{\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle}_2 = {\Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H})\Bigr\rangle}_2" ),
                MathTex( r"-I \mathbf{M} = I \boldsymbol{\nabla} \times \mathbf{E} + { { I \eta } \over c } { \partial \mathbf{H} \over { \partial t } }" ),
                MathTex( r"-\mathbf{M} = \boldsymbol{\nabla} \times \mathbf{E} + \mu { \partial \mathbf{H} \over { \partial t } }" ) ]
        eq3[0].move_to( eq[1] )
        self.play( Write( eq3[0] ) )
        self.wait( 5 )
        for i in range(2):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.40 * DOWN + 4.70 * RIGHT
            if i == 1:
                sh += 0.50 * DOWN + 0.25 * RIGHT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 5 )

        self.play( FadeOut( VGroup( *eq3 ) ) )
        self.wait( 5 )
        eq4 = [ MathTex( r"{\langle\eta ( c \rho - \mathbf{J} ) + I (c \rho_{ \mathrm{m} } - \mathbf{M} )\rangle}_3 = {\Bigl\langle\Bigl( \boldsymbol{\nabla} + { 1 \over c } { \partial \over { \partial t } }\Bigr) (\mathbf{E} + I \eta \mathbf{H})\Bigr\rangle}_3" ),
                MathTex( r"I c \rho_{ \mathrm{m} } = {\Bigl\langle \boldsymbol{\nabla} I \eta \mathbf{H} \Bigr\rangle}_3" ),
                MathTex( r"                        = I \eta \boldsymbol{\nabla} \cdot \mathbf{H}" ),
                MathTex( r"\rho_{ \mathrm{m} } = \mu \boldsymbol{\nabla} \cdot \mathbf{H}" ) ]
        eq4[0].move_to( eq[1] )
        self.play( Write( eq4[0] ) )
        self.wait( 5 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            if i == 0:
                sh += 0.40 * DOWN + 4.80 * RIGHT
            if i == 1:
                sh += 0.00 * DOWN + 1.25 * RIGHT
            if i == 2:
                sh += 0.00 * DOWN - 0.75 * RIGHT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 5 )
        self.play( FadeOut( VGroup( *eq4 ) ) )
        self.wait( 5 )

        # summarize:
        eq5 = [ MathTex( r"\boldsymbol{\nabla} \cdot \mathbf{E} = { \rho \over \epsilon }" ),
                MathTex( r"\boldsymbol{\nabla} \times \mathbf{H} = \mathbf{J} + \epsilon { \partial \mathbf{E} \over { \partial t } }" ),
                MathTex( r"\boldsymbol{\nabla} \times \mathbf{E} = -\mathbf{M} - \mu { \partial \mathbf{H} \over { \partial t } }" ),
                MathTex( r"\mu \boldsymbol{\nabla} \cdot \mathbf{H} = \rho_{ \mathrm{m} }" ) ]
        eq5[0].move_to( eq[1] ).shift( 1.5 * LEFT )
        self.play( Write( eq5[0] ) )
        self.wait( 5 )
        for i in range(3):
            sh = 1.00 * DOWN + 0.00 * RIGHT
            #if i == 0:
            #    sh += 0.40 * DOWN + 4.80 * RIGHT
            #if i == 1:
            #    sh += 0.00 * DOWN + 1.25 * RIGHT
            #if i == 2:
            #    sh += 0.00 * DOWN - 0.75 * RIGHT
            write_aligned( self, eq5[i], eq5[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
