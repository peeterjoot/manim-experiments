from helper import *

def playAndFadeOut( self, eq, pos ):
    eq[ 0 ].move_to( pos )
    eq[ 0 ].shift( 2 * DOWN + 2 * RIGHT )
    eq[ 1 ].next_to( eq[ 0 ], RIGHT )
    self.play( AnimationGroup( Write( eq[ 0 ] ), Write( eq[ 1 ] ) ) )

    n = len( eq )

    last = eq[ 1 ]
    for i in range( 1, n - 1 ):
        eq[ i + 1 ].next_to( eq[ 0 ], RIGHT )
        self.play( TransformMatchingTex( last, eq[ i + 1 ] ) )
        last = eq[ i + 1 ]
        self.wait( )

    g = VGroup( eq[ 0 ], last )
    self.play( FadeOut( g ) )


def playReplacement( self, neweq, oldeq ):
    newat = neweq.copy()
    newat.move_to( oldeq )
    self.play( TransformMatchingTex( oldeq, newat ) )
    return newat

class WedgeR3( Scene ):
    def construct( self ):
        t = MathTex( r'\mathbb{R}^3' ).scale( 2 )
        t.shift( 2 * UP )
        t.set_color( BLUE )
        self.add( t )

        vec_e1 = l.doublebr( l.vec( 'e' ), '_1' )
        vec_e2 = l.doublebr( l.vec( 'e' ), '_2' )
        vec_e3 = l.doublebr( l.vec( 'e' ), '_3' )
        vec_ei = l.doublebr( l.vec( 'e' ), '_i' )
        vec_ej = l.doublebr( l.vec( 'e' ), '_j' )
        eqa1 = MathTex( uwedgev, '=' )
        eqa1.shift( 5 * LEFT )
        eqa2 = MathTex( concat( r'\sum_{i < j} ', detuivj, vec_ei, vec_ej ) )
        eqa1.set_color_by_tex_to_color_map( acolors )
        eqa2.next_to( eqa1, RIGHT )
        self.play( AnimationGroup( Write( eqa1 ), Write( eqa2 ) ) )
        self.wait( 1 );

        d12 = l.doublebr( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ) )
        d13 = l.doublebr( l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ) )
        d31 = l.doublebr( l.det22( 'u_3', 'v_3', 'u_1', 'v_1' ) )
        d23 = l.doublebr( l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ) )
        eqx0 = MathTex( concat( '{}', d12, vec_e1, vec_e2, '+', d13, vec_e1, vec_e3, '+', d23, vec_e2, vec_e3 ) )
        eqx0.next_to( eqa1, RIGHT )
        self.play( TransformMatchingTex( eqa2, eqx0 ) )
        #eqx1 = MathTex( concat( '{}', d23, vec_e2, vec_e3, '+', d31, vec_e3, vec_e1, '+', d12, vec_e1, vec_e2 ) )
        eqy1 = MathTex( d23 )
        eqy2 = MathTex( concat( vec_e2, vec_e3 ) )
        eqy3 = MathTex( concat('+', d31) )
        eqy4 = MathTex( concat( vec_e3, vec_e1 ) )
        eqy5 = MathTex( concat('+', d12) )
        eqy6 = MathTex( concat( vec_e1, vec_e2 ) )
        eqy1.next_to( eqa1, RIGHT )
        eqy2.next_to( eqy1, RIGHT )
        eqy3.next_to( eqy2, RIGHT )
        eqy4.next_to( eqy3, RIGHT )
        eqy5.next_to( eqy4, RIGHT )
        eqy6.next_to( eqy5, RIGHT )
        self.play( ReplacementTransform( eqx0, VGroup( eqy1, eqy2, eqy3, eqy4, eqy5, eqy6 ) ) )
        #self.play( TransformMatchingTex( eqx0, eqx1 ) )
        self.wait( 1 )

        self.play( Indicate( eqy2 ) )
        self.wait( 1 )
        t23 = [ MathTex( vec_e2, vec_e3, '=' ),
                MathTex( l.lr( vec_e1, vec_e1 ), vec_e2, vec_e3 ),
                MathTex( vec_e1, l.lr( vec_e1, vec_e2, vec_e3 ) ),
                MathTex( vec_e1, 'I' ) ]
        playAndFadeOut( self, t23, eqa1 )
        self.wait( 1 )
        c = playReplacement( self, t23[3], eqy2 )
        self.wait( 1 )
        r = VGroup( eqy1, c, eqy3 )

        self.play( Indicate( eqy4 ) )
        self.wait( 1 )
        t31 = [ MathTex( vec_e3, vec_e1, '=' ),
                MathTex( '-', vec_e1, vec_e3 ),
                MathTex( '-', vec_e1, l.lr( vec_e2, vec_e2 ), vec_e3 ),
                MathTex( '-', vec_e1, vec_e2, l.lr( vec_e2, vec_e3 ) ),
                MathTex( '+', vec_e1, vec_e2, l.lr( vec_e3, vec_e2 ) ),
                MathTex( l.lr( vec_e1, vec_e2, vec_e3 ), vec_e2 ),
                MathTex( 'I', vec_e2 ) ]
        playAndFadeOut( self, t31, eqa1 )
        self.wait( 1 )
        c = playReplacement( self, t31[6], eqy4 )
        r += c
        r += eqy5
        self.wait( 1 )

        self.play( Indicate( eqy6 ) )
        self.wait( 1 )
        t12 = [ MathTex( vec_e1,  vec_e2, '=' ),
                MathTex( vec_e1,  vec_e2, r' ( ', vec_e3,  vec_e3, r' )' ),
                MathTex( r' ( ', vec_e1,  vec_e2,  vec_e3, r' ) ', vec_e3 ),
                MathTex( 'I', vec_e3 ) ]
        playAndFadeOut( self, t12, eqa1 )
        self.wait( 1 )
        c = playReplacement( self, t12[3], eqy6 )
        r += c
        self.wait( 1 )

        eqb = MathTex( concat( 'I', l.lr( d23, vec_e1, '+', d31, vec_e2, '+', d12, vec_e3, big = 1 ) ) )
        eqb.next_to( eqa1, RIGHT )
        self.play( ReplacementTransform( r, eqb ) )
        self.wait( 1 )

        eqc = MathTex( concat( 'I',
                       r'\begin{vmatrix}',
                       r'\mathbf{e}_1 & u_1 & v_1 \\',
                       r'\mathbf{e}_2 & u_2 & v_2 \\',
                       r'\mathbf{e}_3 & u_3 & v_3 \\',
                       r'\end{vmatrix}' ) )
        eqc.next_to( eqa1, RIGHT )
        self.play( ReplacementTransform( eqb, eqc ) )
        self.wait( 1 )

        eqd = MathTex( concat( 'I', l.lr( l.cross( vecu, vecv ) ) ) )
        c = eqa1.copy()
        c.next_to( t, DOWN )
        c.shift( LEFT + DOWN )
        eqd.next_to( c, RIGHT )
        eqd.shift( 0.05 * DOWN )
        eqd.set_color_by_tex_to_color_map( acolors )
        self.play( ReplacementTransform( VGroup( eqa1, eqc ), VGroup( c, eqd ) ) )
        self.wait( 1 )

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
        pts = [ o, op1, op3, op2 ]
        poly = Polygon( *pts, color = PURPLE, fill_opacity = 0.5 )
        poly.set_z_index( v1.z_index - 1 )

        v1l = MathTex( vecu )
        v2l = MathTex( vecv )
        v1l.next_to( v1, RIGHT )
        v2l.next_to( v2, UP )
        v1l.set_color( RED )
        v2l.set_color( YELLOW )

        g = VGroup( v1, v2, v1p, v2p, v1l, v2l, poly )
        g.move_to( -4 * RIGHT - 1.5 * UP )

        self.play( Write( g ) )

        eqe = MathTex( concat( l.sq(t_area), ' = ', l.neg( l.lrsq( uwedgev ) ), ' = ', l.norm2( l.cross( vecu, vecv ) ) ) )
        eqe.set_color_by_tex_to_color_map( acolors )
        eqe.move_to( g )
        eqe.shift( 5 * RIGHT )
        self.play( Write( eqe ) )
        self.wait( )


# vim: et sw=4 ts=4
