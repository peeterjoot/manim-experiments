from mycolors import *
import random

class m105_d1xboundary( Scene ):
    def construct( self ):

        title = Text( "2 parameter boundary surface." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_A F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \int_{\partial A} F d^1 {{ \mathbf{x} }} G" ),
               cMathTex( r"\textrm{We write:}\quad d^1 {{ \mathbf{x} }} = d {{ \mathbf{x} }}_1 - d {{ \mathbf{x} }}_2" ),
               cMathTex( r"\textrm{We really mean:}\,\int_{\partial A} F d^1 {{ \mathbf{x} }} G = \int (F d {{ \mathbf{x} }}_1 G )\big\vert_{\Delta v} - \int (F d {{ \mathbf{x} }}_2 G )\big\vert_{\Delta u}" ),
               cMathTex( r"=\int (F d {{ \mathbf{x} }}_1 G )\big\vert_{v(1)}"
                         r"-\int (F d {{ \mathbf{x} }}_1 G )\big\vert_{v(0)}" ),
               cMathTex( r"-\quad \int (F d {{ \mathbf{x} }}_2 G )\big\vert_{u(1)}"
                         r"+ \int (F d {{ \mathbf{x} }}_2 G )\big\vert_{u(0)}" ) ]
        eq[0].shift( 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 1 )
        for i in range(4):
            sh = 1.00 * DOWN
            if i == 2:
                sh += 0.30 * DOWN
            eq[i+1].move_to( eq[i] ).shift( sh )
            self.play( Write( eq[i+1] ) )
            self.wait( 1 )
        eq2 = [ cMathTex( r"\int (F d {{ \mathbf{x} }}_1 G )\big\vert_{v(1)}"
                          r"-\int (F d {{ \mathbf{x} }}_1 G )\big\vert_{v(0)}"
                          r"-\int (F d {{ \mathbf{x} }}_2 G )\big\vert_{u(1)}"
                          r"+ \int (F d {{ \mathbf{x} }}_2 G )\big\vert_{u(0)}" ) ]
        eq2[0].move_to( eq[3] ).shift( 3.30 * UP )
        self.play( ReplacementTransform( VGroup( *eq ), eq2[0] ) )
        self.wait( 3 )


        sc = 4
        sh = 1
        axes = Axes( y_range = [0, 1, 1], x_range = [0, 1, 1], x_length = sc, y_length = sc ).shift( sh * DOWN )
        self.play( Write( axes ) )

        f0 = lambda u: np.array(( sc * u - sc/2,
                                  sc * (0.1 + 0.2 * (u**2)) - sc/2 - sh,
                                  0 ))

        f1 = lambda u: np.array(( sc * u - sc/2,
                                  sc * (0.6 + 0.3 * u**(1.5)) - sc/2 - sh,
                                  0 ))

        f2 = lambda u: np.array(( sc * (0.1 + 0.5 * u**4) - sc/2,
                                  sc * u - sc/2 - sh,
                                  0 ))

        f3 = lambda u: np.array(( sc * (0.7 + 0.5 * u**5) - sc/2,
                                  sc * u - sc/2 - sh,
                                  0 ))

        a0 = Arrow( start = f0(0.6) + 0.1 * UP, end = f0(0.3) + 0.1 * UP, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a1 = Arrow( start = f1(0.3) + 0.1 * UP, end = f1(0.6) + 0.1 * UP, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a2 = Arrow( start = f2(0.3) + 0.2 * LEFT, end = f2(0.6) + 0.2 * LEFT, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a3 = Arrow( start = f3(0.6) + 0.2 * LEFT, end = f3(0.3) + 0.2 * LEFT, color = BLUE, max_stroke_width_to_length_ratio=10 )

        curve0 = ParametricFunction( f0, t_range = np.array([0.05, 1]) )
        curve1 = ParametricFunction( f1, t_range = np.array([0.05, 1]) )
        curve2 = ParametricFunction( f2, t_range = np.array([0.05, 0.7]) )
        curve3 = ParametricFunction( f3, t_range = np.array([0.15, 0.9]) )

        label0 = MathTex( r"\mathbf{x}(u, v(0))" ).scale( 0.7 ).move_to( curve0, LEFT ).shift( 2 * LEFT + 0.4 * DOWN )
        label1 = MathTex( r"\mathbf{x}(u, v(1))" ).scale( 0.7 ).move_to( curve1, LEFT ).shift( 2 * LEFT + 0.4 * DOWN )
        label2 = MathTex( r"\mathbf{x}(u(0), v)" ).scale( 0.7 ).move_to( curve2, DOWN ).shift( 0 * LEFT + 0.7 * DOWN )
        label3 = MathTex( r"\mathbf{x}(u(1), v)" ).scale( 0.7 ).move_to( curve3, DOWN ).shift( 0 * LEFT + 1.2 * DOWN )

        at0 = MathTex( r"- F d \mathbf{x}_1 G\vert_{v(0)}" ).scale( 0.7 ).move_to( a0, LEFT ).shift( 0.3 * UP + 0.8 * LEFT )
        at1 = MathTex( r" F d \mathbf{x}_1 G\vert_{v(1)}" ).scale( 0.7 ).move_to( a1, LEFT ).shift( 0.4 * UP - 0.4 * RIGHT )
        at2 = MathTex( r" F d \mathbf{x}_2 G\vert_{u(0)}" ).scale( 0.7 ).move_to( a2, DOWN ).shift( 1.0 * RIGHT + 0.2 * UP )
        at3 = MathTex( r"- F d \mathbf{x}_2 G\vert_{u(1)}" ).scale( 0.7 ).move_to( a3, DOWN ).shift( 1.2 * RIGHT + 0.2 * UP )

        self.play( AnimationGroup( Write( curve0 ),
                                   Write( curve1 ),
                                   Write( curve2 ),
                                   Write( curve3 ),
                                   Write( label0 ),
                                   Write( label1 ),
                                   Write( label2 ),
                                   Write( label3 ) ) )

        self.play( AnimationGroup( Write( a1 ), Write( at1 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a0 ), Write( at0 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a3 ), Write( at3 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a2 ), Write( at2 ) ) )
        self.wait( 1 )

        eq3 = cMathTex( r"\int_A F d^2 {{ \mathbf{x} }}\, {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \ointclockwise F d {{ \mathbf{x} }}\, G" )
        eq3.move_to( eq[0] ).shift( 6.0 * RIGHT )

        box = SurroundingRectangle( eq3, corner_radius=0.2 )
        self.play( ReplacementTransform( eq2[0], eq3 ) )
        self.play( Write( box ) )
        g = VGroup( box, eq3 )
        self.play( AnimationGroup(
            FadeOut( VGroup( curve0, curve1, curve2, curve3, label0, label1, label2, label3, at0, at1, at2, at3, axes, a0, a1, a2, a3  ) ),
            g.animate.shift(2.00 * DOWN), run_time=1, rate_func=linear ) )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
