from manim import *
import numpy as np
import math
from sys import *
sys.path.append( r'../bin' )
from mylatex import *
import enum # IntFlag

def DrawVectorsAndProjRej( self, prlabels ):
    l = latex( )
    u          = l.vec( 'u' )
    invu       = l.inv( u )
    v          = l.vec( 'v' )

    o = np.array( [ 0, -2, 0 ] )
    p1 = np.array( [ 3, 1, 0 ] )
    p2 = np.array( [ 1, 3, 0 ] )
    op1 = o + p1
    op2 = o + p2

    p1cap = p1/ np.linalg.norm( p1 )
    proj = np.dot( p2, p1cap ) * p1cap
    oproj = o + proj

    vproj = Line( start = o, end = oproj, color = PURPLE )
    if prlabels:
        vprojl = MathTex( concat( l.lr( l.dot( v, u ) ), invu ) )
    else:
        vprojl = Text( 'Proj' )
    vprojl.set_color( PURPLE )
    vprojl.next_to( vproj, DOWN )

    rej = p2 - proj
    vrej = Line( start = oproj, end = op2, color = GREEN )
    if prlabels:
        vrejl = MathTex( concat( l.lr( l.wedge( v, u ) ), invu ) )
    else:
        vrejl = Text( 'Rej' )
    vrejl.set_color( GREEN )
    vrejl.next_to( vrej, 0.2 * RIGHT )

    v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
    v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
    v1l = MathTex( u )
    v1l.set_color( RED )
    v1l.next_to( v1, RIGHT )
    v2l = MathTex( v )
    v2l.set_color( YELLOW )
    v2l.next_to( v2, UP )

    all = VGroup( v1, v1l, v2, v2l, vproj, vrej, vprojl, vrejl )

    move = ( -6.5, 2, 0 )
    all.shift( move )

    self.add( all )

    return ( vprojl, vrejl )


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
    l = latex( )

    poly = Polygon( *vertices, color = c0, fill_opacity = f )

    e1 = concat( l.vec( 'e' ), '_1' )
    e2 = concat( l.vec( 'e' ), '_2' )
    s1str = vecstr( l, s1, e1, vsflags.default )
    s2str = vecstr( l, s2, e2, vsflags.default )

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

    l = latex( )
    e1 = concat( l.vec( 'e' ), '_1' )
    e2 = concat( l.vec( 'e' ), '_2' )
    n1vec = vecstr( l, n1, e1, vsflags.braces )
    n2vec = vecstr( l, n2, e2, vsflags.braces )
    prodvec = vecstr( l, n1 * n2, l.mult( e1, e2 ), vsflags.signed )
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
        l = latex( )
        u          = l.vec( 'u' )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )

        o = np.array( [ 0, -2, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] )
        p2 = np.array( [ 1, 3, 0 ] )
        op1 = o + p1
        op2 = o + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )

        v1l = MathTex( u )
        v2l = MathTex( v )
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

        op3 = op1 + p2
        v1p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW )
        v2p = Arrow( start = op2, end = op3, buff = 0, color = RED )
        #parallelogram = [ o, op1, op3, op2 ]
        #poly = Polygon( *parallelogram )

        cut = op1 + rej
        recttop = cut - p1
        dashrej = DashedLine( start = op1, end = cut, color = BLUE )
        dashtop = DashedLine( start = cut, end = recttop )
        dashside = DashedLine( start = recttop, end = o, color = BLUE )

        self.play( Create( v1g ) )
        self.play( Create( v2g ) )
        v1c = v1.copy( )
        v2c = v2.copy( )
        self.add( v1c )
        self.add( v2c )
        self.play( ReplacementTransform( v1c, v1p ) )
        self.play( ReplacementTransform( v2c, v2p ) )
        #self.play( Create( poly ) )
        #self.play( Create( vprojg ) )
        #self.play( Create( vrejg ) )
        self.play( Create( dashrej ) )
        self.play( Create( dashtop ) )
        self.play( Create( dashside ) )
        #self.play( FadeOut( vprojg, vrejg ) )

        move = ( -6, 1, 0 )
        a = VGroup( dashrej, dashtop, dashside, v1, v1l, v2, v2l, v1p, v2p ) # , poly
        self.play( a.animate.shift( move ) )
        self.wait( 1 )

        squ        = l.norm2( u )
        sqv        = l.norm2( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        rej        = l.sub( v, l.mult( l.lr( l.dot( v, uhat ) ), uhat ) )

        eq2 = MathTex( l.text( 'base' ), r'& = \Vert', u, concat( r'\Vert', l.newline ),
                       l.text( 'height' ), '& = ', concat( l.norm( rej ), l.newline ) )
        #eq2 = MathTex( concat( l.text( 'base' ), '& = ', l.norm( u ), l.newline ),
        #               concat( l.text( 'height' ), '& = ', l.norm( rej ), l.newline ) )
        eq2[0].set_color( RED )
        eq2[1].set_color( RED )
        eq2[2].set_color( RED )
        eq2[3].set_color( RED )
        eq2[4].set_color( GREEN )
        eq2[5].set_color( GREEN )
        eq2[6].set_color( GREEN )

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.newline ), # 1
                      concat( '&= ', squ ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2, 3
                      concat( '&= ', squ ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4, 5
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.newline ) # 6
                    )

        oproj = o + proj
        vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
        vproj.shift( move )
        vprojl = MathTex( concat( l.lr( l.dot( v, uhat ) ), uhat ) )
        vprojl.set_color( PURPLE )
        vprojl.next_to( vproj, DOWN )
        vprojl.shift( 0.2 * ( UP + RIGHT ) )

        vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
        vrej.shift( move )
        vrejl = MathTex( concat( v, ' - ', l.lr( l.dot( v, uhat ) ), uhat ) )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, RIGHT )
        vrejl.shift( 2.0 * UP + 1.5 * LEFT )
        vrejl.shift( ( -0.5, 0, 0 ) )

        self.play( Write( VGroup( vproj, vprojl ) ) )
        self.wait( )
        self.play( Write( VGroup( vrej, vrejl ) ) )
        self.wait( )
        eq.shift( 2.4 * RIGHT )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        #eq2[ 0 ].set_color( RED )
        ##eq2[ 2 ].set_color( RED )
        #eq2[ 4 ].set_color( BLUE )
        self.play( Write( eq[ 0 ] ),
                   Write( eq2[ 0 ] ),
                   Write( eq2[ 1 ] ),
                   Write( eq2[ 2 ] ),
                   Write( eq2[ 3 ] ),
                   Write( eq2[ 4 ] ),
                   Write( eq2[ 5 ] ),
                   Write( eq2[ 6 ] ) )

        for i in range( 1, 4 ):
            self.play( Write( eq[ i ] ) )
        self.wait( )
        eq[ 5 ].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[ 3 ], eq[ 5 ] ) )
        self.wait( 2 )

        i = 6
        eq[ i ].shift( UP )
        self.play( Write( eq[ i ] ) )
        self.wait( )


class ProjRej( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        v          = l.vec( 'v' )
        proj       = l.mult( l.lr( l.dot( v, u ) ), invu )
        rej        = l.mult( l.lr( l.wedge( v, u ) ), invu )

        labels = DrawVectorsAndProjRej( self, 0 )

        eq = MathTex( concat( v, r' &= ', v, r'\times 1', l.newline ),
                      concat( r' &= ', v, u, invu, l.newline ),
                      concat( r' &= ', l.lr( v, u ), invu, l.newline ),
                      concat( r' &= ', l.lr( l.add( l.dot( v, u ), l.wedge( v, u ) ) ), invu, l.newline ),
                      concat( r' &= ', l.add( proj, rej ), l.newline ) )

        eq.shift( 2 * RIGHT )
        for item in eq:
           self.play( Write( item ) )
        self.wait( )

        projl = MathTex( proj )
        projl.set_color( PURPLE )
        projl.move_to( labels[ 0 ] )
        rejl = MathTex( rej )
        rejl.set_color( GREEN )
        rejl.move_to( labels[ 1 ] )
        rejl.shift( 0.25 * RIGHT )
        oldlabels = VGroup( labels[ 0 ], labels[ 1 ] )
        newlabels = VGroup( projl, rejl )
        self.play( ReplacementTransform( oldlabels, newlabels ) )
        self.wait( )



class ProjRej2( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        proj       = l.mult( l.lr( l.dot( v, u ) ), invu )
        rej        = l.mult( l.lr( l.wedge( v, u ) ), invu )
        proj2      = l.mult( l.lr( l.dot( v, uhat ) ), uhat )
        rej2       = l.mult( l.lr( l.wedge( v, uhat ) ), uhat )

        eq = MathTex( concat( l.Proj( u, v ), ' &\equiv ', proj, l.newline ),
                      concat( l.Rej( u, v ),  ' &\equiv ', rej, l.newline ) )
        eq2 = MathTex( concat( l.Proj( u, v ), ' &\equiv ', proj, ' = ', proj2, l.newline ),
                       concat( l.Rej( u, v ),  ' &\equiv ', rej, ' = ', rej2, l.newline ) )

        for item in eq:
            self.play( Write( item ) )

        self.play( ReplacementTransform( eq, eq2 ) )

        self.wait( )



class RejRotate( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )

        o = np.array( [ -1, -1.5, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] )
        p2 = np.array( [ 1, 3, 0 ] )
        op1 = o + p1
        op2 = o + p2

        p1cap = p1/ np.linalg.norm( p1 )
        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
        v1l = MathTex( u )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v2l = MathTex( v )
        v2l.set_color( YELLOW )
        v2l.next_to( v2, UP )

        all = VGroup( v1, v1l, v2, v2l )

        q1 = Arrow( start = o, end = ( o + p1cap ), buff = 0, color = RED )
        q1l = MathTex( uhat )
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

        uhatwedgev = l.wedge( uhat, v )
        bil = MathTex( concat( 'i = ', l.frac( uhatwedgev, l.norm( uhatwedgev ) ) ) )
        bil.next_to( bi[ 1 ], RIGHT )
        bi2l = MathTex( uhatwedgev )
        bi2l.next_to( bi2[ 1 ], RIGHT )
        self.add( bil )
        self.wait( )

        x1 = q1.copy( )
        self.add( x1 )
        x1p = Arrow( o, o + rejcap, buff = 0, color = RED )
        x1pl = MathTex( concat( uhat, 'i' ) )
        x1pl.next_to( x1p, LEFT )
        x1pl.set_color( RED )
        xg = VGroup( x1p, x1pl )
        self.play( ReplacementTransform( x1, xg ) )
        self.wait( 2 )

        x1pp = Arrow( o, o + rej, buff = 0, color = PURPLE )
        x1ppl = MathTex( concat( uhat, l.lr( l.wedge( uhat, v ) ) ) )
        x1ppl.next_to( x1pp, LEFT )
        x1ppl.set_color( PURPLE )
        x1 = VGroup( bi[ 1 ], bi[ 2 ], bi[ 3 ], bil, x1p, x1pl )
        xg2 = VGroup( bi2[ 1 ], bi2[ 2 ], bi2[ 3 ], bi2l, x1pp, x1ppl )
        self.play( ReplacementTransform( x1, xg2 ) )
        self.wait( 2 )


class ProjRejPerp( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        v          = l.vec( 'v' )
        vdotu      = l.dot( v, u )
        vwedgeu    = l.wedge( v, u )
        proj       = l.mult( l.lr( vdotu ), invu )
        rej        = l.mult( l.lr( vwedgeu ), invu )
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex( concat( '&', l.dot( l.Rej( u, v ), l.Proj( u, v ) ), l.newline ),
                      concat( r'\quad&=', l.gpgradezero( rej, proj ), l.newline ),
                      concat( r'\quad &=', l.gpgradezero( vwedgeu, invu, invu ), l.lr( vdotu ), l.newline ),
                      concat( r'\quad &=', l.gpgradezero( vwedgeu ), l.inv( l.sq( u ) ), l.lr( vdotu ), l.newline ),
                      concat( r'\quad &= 0', l.newline ),
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex(
                concat( l.Rej( u, v ), r' &\equiv ', l.lr( l.wedge( v, u ) ), invu, l.newline ),
                concat( r'&= ', l.add( l.dot( l.lr( l.wedge( v, u ) ), invu ), l.wedge( l.lr( l.wedge( v, u ) ), invu ) ), l.newline ),
                concat( r'&= ', l.add( l.dot( l.lr( l.wedge( v, u ) ), invu ), l.wedge( v, l.cancel( l.wedge( u, invu ) ) ) ), l.newline ),
                concat( r'&= ', l.dot( l.lr( l.wedge( v, u ) ), invu ), l.newline ),
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector2( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )

        eq = MathTex( concat( l.Rej( u, v ), r' &= ', l.dot( l.lr( l.wedge( v, u ) ), invu ), l.newline ),
                concat( r'&= ', v, l.sub( l.lr( l.dot( u, invu ) ), l.mult( u, l.lr( l.dot( v, invu ) ) ) ), l.newline ),
                concat( r'&= ', v, l.neg( u, l.lr( l.dot( v, invu ) ) ), l.newline ),
                concat( r'&= ', v, l.neg( uhat, l.lr( l.dot( v, uhat ) ) ), l.newline ) )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )


class ParallelogramComputationGA( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        #uhat       = l.hat( 'u' )
        invu       = l.inv( u )
        v          = l.vec( 'v' )

        DrawVectorsAndProjRej( self, 1 )

        uu         = l.sq( u )
        vv         = l.sq( v )
        vdotusq    = l.lrsq( l.dot( v, u ) )
        vwedgeu    = l.wedge( v, u )
        uwedgev    = l.wedge( u, v )
        rej        = l.mult( l.lr( l.wedge( v, u ) ), invu )
        rrej       = l.mult( invu, l.lr( l.wedge( u, v ) ) )
        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ' ), concat( uu, l.lrsq( rej ), l.newline ), # 1, 2
                      concat( '&= ' ), concat( uu, rej, rrej, l.newline ), # 3, 4
                      concat( '&= ' ), concat( rej, uu, rrej, l.newline ), # 5, 6
                      concat( '&= ' ), concat( l.lr( vwedgeu ), l.lr( uwedgev ), l.newline ), # 7, 8
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
                concat( l.lrsq( vwedgeu ), '&=', l.dot( l.lr( vwedgeu ), l.lr( vwedgeu ) ), l.newline ),
                concat( '&=', l.dot( v, l.lr( l.dot( u, l.lr( vwedgeu ) ) ) ), l.newline ),
                concat( '&=', l.dot( v, l.lr( l.sub(
                    l.mult( l.lr( l.dot( u, v ) ), u ),
                    l.mult( uu, v )
                    ) ) ), l.newline ),
                concat( '&=', l.sub( vdotusq, l.mult( uu, vv ) ), l.newline ) )
        eq2.shift( 1.5 * DOWN + 2 * RIGHT )

        for item in eq2:
            self.play( Write( item ) )

        self.wait( )



class WedgeToDet( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )

        eq = MathTex( concat( r'\text{Let}\,', u, '= \sum_{i = 1}^N u_i \mathbf{e}_i, \quad ', v, '= \sum_{i = 1}^N v_i \mathbf{e}_i' ) )

        eq2 = MathTex( concat( l.wedge( u, v ), r'= '),
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
                concat( r' \sum_{i < j} \begin{vmatrix} u_i & v_i \\ u_j & v_j \end{vmatrix}', r'\mathbf{e}_i \mathbf{e}_j' ) )
        shifts = [ LEFT,
                   0.2 * DOWN,
                   0.5 * LEFT,
                   0.2 * UP + 1.0 * RIGHT,
                   0.2 * DOWN + 0.5 * RIGHT,
                   0.5 * LEFT,
                   0.5 * LEFT + 0.15 * UP ]

        eq4 = MathTex( concat( l.neg( l.lrsq( l.wedge( u, v ) ) ), r'= ', r' \sum_{i < j} {\begin{vmatrix} u_i & v_i \\ u_j & v_j \end{vmatrix} }^2' ) )

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
        l = latex( )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )

        t = MathTex( r'\mathbb{R}^3' ).scale( 2 )
        t.shift( 2 * UP )
        t.set_color( RED )
        self.add( t )

        eqa = MathTex( concat( l.wedge( u, v ), r'= \sum_{i < j} \begin{vmatrix} u_i & v_i \\ u_j & v_j \end{vmatrix} \mathbf{e}_i \mathbf{e}_j' ) )
        for item in eqa:
            self.play( Write( item ) )

        t12 = MathTex( r'i, j = 1, 2:\quad',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_2 & v_2 \end{vmatrix} \mathbf{e}_1 \mathbf{e}_2',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_2 & v_2 \end{vmatrix} \mathbf{e}_1 \mathbf{e}_2 ( \mathbf{e}_3 \mathbf{e}_3 )',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_2 & v_2 \end{vmatrix} ( \mathbf{e}_1 \mathbf{e}_2 \mathbf{e}_3 ) \mathbf{e}_3',
                       r'I \begin{vmatrix} u_1 & v_1 \\ u_2 & v_2 \end{vmatrix} \mathbf{e}_3' )
        playAndFadeOut( self, t12, eqa )

        t13 = MathTex( r'i, j = 1, 3:\quad',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1 \mathbf{e}_3',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1 ( \mathbf{e}_2 \mathbf{e}_2 ) \mathbf{e}_3',
                       r'\begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1 \mathbf{e}_2 ( -\mathbf{e}_3 \mathbf{e}_2 )',
                       r'-\begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} ( \mathbf{e}_1 \mathbf{e}_2 \mathbf{e}_3 ) \mathbf{e}_2',
                       r'- I \begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_2' )
        playAndFadeOut( self, t13, eqa )

        t23 = MathTex( r'i, j = 2, 3:\quad',
                       r'\begin{vmatrix} u_2 & v_2 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_2 \mathbf{e}_3',
                       r'\begin{vmatrix} u_2 & v_2 \\ u_3 & v_3 \end{vmatrix} ( \mathbf{e}_1 \mathbf{e}_1 ) \mathbf{e}_2 \mathbf{e}_3',
                       r'\begin{vmatrix} u_2 & v_2 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1 ( \mathbf{e}_1 \mathbf{e}_2 \mathbf{e}_3 )',
                       r'I \begin{vmatrix} u_2 & v_2 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1' )
        playAndFadeOut( self, t23, eqa )

        eqb = MathTex( concat( l.wedge( u, v ), r'= I ', l.lr(
                       r'\begin{vmatrix} u_1 & v_1 \\ u_2 & v_2 \end{vmatrix} \mathbf{e}_3',
                       r'- \begin{vmatrix} u_1 & v_1 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_2',
                       r'+ \begin{vmatrix} u_2 & v_2 \\ u_3 & v_3 \end{vmatrix} \mathbf{e}_1' ) ) )

        eqc = MathTex( concat( l.wedge( u, v ), r'= I ',
                       r'\begin{vmatrix}',
                       r'\mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\',
                       r'u_1 & u_2 & u_3 \\',
                       r'v_1 & v_2 & v_3',
                       r'\end{vmatrix}' ) )

        eqd = MathTex( concat( l.wedge( u, v ), r'= I ', l.lr( l.cross( u, v ) ) ) )

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

        v1l = MathTex( u )
        v2l = MathTex( v )
        v1l.next_to( v1, RIGHT )
        v2l.next_to( v2, UP )
        v1l.set_color( RED )
        v2l.set_color( YELLOW )

        g = VGroup( v1, v2, v1p, v2p, v1l, v2l )
        g.move_to( -4 * RIGHT - 1.5 * UP )

        self.play( Write( g ) )

        eqe = MathTex( concat( r'{\text{Area} }^2 = ', l.neg( l.lrsq( l.wedge( u, v ) ) ), ' = ', l.norm2( l.cross( u, v ) ) ) )
        eqe.move_to( g )
        eqe.shift( 5 * RIGHT )
        self.play( Write( eqe ) )
        self.wait( )


class WedgeChangeOfBasisPartI( ThreeDScene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )

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
        e1t = MathTex( concat( l.vec( 'e' ), '_1' ) )
        e1t.move_to( e1 )
        e2t = MathTex( concat( l.vec( 'e' ), '_2' ) )
        e2t.move_to( e2 )
        e3t = MathTex( concat( l.vec( 'e' ), '_3' ) )
        e3t.move_to( e3 )
        bases = VGroup( ve1, ve2, ve3, e1t, e2t, e3t )
        ul = MathTex( u )
        ul.move_to( s * p1 )
        vl = MathTex( v )
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


class WedgeChangeOfBasisPartII( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )

        o = 2 * UP + 6 * LEFT
        alpha = math.sqrt(2)
        beta = 1/math.sqrt(2)
        gamma = math.sqrt(6)/2
        a1 = np.array( [ alpha, 0, 0 ] )
        a2 = np.array( [ beta, gamma, 0 ] )
        vf1 = np.array( [ 1, 0, 0 ] )
        vf2 = np.array( [ 0, 1, 0 ] )
        pts = [ o, o + a1, o + a1 + a2, o + a2 ]
        p = OrientedPolygon( *pts, c0 = PURPLE, c1 = RED, c2 = GREEN, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.3 )
        self.add( p )
        self.wait( )

        e1 = concat( l.vec( 'e' ), '_1' )
        e2 = concat( l.vec( 'e' ), '_2' )
        e3 = concat( l.vec( 'e' ), '_3' )
        eq = MathTex( u, ' &= ', l.add( e1, e2 ), l.newline,
                      v, ' &= ', l.add( e2, e3 ), l.newline )

        ul = MathTex( u )
        ul.move_to( o + 1.2 * a1 )
        ul.set_color( RED )
        vl = MathTex( v )
        vl.set_color( GREEN )
        vl.move_to( o + 1.1 * (a1 + a2) )
        eg1 = VGroup( ul )
        eg2 = VGroup( vl )
        for i in range( 4 ):
            eg1 += eq[i]
            eq[i].set_color( RED )
        for i in range( 4, 8 ):
            eg2 += eq[i]
            eq[i].set_color( GREEN )
        eq.shift( 5 * LEFT + 0.5 * DOWN )
        self.play( Write( eg1 ) )
        self.wait( )
        self.play( Write( eg2 ) )
        self.wait( )

        f1 = concat( l.vec( 'f' ), '_1' )
        f2 = concat( l.vec( 'f' ), '_2' )
        uv = l.wedge( u, v )
        uhat = l.hat( 'u' )
        f2e = l.dot( uhat, l.frac( uv, l.norm( uv ) ) )
        #              0               1   2       3     4      5                                       6
        eq2 = MathTex( l.text('Let '), f1, ' &= ', uhat, ' = ', l.frac( l.add( e1, e2 ), r'\sqrt{2}' ), l.newline,
                       l.text('Let '), f2, ' &= ', f2e,  ' = ', concat( l.frac('1', r'\sqrt{6}'), l.lr( l.sub( l.add( e1, l.mult( '2', e2 ) ), e1 ) ) ), l.newline )
        #              7               8   9       10    11     12                                      13
        eq2.shift( 2.0 * UP + 2.0 * RIGHT )
        eq2[1].set_color( BLUE )
        eq2[2].set_color( BLUE )
        eq2[3].set_color( BLUE )
        eq2[8].set_color( YELLOW )
        eq2[9].set_color( YELLOW )
        eq2[10].set_color( YELLOW )
        f1g = VGroup( Arrow( start = o, end = o + vf1, buff = 0, color = BLUE ), MathTex( f1 ).set_color( BLUE ).move_to( o + vf1 + 0.3 * DOWN ) )
        f2g = VGroup( Arrow( start = o, end = o + vf2, buff = 0, color = YELLOW ), MathTex( f2 ).set_color( YELLOW ).move_to( o + vf2 + 0.3 * LEFT ) )
        self.play( Write( eq2[0:6] ), Write( f1g ) )
        self.wait( )
        self.play( Write( eq2[7:13] ), Write( f2g ) )
        self.wait( )

        eqp = MathTex( concat( u, ' &= ', l.mult( r'\sqrt{2}', f1 ), l.newline ),
                       concat( v, ' &= ', l.add( l.mult( r'\frac{\sqrt{2}}{2}', f1 ),
                                                 l.mult( r'\frac{\sqrt{6}}{2}', f2 ) ), l.newline ) )
        eqp[0].set_color( RED )
        eqp[1].set_color( GREEN )
        eqp.move_to( eq )
        eqp.shift( 2 * DOWN + 0.5 * RIGHT )
        self.play( Write( eqp ) )
        self.wait( )

        e12 = concat( l.vec( 'e' ), '_{12}' )
        e13 = concat( l.vec( 'e' ), '_{13}' )
        e23 = concat( l.vec( 'e' ), '_{23}' )
        eq3 = MathTex( concat( l.wedge( u, v ), ' &= ', l.add( e12, e13, e23 ), l.newline ),
                       concat( l.lrsq( l.wedge( u, v ) ), ' &= - 3', l.newline ),
                       concat( l.wedge( u, v ), r' &= \sqrt{(2 \times 6)/4}', f1, f2, l.newline ),
                       concat( l.lrsq( l.wedge( u, v ) ), ' &= - 3', l.newline ) )
        eq3.shift( DOWN + 2 * RIGHT )
        for i in eq3:
            self.play( Write( i ) )
            self.wait( )

        self.play( FadeOut( VGroup( eq3, eqp, eq, eq2 ) ) )
        t = Text( 'General wedge diagonalization' )
        b1 = l.dot( v, f1 )
        b2 = l.frac( l.norm( uv ), l.norm( u ) )
        eq = MathTex( concat( l.setlr( f1, f2 ), ' &= ', l.setlr( uhat, f2e ), l.newline ),
                      concat( u, ' &= ', l.norm( u ), f1, l.newline ),
                      concat( v, ' &= ', l.add( l.mult( l.lr( l.dot( v, f1 ) ), f1 ), l.mult( l.frac( l.norm( uv ), l.norm( u ) ), f2 ) ), l.newline ), 
                      concat( uv, r'&='),
                      concat( r'\sum_{i < j} ', l.det22( 'u_i', 'v_i', 'u_j', 'v_j' ), r'\mathbf{e}_i \mathbf{e}_j', l.newline ),
                          r'&= ', concat( l.det22( l.norm( u ), '0', b1, b2 ), f1, f2, l.newline ),
                          r'&= ', concat( l.norm( uv ), f1, f2, l.newline ) )
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
        l = latex( )
        v1t = concat( l.vec( 'v' ), '_1' )
        v2t = concat( l.vec( 'v' ), '_2' )
        e1t = concat( l.vec( 'e' ), '_1' )
        e2t = concat( l.vec( 'e' ), '_2' )
        #print( v1t )
        v1 = MathTex( v1t )
        v2 = MathTex( v2t )
        e1 = MathTex( concat( l.vec( 'e' ), '_1' ) )
        e2 = MathTex( concat( l.vec( 'e' ), '_2' ) )
        p = MathTex( v1t, r' \wedge ', v2t, ' = 4', e1t, e2t )
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
        p1 = MathTex( v1t, r' \wedge ', v2t, ' = 4', e1t, e2t )
        p1.move_to( add1 )
        p1.shift( 4 * LEFT )
        self.play( ReplacementTransform( p, p1 ) )
        self.wait( )

        add2 = add1.copy( );
        add2.shift( 2 * UP )
        self.play( FadeOut( p1 ) )
        self.play( Write( add2 ) )
        p2 = MathTex( r'2 ', l.lr( v1t, r' \wedge ', v2t ), ' = 8', e1t, e2t )
        p2.move_to( VGroup( add1, add2 ) )
        p2.shift( 4 * LEFT + 2 * UP )
        self.play( Write( p2 ) )
        self.wait( )

        add3 = add1.copy( );
        add3.shift( 2 * LEFT + 0.55 * UP )
        self.play( FadeOut( p2 ) )
        self.play( Write( add3 ) )
        p3 = MathTex( '3 ', l.lr( v1t, r' \wedge ', v2t ), ' = 12 ', e1t, e2t )
        p3.move_to( add2 )
        p3.shift( 4 * LEFT + 1 * UP )
        self.play( Write( p3 ) )
        self.wait( )

        add4 = add3.copy( );
        add4.shift( 2 * UP )
        self.play( FadeOut( p3 ) )
        self.play( Write( add4 ) )
        p4 = MathTex( '4 ', l.lr( v1t, r' \wedge ', v2t ), ' = 16 ', e1t, e2t )
        p4.move_to( VGroup( add2, add4 ) )
        p4.shift( 1.8 * UP + 3 * RIGHT )
        self.play( Write( p4 ) )
        self.wait( )

        o2 = np.array( [ -2, -2, 0 ] )
        p1s = np.array( [ 1, 0, 0 ] )
        p2s = np.array( [ 0, 1, 0 ] )
        sqpts = unitParallelogram( o2, p1s, p2s, 4 )
        sq = OrientedPolygon( *sqpts, c0 = PURPLE, c1 = PURPLE, c2 = PURPLE, f = 0.5, d1 = 0, d2 = 0, tex = 0, r = 0.1 )
        p5 = MathTex( '16 ', e1t, e2t ).scale( 2 )
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
        g = VGroup( t, t2 )
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
