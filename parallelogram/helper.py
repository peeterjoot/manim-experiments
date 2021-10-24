from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *
#from mylatex2 import *
import enum # IntFlag

l          = latex( )
vecu       = l.vec( 'u' )
invu       = l.inv( vecu )
hatu       = l.hat( vecu )
vecv       = l.vec( 'v' )
vec_v1     = concat( l.vec( 'v' ), '_1' )
vec_v2     = concat( l.vec( 'v' ), '_2' )
vec_e1     = concat( l.vec( 'e' ), '_1' )
vec_e2     = concat( l.vec( 'e' ), '_2' )
vec_e3     = concat( l.vec( 'e' ), '_3' )
vec_f1     = concat( l.vec( 'f' ), '_1' )
vec_f2     = concat( l.vec( 'f' ), '_2' )
vec_e12    = concat( l.vec( 'e' ), '_{12}' )
vec_e13    = concat( l.vec( 'e' ), '_{13}' )
vec_e23    = concat( l.vec( 'e' ), '_{23}' )
uu         = l.sq( vecu )
vv         = l.sq( vecv )
uwedgev    = l.wedge( vecu, vecv )
vwedgeu    = l.wedge( vecv, vecu )
udotv      = l.dot( vecu, vecv )
vdotu      = l.dot( vecv, vecu )
lr_uwedgev = l.lr( uwedgev )
lr_vwedgeu = l.lr( vwedgeu )
lr_udotv   = l.lr( udotv )
lr_vdotu   = l.lr( vdotu )
detuivj    = l.det22( 'u_i', 'v_i', 'u_j', 'v_j' )
normu      = l.norm( vecu )
uvcolors   = { l.vec('u'): RED, l.vec('v'): YELLOW }

vec_v1, r' \wedge ', vec_v2

dv_p1 = np.array( [ 3, 1, 0 ] )
dv_p2 = np.array( [ 1, 3, 0 ] )

def DrawVectorsAndProjRej( self, prlabels ):

    o = np.array( [ 0, -2, 0 ] )
    dv_p1 = np.array( [ 3, 1, 0 ] )
    dv_p2 = np.array( [ 1, 3, 0 ] )
    op1 = o + dv_p1
    op2 = o + dv_p2

    p1cap = dv_p1/ np.linalg.norm( dv_p1 )
    proj = np.dot( dv_p2, p1cap ) * p1cap
    oproj = o + proj

    vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
    if prlabels:
        vprojl = MathTex( concat( lr_vdotu, invu ) )
    else:
        vprojl = Text( 'Proj' )
    vprojl.set_color( PURPLE )
    vprojl.next_to( vproj, DOWN )

    rej = dv_p2 - proj
    vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
    if prlabels:
        vrejl = MathTex( concat( lr_vwedgeu, invu ) )
    else:
        vrejl = Text( 'Rej' )
    vrejl.set_color( GREEN )
    vrejl.next_to( vrej, 0.2 * RIGHT )

    v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
    v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
    v1l = MathTex( vecu )
    v1l.set_color( RED )
    v1l.next_to( v1, RIGHT )
    v1l.shift( 0.5 * LEFT )
    v2l = MathTex( vecv )
    v2l.set_color( YELLOW )
    v2l.next_to( v2, UP )
    v2l.shift( 0.5 * DOWN )

    all = VGroup( v1, v1l, v2, v2l, vproj, vrej, vprojl, vrejl )

    move = ( -6.5, 2, 0 )
    all.shift( move )

    self.add( all )

    return ( vprojl, vrejl )


def OrientedPolygon( *vertices, c0, c1, c2, f, d1, d2, tex, r ):
    n = len( vertices )

    #print( vertices )

    poly = Polygon( *vertices, color = c0 , fill_opacity = f )
    g = VGroup( poly )

    if tex:
        v1 = MathTex( vec_v1 )
        v1.set_color( c1 )
        v2 = MathTex( vec_v2 )
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


def OrientedRegularPolygon( num, r, c, f ):
    x = np.array( [ r, 0, 0 ] )
    pts = [ x ]
    theta = math.pi * 2 / num
    for i in range( 1, num ):
        y = np.array( [ r * math.cos( i * theta ), r * math.sin( i * theta ), 0 ] )
        direction = x - y
        x = y
        last = pts[ i - 1 ]
        pts.append( last + direction )

    sq = OrientedPolygon( *pts, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )

    return sq


def playAndFadeOut( self, eq, pos ):
    eq[ 0 ].move_to( pos )
    eq[ 0 ].shift( 2 * DOWN )
    eq[ 1 ].move_to( eq[ 0 ] )
    eq[ 0 ].shift( 3 * LEFT )
    eq[ 1 ].shift( RIGHT )
    self.play( Write( eq[ 0 ] ), Write( eq[ 1 ] ) )

    n = len( eq )

    last = eq[ 1 ]
    for i in range( 1, n - 1 ):
        eq[ i + 1 ].move_to( last )
        self.play( ReplacementTransform( last, eq[ i + 1 ] ) )
        last = eq[ i + 1 ]
        self.wait( )

    g = VGroup( eq[ 0 ], last )
    self.play( FadeOut( g ) )


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


def int2str( v ):
    if v == 1:
        vstr = ''
    elif v == -1:
        vstr = '-'
    else:
        vstr = str( v )
    return vstr

class vsflags( enum.IntFlag ):
    default = 0
    braces = 1
    signed = 2

def vecstr( l, v, e, flags ):
    vs = str( v )
    if v == 1:
        if flags & vsflags.signed:
            vstr = concat( '+', e )
        else:
            vstr = e
    else:
        if v == -1:
            if flags & vsflags.braces:
                vstr = l.lr( '-', e )
            else:
                vstr = concat( '-', e )
        else:
            if flags & vsflags.braces:
                if (flags & vsflags.signed) and (v > 0):
                    vstr = l.lr( '+', vs, e )
                else:
                    vstr = l.lr( vs, e )
            else:
                if (flags & vsflags.signed) and (v > 0):
                    vstr = concat( '+', vs, e )
                else:
                    vstr = concat( vs, e )
    return vstr


def OrientedPolygon2( *vertices, c0, c1, c2, f, s1, s2, r ):
    n = len( vertices )

    poly = Polygon( *vertices, color = c0, fill_opacity = f )

    s1str = vecstr( l, s1, vec_e1, vsflags.default )
    s2str = vecstr( l, s2, vec_e2, vsflags.default )

    v1 = MathTex( s1str )
    v1.set_color( c1 )
    v2 = MathTex( s2str )
    v2.set_color( c2 )
    g = VGroup( poly, v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            v1.move_to( (vertices[0] + vertices[1])/2 - np.sign( s2 ) * UP/2 )
            a.set_color( c1 )
        elif i == 1:
            v2.move_to( (vertices[2] + vertices[1])/2 - np.sign( s1 ) * LEFT/2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g



def write_area_products( self, n1, n2, ar, o ):
    p = n1 * n2
    an1 = abs( n1 )
    an2 = abs( n2 )
    rect1   = Rectangle( color = GREEN_B, width = an1, height = an2, fill_opacity = 0.5 )
    rect1.move_to( RIGHT * n1/2 + UP * n2/2 )

    absp = abs( p )
    prod_string = int2str( p )

    n1vec = vecstr( l, n1, vec_e1, vsflags.braces )
    n2vec = vecstr( l, n2, vec_e2, vsflags.braces )
    prodvec = vecstr( l, n1 * n2, l.mult( vec_e1, vec_e2 ), vsflags.signed )
    pp2 = MathTex( n1vec, n2vec, ' = ', prodvec )
    pp2[0].set_color( RED )
    pp2[1].set_color( BLUE )
    pp2[3].set_color( GREEN_B )

    v1 = np.array( [ n1, 0, 0 ] )
    v2 = np.array( [ 0, n2, 0 ] )
    pts = [ o, o + v1, o + v1 + v2, o + v2 ]
    rect2 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = n1, s2 = n2, r = ar )
    pp2.move_to( 3 * DOWN )

    tog = VGroup( rect2, pp2 )
    self.play( Write( tog ) )
    self.wait( 2 )

    return rect2, pp2

# vim: et sw=4 ts=4
