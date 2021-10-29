from helper import *
from helper2 import *

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


class WedgeR3( Scene ):
    def construct( self ):
        t = MathTex( r'\mathbb{R}^3' ).scale( 2 )
        t.shift( 2 * UP )
        t.set_color( RED )
        self.add( t )

        eqa = MathTex( concat( uwedgev, r'= \sum_{i < j} ', detuivj, r' \mathbf{e}_i \mathbf{e}_j' ) )
        eqa.set_color_by_tex_to_color_map( acolors )
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
        eqb.set_color_by_tex_to_color_map( acolors )

        eqc = MathTex( concat( uwedgev, r'= I ',
                       r'\begin{vmatrix}',
                       r'\mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\',
                       r'u_1 & u_2 & u_3 \\',
                       r'v_1 & v_2 & v_3',
                       r'\end{vmatrix}' ) )
        eqc.set_color_by_tex_to_color_map( acolors )

        eqd = MathTex( concat( uwedgev, r'= I ', l.lr( l.cross( vecu, vecv ) ) ) )
        eqd.set_color_by_tex_to_color_map( acolors )

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
        eqe.set_color_by_tex_to_color_map( acolors )
        eqe.move_to( g )
        eqe.shift( 5 * RIGHT )
        self.play( Write( eqe ) )
        self.wait( )


# vim: et sw=4 ts=4
