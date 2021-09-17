from manim import *

class ProjRej(Scene):
    def construct(self):

        eq = MathTex( 
'&',
r'{\left\lVert{ \vec{v} }\right\rVert}^2',
r'{\left\lVert{ \vec{u} }\right\rVert}^2',
r'-{\left(\vec{ u } \cdot \vec{v} \right)}^2', r'\\',
'&',
r'{\left\lVert{ \vec{b} }\right\rVert}^2',
r'{\left\lVert{ \vec{a} }\right\rVert}^2',
r'-{\left( \vec{a} \cdot \vec{b} \right)}^2', r'\\',
'&',
'(', r'\vec{a}', r'\cdot', r'\vec{b}', '){}^2'
                )
        eq.set_color_by_tex_to_color_map( { 
                  "{u}": RED, "{v}": YELLOW,
                  "{a}": RED, "{b}": YELLOW 
                  } )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
