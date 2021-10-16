from manim import *
import numpy as np

class DrawParallelogram( Scene ):
    def construct( self ):
        o = np.array( [ 0, -2, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] ) # u
        p2 = np.array( [ 1, 3, 0 ] ) # v
        op1 = o + p1
        op2 = o + p2
        op3 = o + p1 + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED ) # u
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW ) # v
        v1p = Arrow( start = op2, end = op3, buff = 0, color = RED ) # u'
        v2p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW ) # v'

        parallelogram = [ o, op1, op3, op2 ]
        poly = Polygon( *parallelogram, color = PURPLE, fill_opacity = 0.5 )

        self.play( Write( poly ) )
        #self.wait( )
        self.play( AnimationGroup( Write( v1 ), Write( v2 ), Write( v1p ), Write( v2p ) ) )
