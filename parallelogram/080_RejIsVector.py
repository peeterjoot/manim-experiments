from helper import *
from helper2 import *

class RejIsVector( Scene ):
    def construct( self ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq1 = MathTex( l.Rej( vecu, vecv ), '=', lr_vwedgeu, invu )
        eq2a = MathTex( '=', l.dot( lr_vwedgeu, invu ), '+' )
        eq2b = MathTex( l.wedge( lr_vwedgeu, invu ) )

        # just the trivector term:
        eq3a = MathTex( vecv, r'\wedge' )
        eq3b = MathTex( l.lr( l.wedge( vecu, invu ), big = 1 ) )
        eq4 = MathTex( '=', l.dot( lr_vwedgeu, invu ) )
        eq5 = MathTex( '=', vecv, ' - ', l.lr( l.dot( vecv, vecu ) ), invu )
        eq1.set_color_by_tex_to_color_map( acolors )
        eq1.shift( 2 * UP + 2 * LEFT )

        self.play( Write( eq1 ) )
        self.wait( )
        g = VGroup( eq2a, eq2b )
        where = eq1.get_part_by_tex( '=' )
        eq2a.move_to( where, LEFT )
        eq2a.shift( 1.25 * DOWN )
        eq2a.set_color_by_tex_to_color_map( acolors )
        eq2b.next_to( eq2a, RIGHT )
        eq2b.set_color_by_tex_to_color_map( acolors )
        self.play( AnimationGroup( Write( eq2a ), Write( eq2b ) ) )
        self.wait( )

        eq3a.set_color_by_tex_to_color_map( acolors )
        eq3b.set_color_by_tex_to_color_map( acolors )
        eq3a.move_to( eq2b, LEFT )
        eq3b.next_to( eq3a, RIGHT )
        self.play( ReplacementTransform( eq2b, VGroup( eq3a, eq3b ) ) )
        self.wait( )
        self.play( Indicate( eq3b ) )
        self.wait( )

        write_aligned( self, eq2a, eq4, 1.25 * DOWN, acolors )
        self.wait( )

        write_aligned( self, eq4, eq5, 1.25 * DOWN, acolors )
        self.wait( )

        #cancel = MathTex( l.lr( l.cancel( l.wedge( vecu, invu ) ) ), tex_template = myTemplate )



# vim: et sw=4 ts=4
