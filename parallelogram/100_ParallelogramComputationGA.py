from helper import *

class ParallelogramComputationGA( Scene ):
    def construct( self ):
        DrawVectorsAndProjRej( self, 1 )

        vdotusq    = l.lrsq( vdotu )
        rej        = l.mult( lr_vwedgeu, invu )
        rrej       = l.mult( invu, lr_uwedgev )
        #d0 = concat( l.sq( l.text( 'Area' ) ), r' &= ' )
        #print( d0 )
        #d1 = concat( uu, l.lrsq( rej ), l.newline )
        #print( d1 )
        #d2 = concat( uu, rej, rrej, l.newline )
        #print( d2 )
        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      #concat( l.sq( l.text( 'Area' ) ), r' &= ' ), concat( uu, l.lrsq( rej, big = 1 ), l.newline ), # 1, 2
                      concat( l.sq( l.text( 'Area' ) ), r' &= ' ), concat( uu, l.lrsq( rej ), l.newline ), # 1, 2
                      #r'& { 1', r' \over ', r'\mathbf{u}', ' } ', '{', '1', r' \over ', r'\mathbf{u}', r' } \\',
                      '&= ', concat( uu, rej, rrej, l.newline ), # 3, 4
                      '&= ', concat( rej, uu, rrej, l.newline ), # 5, 6
                      '&= ', concat( lr_vwedgeu, lr_uwedgev, l.newline ), # 7, 8
                      concat( '&= ', l.neg( l.lrsq( vwedgeu ) ), l.newline )
                      #, tex_to_color_map = uvcolors
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



# vim: et sw=4 ts=4
