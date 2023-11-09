from manim import *
import numpy as np
import math
from sys import *

class x( Scene ):
    def construct( self ):

        sc = 4
        axes = Axes( y_range = [0, 1, 1], x_range = [0, 1, 1], x_length = sc, y_length = sc )
        self.play( Write( axes ) )

        f0 = lambda u: np.array(( sc * u - sc/2,
                                  sc * (0.1 + 0.2 * (u**2)) - sc/2,
                                  0 ))

        f1 = lambda u: np.array(( sc * u - sc/2,
                                  sc * (0.6 + 0.3 * u**(1.5)) - sc/2,
                                  0 ))

        f2 = lambda u: np.array(( sc * (0.1 + 0.5 * u**4) - sc/2,
                                  sc * u - sc/2,
                                  0 ))

        f3 = lambda u: np.array(( sc * (0.7 + 0.5 * u**5) - sc/2,
                                  sc * u - sc/2,
                                  0 ))

        a0 = Arrow( start = f0(0.6) + 0.1 * UP, end = f0(0.3) + 0.1 * UP, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a1 = Arrow( start = f1(0.3) + 0.1 * UP, end = f1(0.6) + 0.1 * UP, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a2 = Arrow( start = f2(0.3) + 0.2 * LEFT, end = f2(0.6) + 0.2 * LEFT, color = BLUE, max_stroke_width_to_length_ratio=10 )
        a3 = Arrow( start = f3(0.6) + 0.2 * LEFT, end = f3(0.3) + 0.2 * LEFT, color = BLUE, max_stroke_width_to_length_ratio=10 )

        curve0 = ParametricFunction( f0, t_range = np.array([0, 1]) )
        curve1 = ParametricFunction( f1, t_range = np.array([0, 1]) )
        curve2 = ParametricFunction( f2, t_range = np.array([0, 1]) )
        curve3 = ParametricFunction( f3, t_range = np.array([0, 1]) )

        label0 = MathTex( r"\mathbf{x}(u, v = 0)" ).scale( 0.7 ).move_to( curve0, LEFT ).shift( 2 * LEFT + 0.4 * DOWN )
        label1 = MathTex( r"\mathbf{x}(u, v = 1)" ).scale( 0.7 ).move_to( curve1, LEFT ).shift( 2 * LEFT + 0.4 * DOWN )
        label2 = MathTex( r"\mathbf{x}(u = 0, v)" ).scale( 0.7 ).move_to( curve2, DOWN ).shift( 1 * LEFT + 0.5 * DOWN )
        label3 = MathTex( r"\mathbf{x}(u = 1, v)" ).scale( 0.7 ).move_to( curve3, DOWN ).shift( 1 * LEFT + 0.5 * DOWN )

        at0 = MathTex( r"-d \mathbf{x}_u\vert_{v = 0}" ).scale( 0.7 ).move_to( a0, LEFT ).shift( 0.3 * UP + 0.8 * LEFT )
        at1 = MathTex( r"d \mathbf{x}_u\vert_{v = 1}" ).scale( 0.7 ).move_to( a1, LEFT ).shift( 0.4 * UP + 0.2 * RIGHT )
        at2 = MathTex( r"d \mathbf{x}_v\vert_{u = 0}" ).scale( 0.7 ).move_to( a2, DOWN ).shift( 0.8 * RIGHT + 0.2 * UP )
        at3 = MathTex( r"-d \mathbf{x}_v\vert_{u = 1}" ).scale( 0.7 ).move_to( a3, DOWN ).shift( 1.0 * RIGHT + 0.2 * UP )

        self.play( AnimationGroup( Write( curve0 ),
                                   Write( curve1 ),
                                   Write( curve2 ),
                                   Write( curve3 ),
                                   Write( label0 ),
                                   Write( label1 ),
                                   Write( label2 ),
                                   Write( label3 ) ) )

        self.play( AnimationGroup( Write( a0 ), Write( at0 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a2 ), Write( at1 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a1 ), Write( at2 ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( Write( a3 ), Write( at3 ) ) )
        self.wait( 1 )

        self.wait( 5 )

# vim: et sw=4 ts=4
