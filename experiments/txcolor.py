from manim import *

# Followup experimention related to:
#
# https://stackoverflow.com/questions/69234696/can-i-override-manim-color-defaults-for-tex-and-use-xcolor-directly
#
# self.play(Write()) works too slowly for separately colored items like this, but add + Transform works really nicely:

class txcolor(Scene):
    def construct(self):

        eq3 = MathTex( '(', r'\vec{u}', r'\cdot', r'\vec{v}', r'){}^2' )
        eq3.set_color_by_tex_to_color_map( { "{u}": RED, "{v}": YELLOW } )

        eq4 = MathTex( '(', r'\vec{u}', r'\cdot', r'\vec{v}', r')(', r'\vec{u}', r'\cdot', r'\vec{v}', r')' )
        eq4.set_color_by_tex_to_color_map( { "{u}": RED, "{v}": YELLOW } )

        for item in eq3:
           self.add( item )

        self.play( Transform( eq3, eq4 ) )

        self.wait( )
