from helper import *

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


# vim: et sw=4 ts=4
