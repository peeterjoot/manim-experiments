from helper import *

mycolors = { l.vec('x'): GREEN, l.vec('a'):RED, l.vec('f'): BLUE, l.vec('b'): PURPLE, l.vec('c'):YELLOW }

class cMathTex(MathTex):
    def __init__(
        self,
        *tex_strings,
        arg_separator = " ",
        **kwargs,
    ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        myTemplate.add_to_preamble( r'\usepackage{txfonts}' )
        super().__init__(
                arg_separator.join( tex_strings ),
                tex_template = myTemplate,
                **kwargs,
            )
        self.set_color_by_tex_to_color_map( mycolors )
