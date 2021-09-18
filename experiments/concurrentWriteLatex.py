from manim import *

class ProjRej(Scene):
    def construct(self):

        eq = MathTex( 
r'&{\left\lVert{ \vec{v} }\right\rVert}^2{\left\lVert{ \vec{u} }\right\rVert}^2-{\left(\vec{ u } \cdot \vec{v} \right)}^2\\',
r'&{\left\lVert{ \vec{v} }\right\rVert}^2{\left\lVert{ \vec{u} }\right\rVert}^2-{\left(\vec{ u } \cdot \vec{v} \right)}^2\\'
                )

        self.play( Write( eq[0] ), Write( eq[1] ) )

        self.wait( )
