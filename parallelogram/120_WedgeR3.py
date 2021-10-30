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


class WedgeR3( Scene ):
    def construct( self ):
        t = MathTex( r'\mathbb{R}^3' ).scale( 2 )
        t.shift( 2 * UP )
        t.set_color( RED )
        self.add( t )

        vec_e1 = l.doublebr( l.vec( 'e' ), '_1' )
        vec_e2 = l.doublebr( l.vec( 'e' ), '_2' )
        vec_e3 = l.doublebr( l.vec( 'e' ), '_3' )
        vec_ei = l.doublebr( l.vec( 'e' ), '_i' )
        vec_ej = l.doublebr( l.vec( 'e' ), '_j' )
        eqa1 = MathTex( uwedgev, '=' )
        eqa1.shift( 4 * LEFT )
        eqa2 = MathTex( concat( r'\sum_{i < j} ', detuivj, vec_ei, vec_ej ) )
        eqa1.set_color_by_tex_to_color_map( acolors )
        eqa2.next_to( eqa1, RIGHT )
        self.play( AnimationGroup( Write( eqa1 ), Write( eqa2 ) ) )

        d12 = l.doublebr( l.det22( 'u_1', 'v_1', 'u_2', 'v_2' ) )
        t12 = [ MathTex( r'i, j = 1, 2:\quad' ),
                MathTex( d12,  vec_e1,  vec_e2 ),
                MathTex( d12,  vec_e1,  vec_e2, r' ( ', vec_e3,  vec_e3, r' )' ),
                MathTex( d12, r' ( ', vec_e1,  vec_e2,  vec_e3, r' ) ', vec_e3 ),
                MathTex( d12, 'I', vec_e3 ) ]
        playAndFadeOut( self, t12, eqa1 )

        d13 = l.doublebr( l.det22( 'u_1', 'v_1', 'u_3', 'v_3' ) )
        t13 = [ MathTex( r'i, j = 1, 3:\quad' ),
                MathTex( d13, vec_e1, vec_e3 ),
                MathTex( d13, vec_e1, l.lr( vec_e2, vec_e2 ), vec_e3 ),
                MathTex( d13, vec_e1, vec_e2, l.lr( l.neg( l.mult( vec_e3, vec_e2 ) ) ) ),
                MathTex( '-', d13, l.lr( vec_e1, vec_e2, vec_e3 ), vec_e2 ),
                MathTex( '-', d13, 'I', vec_e2 ) ]
        playAndFadeOut( self, t13, eqa1 )

        d23 = l.doublebr( l.det22( 'u_2', 'v_2', 'u_3', 'v_3' ) )
        t23 = [ MathTex( r'i, j = 2, 3:\quad' ),
                MathTex( d23, vec_e2, vec_e3 ),
                MathTex( d23, l.lr( vec_e1, vec_e1 ), vec_e2, vec_e3 ),
                MathTex( d23, vec_e1, l.lr( vec_e1, vec_e2, vec_e3 ) ),
                MathTex( d23, vec_e1, 'I' ) ]
        playAndFadeOut( self, t23, eqa1 )

        eqb = MathTex( concat( 'I', l.lr( d12, vec_e3, '-', d13, vec_e2, '+', d23, vec_e1, big = 2 ) ) )
        eqb.set_color_by_tex_to_color_map( acolors )
        eqb.next_to( eqa1, RIGHT )
        self.play( TransformMatchingTex( eqa2, eqb ) )
        self.wait( )

        eqc = MathTex( concat( 'I',
                               r'\begin{vmatrix}',
                               r'\mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\',
                               r'u_1 & u_2 & u_3 \\',
                               r'v_1 & v_2 & v_3',
                               r'\end{vmatrix}' ) )
        eqc.next_to( eqa1, RIGHT )
        self.play( TransformMatchingTex( eqb, eqc ) )
        self.wait( )
        a = VGroup( eqa1, eqc )
        self.play( a.animate.shift( 3 * RIGHT ) )

        eqd = MathTex( concat( 'I', l.lr( l.cross( vecu, vecv ) ) ) )
        eqd.next_to( eqa1 )
        eqd.set_color_by_tex_to_color_map( acolors )
        self.play( TransformMatchingTex( eqc, eqd ) )

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

        eqe = MathTex( concat( l.sq(t_area), ' = ', l.neg( l.lrsq( uwedgev ) ), ' = ', l.norm2( l.cross( vecu, vecv ) ) ) )
        eqe.set_color_by_tex_to_color_map( acolors )
        eqe.move_to( g )
        eqe.shift( 5 * RIGHT )
        self.play( Write( eqe ) )
        self.wait( )




# vim: et sw=4 ts=4
