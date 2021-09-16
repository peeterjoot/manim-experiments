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
def math(a):
    return '$' + a + '$'

class ParallelogramComputationClassic(Scene):
    def construct(self):
        vecu = r'\vec{u}'
        uhat = r'\hat{u}'
        vecv = r'\vec{v}'
        nsqu = mknorm2( vecu )
        nsqv = mknorm2( vecv )
        eq   = math( r'\,=\,' )
        nbsp = r'$\,$' # alignment with empty string doesn't seem to work

        eq1_text = [ math( r'\text{Area}' ), eq, math( r'\text{base} \times \text{height}' ) ]
        eq2_text = [ math( r'{\text{Area}}^2' ), eq, '${}{}$'.format( nsqu, mknorm2(r'{} - \left({} \cdot {} \right){}'.format(vecv, vecv, uhat, uhat)) ) ]
        vdotusq = lrsq( dot( vecv, uhat ) )
        eq3_text = [ nbsp, eq, math( nsqu + r'\left(' + nsqv + ' + ' + vdotusq + '- 2 ' + vdotusq + r'\right)' ) ]

        eq1_mob = Tex( *eq1_text )
        eq2_mob = Tex( *eq2_text )
        eq3_mob = Tex( *eq3_text )

        for i,item in enumerate( eq2_mob ):
            dir = RIGHT
            if i == 2:
                dir = LEFT
            item.align_to( eq1_mob[i], dir )

        for i,item in enumerate( eq3_mob ):
            dir = RIGHT
            if i == 2:
                dir = LEFT
            item.align_to( eq2_mob[i], dir )

        eq1=VGroup( *eq1_mob )
        eq1.shift( 3*LEFT + 2*UP )
        eq2=VGroup( *eq2_mob )
        eq2.shift( UP + 3*LEFT )
        eq3=VGroup( *eq3_mob )
        eq3.shift( 3*LEFT )
        self.play( Write( eq1 ) )
        self.play( Write( eq2 ) )
        self.play( Write( eq3 ) )
        self.wait( 6 )
