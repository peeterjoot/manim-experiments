from manim import *
import numpy as np
from mylatex import *

class ProjRejPerp(Scene):
    def construct(self):
        l = latex()
        vecu       = l.vec('u')
        uhat       = l.hat('u')
        vecv       = l.vec('v')
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{cancel}')

        eq = MathTex( concat( r'&{', l.text('Proj'), r'}_{\vec{u}}(\vec{v}) \cdot {', l.text('Rej'), r'}_{\vec{u}}(\vec{v})', l.nextline ),
                      concat( r'&\quad', l.gpgradezero( l.lr( l.wedge(vecv, uhat) ), uhat, uhat, l.lr( l.dot(vecv, uhat) ) ), l.nextline ),
                      concat( r'&\quad', l.cancel(l.gpgradezero( l.wedge(vecv, uhat) )), l.lr( l.dot(vecv, uhat) ), l.nextline ),
                      concat( r'&\quad = 0', l.nextline ),
                      tex_template = myTemplate)

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
