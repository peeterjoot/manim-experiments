from helper import *

class Position_010( Scene ):
    def construct( self ):

        #title = Text( 'Circular velocity and acceleration.' )
        title = Text( 'Circular coordinates.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        if 0:
            eq = [ AcolorsMathTex( concat( vec_x, ' = x_r ', hat_r, r' + x_\theta', hat_theta ) ),
                   AcolorsMathTex( concat( hat_r, ' = ', vec_e1, r'e^{i\theta}' ) ),
                   AcolorsMathTex( concat( hat_theta, ' = ', vec_e2, r'e^{i\theta}' ) ),
                   AcolorsMathTex( concat( 'i = ', vec_e1, vec_e2 ) ),
                   AcolorsMathTex( concat( vec_e1, vec_e1, ' = ', vec_e2, vec_e2, '= 1' ) ),
                   AcolorsMathTex( concat( vec_e1, vec_e2, ' = -', vec_e2, vec_e1 ) ) ]

            eq[0].shift( 1.5 * UP )
            self.play( Write( eq[0] ) )
            self.wait( 5 )

            i = 0
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.40 * LEFT, None )
            self.wait( 5 )
            i = 1
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.40 * LEFT, None )
            self.wait( 5 )
            i = 2
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.35 * LEFT, None )
            self.wait( 5 )
            i = 3
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.80 * LEFT, None )
            self.wait( 5 )
            i = 4
            write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.00 * LEFT, None )
            self.wait( 5 )

        axes = Axes( x_range = [-1, 4, 1], y_range = [-1, 4, 1], x_length = 4, y_length = 4,
                     axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

        #axes.to_edge(UR)
        axes.to_edge( DOWN + LEFT )
        #axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        #graph = axes.plot( lambda x : x**0.5, x_range = [0, 4], color = YELLOW )
        #graph = axes.plot_parametric_curve( lambda x : x**0.5, x_range = [0, 4], color = YELLOW )
        #r = lambda theta: 2 * np.sin(theta * 5)
        r = lambda theta: 3
        graph = axes.plot_polar_graph(r, [0, 0.5 * PI], color=ORANGE)

        #r2 = lambda t: 1 + 3 * t
        #graph2 = ParametricFunction(
        #    function=lambda r: self.pr2pt(r2, t_func(th), th),
        #    t_range=theta_range,
        #    **kwargs,
        #)
        #graph2.underlying_function = r_func

        graphing_stuff = VGroup( axes, graph )
        #graphing_stuff += axis_labels

        self.play(DrawBorderThenFill(axes), run_time = 2)
        #self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
        self.wait()
        self.play(Create(graph), run_time = 2)
        self.wait()

        #plane = PolarPlane()
        #self.add(plane, graph)

# def plot_parametric_curve(self, function, **kwargs):
#        dim = self.dimension
#        graph = ParametricFunction(
#            lambda t: self.coords_to_point(*function(t)[:dim]), **kwargs
#        )
#        graph.underlying_function = function
#        return graph


# vim: et sw=4 ts=4
