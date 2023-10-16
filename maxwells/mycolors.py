from helper import *

mycolors = { l.vec('E'): GREEN, l.vec('B'):RED, l.vec('J'): BLUE, l.vec('D'): GREEN, l.vec('H'):RED, l.vec('M'): BLUE }
    
class cMathTex(MathTex):
    def __init__(
        self,
        *tex_strings,
        arg_separator = " ",
        **kwargs,
    ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        super().__init__(
                arg_separator.join( tex_strings ),
                tex_template = myTemplate,
                **kwargs,
            )
        self.set_color_by_tex_to_color_map( mycolors )
