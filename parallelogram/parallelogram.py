from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *
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



class TitlePage( ThreeDScene ):
    def construct( self ):
        t = Text( "Geometric algebra: wedge products and area." )
        t.shift( 3 * DOWN )

        self.add_fixed_in_frame_mobjects( t )
        #self.wait( )
        #self.play( FadeOut( t ) )

        #t2 = t.copy()
        #self.play( ReplacementTransform( t, t2 ) )
        #self.remove( t2 )
        #self.add_fixed_in_frame_mobjects( t2 )

        axes = ThreeDAxes( )

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

        self.set_camera_orientation( phi = 75 * DEGREES, theta = 0 * DEGREES )
        self.add( axes, s1, s2, s3 )
        self.begin_ambient_camera_rotation( rate = 0.5 )
        self.wait( 8 ) # how long to animate the motion.
        # This results in a zippy move at the very end of the smooth rotation:
        #self.move_camera( phi = 75 * DEGREES, theta = 360 * DEGREES )
        self.stop_ambient_camera_rotation( )
        self.wait( 1 )


class Overview( Scene ):
    def construct( self ):
        blist = BulletedList( "Parallelogram area (visually, algebraic)",
                              "Projection and rejection (geometric algebra)",
                              "Parallelogram area (GA)",
                              "Determinant structure of the wedge product",
                              "Orientation and signed areas",
                              height = 3 )
        for item in blist:
            self.play( Write( item ) )

        self.wait( )

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram( Scene ):
    def construct( self ):
        o = np.array( [ -2, -2, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] ) # u
        p2 = np.array( [ 1, 3, 0 ] ) # v
        op1 = o + p1
        op2 = o + p2
        op3 = o + p1 + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED ) # u
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW ) # v

        v1l = MathTex( vecu )
        v2l = MathTex( vecv )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v1l.shift( - 0.3 * p1 )
        v2l.next_to( v2, UP )
        v2l.shift( - 0.3 * p2 )
        v2l.set_color( YELLOW )

        p1cap = p1/ np.linalg.norm( p1 )
        proj = np.dot( p2, p1cap ) * p1cap

        rej = p2 - proj

        v1g = VGroup( v1, v1l )
        v2g = VGroup( v2, v2l )

        v1p = Arrow( start = op2, end = op3, buff = 0, color = RED ) # u'
        v2p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW ) # v'
        parallelogram = [ o, op1, op3, op2 ]
        poly = Polygon( *parallelogram, color = PURPLE, fill_opacity = 0.5 )

        cut = op1 + rej
        recttop = cut - p1
        dashrej = DashedLine( start = op1, end = cut, color = BLUE )
        dashtop = DashedLine( start = cut, end = recttop )
        dashside = DashedLine( start = recttop, end = o, color = BLUE )

        self.play( AnimationGroup( Write( v1g ) ) )
        self.play( AnimationGroup( Write( v2g ) ) )
        self.wait( )
        v1c = v1.copy( )
        v2c = v2.copy( )
        self.add( v1c )
        self.add( v2c )
        self.play( ReplacementTransform( v1c, v1p ) )
        self.wait( )
        self.play( ReplacementTransform( v2c, v2p ) )
        self.wait( 2 )
        # audio: 08:00: +08s

        fromg = v1g + v2g + VGroup( v1p, v2p )
        self.play( FadeOut( fromg ) )
        self.play( FadeIn( poly ) )
        self.play( FadeIn( fromg ) )
        self.wait( 2 )

        self.play( Write( dashrej ) )
        self.play( Write( dashtop ) )
        self.play( Write( dashside ) )
        self.wait( 2 )
        self.play( FadeOut( poly ) )
        rectpoints = [ o, op1, op1 + rej, o + rej ]
        rect = Polygon( *rectpoints, color = PURPLE, fill_opacity = 0.5 )
        self.play( FadeIn( rect ) )
        self.wait( 1 )
        # audio: 23:00: +15s

        self.play( FadeOut( rect ) )
        move = ( -4, 1, 0 )
        a = VGroup( dashrej, dashtop, dashside, v1, v1l, v2, v2l, v1p, v2p ) # , poly
        self.play( a.animate.shift( move ) )
        self.wait( 1 )

        squ        = l.norm2( vecu )
        sqv        = l.norm2( vecv )
        vdotuhatsq = l.lrsq( l.dot( vecv, hatu ) )
        rej        = l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) )

        eq2 = MathTex( l.text( 'base' ), r'& = \Vert', vecu, concat( r'\Vert', l.newline ),
                       l.text( 'height' ), '& = ', concat( l.norm( rej ), l.newline ) )
        eq2[0].set_color( RED )
        eq2[1].set_color( RED )
        eq2[2].set_color( RED )
        eq2[3].set_color( RED )
        eq2[4].set_color( GREEN )
        eq2[5].set_color( GREEN )
        eq2[6].set_color( GREEN )

        vdotuhatsq_dist = l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) )
        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.newline ), # 1
                      concat( '&= ', squ ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2, 3
                      concat( '&= ', squ ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4, 5
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.mult( squ, vdotuhatsq ) ), l.newline ), # 6
                      concat( '&= ', l.sub( l.mult( squ, sqv ), vdotuhatsq_dist ), l.newline ), # 7
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( vdotu ) ), l.newline ) # 8
                    )

        oproj = o + proj
        vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
        vproj.shift( move )
        vprojl = MathTex( concat( l.lr( l.dot( vecv, hatu ) ), hatu ) )
        vprojl.set_color( PURPLE )
        vprojl.next_to( vproj, DOWN )
        vprojl.shift( 0.2 * ( UP + RIGHT ) )

        vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
        vrej.shift( move )
        vrejl = MathTex( concat( vecv, ' - ', l.lr( l.dot( vecv, hatu ) ), hatu ) )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, RIGHT )
        vrejl.shift( 2.0 * UP + 1.5 * LEFT )
        vrejl.shift( ( -0.5, 0, 0 ) )

        self.play( Write( VGroup( vproj, vprojl ) ) )
        self.wait( )
        self.play( Write( VGroup( vrej, vrejl ) ) )
        self.wait( )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        self.play( Write( eq2 ) )
        self.wait( 4 )
        # audio: 35:00: +12s

        eq.shift( 2 * DOWN + 2.4 * RIGHT )
        self.play( Write( eq[ 0 ] ) )
        self.wait( 2 )

        for i in range( 1, 4 ):
            self.play( Write( eq[ i ] ) )
            self.wait( 2 )
        self.wait( 2 )
        eq[ 5 ].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[ 3 ], eq[ 5 ] ) )
        self.wait( 3 )

        i = 6
        eq[ i ].shift( 1.1 * UP )
        self.play( Write( eq[ i ] ) )
        self.wait( 3 )

        i = 7
        eq[ i ].shift( 1.95 * UP )
        self.play( ReplacementTransform( eq[ 6 ], eq[ 7 ] ) )
        self.wait( 3 )

        i = 8
        eq[ i ].shift( 2.8 * UP )
        self.play( ReplacementTransform( eq[ 7 ], eq[ 8 ] ) )
        self.wait( 3 )


class ProjRej( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )

        labels = DrawVectorsAndProjRej( self, 0 )

        eq = MathTex( concat( vecv, r' &= ', vecv, r'\times 1', l.newline ),
                      concat( r' &= ', vecv, l.lr( vecu, invu ), l.newline ),
                      concat( r' &= ', l.lr( vecv, vecu ), invu, l.newline ),
                      concat( r' &= ', l.lr( l.add( vdotu, vwedgeu ) ), invu, l.newline ),
                      concat( r' &= ', l.add( proj, rej ), l.newline ) )

        eq.shift( 2 * RIGHT )
        for item in eq:
           self.play( Write( item ) )
           self.wait( 7 )
        self.wait( 1 )

        o = np.array( [ -4, -2, 0 ] )
        p1 = dv_p1
        p2 = dv_p2

        ulen = np.linalg.norm( p1 )
        ucap = p1 / ulen
        n_udotv = np.dot( p1, p2 )
        uinverse = ucap / ulen

        a_u = Arrow( start = o, end = o + p1, buff = 0, color = PURPLE )
        l_u = MathTex( vecu )
        l_u.move_to( a_u, LEFT )
        l_u.shift( 0.6 * LEFT + 0.8 * DOWN )
        l_u.set_color( PURPLE )
        self.play( AnimationGroup( Write( a_u ), Write( l_u ) ) )
        self.wait( 2 )

        a_ucap = Arrow( start = o, end = o + ucap, buff = 0, color = PURPLE )
        l_ucap = MathTex( hatu )
        l_ucap.move_to( l_u )
        l_ucap.set_color( PURPLE )
        g1 = VGroup( a_u, l_u )
        g2 = VGroup( a_ucap, l_ucap )
        self.play( ReplacementTransform( g1, g2 ) )
        self.wait( 2 )

        a_uinverse = Arrow( start = o, end = o + uinverse, buff = 0, color = PURPLE )
        l_uinverse = MathTex( l.inv( vecu ) )
        l_uinverse.move_to( l_u )
        l_uinverse.set_color( PURPLE )
        g3 = VGroup( a_uinverse, l_uinverse )
        self.play( ReplacementTransform( g2, g3 ) )
        self.wait( 2 )

        v_proj = uinverse * n_udotv
        a_proj = Arrow( start = o, end = o + v_proj, buff = 0, color = PURPLE )
        l_proj = MathTex( proj )
        l_proj.move_to( l_u )
        l_proj.shift( LEFT )
        l_proj.set_color( PURPLE )
        g4 = VGroup( a_proj, l_proj )
        self.play( ReplacementTransform( g3, g4 ) )
        self.wait( 2 )
        projl = MathTex( proj )
        projl.set_color( PURPLE )
        projl.move_to( labels[ 0 ] )
        self.play( ReplacementTransform( VGroup( labels[0] ) + g4, projl ) )
        self.wait( 7 )

        o2 = o + DOWN + RIGHT
        a_uinverse2 = Arrow( start = o2, end = o2 + uinverse, buff = 0, color = GREEN )
        l_uinverse2 = MathTex( l.inv( vecu ) )
        l_uinverse2.move_to( a_uinverse2 )
        l_uinverse2.set_color( GREEN )
        l_uinverse2.shift( LEFT )
        g3p = VGroup( a_uinverse2, l_uinverse2 )

        self.play( AnimationGroup( Write( a_uinverse2 ), Write( l_uinverse2 ) ) )
        self.wait( 1 )
        v_rej = p2 - v_proj
        a_rej = Arrow( start = o2, end = o2 + v_rej, buff = 0, color = GREEN )
        l_rej = MathTex( rej )
        l_rej.move_to( a_rej )
        l_rej.shift( LEFT + DOWN )
        l_rej.set_color( GREEN )
        g5 = VGroup( a_rej, l_rej )
        self.play( ReplacementTransform( g3p, g5 ) )
        self.wait( 2 )
        rejl = MathTex( rej )
        rejl.set_color( GREEN )
        rejl.move_to( labels[ 1 ] )
        rejl.shift( 0.5 * RIGHT )
        self.play( ReplacementTransform( VGroup( labels[1] ) + g5, rejl ) )
        self.wait( 3 )



class ProjRej2( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        proj2      = l.mult( l.lr( l.dot( vecv, hatu ) ), hatu )
        rej2       = l.mult( l.lr( l.wedge( vecv, hatu ) ), hatu )

        eq = MathTex( concat( l.Proj( vecu, vecv ), ' &\equiv ', proj, l.newline ),
                      concat( l.Rej( vecu, vecv ),  ' &\equiv ', rej, l.newline ) )
        eq2 = MathTex( concat( l.Proj( vecu, vecv ), ' &\equiv ', proj, ' = ', proj2, l.newline ),
                       concat( l.Rej( vecu, vecv ),  ' &\equiv ', rej, ' = ', rej2, l.newline ) )

        for item in eq:
            self.play( Write( item ) )

        self.play( ReplacementTransform( eq, eq2 ) )

        self.wait( )



class RejRotate( Scene ):
    def construct( self ):
        o = np.array( [ -1, -1.5, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] )
        p2 = np.array( [ 1, 3, 0 ] )
        op1 = o + p1
        op2 = o + p2

        p1cap = p1/ np.linalg.norm( p1 )
        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
        v1l = MathTex( vecu )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v2l = MathTex( vecv )
        v2l.set_color( YELLOW )
        v2l.next_to( v2, UP )

        all = VGroup( v1, v1l, v2, v2l )

        q1 = Arrow( start = o, end = ( o + p1cap ), buff = 0, color = RED )
        q1l = MathTex( hatu )
        q1l.set_color( RED )
        q1l.next_to( q1, DOWN )
        q1g = VGroup( q1, q1l )
        v1g = VGroup( v1, v1l )

        proj = p1cap * np.dot( p2, p1cap )
        rej = p2 - proj
        rejcap = rej/ np.linalg.norm( rej )
        rot = [ o, o + p1cap, o + p1cap + rejcap, o + rejcap ]
        rot2 = [ o, o + p1cap, o + p1cap + rej, o + rej ]

        self.add( all )
        self.play( ReplacementTransform( v1g, q1g ) )
        self.wait( )
        bi = np.empty( 4, dtype = object )
        bi2 = np.empty( 4, dtype = object )
        for i in range( 3 ):
            bi[ i ] = Arrow( rot[ i ], rot[ ( i + 1 ) % 4 ], buff = 0 )
            bi2[ i ] = Arrow( rot2[ i ], rot2[ ( i + 1 ) % 4 ], buff = 0 )
            self.play( Write( bi[ i ] ) )

        i = 3
        bi[ i ] = Arrow( rot[ 3 ], o + 0.1 * rejcap, buff = 0 )
        bi2[ i ] = Arrow( rot2[ 3 ], o + 0.1 * rejcap, buff = 0 )
        self.play( Write( bi[ i ] ) )

        uhatwedgev = l.wedge( hatu, vecv )
        bil = MathTex( concat( 'i = ', l.frac( uhatwedgev, l.norm( uhatwedgev ) ) ) )
        bil.next_to( bi[ 1 ], RIGHT )
        bi2l = MathTex( uhatwedgev )
        bi2l.next_to( bi2[ 1 ], RIGHT )
        self.add( bil )
        self.wait( )

        x1 = q1.copy( )
        self.add( x1 )
        x1p = Arrow( o, o + rejcap, buff = 0, color = RED )
        x1pl = MathTex( concat( hatu, 'i' ) )
        x1pl.next_to( x1p, LEFT )
        x1pl.set_color( RED )
        xg = VGroup( x1p, x1pl )
        self.play( ReplacementTransform( x1, xg ) )
        self.wait( 2 )

        x1pp = Arrow( o, o + rej, buff = 0, color = PURPLE )
        x1ppl = MathTex( concat( hatu, l.lr( l.wedge( hatu, vecv ) ) ) )
        x1ppl.next_to( x1pp, LEFT )
        x1ppl.set_color( PURPLE )
        x1 = VGroup( bi[ 1 ], bi[ 2 ], bi[ 3 ], bil, x1p, x1pl )
        xg2 = VGroup( bi2[ 1 ], bi2[ 2 ], bi2[ 3 ], bi2l, x1pp, x1ppl )
        self.play( ReplacementTransform( x1, xg2 ) )
        self.wait( 2 )


class ProjRejPerp( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex( concat( '&', l.dot( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) ), l.newline ),
                      concat( r'\quad&=', l.gpgradezero( rej, proj ), l.newline ),
                      concat( r'\quad &=', l.gpgradezero( vwedgeu, invu, invu ), lr_vdotu, l.newline ),
                      concat( r'\quad &=', l.gpgradezero( vwedgeu ), l.inv( l.sq( vecu ) ), lr_vdotu, l.newline ),
                      concat( r'\quad &= 0', l.newline ),
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector( Scene ):
    def construct( self ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex(
                concat( l.Rej( vecu, vecv ), r' &\equiv ', lr_vwedgeu, invu, l.newline ),
                concat( r'&= ', l.add( l.dot( lr_vwedgeu, invu ), l.wedge( lr_vwedgeu, invu ) ), l.newline ),
                concat( r'&= ', l.add( l.dot( lr_vwedgeu, invu ), l.wedge( vecv, l.cancel( l.wedge( vecu, invu ) ) ) ), l.newline ),
                concat( r'&= ', l.dot( lr_vwedgeu, invu ), l.newline ),
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector2( Scene ):
    def construct( self ):

        eq = MathTex( concat( l.Rej( vecu, vecv ), r' &= ', l.dot( lr_vwedgeu, invu ), l.newline ),
                concat( r'&= ', vecv, l.sub( l.lr( l.dot( vecu, invu ) ), l.mult( vecu, l.lr( l.dot( vecv, invu ) ) ) ), l.newline ),
                concat( r'&= ', vecv, l.neg( vecu, l.lr( l.dot( vecv, invu ) ) ), l.newline ),
                concat( r'&= ', vecv, l.neg( hatu, l.lr( l.dot( vecv, hatu ) ) ), l.newline ) )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )


class ParallelogramComputationGA( Scene ):
    def construct( self ):
        DrawVectorsAndProjRej( self, 1 )

        vdotusq    = l.lrsq( vdotu )
        rej        = l.mult( lr_vwedgeu, invu )
        rrej       = l.mult( invu, lr_uwedgev )
        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ' ), concat( uu, l.lrsq( rej ), l.newline ), # 1, 2
                      concat( '&= ' ), concat( uu, rej, rrej, l.newline ), # 3, 4
                      concat( '&= ' ), concat( rej, uu, rrej, l.newline ), # 5, 6
                      concat( '&= ' ), concat( lr_vwedgeu, lr_uwedgev, l.newline ), # 7, 8
                      concat( '&= ', l.neg( l.lrsq( vwedgeu ) ), l.newline ),
                    )

        eq.shift( 2 * RIGHT )

        for i in range( 3 ):
            self.play( Write( eq[ i ] ) )

        eq[ 4 ].shift( 1.35 * UP )
        self.play( ReplacementTransform( eq[ 2 ], eq[ 4 ] ) )
        self.wait( )

        eq[ 6 ].shift( 2.5 * UP )
        self.play( ReplacementTransform( eq[ 4 ], eq[ 6 ] ) )
        self.wait( )

        eq[ 8 ].shift( 3.5 * UP )
        self.play( ReplacementTransform( eq[ 6 ], eq[ 8 ] ) )
        self.wait( )

        i = 9
        eq[ i ].shift( 3.5 * UP )
        self.play( Write( eq[ i ] ) )
        self.wait( )

        eq2 = MathTex(
                concat( l.lrsq( vwedgeu ), '&=', l.dot( lr_vwedgeu, lr_vwedgeu ), l.newline ),
                concat( '&=', l.dot( vecv, l.lr( l.dot( vecu, lr_vwedgeu ) ) ), l.newline ),
                concat( '&=', l.dot( vecv, l.lr( l.sub(
                    l.mult( lr_udotv, vecu ),
                    l.mult( uu, vecv )
                    ) ) ), l.newline ),
                concat( '&=', l.sub( vdotusq, l.mult( uu, vv ) ), l.newline ) )
        eq2.shift( 1.5 * DOWN + 2 * RIGHT )

        for item in eq2:
            self.play( Write( item ) )

        self.wait( )



class WedgeToDet( Scene ):
    def construct( self ):
        eq = MathTex( concat( r'\text{Let}\,', vecu, '= \sum_{i = 1}^N u_i \mathbf{e}_i, \quad ', vecv, '= \sum_{i = 1}^N v_i \mathbf{e}_i' ) )

        eq2 = MathTex( concat( uwedgev, r'= '),
                       l.wedge( l.lr( r'\sum_{i = 1}^N u_i \mathbf{e}_i' ), l.lr( r'\sum_{j = 1}^N v_i \mathbf{e}_j' ) ) )
        eq2.shift( 2 * LEFT )

        eq3 = MathTex(
                concat( r' \sum_{ij = 1}^N u_i v_j', l.lr( r'\mathbf{e}_i \wedge \mathbf{e}_j' ) ),
                concat( r' \sum_{i \ne j} u_i v_j', l.lr( r'\mathbf{e}_i \wedge \mathbf{e}_j' ) ),
                concat( r' \sum_{i \ne j} u_i v_j', r'\mathbf{e}_i \mathbf{e}_j' ),
                concat( l.lr( l.add( r' \sum_{i < j}', r' \sum_{i > j}' ) ), r' u_i v_j', r'\mathbf{e}_i \mathbf{e}_j' ),
                concat( l.add( l.mult( r' \sum_{i < j} u_i v_j', r'\mathbf{e}_i \mathbf{e}_j' ),
                               l.mult( r' \sum_{j > i} u_j u_i', r'\mathbf{e}_j \mathbf{e}_i' ) ) ),
                concat( r' \sum_{i < j} ( u_i v_j - u_j v_i)', r'\mathbf{e}_i \mathbf{e}_j' ),
                concat( r' \sum_{i < j}', detuivj, r'\mathbf{e}_i \mathbf{e}_j' ) )
        shifts = [ LEFT,
                   0.2 * DOWN,
                   0.5 * LEFT,
                   0.2 * UP + 1.0 * RIGHT,
                   0.2 * DOWN + 0.5 * RIGHT,
                   0.5 * LEFT,
                   0.5 * LEFT + 0.15 * UP ]

        eq4 = MathTex( concat( l.neg( l.lrsq( uwedgev ) ), r'= ', r' \sum_{i < j} {', detuivj, ' }^2' ) )

        for item in eq:
            self.play( Write( item ) )
        self.wait( )
        self.play( FadeOut( eq ) )

        for item in eq2:
            self.play( Write( item ) )
        self.wait( )

        last = eq2[ 1 ]
        i = 0
        for item in eq3:
            item.move_to( last )
            item.shift( shifts[ i ] )
            self.play( ReplacementTransform( last, item ) )
            self.wait( )
            last = item
            i = i + 1

        self.wait( )

        g = VGroup( eq2[ 0 ], last )
        gc = g.copy( )
        gc.shift( 1 * UP + 3 * RIGHT )

        self.play( ReplacementTransform( g, gc ) )
        self.wait( 2 )

        eq4.move_to( gc )
        eq4.shift( 2 * DOWN )
        self.play( Write( eq4 ) )
        self.wait( )


class WedgeR3( Scene ):
    def construct( self ):
        t = MathTex( r'\mathbb{R}^3' ).scale( 2 )
        t.shift( 2 * UP )
        t.set_color( RED )
        self.add( t )

        eqa = MathTex( concat( uwedgev, r'= \sum_{i < j} ', detuivj, r' \mathbf{e}_i \mathbf{e}_j' ) )
        for item in eqa:
            self.play( Write( item ) )

        t12 = MathTex( r'i, j = 1, 2:\quad',
                       concat( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ), r' \mathbf{e}_1 \mathbf{e}_2' ),
                       concat( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ), r' \mathbf{e}_1 \mathbf{e}_2 ( \mathbf{e}_3 \mathbf{e}_3 )' ),
                       concat( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ), r' ( \mathbf{e}_1 \mathbf{e}_2 \mathbf{e}_3 ) \mathbf{e}_3' ),
                       concat( 'I ', l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ), vec_e3 ) )
        playAndFadeOut( self, t12, eqa )

        t13 = MathTex( r'i, j = 1, 3:\quad',
                       concat( l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), vec_e1, vec_e3 ),
                       concat( l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), vec_e1, l.lr( vec_e2, vec_e2 ), vec_e3 ),
                       concat( l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), vec_e1, vec_e2, l.lr( l.neg( l.mult( vec_e3, vec_e2 ) ) ) ),
                       concat( '-', l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), l.lr( vec_e1, vec_e2, vec_e3 ), vec_e2 ),
                       concat( '-I ', l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), vec_e2 ) )
        playAndFadeOut( self, t13, eqa )

        t23 = MathTex( r'i, j = 2, 3:\quad',
                       concat( l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ), vec_e2, vec_e3 ),
                       concat( l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ), l.lr( vec_e1, vec_e1 ), vec_e2, vec_e3 ),
                       concat( l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ), vec_e1, l.lr( vec_e1, vec_e2, vec_e3 ) ),
                       concat( 'I ', l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ), vec_e1 ) )
        playAndFadeOut( self, t23, eqa )

        eqb = MathTex( concat( uwedgev, r'= I ', l.lr(
                       concat( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ), vec_e3 ),
                       concat( '- ', l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ), vec_e2 ),
                       concat( '+ ', l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ), vec_e1 ) ) ) )

        eqc = MathTex( concat( uwedgev, r'= I ',
                       r'\begin{vmatrix}',
                       r'\mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\',
                       r'u_1 & u_2 & u_3 \\',
                       r'v_1 & v_2 & v_3',
                       r'\end{vmatrix}' ) )

        eqd = MathTex( concat( uwedgev, r'= I ', l.lr( l.cross( vecu, vecv ) ) ) )

        self.play( ReplacementTransform( eqa, eqb ) )
        self.wait( )
        self.play( ReplacementTransform( eqb, eqc ) )
        self.wait( )
        self.play( ReplacementTransform( eqc, eqd ) )
        self.wait( )

        o = np.array( [ 0, -2, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] )
        p2 = np.array( [ 1, 3, 0 ] )
        p1 = 0.6 * p1
        p2 = 0.6 * p2
        op1 = o + p1
        op2 = o + p2
        op3 = op1 + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
        v1p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW )
        v2p = Arrow( start = op2, end = op3, buff = 0, color = RED )

        v1l = MathTex( vecu )
        v2l = MathTex( vecv )
        v1l.next_to( v1, RIGHT )
        v2l.next_to( v2, UP )
        v1l.set_color( RED )
        v2l.set_color( YELLOW )

        g = VGroup( v1, v2, v1p, v2p, v1l, v2l )
        g.move_to( -4 * RIGHT - 1.5 * UP )

        self.play( Write( g ) )

        eqe = MathTex( concat( r'{\text{Area} }^2 = ', l.neg( l.lrsq( uwedgev ) ), ' = ', l.norm2( l.cross( vecu, vecv ) ) ) )
        eqe.move_to( g )
        eqe.shift( 5 * RIGHT )
        self.play( Write( eqe ) )
        self.wait( )


class WedgeChangeOfBasisPartI( ThreeDScene ):
    def construct( self ):
        axes = ThreeDAxes()
        self.set_camera_orientation( phi = 70 * DEGREES, theta = 90 * DEGREES )

        o = ORIGIN
        s = 2
        p1 = np.array( [ 1, 1, 0 ] )
        p2 = np.array( [ 0, 1, 1 ] )
        e1 = np.array( [ 1, 0, 0 ] )
        e2 = np.array( [ 0, 1, 0 ] )
        e3 = np.array( [ 0, 0, 1 ] )
        ve1 = Arrow( start = o, end = e1, buff = 0, color = RED )
        ve2 = Arrow( start = o, end = e2, buff = 0, color = GREEN )
        ve3 = Arrow( start = o, end = e3, buff = 0, color = BLUE )
        e1t = MathTex( vec_e1 )
        e1t.move_to( e1 )
        e2t = MathTex( vec_e2 )
        e2t.move_to( e2 )
        e3t = MathTex( vec_e3 )
        e3t.move_to( e3 )
        bases = VGroup( ve1, ve2, ve3, e1t, e2t, e3t )
        ul = MathTex( vecu )
        ul.move_to( s * p1 )
        vl = MathTex( vecv )
        vl.move_to( o + s* (p1 + p2) )

        sq1 = [ o, o + s * p1, o + s *( p1 + p2), o + s * p2 ]
        s1 = OrientedPolygon( *sq1, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )

        p = -np.arccos( math.sqrt( 2/5 ) )
        g = bases + s1 + VGroup( axes )
        self.add( g )
        self.begin_ambient_camera_rotation( rate = 1.0 )
        self.wait( 4 )
        self.stop_ambient_camera_rotation( )
        self.wait( 1 )
        self.play( FadeOut( g ) )


class WedgeChangeOfBasisPartII( Scene ):
    def construct( self ):
        o = 2 * UP + 6 * LEFT
        alpha = math.sqrt(2)
        beta = 1/math.sqrt(2)
        gamma = math.sqrt(6)/2
        a1 = np.array( [ alpha, 0, 0 ] )
        a2 = np.array( [ beta, gamma, 0 ] )
        vf1 = np.array( [ 1, 0, 0 ] )
        vf2 = np.array( [ 0, 1, 0 ] )
        pts = [ o, o + a1, o + a1 + a2, o + a2 ]
        #self.play( FadeIn( p ) )
        self.wait( )

        x1 = Arrow( pts[ 0 ], pts[ 1 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x1.set_color( RED )
        x2 = Arrow( pts[ 1 ], pts[ 2 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x2.set_color( GREEN )
        x3 = Arrow( pts[ 2 ], pts[ 3 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x3.set_color( PURPLE )
        x4 = Arrow( pts[ 3 ], pts[ 0 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x4.set_color( PURPLE )
        poly = Polygon( *pts, color = PURPLE, fill_opacity = 0.5 )

        eq = MathTex( vecu, ' &= ', l.add( vec_e1, vec_e2 ), l.newline,
                      vecv, ' &= ', l.add( vec_e2, vec_e3 ), l.newline )

        ul = MathTex( vecu )
        ul.move_to( o + 1.2 * a1 )
        ul.set_color( RED )
        vl = MathTex( vecv )
        vl.set_color( GREEN )
        vl.move_to( o + 1.1 * (a1 + a2) )
        eg1 = VGroup( ul, x1 )
        eg2 = VGroup( vl, x2 )
        for i in range( 4 ):
            eg1 += eq[i]
            eq[i].set_color( RED )
        for i in range( 4, 8 ):
            eg2 += eq[i]
            eq[i].set_color( GREEN )
        eg3 = VGroup( poly, x3, x4 )

        eq.shift( 5 * LEFT + 0.5 * DOWN )
        self.play( AnimationGroup( Write( eg1 ) ) )
        self.play( AnimationGroup( Write( eg2 ) ) )
        self.play( Write( poly ) )
        self.play( AnimationGroup( Write( VGroup( x1, x2, x3, x4 ) ) ) )

        uv = l.wedge( vecu, vecv )
        f2e = l.dot( hatu, l.frac( uwedgev, l.norm( uwedgev ) ) )
        #              0               1   2       3     4      5                                       6
        eq2 = MathTex( l.text('Let '), vec_f1, ' &= ', hatu, ' = ', l.frac( l.add( vec_e1, vec_e2 ), r'\sqrt{2}' ), l.newline,
                       l.text('Let '), vec_f2, ' &= ', f2e,  ' = ', concat( l.frac('1', r'\sqrt{6}'), l.lr( l.sub( l.add( vec_e1, l.mult( '2', vec_e2 ) ), vec_e1 ) ) ), l.newline )
        #              7               8   9       10    11     12                                      13
        eq2.shift( 2.0 * UP + 2.0 * RIGHT )
        eq2[1].set_color( BLUE )
        eq2[2].set_color( BLUE )
        eq2[3].set_color( BLUE )
        eq2[8].set_color( YELLOW )
        eq2[9].set_color( YELLOW )
        eq2[10].set_color( YELLOW )
        f1g = VGroup( Arrow( start = o, end = o + vf1, buff = 0, color = BLUE ), MathTex( vec_f1 ).set_color( BLUE ).move_to( o + vf1 + 0.3 * DOWN ) )
        f2g = VGroup( Arrow( start = o, end = o + vf2, buff = 0, color = YELLOW ), MathTex( vec_f2 ).set_color( YELLOW ).move_to( o + vf2 + 0.3 * LEFT ) )
        self.play( Write( eq2[0:6] ), Write( f1g ) )
        self.wait( )
        self.play( Write( eq2[7:13] ), Write( f2g ) )
        self.wait( )

        eqp = MathTex( concat( vecu, ' &= ', l.mult( r'\sqrt{2}', vec_f1 ), l.newline ),
                       concat( vecv, ' &= ', l.add( l.mult( r'\frac{\sqrt{2}}{2}', vec_f1 ),
                                                 l.mult( r'\frac{\sqrt{6}}{2}', vec_f2 ) ), l.newline ) )
        eqp[0].set_color( RED )
        eqp[1].set_color( GREEN )
        eqp.move_to( eq )
        eqp.shift( 2 * DOWN + 0.5 * RIGHT )
        self.play( Write( eqp ) )
        self.wait( )

        eq3 = MathTex( concat( uwedgev, ' &= ', l.add( vec_e12, vec_e13, vec_e23 ), l.newline ),
                       concat( l.lrsq( uwedgev ), ' &= - 3', l.newline ),
                       concat( uwedgev, r' &= \sqrt{\frac{2 \times 6}{4}}', vec_f1, vec_f2, l.newline ),
                       concat( l.lrsq( uwedgev ), ' &= - 3', l.newline ) )
        eq3.shift( 1.5 * DOWN + 2 * RIGHT )
        for i in eq3:
            self.play( Write( i ) )
            self.wait( )
        self.wait( 2 )

        self.play( FadeOut( VGroup( eq3, eqp, eq, eq2 ) ) )
        t = Text( 'General wedge diagonalization' )
        b1 = l.dot( vecv, vec_f1 )
        b2 = l.frac( l.norm( uwedgev ), normu )
        eq = MathTex( concat( l.setlr( vec_f1, vec_f2 ), ' &= ', l.setlr( hatu, f2e ), l.newline ),
                      concat( vecu, ' &= ', normu, vec_f1, l.newline ),
                      concat( vecv, ' &= ', l.add( l.mult( l.lr( l.dot( vecv, vec_f1 ) ), vec_f1 ), l.mult( l.frac( l.norm( uwedgev ), normu ), vec_f2 ) ), l.newline ),
                      concat( uwedgev, r'&='),
                      concat( r'\sum_{i < j} ', l.det22( 'u_i', 'v_i', 'u_j', 'v_j' ), r'\mathbf{e}_i \mathbf{e}_j', l.newline ),
                          r'&= ', concat( l.det22( normu, '0', b1, b2 ), vec_f1, vec_f2, l.newline ),
                          r'&= ', concat( l.norm( uwedgev ), vec_f1, vec_f2, l.newline ) )
        t.move_to( 3 * UP + 1 * RIGHT )
        t.set_color( BLUE )
        self.play( Write( t ) )
        eq.shift( 1.25 * DOWN )
        for i in range( 5 ):
            self.play( Write( eq[i] ) )
        self.wait( 2 )
        eq[6].shift( 1.5 * UP )
        self.play( ReplacementTransform( eq[4], eq[6] ) )
        self.wait( 2 )
        eq[8].shift( 3 * UP )
        self.play( ReplacementTransform( eq[6], eq[8] ) )
        self.wait( )


class BivectorAddition( Scene ):
    def construct( self ):
        number_plane = NumberPlane(
            x_range = [ -10, 10, 1 ],
            y_range = [ -10, 10, 1 ],

            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )

        o = np.array( [ 0, 0, 0 ] )
        p1 = [ np.array( [ 1, 1/3, 0 ] ), np.array( [ -1/4, 1, 0 ] ), np.array( [ -1, -1/2, 0 ] ),  np.array( [ 1/4, -1, 0 ] ) ]
        p2 = [ np.array( [ 1/3, 1, 0 ] ), np.array( [ -0.8, 1/3, 0 ] ), np.array( [ -1/2, -1.25, 0 ] ), np.array( [ 1, -2/7, 0 ] ) ]

        self.add( number_plane )
        v1 = MathTex( vec_v1 )
        v2 = MathTex( vec_v2 )
        e1 = MathTex( vec_e1 )
        e2 = MathTex( vec_e2 )
        p = MathTex( vec_v1, r' \wedge ', vec_v2, ' = 4', vec_e1, vec_e2 )
        p[ 0 ].set_color( RED )
        p[ 2 ].set_color( BLUE )

        dir1 = ( RIGHT, UP, LEFT, DOWN )
        dir2 = ( RIGHT + 0.5 * UP, LEFT, LEFT + 0.25 * DOWN, DOWN + 0.25 * RIGHT )
        shift = 4
        pos = ( shift * LEFT, shift * RIGHT, shift * RIGHT, shift * LEFT )

        for i in range( 4 ):
            ppoints = unitParallelogram( o, p1[ i ], p2[ i ], 2 )
            pg = OrientedPolygon( *ppoints, c0 = PURPLE, c1 = RED, c2 = BLUE, f = 0.5, d1 = dir1[ i ], d2 = dir2[ i ], tex = 1, r = 0.1 )

            p.move_to( pg )
            p.shift( pos[ i ] )
            totx = VGroup( pg, p )
            if i == 0:
                self.play( Write( totx ) )
                self.wait( )
            else:
                self.play( ReplacementTransform( fromtx, totx ) )
                self.wait( )

            fromtx = totx

        i = 3
        add1 = OrientedPolygon( *ppoints, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )
        self.play( ReplacementTransform( fromtx, add1 ) )
        p1 = MathTex( vec_v1, r' \wedge ', vec_v2, ' = 4', vec_e1, vec_e2 )
        p1.move_to( add1 )
        p1.shift( 4 * LEFT )
        self.play( ReplacementTransform( p, p1 ) )
        self.wait( )

        add2 = add1.copy( );
        add2.shift( 2 * UP )
        self.play( FadeOut( p1 ) )
        self.play( Write( add2 ) )
        p2 = MathTex( r'2 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 8', vec_e1, vec_e2 )
        p2.move_to( VGroup( add1, add2 ) )
        p2.shift( 4 * LEFT + 2 * UP )
        self.play( Write( p2 ) )
        self.wait( )

        add3 = add1.copy( );
        add3.shift( 2 * LEFT + 0.55 * UP )
        self.play( FadeOut( p2 ) )
        self.play( Write( add3 ) )
        p3 = MathTex( '3 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 12 ', vec_e1, vec_e2 )
        p3.move_to( add2 )
        p3.shift( 4 * LEFT + 1 * UP )
        self.play( Write( p3 ) )
        self.wait( )

        add4 = add3.copy( );
        add4.shift( 2 * UP )
        self.play( FadeOut( p3 ) )
        self.play( Write( add4 ) )
        p4 = MathTex( '4 ', l.lr( vec_v1, r' \wedge ', vec_v2 ), ' = 16 ', vec_e1, vec_e2 )
        p4.move_to( VGroup( add2, add4 ) )
        p4.shift( 1.8 * UP + 3 * RIGHT )
        self.play( Write( p4 ) )
        self.wait( )

        o2 = np.array( [ -2, -2, 0 ] )
        p1s = np.array( [ 1, 0, 0 ] )
        p2s = np.array( [ 0, 1, 0 ] )
        sqpts = unitParallelogram( o2, p1s, p2s, 4 )
        sq = OrientedPolygon( *sqpts, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )
        p5 = MathTex( '16 ', vec_e1, vec_e2 ).scale( 2 )
        p5.move_to( sq )
        p5.shift( 2 * UP + 4 * RIGHT )
        g = VGroup( sq, p5 )
        self.play( ReplacementTransform( VGroup( add1, add2, add3, add4, p4 ), g ) )

        pentwidth = np.sqrt( 2/( 5 * math.sin( 2 * math.pi / 5 ) ) )
        pentagon = OrientedRegularPolygon( 5, pentwidth, PURPLE, 0.5 )
        pentagon.scale( 4 )
        pentagon.shift( 2 * LEFT * pentwidth )
        self.play( ReplacementTransform( sq, pentagon ) )
        self.wait( )

        hexwidth = np.sqrt( 2 * np.sqrt( 3 ) ) * 2/3
        hexagon = OrientedRegularPolygon( 6, hexwidth, PURPLE, 0.5 )
        hexagon.scale( 2 )
        hexagon.shift( 2 * LEFT * hexwidth )
        self.play( ReplacementTransform( pentagon, hexagon ) )
        self.wait( )

        r = 1/np.sqrt( math.pi )
        circle = Ellipse( width = 2*r, height = 2*r, color = PURPLE, fill_opacity = 0.5 )
        circle.scale( 4 )
        ac = CurvedArrow( [ 2 * r, 0, 0 ], [ 0, 2 * r, 0 ] )
        ac.move_to( circle )
        ac.set_color( PURPLE )
        self.play( ReplacementTransform( hexagon, circle ) )
        self.add( ac )
        self.wait( )

        a = 1.3/np.sqrt( math.pi )
        b = 1/( math.pi * a )
        ellipse = Ellipse( width = 2*a, height = 2*b, color = PURPLE, fill_opacity = 0.5 )
        ellipse.scale( 4 )
        self.play( ReplacementTransform( circle, ellipse ) )
        self.wait( )



class ScalarMultiplicationSign( Scene ):
    def construct( self ):
        number_line = NumberLine(
            x_range = [-7, 7, 1],
            length = 14,
            color = TEAL,
            include_numbers = True,
            label_direction = UP,
            stroke_width = 4,
            stroke_opacity = 0.4,
        )

        #title = Text( 'Geometry of scalar multiplication signs.' )
        #self.play( Write( title ) )
        #self.wait( )
        #self.play( FadeOut( title ) )

        number_plane = NumberPlane(
            x_range = [ -10, 10, 1 ],
            y_range = [ -10, 10, 1 ],

            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )

        plus = MathTex( '+' )
        minus = MathTex( '-' )

        self.play( Write( number_plane ) )
        self.wait( )
        t = write_area_products( self, 2, 3, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        t = write_area_products( self, 3, 2, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        x = 1
        y = 1
        t = write_area_products( self, x, y, 0.2, ORIGIN )
        g = t[0] + t[1]

        o = np.array( 1 * (RIGHT + UP) )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        rect1 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = x, s2 = y, r = 0.2 )
        plus.move_to( 1.5 * (RIGHT + UP) )
        g1 = rect1 + plus
        self.play( ReplacementTransform( g, g1 ) )
        self.wait( )


        t = write_area_products( self, -2, 3, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        t = write_area_products( self, -3, 2, 0.1, ORIGIN )
        g = t[0] + t[1]
        self.play( FadeOut( g ) )
        x = -1
        t = write_area_products( self, x, y, 0.2, ORIGIN )
        g = t[0] + t[1]

        o = np.array( 1 * (LEFT + UP) )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        rect2 = OrientedPolygon2( *pts, c0 = GREEN_B, c1 = RED, c2 = BLUE, f = 0.5, s1 = x, s2 = y, r = 0.2 )
        minus.move_to( 1.5 * (LEFT + UP) )
        g2 = rect2 + minus
        self.play( ReplacementTransform( g, g2 ) )
        self.wait( )

        o = np.array( 1 * (LEFT + DOWN) )
        y = -1
        t = write_area_products( self, x, y, 0.2, o )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        plus2 = plus.copy( )
        plus2.move_to( 1.5 * (LEFT + DOWN) )
        self.play( FadeOut( t[1] ), Write( plus2 ) )
        self.wait( )

        o = np.array( 1 * (RIGHT + DOWN) )
        x = 1
        t = write_area_products( self, x, y, 0.2, o )
        v1 = np.array( [ x, 0, 0 ] )
        v2 = np.array( [ 0, y, 0 ] )
        pts = [ o, o + v1, o + v1 + v2, o + v2 ]
        minus2 = minus.copy( )
        minus2.move_to( 1.5 * (RIGHT + DOWN) )
        self.play( FadeOut( t[1] ), Write( minus2 ) )
        self.wait( )


class Finale( Scene ):
    def construct( self ):
        t = Text( 'Special thanks to' )
        t.move_to( 2.5 * UP + 4 * LEFT )
        t2 = Text( 'sudgylacmoe' )
        t2.next_to( t, DOWN )
        t3 = Text( '(who generously hand held me through my first manim baby steps.)' ).scale( 0.6 )
        t3.next_to( t2, DOWN )
        t3.shift( 3 * RIGHT )
        g = VGroup( t, t2, t3 )
        t.set_color( TEAL )
        self.add( g )

        # This is from sudgy.  I had to tweak the alignment since I don't appear to have ManimBanner2() available.
        #banner = ManimBanner2()
        banner = ManimBanner()
        banner.scale(0.3)
        banner.to_edge(DOWN)
        banner.shift(2 * RIGHT + 0.5 * UP)
        self.play(FadeIn(banner))
        made_with = Tex("Made with ")
        made_with.scale(1.5)
        made_with.next_to(banner, 4 * LEFT, buff = 0.3)
        made_with.align_to(banner.M, DOWN)
        url = Tex("\\verb|https://manim.community|")
        url.next_to(VGroup(made_with, banner), DOWN, buff = -0.2)
        url.shift(0.3*RIGHT + 0.25 * DOWN)
        self.play(AnimationGroup(
            AnimationGroup(banner.expand(), Write(made_with)),
            FadeIn(url),
            lag_ratio = 0.5
        ))


class test( Scene ):
    def construct( self ):
        print( 'hi' )


def foo():
    if 0:
        #self.play( Write( number_line ) )
        return 0


# vim: et sw=4 ts=4
