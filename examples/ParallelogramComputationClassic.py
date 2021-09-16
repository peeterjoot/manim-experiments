from manim import *
import numpy as np

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'
def mknorm2(v):
    return r'{\left\lVert{' + v + r'}\right\rVert}^2'
def lr(v):
    return r'\left( ' + v + r' \right)'

class ParallelogramComputationClassic(Scene):
    def construct(self):
        eq1_text=[ r'$\text{Area}$', '$=$', r'$\text{base} \times \text{height}$' ]
        eq2_text=[ r'${\text{Area}}^2$', '$=$', '$' + mknorm2(r'\vec{u}') + mknorm2(r'\vec{v} - \left(\vec{v} \cdot \hat{u}\right) \hat{u}') + r'$' ]
        eq3_text=[ r'$\,$', '$=$', '$' + mknorm2(r'\vec{u}') + '\left(' + mknorm2( r'\vec{v}') + r' + {\left(\vec{v} \cdot \hat{u}\right)}^2 -2 {\left(\vec{v} \cdot \hat{u}\right)}^2 \right) $' ]
        #eq4_text=[ '', '$=$', '$' + mknorm2(r'\vec{u}') + '\left(' + mknorm2( r'\vec{v}') + r' - {\left(\vec{v} \cdot \hat{u}\right)}^2 \right) $' ]
        eq1_mob=Tex(*eq1_text)
        eq2_mob=Tex(*eq2_text)
        eq3_mob=Tex(*eq3_text)
        #eq4_mob=Tex(*eq4_text)

        for i,item in enumerate(eq2_mob):
            dir = RIGHT
            if i == 2:
                dir = LEFT
            item.align_to(eq1_mob[i], dir)

        for i,item in enumerate(eq3_mob):
            dir = RIGHT
            if i == 2:
                dir = LEFT
            item.align_to(eq2_mob[i], dir)

        #for i,item in enumerate(eq4_mob):
        #    dir = RIGHT
        #    if i == 2:
        #        dir = LEFT
        #    item.align_to(eq3_mob[i], dir)

        eq1=VGroup(*eq1_mob)
        #eq1.shift(UP)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq3=VGroup(*eq3_mob)
        eq3.shift(DOWN)
        #eq4=VGroup(*eq4_mob)
        #eq4.shift(DOWN)
        self.play( Write(eq1) )
        self.play( Write(eq2) )
        self.play( Write(eq3) )
        #self.play( Write(eq4) )
        #self.play( FadeOut(eq2_mob[2]) )
