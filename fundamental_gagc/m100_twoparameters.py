from mycolors import *
import random

class m100_twoparameters( Scene ):
    def construct( self ):

        title = Text( "Fundamental theorem of GC: 2 parameters." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \int_{\partial V} F d^1 {{ \mathbf{x} }} G" ),
               cMathTex( r"F = F(u, v),\quad G = G(u, v),\quad {{ \mathbf{x} }} = {{ \mathbf{x} }}(u, v)" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        eq[1].move_to( eq[0] ).shift( 1.00 * DOWN )
        self.play( Write( eq[1] ) )
        self.wait( 3 )
        self.play( FadeOut( eq[1] ) )
        self.wait( 1 )
        

        eq2 = [ cMathTex( r"d^2 {{ \mathbf{x} }} \stackrel{ \leftrightarrow }{ \boldsymbol{\partial} }\, = \sum_i du dv\, ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \, {{ \mathbf{x} }}^i { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial u_i } }" ),
                cMathTex( r"= du dv\, \Bigl( - {{ \mathbf{x} }}_2 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial u } } + {{ \mathbf{x} }}_1 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial v } } \Bigr)" ) ]

        eq2[0].move_to( eq[0] ).shift( 2.00 * DOWN + 1.00 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )

        eq3 = [ cMathTex( r"({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \, {{ \mathbf{x} }}^1 = ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \wedge {{ \mathbf{x} }}^1 + ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \cdot {{ \mathbf{x} }}^1 " ),
                cMathTex( r"= ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \cdot {{ \mathbf{x} }}^1 " ),
                cMathTex( r"= {{ \mathbf{x} }}_1 ({{ \mathbf{x} }}_2 \cdot {{ \mathbf{x} }}^1) - {{ \mathbf{x} }}_2 ({{ \mathbf{x} }}_1 \cdot {{ \mathbf{x} }}^1)" ),
                cMathTex( r"= - {{ \mathbf{x} }}_2" ) ]

        eq4 = [ cMathTex( r"({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \, {{ \mathbf{x} }}^2 = ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \wedge {{ \mathbf{x} }}^2 + ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \cdot {{ \mathbf{x} }}^2 " ),
                cMathTex( r"= ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) \cdot {{ \mathbf{x} }}^2 " ),
                cMathTex( r"= {{ \mathbf{x} }}_1 ({{ \mathbf{x} }}_2 \cdot {{ \mathbf{x} }}^2) - {{ \mathbf{x} }}_2 ({{ \mathbf{x} }}_1 \cdot {{ \mathbf{x} }}^2)" ),
                cMathTex( r"= {{ \mathbf{x} }}_1" ) ]

        eq3[0].move_to( eq2[0] ).shift( 1.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq3[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.65 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            write_aligned( self, eq3[i], eq3[i+1], sh, None )
            self.wait( 1 )
        self.wait( 4 )
        self.play( FadeOut( VGroup( *eq3 ) ) )
        self.wait( 1 )

        eq4[0].move_to( eq2[0] ).shift( 1.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq4[0] ) )
        self.wait( 1 )
        for i in range(3):
            sh = 0.65 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 1 )
        self.wait( 4 )
        self.play( FadeOut( VGroup( *eq4 ) ) )
        self.wait( 1 )

        for i in range(1):
            sh = 1.20 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )
        self.wait( 4 )
        self.play( FadeOut( VGroup( *eq2 ) ) )
        self.wait( 1 )

        eq5 = [ cMathTex( r"\textrm{Let}\, V = [u(0), u(1)] \times [v(0), v(1)]" ) ]
        eq5[0].move_to( eq[0] ).shift( 1.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq5[0] ) )
        self.wait( 3 )
        self.play( FadeOut( VGroup( *eq5 ) ) )
        self.wait( 1 )

        eq6 = [ cMathTex( r"\int_V F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G" ),
                cMathTex( r" = \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} du dv\, F \Bigl( - {{ \mathbf{x} }}_2 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial u } } + {{ \mathbf{x} }}_1 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial v } } \Bigr) G" ),
                cMathTex( r" = \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} du dv\, \Bigl( -{ \partial \over { \partial u } } (F {{ \mathbf{x} }}_2 G) + { \partial \over { \partial v } } (F {{ \mathbf{x} }}_1 G) \Bigr) " ) ]
        eq6[0].move_to( eq[0] ).shift( 1.30 * DOWN + 3.00 * LEFT )
        self.play( Write( eq6[0] ) )
        self.wait( 3 )
        for i in range(2):
            sh = 1.30 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.34 * RIGHT
            write_aligned( self, eq6[i], eq6[i+1], sh, None )
            self.wait( 1 )
        self.wait( 4 )
        #self.play( FadeOut( VGroup( *eq6 ) ) )
        #self.wait( 1 )

        eq7 = [ MathTex( r" \quad + \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} du dv\, \Bigl( F \Bigl( { \partial \mathbf{x}_2 \over \partial u } \Bigr) G - F \Bigl( { \partial  \mathbf{x}_1 \over \partial v } \Bigr) G \Bigr) " ),
                MathTex( r" \quad + \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} du dv\, F \Bigl( { \partial \mathbf{x}_2 \over \partial u } - { \partial  \mathbf{x}_1 \over \partial v } \Bigr) G" ),
                MathTex( r" \quad + \int_{u = u(0)}^{u(1)} \int_{v = v(0)}^{v(1)} du dv\, F \Bigl( { \partial^2 \mathbf{x} \over { \partial u \partial v } } - { \partial^2  \mathbf{x} \over { \partial v \partial u } } \Bigr) G" ) ]
        eq7[0].move_to( eq6[2] ).shift( 1.30 * DOWN )
        self.play( Write( eq7[0] ) )
        self.wait( 3 )
        for i in range(2):
            eq7[i+1].move_to( eq7[i] )
            self.play( ReplacementTransform( eq7[i], eq7[i+1] ) )
            self.wait( 1 )
        self.wait( 4 )

        eq8 = [ cMathTex( r" \int_V F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G" ),
                cMathTex( r"= \int_{u = u(0)}^{u(1)} du \int_{v = v(0)}^{v(1)} dv\, { \partial \over { \partial v } } (F {{ \mathbf{x} }}_1 G) - \int_{v = v(0)}^{v(1)} dv \int_{u = u(0)}^{u(1)} du\, { \partial \over { \partial u } } (F {{ \mathbf{x} }}_2 G)" ),
                cMathTex( r"= \int_{u = u(0)}^{u(1)} du\, \Bigl( F {{ \mathbf{x} }}_1 G \Bigr) \big\vert_{v(0)}^{v(1)} - \int_{v = v(0)}^{v(1)} dv\, \Bigl( F {{ \mathbf{x} }}_2 G \Bigr) \big\vert_{u(0)}^{u(1)}" ),
                cMathTex( r"\equiv \int_{\partial V} F d^1 {{ \mathbf{x} }} G, \quad d^1 {{ \mathbf{x} }} \sim du\, {{ \mathbf{x} }}_1 - dv\, {{ \mathbf{x} }}_1 " ) ]
        self.play( AnimationGroup( FadeOut( eq[0] ), FadeOut( eq7[2] ), FadeOut( VGroup( *eq6 ) ) ) )
        self.wait( 3 )

        eq8[0].move_to( eq[0] ).shift( 5.00 * LEFT )
        self.play( Write( eq8[0] ) )
        self.wait( 3 )
        eq8[1].move_to( eq8[0], LEFT ).shift( 1.30 * DOWN )
        self.play( Write( eq8[1] ) )
        self.wait( 3 )
        for i in range(1,3):
            sh = 1.30 * DOWN
            #if i == 0:
            #    sh += 0.00 * DOWN + 0.34 * RIGHT
            write_aligned( self, eq8[i], eq8[i+1], sh, None )
            self.wait( 1 )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
