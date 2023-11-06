from mycolors import *
import random

class m110_threeparameters( Scene ):
    def construct( self ):

        title = Text( "Fundamental theorem of GC: 3 parameters." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^3 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \int_{\partial V} F d^2 {{ \mathbf{x} }} G" ),
               cMathTex( r"F = F(u, v, w),\quad G = G(u, v, w),\quad {{ \mathbf{x} }} = {{ \mathbf{x} }}(u, v, w)" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        eq[1].move_to( eq[0] ).shift( 1.00 * DOWN )
        self.play( Write( eq[1] ) )
        self.wait( 3 )
        self.play( FadeOut( eq[1] ) )
        self.wait( 1 )

        eq2 = [ cMathTex( r"d^3 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } ="
                          r"du dv dw\, \Bigl( "
                          r"{{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial w } }"
                          r"-{{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_3 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial v } }"
                          r"+{{ \mathbf{x} }}_2 \wedge {{ \mathbf{x} }}_3 { { \stackrel{ \leftrightarrow }{ \partial } } \over { \partial u } }"
                          r"\Bigr)" ) ]
        eq2[0].move_to( eq[0] ).shift( 1.00 * DOWN )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )

        eq3 = [ cMathTex( r"\textrm{Let}\, V = [u(0), u(1)] \times [v(0), v(1)] \times [w(0), w(1)]" ) ]
        eq3[0].move_to( eq2[0] ).shift( 1.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq3[0] ) )
        self.wait( 2 )
        self.play( AnimationGroup( FadeOut( eq[0] ),
                                   FadeOut( VGroup( *eq2 ) ),
                                   FadeOut( VGroup( *eq3 ) ) ) )
        self.wait( 4 )

        eq4 = [ cMathTex( r"\int_V F d^3 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G"
                          r"=\int_{u(0)}^{u(1)} \int_{v(0)}^{v(1)} \int_{w(0)}^{w(1)} du dv dw\quad \times " ),
                cMathTex( r"\quad{ \partial \over { \partial u } } ( F ({{ \mathbf{x} }}_2 \wedge {{ \mathbf{x} }}_3) G )"
                          r"-{ \partial \over { \partial v } } ( F ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_3) G )"
                          r"+{ \partial \over { \partial w } } ( F ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2) G )" ),
                cMathTex( r"-\quad \int_{u(0)}^{u(1)} \int_{v(0)}^{v(1)} \int_{w(0)}^{w(1)} du dv dw\, F (*) G" ),
                cMathTex( r"(*) = { \partial \over { \partial u } } ({{ \mathbf{x} }}_2 \wedge {{ \mathbf{x} }}_3)"
                          r"-{ \partial \over { \partial v } } ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_3)"
                          r"+{ \partial \over { \partial w } } ({{ \mathbf{x} }}_1 \wedge {{ \mathbf{x} }}_2)" ),
                cMathTex( r"= 0" ) ]
        i = 0
        eq4[i].move_to( eq[0] ).shift( 0.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq4[i] ) )
        self.wait( 3 )
        i = 1
        eq4[i].move_to( eq4[i-1] ).shift( 1.30 * DOWN + 0.00 * LEFT )
        self.play( Write( eq4[i] ) )
        self.wait( 3 )
        i = 2
        eq4[i].move_to( eq4[i-1] ).shift( 1.30 * DOWN + 0.00 * LEFT )
        self.play( Write( eq4[i] ) )
        self.wait( 3 )
        i = 3
        eq4[i].move_to( eq4[i-1] ).shift( 1.30 * DOWN + 1.00 * LEFT )
        self.play( Write( eq4[i] ) )
        self.wait( 3 )
        #i = 4
        #eq4[i].move_to( eq4[i-1] ).shift( 1.30 * DOWN + 0.00 * LEFT )
        #self.play( Write( eq4[i] ) )
        sh = 1.30 * DOWN + 0.80 * RIGHT
        write_aligned( self, eq4[i], eq4[i+1], sh, None )
        self.wait( 3 )

        self.play( FadeOut( VGroup( *eq4 ) ) )
        self.wait( 4 )

        eq5 = [ cMathTex( r"\mathrm{Let}\, d{{ \mathbf{x} }}_i = du_i {{ \mathbf{x} }}_i" ) ]
        i = 0
        eq5[i].move_to( eq[0] ).shift( 0.00 * DOWN + 0.00 * LEFT )
        self.play( Write( eq5[i] ) )
        self.wait( 3 )
        self.play( FadeOut( VGroup( *eq5 ) ) )
        self.wait( 4 )

        eq6 = [ cMathTex( r"\int_V F d^3 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G"
                          r"=\int_{v(0)}^{v(1)} \int_{w(0)}^{w(1)} ( F (d{{ \mathbf{x} }}_2 \wedge d{{ \mathbf{x} }}_3) G )\Big\vert_{u(0)}^{u(1)}" ),
                cMathTex( r"\quad -\int_{u(0)}^{u(1)} \int_{w(0)}^{w(1)} ( F (d{{ \mathbf{x} }}_1 \wedge d{{ \mathbf{x} }}_3) G )\Big\vert_{v(0)}^{v(1)}" ),
                cMathTex( r"\quad +\int_{u(0)}^{u(1)} \int_{v(0)}^{v(1)} ( F (d{{ \mathbf{x} }}_1 \wedge d{{ \mathbf{x} }}_2) G )\Big\vert_{w(0)}^{w(1)}" ),
                cMathTex( r"\equiv \int_{\partial V} F d^2 {{ \mathbf{x} }} G" ),
                cMathTex( r"d^2 {{ \mathbf{x} }} \sim d{{ \mathbf{x} }}_1 \wedge d{{ \mathbf{x} }}_3 - d{{ \mathbf{x} }}_1 \wedge d{{ \mathbf{x} }}_2 + d{{ \mathbf{x} }}_1 \wedge d{{ \mathbf{x} }}_2" ) ]
        eq6[0].move_to( eq[0] )
        self.play( Write( eq6[i] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.30 * DOWN + 0.00 * RIGHT 
            if i == 0:
                sh += 2.00 * RIGHT 
            eq6[i+1].move_to( eq6[i] ).shift( sh )
            self.play( Write( eq6[i+1] ) )
            self.wait( 3 )
        sh = 3.90 * DOWN + 1.00 * RIGHT
        write_aligned( self, eq6[0], eq6[3], sh, None )
        self.wait( 3 )
        sh = 1.30 * DOWN + 1.00 * LEFT
        write_aligned( self, eq6[3], eq6[4], sh, what = "\equiv" )
        self.wait( 3 )

        fadeall( self )

# vim: et sw=4 ts=4
