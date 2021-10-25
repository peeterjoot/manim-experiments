from helper import *

class ProjRejPerp( Scene ):
    def construct( self ):
        labels = DrawVectorsAndProjRej( self, 1 )

        eqga = MathTex( l.mult( vecu, vecv ), ' &= ', l.dot( vecu, vecv ), ' + ', l.wedge( vecu, vecv ), l.newline,
                                              ' &= ', l.gpgradezero( vecu, vecv ), ' + ', l.gpgradetwo( vecu, vecv ) )
        eqga[2].set_color( BLUE )
        eqga[4].set_color( RED )
        eqga[7].set_color( BLUE )
        eqga[9].set_color( RED )

        for i in range(0, 5):
           self.play( Write( eqga[i] ) )
        self.wait( )
        for i in range(5, 10):
           self.play( Write( eqga[i] ) )
        self.wait( 2 )
        self.play( AnimationGroup( Indicate( eqga[2] ), Indicate( eqga[7] ) ) )
        self.play( AnimationGroup( Indicate( eqga[4] ), Indicate( eqga[9] ) ) )
        self.wait( 1 )
        self.play( FadeOut( eqga ) )
        self.wait( 1 )

        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        #myTemplate = TexTemplate( )
        #myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex( concat( '&', l.dot( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) ), l.newline ),
                      concat( r'\quad&=', l.Bigl, l.lgr, rej), lr_vdotu, concat( invu, l.Bigr, l.rgr, l.newline ),
                      concat( r'\quad &=', l.Bigl, l.lgr, vwedgeu), concat( invu, invu ), concat( l.Bigr, l.rgr, lr_vdotu, l.newline ),
                              r'\quad &=', l.gpgradezero( vwedgeu ), concat( l.inv( l.sq( vecu ) ), lr_vdotu, l.newline ),
                      concat( r'\quad &= 0', l.newline ) )
                      #tex_template = myTemplate

        eq.shift( RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 2 )
        i = 1
        self.play( AnimationGroup( *[Write( eq[ i + j ] ) for j in range(3)] ) )
        self.wait( 2 )
        self.play( Indicate( eq[i+1] ) ) # vdotu

        i += 3
        self.play( AnimationGroup( *[Write( eq[ i + j ] ) for j in range(3)] ) )
        self.wait( 2 )
        self.play( Indicate( eq[i+1] ) ) # 1/u 1/u

        i += 3
        self.play( AnimationGroup( *[Write( eq[ i + j ] ) for j in range(3)] ) )
        self.wait( 2 )
        self.play( Indicate( eq[i+1] ) ) # vwedgeu

        i += 3
        self.wait( 2 )
        self.play( Write( eq[i+0] ) )

        # done.
        self.wait( 2 )



# vim: et sw=4 ts=4
