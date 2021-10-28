from helper import *
from helper2 import *

class ProjRejPerp( Scene ):
    def construct( self ):
        labels = DrawVectorsAndProjRej( self, 1 )

        eqga = MathTex( concat( l.mult( vecu, vecv ), ' &= ', l.dot( vecu, vecv ), ' + ', l.wedge( vecu, vecv ), l.newline ),
                                              concat( ' &= ', l.gpgradezero( vecu, vecv ), ' + ', l.gpgradetwo( vecu, vecv ) ) )
        eqga.set_color_by_tex_to_color_map( acolors )

        i = 0
        self.play( Write( eqga[i] ) )
        self.wait( )
        i = 1
        self.play( Write( eqga[i] ) )
        self.wait( 2 )
        self.play( FadeOut( eqga ) )
        self.wait( 1 )

        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )

        eq = MathTex( *[l.dot( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) )] )
        eq.set_color_by_tex_to_color_map( acolors )
        eq.shift( 2 * UP + 1 * RIGHT )
        self.play( Write( eq ) )
        self.wait( )

        where = eq.get_part_by_tex( r'\cdot' )
        eq2 = MathTex( *['=', l.gpgradezero( l.Rej( vecu, vecv ), l.Proj( vecu, vecv ) )] )
        write_aligned( self, eq, eq2, 0.75 * DOWN + LEFT, acolors, r'\cdot' )
        self.wait( )

        eq3a = MathTex( '=', concat( l.Bigl, l.lgr, rej) )
        eq3b = MathTex( '{{ (', l.vec('v'), r'\cdot', l.vec('u'), ')}}' )
        eq3c = MathTex( concat( invu, l.Bigr, l.rgr ) )
        eq3b[1].set_color( YELLOW )
        eq3b[3].set_color( RED )
        g = VGroup( eq3a, eq3b, eq3c )
        where = eq2.get_part_by_tex( '=' )
        eq3a.move_to( where, LEFT )
        eq3a.shift( DOWN )
        eq3b.next_to( eq3a, RIGHT )
        eq3c.next_to( eq3b, RIGHT )
        eq3a.set_color_by_tex_to_color_map( acolors )
        eq3c.set_color_by_tex_to_color_map( acolors )
        self.play( AnimationGroup( Write( eq3a ), Write( eq3b ), Write( eq3c ) ) )
        self.wait( 2 )
        self.play( Indicate( eq3b ) ) # vdotu
        self.wait( 2 )

        eq4 = MathTex( *['=', l.gpgradezero( rej, invu, big = 1 ), lr_vdotu ] )
        eq4.set_color_by_tex_to_color_map( acolors )
        where = eq3a.get_part_by_tex( '=' )
        eq4.move_to( where, LEFT )
        self.play( ReplacementTransform( g, eq4 ) )
        self.wait( 2 )

        eq5a = MathTex( '=' )
        eq5b = MathTex( r'{{ \langle', l.vec('v'), r'\wedge', l.vec('u'), r'\rangle }}' )
        eq5c = MathTex( l.frac( vdotu, l.sq( vecu ) ) )
        eq5b[1].set_color( YELLOW )
        eq5b[3].set_color( RED )
        eq5c.set_color_by_tex_to_color_map( acolors )
        where = eq4.get_part_by_tex( '=' )
        eq5a.move_to( where, LEFT )
        eq5b.next_to( eq5a, RIGHT )
        eq5c.next_to( eq5b, RIGHT )
        g = VGroup( eq5a, eq5b, eq5c )
        self.play( ReplacementTransform( eq4, g ) )
        self.wait( 2 )

        self.play( Indicate( eq5b ) )
        self.wait( 1 )
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        eq5bp = MathTex( l.cancel( r'\langle', l.vec('v'), r'\wedge', l.vec('u'), r'\rangle' ), tex_template = myTemplate )
        eq5bp.move_to( eq5b )
        #eq5bp.set_color_by_tex_to_color_map( acolors )
        self.play( ReplacementTransform( eq5b, eq5bp ) )
        self.wait( 1 )

        eq6 = MathTex( '= 0' )
        write_aligned( self, eq5a, eq6, 0.75 * DOWN, acolors )
        self.wait( 2 )

        # done.



# vim: et sw=4 ts=4
