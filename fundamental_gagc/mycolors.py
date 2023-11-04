from helper import *

mycolors = { l.vec('x'): GREEN, '{{ F }}':RED, '{{ G }}': BLUE }
#, '{{ J }}': YELLOW }

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
