from manim import *
import numpy as np
from mylatex import *

class ProjRejPerp(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{cancel}')

        eq = MathTex( concat( '&', l.dot( l.Rej(u, v), l.Proj(u, v) ), l.nextline ),
                      concat( r'\quad&=', l.gpgradezero(
                          l.underbrace( l.lr( l.wedge(v, uhat) ), uhat, helptext=l.text('Rej') ),
                          l.underbrace( uhat, l.lr( l.dot(v, uhat) ), helptext=l.text('Proj') ) ),
                          l.nextline ),
                      concat( r'\quad &=', l.gpgradezero( l.wedge(v, uhat) ), l.lr( l.dot(v, uhat) ), l.nextline ),
                      concat( r'\quad &=', l.cancel(l.gpgradezero( l.wedge(v, uhat) )), l.lr( l.dot(v, uhat) ), l.nextline ),
                      concat( r'\quad &= 0', l.nextline ),
                      tex_template = myTemplate)

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
