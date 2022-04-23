from helper import *

class RejIsVector( Scene ):
    def construct( self ):

        title = Tex( 'Rejection is a vector.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        eq1 = AcolorsMathTex( l.Rej( vecu, vecv ), '=', lr_vwedgeu, invu )
        eq2a = AcolorsMathTex( '=', l.dot( lr_vwedgeu, invu ), '+' )
        eq2b = AcolorsMathTex( l.wedge( lr_vwedgeu, invu ) )

        # just the trivector term:
        eq3a = AcolorsMathTex( vecv, r'\wedge' )
        eq3b = AcolorsMathTex( l.lr( l.wedge( vecu, invu ), big = 1 ) )
        eq4 = AcolorsMathTex( '=', l.dot( lr_vwedgeu, invu ) )
        eq5 = AcolorsMathTex( '=', vecv, ' - ', l.lr( l.dot( vecv, vecu ) ), invu )
        eq1.shift( 2 * UP + 2 * LEFT )

        self.play( Write( eq1 ) )
        self.wait( 10 )
        g = VGroup( eq2a, eq2b )
        where = eq1.get_part_by_tex( '=' )
        eq2a.move_to( where, LEFT )
        eq2a.shift( 1.25 * DOWN )
        eq2b.next_to( eq2a, RIGHT )
        self.play( AnimationGroup( Write( eq2a ), Write( eq2b ) ) )
        self.wait( 5 )

        eq3a.move_to( eq2b, LEFT )
        eq3b.next_to( eq3a, RIGHT )
        self.play( ReplacementTransform( eq2b, VGroup( eq3a, eq3b ) ) )
        self.wait( 5 )
        self.play( Indicate( eq3b ) )
        self.wait( 5 )

        write_aligned( self, eq2a, eq4, 1.25 * DOWN )
        self.wait( 5 )

        write_aligned( self, eq4, eq5, 1.25 * DOWN )
        self.wait( 5 )

        #myTemplate = TexTemplate( )
        #myTemplate.add_to_preamble( r'\usepackage{cancel}' )
        #cancel = MathTex( l.lr( l.cancel( l.wedge( vecu, invu ) ) ), tex_template = myTemplate )



# vim: et sw=4 ts=4
