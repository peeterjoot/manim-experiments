from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

class Overview( Scene ):
    def construct( self ):
        blist = BulletedList( "Parallelogram Area (visually)",
                              "Parallelogram Area (vector algebra)",
                              "Projection and rejection (geometric algebra)",
                              "Parallelogram Area (GA)",
                              "Determinant structure of the wedge product",
                              height=2 )
        for item in blist:
            self.play( Write( item ) )

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

        o = np.array( [0, -2, 0] )
        p1 = np.array( [3, 1, 0] )
        p2 = np.array( [1, 3, 0] )
        op1 = o + p1
        op2 = o + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )

        v1l = MathTex( u )
        v2l = MathTex( v )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v2l.next_to( v2, UP )
        v2l.set_color( YELLOW )

        p1cap = p1/ np.linalg.norm( p1 )
        proj = np.dot( p2, p1cap ) * p1cap
        oproj = o + proj
        vproj = Line( start = o, end = oproj, color = PURPLE )
        vprojl = MathTex( concat( l.lr( l.dot( v, uhat ) ), uhat ) )
        vprojl.next_to( vproj, DOWN )
        v1g = VGroup( v1, v1l )
        vprojg = VGroup( vproj, vprojl )

        rej = p2 - proj
        vrej = Line( start = oproj, end = op2, color = GREEN )
        vrejl = MathTex( concat( v, ' - ', l.lr( l.dot( v, uhat ) ), uhat ) )
        vrejl.next_to( vrej, RIGHT )
        vrejl.shift( (-0.5,0,0 ))
        v2g = VGroup( v2, v2l )
        vrejg = VGroup( vrej, vrejl )

        op3 = op1 + p2
        v1p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW )
        v2p = Arrow( start = op2, end = op3, buff = 0, color = RED )
        #parallelogram = [o, op1, op3, op2]
        #poly = Polygon( *parallelogram )

        cut = op1 + rej
        recttop = cut - p1
        dashrej = DashedLine( start = op1, end = cut, color = BLUE )
        dashtop = DashedLine( start = cut, end = recttop )
        dashside = DashedLine( start = recttop, end = o, color = BLUE )

        self.play( Create( v1g ))
        self.play( Create( v2g ))
        v1c = v1.copy()
        v2c = v2.copy()
        self.add( v1c )
        self.add( v2c )
        self.play( ReplacementTransform( v1c, v1p ) )
        self.play( ReplacementTransform( v2c, v2p ) )
        #self.play( Create( poly ))
        self.play( Create( vprojg ))
        self.play( Create( vrejg ))
        self.play( Create( dashrej ))
        self.play( Create( dashtop ))
        self.play( Create( dashside ))
        self.play( FadeOut( vprojg, vrejg ))

        move = ( -6, 1, 0 )
        a = VGroup( dashrej, dashtop, dashside, v1, v1l, v2, v2l, v1p, v2p ) # , poly
        self.play( a.animate.shift( move ))
        self.wait( 1 )

        squ        = l.norm2( u )
        sqv        = l.norm2( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        rej        = l.sub( v, l.mult( l.lr( l.dot( v, uhat ) ), uhat ) )

        eq2 = MathTex( l.text( 'base' ), r'& = \Vert', u, concat( r'\Vert', l.newline ),
                       l.text( 'height' ), '& = ', concat( l.norm( rej ), l.newline ) )

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.newline ), # 1
                      concat( '&= ', squ ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2,3
                      concat( '&= ', squ ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4,5
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.newline ) # 6
                    )

        eq.shift( 2.4 * RIGHT )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        #eq2[0].set_color( RED )
        ##eq2[2].set_color( RED )
        #eq2[4].set_color( BLUE )
        self.play( Write( eq[0] ),
                   Write( eq2[0] ),
                   Write( eq2[1] ),
                   Write( eq2[2] ),
                   Write( eq2[3] ),
                   Write( eq2[4] ),
                   Write( eq2[5] ),
                   Write( eq2[6] ) )

        for i in range( 1, 4 ):
            self.play( Write( eq[i] ) )
        self.wait( )
        eq[5].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[3], eq[5] ) )
        self.wait( 2 )

        i = 6
        eq[i].shift( UP )
        self.play( Write( eq[i] ) )
        self.wait( )


class ProjRej( Scene ):
    def construct( self ):
        l = latex()
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        v          = l.vec( 'v' )
        proj       = l.mult( l.lr( l.dot(v, u) ), invu )
        rej        = l.mult( l.lr( l.wedge(v, u) ), invu )

        eq = MathTex( concat( v, r' &= ', v, r'\times 1', l.newline ),
                      concat( r' &= ', v, u, invu, l.newline ),
                      concat( r' &= ', l.lr(v, u), invu, l.newline ),
                      concat( r' &= ', l.lr( l.add( l.dot(v, u), l.wedge(v, u) ) ), invu, l.newline ),
                      concat( r' &= ', l.add( proj, rej ), l.newline ) )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )

class ProjRej2( Scene ):
    def construct( self ):
        l = latex()
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        proj       = l.mult( l.lr( l.dot(v, u) ), invu )
        rej        = l.mult( l.lr( l.wedge(v, u) ), invu )
        proj2      = l.mult( l.lr( l.dot(v, uhat) ), uhat )
        rej2       = l.mult( l.lr( l.wedge(v, uhat) ), uhat )

        eq = MathTex( concat( l.Proj(u, v), ' &\equiv ', proj, l.newline ),
                      concat( l.Rej(u, v),  ' &\equiv ', rej, l.newline ) )
        eq2 = MathTex( concat( l.Proj(u, v), ' &\equiv ', proj, ' = ', proj2, l.newline ),
                       concat( l.Rej(u, v),  ' &\equiv ', rej, ' = ', rej2, l.newline ) )

        for item in eq:
            self.play( Write( item ) )
        #for i in range(2):
        #   self.play( Write( eq[i] ) )
#
#        tb = VGroup( eq[0], eq[1] )
#        tn = VGroup( eq[2], eq[3] )
#        self.play( ReplacementTransform( tb, tn ) )
        self.play( ReplacementTransform( eq, eq2 ) )

        self.wait( )


class ProjRejPerp(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        invu       = l.inv(u)
        v          = l.vec('v')
        proj       = l.mult( u, l.lr( l.dot(v, invu) ) )
        rej        = l.mult( l.lr( l.wedge(v, u) ), invu )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\usepackage{cancel}')

        eq = MathTex( concat( '&', l.dot( l.Rej(u, v), l.Proj(u, v) ), l.newline ),
                      concat( r'\quad&=', l.gpgradezero(
                          l.underbrace( rej, helptext=l.text('Rej') ),
                          l.underbrace( proj, helptext=l.text('Proj') ) ),
                          l.newline ),
                      concat( r'\quad &=', l.gpgradezero( l.wedge(v, u) ), l.lr( l.dot(v, invu) ), l.newline ),
                      concat( r'\quad &=', l.cancel(l.gpgradezero( l.wedge(v, u) )), l.lr( l.dot(v, invu) ), l.newline ),
                      concat( r'\quad &= 0', l.newline ),
                      tex_template = myTemplate)

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector(Scene):
    def construct(self):
        l = latex()
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex(
                concat( l.Rej( u, v ), r' &\equiv ', l.lr( l.wedge( v, u ) ), invu, l.newline ),
                concat( r'&= ', l.add( l.dot( l.lr( l.wedge( v, u ) ), invu, l.wedge( l.lr( l.wedge( v, u ) ), invu ) ) ), l.newline ),
                concat( r'&= ', l.add( l.dot( l.lr( l.wedge( v, u ) ), invu), l.wedge( v, l.cancel( l.wedge( u, invu ) ) ) ), l.newline ),
                concat( r'&= ', l.dot( l.lr( l.wedge( v, u ) ), invu ), l.newline ),
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )



class RejIsVector2(Scene):
    def construct(self):
        l = latex()
        u          = l.vec( 'u' )
        invu       = l.inv( u )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )

        eq = MathTex( concat( l.Rej( u, v ), r' &= ', l.dot( l.lr( l.wedge( v, u ) ), invu ), l.newline ),
                concat( r'&= ', v, l.sub( l.lr( l.dot( u, invu ) ), l.mult( u, l.lr( l.dot( v, invu) ) ) ), l.newline ),
                concat( r'&= ', v, l.neg( u, l.lr( l.dot( v, invu ) ) ), l.newline ),
                concat( r'&= ', v, l.neg( uhat, l.lr( l.dot( v, uhat ) ) ), l.newline ) )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )


def DrawVectorsAndProjRej(self):
    l = latex()
    u          = l.vec( 'u' )
    invu       = l.inv( u )
    v          = l.vec( 'v' )

    o = np.array( [0, -2, 0] )
    p1 = np.array( [3, 1, 0] )
    p2 = np.array( [1, 3, 0] )
    op1 = o + p1
    op2 = o + p2

    p1cap = p1/ np.linalg.norm( p1 )
    proj = np.dot( p2, p1cap ) * p1cap
    oproj = o + proj

    vproj = Line( start = o, end = oproj, color = PURPLE )
    vprojl = MathTex( concat( l.lr( l.dot( v, u ) ), invu ) )
    vprojl.set_color( PURPLE )
    vprojl.next_to( vproj, DOWN )

    rej = p2 - proj
    vrej = Line( start = oproj, end = op2, color = GREEN )
    vrejl = MathTex( concat( l.lr( l.wedge( v, u ) ), invu ) )
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

class ParallelogramComputationGA(Scene):
    def construct(self):
        l = latex()
        u          = l.vec( 'u' )
        #uhat       = l.hat( 'u' )
        invu       = l.inv( u )
        v          = l.vec( 'v' )

        DrawVectorsAndProjRej( self )

        uu         = l.sq( u )
        vv         = l.sq( v )
        vdotusq    = l.lrsq( l.dot( v, u ) )
        vwedgeu    = l.wedge( v, u )
        uwedgev    = l.wedge( u, v )
        rej        = l.mult( l.lr( l.wedge( v, u ) ), invu )
        rrej       = l.mult( invu, l.lr( l.wedge( u, v ) ) )
        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ' ), concat( uu, l.lrsq( rej ), l.newline ), # 1,2
                      concat( '&= ' ), concat( uu, rej, rrej, l.newline ), # 3,4
                      concat( '&= ' ), concat( rej, uu, rrej, l.newline ), # 5,6
                      concat( '&= ' ), concat( l.lr(vwedgeu), l.lr(uwedgev), l.newline ), # 7,8
                      concat( '&= ', l.neg( l.lrsq( vwedgeu )), l.newline ),
                    )

        eq.shift( 2 * RIGHT )

        for i in range( 3 ):
            self.play( Write( eq[i] ) )

        eq[4].shift( 1.35 * UP )
        self.play( ReplacementTransform( eq[2], eq[4] ) )
        self.wait( )

        eq[6].shift( 2.5 * UP )
        self.play( ReplacementTransform( eq[4], eq[6] ) )
        self.wait( )

        eq[8].shift( 3.5 * UP )
        self.play( ReplacementTransform( eq[6], eq[8] ) )
        self.wait( )

        i = 9
        eq[i].shift( 3.5 * UP )
        self.play( Write( eq[i] ) )
        self.wait( )

        eq2 = MathTex(
                concat( l.lrsq( vwedgeu ), '&=', l.dot( l.lr(vwedgeu), l.lr(vwedgeu) ), l.newline ),
                concat( '&=', l.dot( v, l.lr( l.dot( u, l.lr(vwedgeu) ) ) ), l.newline ),
                concat( '&=', l.dot( v, l.lr( l.sub(
                    l.mult( l.lr( l.dot(u, v) ), u ),
                    l.mult(uu, v)
                    ) ) ), l.newline ),
                concat( '&=', l.sub( vdotusq, l.mult( uu, vv ) ), l.newline ) )
        eq2.shift( 1.5 * DOWN + 2 * RIGHT )

        for item in eq2:
            self.play( Write( item ) )

