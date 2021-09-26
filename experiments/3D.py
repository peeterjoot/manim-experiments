# https://docs.manim.community/en/stable/examples.html
from manim import *

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 42

        def param_gauss(u, v):
            x = u
            y = v

            # what were the python language designs smoking to allow assignment syntax like this:
            #sigma, mu = 0.4, [0.0, 0.0]

            sigma = 0.4
            mu = [0.0, 0.0]

            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        # looks like manim gets phi vs. theta mixed up.  phi seems to be the angle from the z-axis
        gauss_plane.scale_about_point(2, ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        #gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes,gauss_plane)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=100 * DEGREES, theta=60 * DEGREES)
        self.wait()

