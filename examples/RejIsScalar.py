from manim import *
import numpy as np
from mylatex import *

class RejIsScalar(Scene):
    def construct(self):
        l = latex()
        uhat       = l.hat('u')
        v          = l.vec('v')
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{cancel}')

        eq = MathTex( 
                concat( r'{', l.text('Rej'), r'}_{\vec{u}}(\vec{v}) &\equiv ', l.lr( l.wedge(v, uhat) ), uhat, l.nextline ),
                concat( r'&= ', 
                    l.dot(l.lr( l.wedge(v, uhat) ), uhat), ' + ',
                    l.wedge(l.lr( l.wedge(v, uhat) ), uhat),
                    l.nextline ),
                concat( r'&= ', 
                    l.dot(l.lr( l.wedge(v, uhat) ), uhat), ' + ',
                    l.wedge(v, l.cancel(l.wedge( uhat, uhat)) ),
                    l.nextline ),
                concat( r'&= ', 
                    l.dot(l.lr( l.wedge(v, uhat) ), uhat), 
                    l.nextline ),
                concat( r'&= ', v, l.lr(l.dot(uhat, uhat)), ' - ', uhat, l.lr(l.dot(v, uhat)),
                    l.nextline ),
                concat( r'&= ', v, ' - ', uhat, l.lr(l.dot(v, uhat)),
                    l.nextline ),
                      tex_template = myTemplate)

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
