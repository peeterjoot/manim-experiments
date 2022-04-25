from manim import *
import numpy as np

config.background_color = "#3d3d3d"

class VectorFieldScene1(Scene):
    def construct(self):

        grid = NumberPlane(axis_config={"include_tip":True},
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 0.8,
                "stroke_opacity": 0.2
            }
        )
        self.play(Create(grid))
        self.wait()

        # length_func = lambda x: 2
        mu = 0.45
        def x_dot(x,y):
            return y

        def y_dot(x,y):
            return mu*(1-x*x)*y-x

        func = lambda pos: (x_dot(pos[0],pos[1]))*RIGHT + (y_dot(pos[0],pos[1]))*UP
        vf = ArrowVectorField(func, x_range = [-7, 7, 0.4], y_range = [-5, 5, 0.4])#, length_func  = length_func) #stroke_width does nothing :(
        self.play(Create(vf))
        self.wait()


        self.x1 = 0.5 #initial value
        self.v1 = 0
        self.t = 0
        dot = always_redraw(
            lambda: Dot().move_to(
                grid.c2p(self.x1, self.v1)
                # grid.c2p(t.get_value(), np.sin(t.get_value()))
            )
        )
        self.play(Create(dot))

        path = VMobject()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path)

        def update_box(mob, dt):
            #update acceleration
            self.a1 = y_dot(self.x1,self.v1)
            # #update velocity
            self.v1 = self.v1 + self.a1 * dt
            #update position
            self.x1 = self.x1 + self.v1 * dt
            #update time
            self.t = self.t + dt

        dot.add_updater(update_box)

        self.wait(1)

        stream_lines = StreamLines(
            func, stroke_width=1,
            max_anchors_per_line=50
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1, max_anchors_per_line=5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

        self.wait(20)
