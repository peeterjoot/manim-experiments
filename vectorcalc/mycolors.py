from helper import *

# write just the "&= foo \\" line for aligned:
def aligned1( self, eq, ref, sh, w ):
    eq[0].next_to( ref, DOWN ).shift( sh )
    elen = len(eq)
    for i in range(elen):
        if i + 1 < elen:
            eq[i+1].next_to( eq[i], RIGHT )
        self.play( Write( eq[i] ) )
    self.wait( w )

# Model this common aligned construct:
#
# \begin{aligned}
# a &= b0 + b1 \\
#   &= c0 + c1 + c2
#   &= d0 + d1 + d2 + d3
# \end{aligned}
#
# The input would look like:
#
# eq = [ [ MathTex( r"a" )
#          MathTex( r"=" )
#          MathTex( r"b0" ), MathTex( r"+ b1" ) ],
#        [ MathTex( r"=" )
#          MathTex( r"c0" ), MathTex( r"+ c1" ), MathTex( r"+ c2" ) ],
#        [ MathTex( r"=" )
#          MathTex( r"d0" ), MathTex( r"+ d1" ), MathTex( r"+ d2" ), MathTex( r"+ d3" ) ] ]
#
# The stuff after the = sign doesn't have to be split up, but it can be (to allow for easy Indicate() or transformation if desired.)
#
def aligned( self, eq, ref, ish, sh, w1, w2 ):
    eq[0][1].next_to( ref, DOWN ).shift( ish )
    eq[0][0].next_to( eq[0][1], LEFT )
    elen = len(eq[0])
    for i in range(elen):
        if i > 1:
            eq[0][i].next_to( eq[0][i-1], RIGHT )
        self.play( Write( eq[0][i] ) )
    ref = eq[0][1]
    self.wait( w1 )
    alen = len(eq)
    for j in range(alen-1):
        #eq[j+1][0].next_to( ref, DOWN ).shift( sh )
        #elen = len(eq[j+1])
        #for i in range(elen):
        #    if i + 1 < elen:
        #        eq[j+1][i+1].next_to( eq[j+1][i], RIGHT )
        #    self.play( Write( eq[j+1][i] ) )
        #self.wait( w2 )
        aligned1( self, eq[j+1], ref, sh, w2 )
        ref = eq[j+1][0]

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
