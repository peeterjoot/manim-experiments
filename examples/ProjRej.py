from manim import *
import numpy as np
from mylatex import *

class ProjRej(Scene):
    def construct(self):
        l = latex()
        vecu       = l.vec('u')
        uhat       = l.hat('u')
        vecv       = l.vec('v')

        eq = MathTex( concat( vecv, r' &= ', vecv, r'\times 1', l.nextline ),
                      concat( r' &= ', vecv, uhat, uhat, l.nextline ),
                      concat( r' &= ', l.lr(vecv, uhat), uhat, l.nextline ),
                      concat( r' &= ', l.lr( l.dot(vecv, uhat), ' + ', l.wedge(vecv, uhat) ), uhat, l.nextline ),
                      concat( r' &= ', l.lr( l.dot(vecv, uhat) ), uhat, ' + ', l.lr(l.wedge(vecv, uhat)), uhat, l.nextline ),
                      concat( r'{', l.text('Proj'), r'}_{\vec{u}}(\vec{v}) &\equiv ', l.lr( l.dot(vecv, uhat) ), uhat, l.nextline ),
                      concat( r'{', l.text('Rej'), r'}_{\vec{u}}(\vec{v}) &\equiv ', l.lr( l.wedge(vecv, uhat) ), uhat, l.nextline )
                    )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
