from manim import *

class colorlist( Scene ):
    def construct( self ):
        colormap = { "{u}": RED, "{v}": YELLOW }

        # \right\rVert gets colored, and the overarrows do not!
        #e = MathTex( r'\left\lVert{', r'\vec{u}', r'\cdot', r'\vec{v}', r'}\right\rVert' )

        # but this is okay:
        e = MathTex( r'\lVert', r'\vec{u}', r'\cdot', r'\vec{v}', r'\rVert' )
        self.add( e )
        e.set_color_by_tex_to_color_map( colormap )

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        # can we split up {} braces between list items -- in some cases:
        # this shows that the cancel sign doesn't get colored, which may be undesirable.
        e2 = MathTex( r'\cancel{', r'\vec{u}', r'}',
                      tex_template = myTemplate )
        e2.set_color_by_tex_to_color_map( colormap )

        # can't split some terms though, like '}_{' : but this works:
        e3 = MathTex( r'{\text{Proj}}_', r'{\vec{u}}', '(', r'{\vec{v}', ')',
                      tex_template = myTemplate )
        e3.set_color_by_tex_to_color_map( colormap )

        self.add( e )
        self.wait( )

        e2.shift( DOWN )
        self.add( e2 )
        self.wait( )

        e3.shift( 2 * DOWN )
        self.add( e3 )
        self.wait( )
