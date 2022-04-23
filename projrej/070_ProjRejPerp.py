from helper import *

class ProjRejPerp( Scene ):
    def construct( self ):
        labels = DrawVectorsAndProjRej( self, 1 )

        title = Tex( 'Orthogonality.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        eqga = [ AcolorsMathTex( concat( l.mult( vecu, vecv ), ' = ', l.dot( vecu, vecv ), ' + ', l.wedge( vecu, vecv ) ) ),
                 AcolorsMathTex( concat( ' = ', l.gpgradezero( vecu, vecv ), ' + ', l.gpgradetwo( vecu, vecv ) ) ) ]

        i = 0
        self.wait( 10 )
        self.play( Write( eqga[0] ) )
        self.wait( 10 )
        write_aligned( self, eqga[0], eqga[1], 0.75 * DOWN, None )
        self.wait( 10 )
        self.play( FadeOut( *eqga ) )
        self.wait( 10 )

        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )

        eq = AcolorsMathTex( *[l.dot( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) )] )
        eq.shift( 2 * UP + 1 * RIGHT )
        self.play( Write( eq ) )
        self.wait( 4 )

        where = eq.get_part_by_tex( r'\cdot' )
        eq2 = AcolorsMathTex( *['=', l.gpgradezero( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) )] )
        write_aligned( self, eq, eq2, 0.75 * DOWN + LEFT, None, r'\cdot' )
        self.wait( 4 )

        eq3a = AcolorsMathTex( '=', concat( l.Bigl, l.lgr, rej) )
        eq3b = MathTex( '{{ (', l.vec('v'), r'\cdot', l.vec('u'), ')}}' )
        eq3c = AcolorsMathTex( concat( invu, l.Bigr, l.rgr ) )
        eq3b[1].set_color( YELLOW )
        eq3b[3].set_color( RED )
        g = VGroup( eq3a, eq3b, eq3c )
        where = eq2.get_part_by_tex( '=' )
        eq3a.move_to( where, LEFT )
        eq3a.shift( DOWN )
        eq3b.next_to( eq3a, RIGHT )
        eq3c.next_to( eq3b, RIGHT )
        self.play( AnimationGroup( Write( eq3a ), Write( eq3b ), Write( eq3c ) ) )
        self.wait( 4 )
        self.play( Indicate( eq3b ) ) # vdotu
        self.wait( 4 )

        eq4 = AcolorsMathTex( *['=', l.gpgradezero( rej, invu, big = 1 ), lr_vdotu ] )
        where = eq3a.get_part_by_tex( '=' )
        eq4.move_to( where, LEFT )
        self.play( ReplacementTransform( g, eq4 ) )
        self.wait( 4 )

        eq5a = AcolorsMathTex( '=' )
        eq5b = MathTex( r'{{ \langle', l.vec('v'), r'\wedge', l.vec('u'), r'\rangle }}' )
        eq5c = AcolorsMathTex( l.frac( vdotu, l.sq( vecu ) ) )
        eq5b[1].set_color( YELLOW )
        eq5b[3].set_color( RED )
        where = eq4.get_part_by_tex( '=' )
        eq5a.move_to( where, LEFT )
        eq5b.next_to( eq5a, RIGHT )
        eq5c.next_to( eq5b, RIGHT )
        g = VGroup( eq5a, eq5b, eq5c )
        self.play( ReplacementTransform( eq4, g ) )
        self.wait( 4 )

        self.play( Indicate( eq5b ) )
        self.wait( 4 )
        eq5bp = AcolorsMathTex( l.cancel( r'\langle', l.vec('v'), r'\wedge', l.vec('u'), r'\rangle' ) )
        eq5bp.move_to( eq5b )
        self.play( ReplacementTransform( eq5b, eq5bp ) )
        self.wait( 4 )

        eq6 = AcolorsMathTex( '= 0' )
        write_aligned( self, eq5a, eq6, 0.75 * DOWN, None )
        self.wait( 10 )

        # done.



# vim: et sw=4 ts=4
