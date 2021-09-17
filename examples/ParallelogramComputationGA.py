from manim import *
import numpy as np

def concat(*args, sep=''):
    return sep.join(args)
def mknorm(*args, sep=''):
    return concat( r'\left\lVert{', sep.join(args), r'}\right\rVert' )
def mknorm2(*args, sep=''):
    return concat( r'{', mknorm( sep.join(args) ), r'}^2' )
def lr(*args, sep=''):
    return concat( r'\left( ', sep.join(args), r' \right)' )
def lrsq(*args, sep=''):
    return concat( r'{', lr( sep.join(args) ), r'}^2' )
def sq(*args, sep=''):
    return concat( r'{', sep.join(args), r'}^2' )
def dot(a, b):
    return a + r' \cdot ' + b

class ParallelogramComputationGA(Scene):
    def construct(self):
        vecu = r'\vec{u}'
        uhat = r'\hat{u}'
        vecv = r'\vec{v}'
        squ = sq( vecu )
        sqv = sq( vecv )
        lbr  = r'\left('
        rbr  = r'\right)'
        vdotusq = lrsq( dot( vecv, uhat ) )
        nextline = r'\\'
        vwedgeuhat = concat( vecv, r'\wedge', uhat )
        vwedgeu = concat( vecv, r'\wedge', vecu )
        uwedgev = concat( vecu, r'\wedge', vecv )
        rej = concat( lr( vwedgeuhat ), uhat )

        eq = MathTex( r'\text{Area} &= \text{base} \times \text{height} \\',
                      concat( r'{\text{Area}}^2 &= ', squ, lrsq( rej ), nextline ),
                      concat( '&= -', squ, lrsq( vwedgeuhat ), nextline ),
                      concat( '&= - ', lrsq( vwedgeu ), nextline ),
                      concat( '&= ', dot( lr(vwedgeu), lr(uwedgev) ), nextline ),
                      concat( '&= ', squ, sqv, '-', lrsq( dot( vecv, vecu ) ), nextline )
                    )

        self.play( Write( eq[0] ) )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.play( Write( eq[4] ) )
        self.play( Write( eq[5] ) )
        self.wait( )
