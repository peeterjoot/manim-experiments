from helper import *

class AcolorsMathTex(MathTex):
    def __init__(
        self,
        *tex_strings,
        arg_separator=" ",
        **kwargs,
    ):
        super().__init__(
                arg_separator.join(tex_strings),
                **kwargs,
            )
        self.set_color_by_tex_to_color_map( acolors )

