from helper import *

def writeem(self, eqref, eq, n, f = 1):
    eq[0].move_to( eqref, DOWN )
    eq[0].shift( 1.75 * DOWN )
    self.play( Write( eq[0] ) )
    self.wait( 4 )
    last = eq[0]
    for i in range(n):
        write_aligned( self, last, eq[i+1], 1.25 * DOWN, None )
        last = eq[i+1]
        self.wait( 5 )
    if f:
        self.play( FadeOut( *eq ) )
    self.wait( 5 )

class Inverse( Scene ):
    def construct( self ):

        title = Tex( 'The vector inverse.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        eq = AcolorsMathTex( concat( r'Claim: ', invu, '=', l.frac( vecu, uu ) ) )
        eq.move_to( title, DOWN )
        eq.shift( 2 * DOWN )
        self.play( Write( eq ) )
        self.wait( 8 )

        #eq2 = [ AcolorsMathTex( concat( vecu, invu, '=', vecu, r'\,', l.frac( vecu, uu ) ) ),
        #        AcolorsMathTex( concat( '=', l.frac( uu, uu ) ) ),
        #        AcolorsMathTex( concat( '= 1' ) ) ]
        #writeem( self, eq, eq2, 2 )

        eq3 = [ AcolorsMathTex( concat( invu, vecu, '=', l.frac( vecu, uu ), vecu ) ),
                AcolorsMathTex( concat( '=', l.frac( uu, uu ) ) ),
                AcolorsMathTex( concat( '= 1' ) ) ]
        writeem( self, eq, eq3, 2 )

        eqx = AcolorsMathTex( concat( uu, '=', l.dot( vecu, vecu ), '=', l.sq( l.norm( vecu ) ) ) )
        self.play( Write( eqx ) )
        self.wait( 10 )
        self.play( FadeOut( eqx ) )

        eqy = [ AcolorsMathTex( concat( invu, '=', l.frac( vecu, uu ) ) ),
                #AcolorsMathTex( concat( '=', vecu, l.pow( l.norm( vecu ), n = -2 ) ) ),
                AcolorsMathTex( concat( '=', l.frac( hatu, l.norm( vecu ) ) ) ) ]
        writeem( self, eq, eqy, 1, f = 0 )
        self.wait( 10 )


# vim: et sw=4 ts=4
