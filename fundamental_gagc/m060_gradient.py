from mycolors import *

class m060_gradient( Scene ):
    def construct( self ):

        title = Text( "Gradient." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }}(u_1, u_2, \cdots, u_N)" ),
               cMathTex( r"\textrm{Theorem: }\, \boldsymbol{\nabla} = \sum_{j=1}^N {{ \mathbf{x} }}^j {\partial \over {\partial u_j} },\quad {{ \mathbf{x} }}^i = \boldsymbol{\nabla} u_i" ) ]

        eq[0].shift( 2.00 * UP + 0.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 3.00 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )

        eq2 = [ cMathTex( r"\boldsymbol{\nabla} = \sum_i {{ \mathbf{e} }}_i {\partial \over {\partial x_i} }" ),
                cMathTex( r"                    = \sum_{i,j} {{ \mathbf{e} }}_i {\partial u_j \over {\partial x_i} } {\partial \over {\partial u_j} }" ),
                #cMathTex( r"                    = \sum_j \Bigl( \sum_i {{ \mathbf{e} }}_i {\partial u_j \over {\partial x_i} } \Bigr) {\partial \over {\partial u_j} }" ),
                cMathTex( r"                    = \sum_j (\boldsymbol{\nabla} u_j ) {\partial \over {\partial u_j} }" ) ]

        eq2[0].move_to( eq[1] ).shift( 1.20 * DOWN + 3.00 * LEFT )
        self.play( Write( eq2[0] ) )
        self.wait( 1 )
        for i in range(2):
            sh = 1.20 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.48 * RIGHT
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 1 )

        eq3 = cMathTex( r"\boldsymbol{\nabla} u_i = {{ \mathbf{x} }}^i, \textrm{iff}\, {{ \mathbf{x} }}^i \cdot {{ \mathbf{x} }}_j = {\delta^i}_j" )
        eq3.move_to( eq2[0], LEFT ).shift( 5.00 * RIGHT )
        self.play( Write( eq3 ) )
        self.wait( 3 )

        self.play( AnimationGroup( eq3.animate.shift(6.00 * LEFT), run_time=1, rate_func=linear ), FadeOut( *eq2 ) )
        self.wait( 8 )

        eq4 = [ cMathTex( r"{{ \mathbf{x} }}_j \cdot \boldsymbol{\nabla} u_i = \sum_{r,s} \Bigl( {{ \mathbf{e} }}_r { { \partial x_r } \over { \partial u_j } } \Bigr) \cdot \Bigl( {{ \mathbf{e} }}_s { {\partial u_i} \over {\partial x_s} } \Bigr)" ),
                cMathTex( r"= \sum_{r,s} \delta_{rs} { { \partial x_r } \over { \partial u_j } } { {\partial u_i} \over {\partial x_s} }" ),
                cMathTex( r"= \sum_{r} { { \partial x_r } \over { \partial u_j } } { {\partial u_i} \over {\partial x_r} }" ),
                cMathTex( r"= { {\partial u_i} \over {\partial u_j} }" ),
                cMathTex( r"= \delta_{ij}" ) ]
        eq4[0].move_to( eq3 ).shift( 6.00 * RIGHT + 0.10 * DOWN )
        self.play( Write( eq4[0] ) )
        self.wait( 3 )
        for i in range(2):
            sh = 1.30 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.40 * RIGHT
            write_aligned( self, eq4[i], eq4[i+1], sh, None )
            self.wait( 1 )
        i=2
        eq4[i+1].move_to( eq4[i], LEFT )
        self.play( ReplacementTransform( eq4[i], eq4[i+1] ) )
        self.wait( 5 )
        i = i + 1
        eq4[i+1].move_to( eq4[i], LEFT )
        self.play( ReplacementTransform( eq4[i], eq4[i+1] ) )
        self.wait( 5 )

        eq5 = [ cMathTex( r"{{ \mathbf{x} }} = {{ \mathbf{x} }}(u_1, u_2, \cdots, u_k)" ),
                cMathTex( r"\boldsymbol{\partial} = \sum_{j=1}^k {{ \mathbf{x} }}^j {\partial \over {\partial u_j} }" ),
                cMathTex( r"\mathrm{If}\, k = N:\quad \boldsymbol{\partial} = \boldsymbol{\nabla}" ) ]
        eq5[0].move_to( eq[0] )
        eq5[1].move_to( eq[1] ).shift( 1.00 * RIGHT + 0.50 * DOWN )

        title2 = Text( "Vector derivative." )
        title2.move_to( title ).shift( 0 * LEFT )
        title2.set_color( BLUE )
        self.play( AnimationGroup( FadeOut( eq3 ),
                                   FadeOut( VGroup( *eq ) ),
                                   FadeOut( VGroup( *eq4 ) ),
                                   ReplacementTransform( title, title2 ),
                                   ReplacementTransform( eq[0], eq5[0] ),
                                   ReplacementTransform( eq[1], eq5[1] ) ) )
        self.wait( 2 )
        eq5[2].shift( 1.00 * DOWN )
        self.play( Write( eq5[2] ) )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
