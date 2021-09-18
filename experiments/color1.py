from manim import *

# https://stackoverflow.com/questions/69234696/can-i-override-manim-color-defaults-for-tex-and-use-xcolor-directly

class color1(Scene):
    def construct(self):

        eq1 = MathTex( r'&{\left(\vec{u} \cdot \vec{v} \right)}^2 \\',
                       '&(', r'\vec{u}', r'\cdot', r'\vec{v}', r'){}^2 \\' )
        eq1.set_color_by_tex_to_color_map( { "{u}": RED, "{v}": YELLOW } )

        eq2 = MathTex( r'&{\color{blue}{\left(\vec{u} \cdot \vec{v} \right)}^2} \\' )

        for item in eq1:
           self.play( Write( item ) )

        eq2.shift( 2 * DOWN )
        for item in eq2:
           self.play( Write( item ) )

        self.wait( )
