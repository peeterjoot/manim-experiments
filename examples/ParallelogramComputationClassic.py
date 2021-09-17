from manim import *
import numpy as np

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'
def mknorm2(v):
    return r'{\left\lVert{' + v + r'}\right\rVert}^2'
def lr(v):
    return r'\left( ' + v + r' \right)'
def lrsq(v):
    return r'{\left( ' + v + r' \right)}^2'
def dot(a,b):
    return a + r' \cdot ' + b
def concat(*args, sep=''):
    return sep.join(args)

class ParallelogramComputationClassic(Scene):
    def construct(self):
        vecu = r'\vec{u}'
        uhat = r'\hat{u}'
        vecv = r'\vec{v}'
        nsqu = mknorm2( vecu )
        nsqv = mknorm2( vecv )
        lbr  = r'\left('
        rbr  = r'\right)'
        vdotusq = lrsq( dot( vecv, uhat ) )
        nextline = r'\\'
        rej = concat( vecv, '-', lbr, dot( vecv, uhat ), rbr, uhat )

        eq = MathTex( r'\text{Area} &= \text{base} \times \text{height} \\',
                      concat( r'{\text{Area}}^2 &= ', nsqu, mknorm2( rej ), nextline ),
                      concat( '&= ', nsqu, lbr, nsqv, ' + ', vdotusq, '- 2 ', vdotusq, rbr, nextline ),
                      concat( '&= ', nsqu, lbr, nsqv, ' - ', vdotusq, rbr, nextline ),
                      concat( '&= ', nsqu, nsqv, ' - ', lrsq( dot( vecv, vecu ) ), nextline )
                    )

        self.play( Write( eq[0] ) )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.play( Write( eq[4] ) )
        self.wait( )
