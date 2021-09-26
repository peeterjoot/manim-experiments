from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *

def unitParallelogram( o, v1, v2, scale ):
    v1cap = v1/ np.linalg.norm( v1 )
    cross = np.cross( v2, v1cap )

    v1 = scale * v1cap / np.linalg.norm( cross )
    v2 = scale * v2
    ov1 = o + v1
    ov2 = o + v2
    ov12 = ov1 + v2

    ppoints = [ o, ov1, ov12, ov2 ]

    return ppoints


def OrientedPolygon( *vertices, c0, c1, c2, f, d1, d2, tex, r ):
    n = len( vertices )
    l = latex( )

    #print( vertices )

    poly = Polygon( *vertices, color = c0 , fill_opacity = f )
    g = VGroup( poly )

    if tex:
        v1 = MathTex( concat( r'{ ', l.vec( 'v' ), r' }_1' ) )
        v1.set_color( c1 )
        v2 = MathTex( concat( r'{ ', l.vec( 'v' ), r' }_2' ) )
        v2.set_color( c2 )
        g = g + VGroup( v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            if tex:
                v1.next_to( a, d1 )
            a.set_color( c1 )
        elif i == 1:
            if tex:
                v2.next_to( a, d2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g



class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        t = Text( "Geometric algebra, wedge products and area." )
        t.shift( 3 * DOWN )

        self.add_fixed_in_frame_mobjects( t )
        #self.wait( )
        #self.play( FadeOut( t ) )

        #t2 = t.copy()
        #self.play( ReplacementTransform( t, t2 ) )
        #self.remove( t2 )
        #self.add_fixed_in_frame_mobjects( t2 )

        axes = ThreeDAxes()

        o0 = np.array( [ -2, -2, -1 ] )
        p1 = np.array( [ 1, 1, 1 ] )
        p2 = np.array( [ -1, 1, 0.5 ] )
        sq1 = unitParallelogram( o0, p1, p2, 4 )
        s1 = OrientedPolygon( *sq1, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )

        o1 = np.array( [ 0, 0, -1 ] )
        q1 = np.array( [ 1, -1, 1 ] )
        q2 = np.array( [ 0, 1, 1 ] )
        sq2 = unitParallelogram( o1, q1, q2, 2 )
        s2 = OrientedPolygon( *sq2, c0 = RED, c1 = RED, c2 = RED, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.2 )

        o2 = np.array( [ 0, 0, -2 ] )
        r1 = np.array( [ 1, -0.5, 0 ] )
        r2 = np.array( [ 0, -0.5, 1 ] )
        sq3 = unitParallelogram( o2, r1, r2, 3 )
        s3 = OrientedPolygon( *sq3, c0 = GREEN, c1 = GREEN, c2 = GREEN, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.2 )
       
        self.set_camera_orientation( phi = 75 * DEGREES, theta = 180 * DEGREES )
        self.add( axes, s1, s2, s3 )
        self.begin_ambient_camera_rotation( rate = 0.2 )
        self.wait( )
        self.stop_ambient_camera_rotation( )
        self.move_camera( phi = 75 * DEGREES, theta = 240 * DEGREES )
        self.wait( )

