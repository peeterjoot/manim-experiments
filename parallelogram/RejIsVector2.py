from helper import *

class RejIsVector2( Scene ):
    def construct( self ):

        eq = MathTex( concat( l.Rej( vecu, vecv ), r' &= ', l.dot( lr_vwedgeu, invu ), l.newline ),
                concat( r'&= ', vecv, l.sub( l.lr( l.dot( vecu, invu ) ), l.mult( vecu, l.lr( l.dot( vecv, invu ) ) ) ), l.newline ),
                concat( r'&= ', vecv, l.neg( vecu, l.lr( l.dot( vecv, invu ) ) ), l.newline ),
                concat( r'&= ', vecv, l.neg( hatu, l.lr( l.dot( vecv, hatu ) ) ), l.newline ) )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )


# vim: et sw=4 ts=4
