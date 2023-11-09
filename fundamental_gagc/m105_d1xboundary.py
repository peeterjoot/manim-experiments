from mycolors import *
import random

class m105_d1xboundary( Scene ):
    def construct( self ):

        title = Text( "2 parameter boundary surface." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq = [ cMathTex( r"\int_V F d^2 {{ \mathbf{x} }} {\stackrel{ \leftrightarrow }{ \boldsymbol{\partial} } G = \int_{\partial V} F d^1 {{ \mathbf{x} }} G" ),
               cMathTex( r"\textrm{Although we write:}\,d^1 {{ \mathbf{x} }} = d {{ \mathbf{x} }}_1 - d {{ \mathbf{x} }}_2" ),
               cMathTex( r"\textrm{Really mean:}\,\int_{\partial V} F d^1 {{ \mathbf{x} }} G = \int (F d {{ \mathbf{x} }}_1 G )\big\vert_{\Delta v} - \int (F d {{ \mathbf{x} }}_2 G )\big\vert_{\Delta u}" ),
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

        axes = Axes( y_range = [0, 1, 1], x_range = [0, 1, 1], x_length = 4, y_length = 4 )
        axes.shift( 1.00 * DOWN )
        #labels = axes.get_axis_labels(
        #    Tex( "u" ).scale( 0.7 ), Tex( "v" ).scale( 0.7 )
        #)
        #self.add( axes, labels )
        self.play( Write( axes ) )

        curve0 = ParametricFunction(
            lambda u: np.array([
                u,
                0.1 + 0.2 * u**2
            ]), color=WHITE, t_range = np.array([0.01, 1])
        )
        #curve1 = ParametricFunction(
        #    lambda u: np.array([
        #        0.6 + 0.2 * u**1.5,
        #        u, 0
        #    ]), color=WHITE, t_range = np.array([0, 1])
        #)
        #curve2 = ParametricFunction(
        #    lambda u: np.array([
        #        0.1 + 0.5 * u**4,
        #        u, 0
        #    ]), color=WHITE, t_range = np.array([0, 1])
        #)
        #curve3 = ParametricFunction(
        #    lambda u: np.array([
        #        0.7 + 0.5 * u**5,
        #        u, 0
        #    ]), color=WHITE, t_range = np.array([0, 1])
        #)
        #graphs = [ axes.plot( lambda x: 0.1 + 0.2 * x**2, color = WHITE, x_range = [0,1] ),
        #           axes.plot( lambda x: 0.6 * 0.2 * math.pow(x, 1.5), color = WHITE, x_range = [0,1] ),
        #           axes.plot( lambda x: math.pow((x - 0.5)/0.5, 1/4), color = WHITE, x_range = [0,1] ),
        #           axes.plot( lambda x: math.pow((x - 0.7)/0.5, 1/5), color = WHITE, x_range = [0,1] ) ]

        self.play( Write( curve0 ) )
        #self.play( AnimationGroup( Write( curve0 ) ) )
        #                          Write( curve1 ),
        #                          Write( curve2 ),
        #                          Write( curve3 ) ) )

        self.wait( 5 )
        fadeall( self )

# vim: et sw=4 ts=4
