from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from listlatex import *

#def showeq( self, *eq, doshift = True ):
def showeq( self, *eq ):
    for item in eq:
        #if doshift:
        #    self.shift( DOWN )
        self.add( item )
    self.wait( )

class RejIsScalar( Scene ):
    def construct( self ):
        l = latex()
        uhat       = l.hat( 'u' )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        #eq1 = MathTex( *l.Rej( u, v ), r' &\equiv ', *l.lr( l.wedge( v, uhat ) ), *uhat, *l.newline )
        eq1 = MathTex( u, ' ', v, ' ', uhat, ' ', *l.Proj(u,v) )
        #eq2 = MathTex( r'&= ', l.lr( l.wedge( v, uhat ) ), l.cdot, uhat, l.plus, l.wedge( l.lr( l.wedge( v, uhat ) ), uhat ), l.newline )k
        #eq3 = MathTex( r'&= ', l.add( l.dot( l.lr( l.wedge( v, uhat ) ), uhat), l.wedge( v, l.cancel( l.wedge( uhat, uhat ) ) ) ), l.newline,
        #               tex_template = myTemplate )
        #eq4 = MathTex( r'&= ', l.dot( l.lr( l.wedge( v, uhat ) ), uhat, l.newline )
        #eq5 = MathTex( r'&= ', v, l.sub( l.lr( l.dot( uhat, uhat ) ), l.mult( uhat, l.lr( l.dot( v, uhat) ) ), l.newline )
        #eq6 = MathTex( r'&= ', v, l.neg( uhat, l.lr( l.dot( v, uhat ) ), l.newline )

        showeq( self, eq1 )
        #eq2.shift( DOWN )
        #showeq( self, eq2 )
        #showeq( self, eq3 )
        #showeq( self, eq4 )
        #showeq( self, eq5 )
        #showeq( self, eq6 )
