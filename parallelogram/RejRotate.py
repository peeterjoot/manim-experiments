from helper import *

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


# vim: et sw=4 ts=4
