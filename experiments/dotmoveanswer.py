from manim import *

class Example(Scene):
    def construct(self):
        tline = NumberLine(
            x_range=[ 0, 1 ],
            length=4,
            color=BLUE,
            include_numbers=False )

        t_parameter = ValueTracker(0)
        t_marker = Dot(color=YELLOW).add_updater(
            lambda mob: mob.move_to(tline.number_to_point(t_parameter.get_value())),
        ).update()
        self.play( DrawBorderThenFill( VGroup( tline ) ), run_time = 2 )
        self.add(t_marker)
        self.play(
            UpdateFromAlphaFunc(
                t_parameter, 
                lambda mob, alpha: mob.set_value(np.sin(alpha * PI)),
                run_time=6
            )
        )
