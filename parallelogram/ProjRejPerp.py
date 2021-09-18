from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

class ProjRejPerp(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')
        proj       = l.mult( uhat, l.lr( l.wedge(v, uhat) ) )
        rej        = l.mult( l.lr( l.wedge(v, uhat) ), uhat )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{cancel}')

        eq = MathTex( concat( '&', l.dot( l.Rej(u, v), l.Proj(u, v) ), l.newline ),
                      concat( r'\quad&=', l.gpgradezero(
                          l.underbrace( rej, helptext=l.text('Rej') ),
                          l.underbrace( proj, helptext=l.text('Proj') ) ),
                          l.newline ),
                      concat( r'\quad &=', l.gpgradezero( l.wedge(v, uhat) ), l.lr( l.dot(v, uhat) ), l.newline ),
                      concat( r'\quad &=', l.cancel(l.gpgradezero( l.wedge(v, uhat) )), l.lr( l.dot(v, uhat) ), l.newline ),
                      concat( r'\quad &= 0', l.newline ),
                      tex_template = myTemplate)

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
