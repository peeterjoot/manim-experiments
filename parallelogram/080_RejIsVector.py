from helper import *

class RejIsVector( Scene ):
    def construct( self ):
        myTemplate = TexTemplate( )
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex(
                concat( l.Rej( vecu, vecv ), r' &= ', lr_vwedgeu, invu, l.newline ),
                concat( r'&= ', l.add( l.dot( lr_vwedgeu, invu ), l.wedge( lr_vwedgeu, invu ) ), l.newline ),
                concat( r'&= ', l.dot( lr_vwedgeu, invu ), ' + ', vecv, r'\wedge' ), concat( l.lr( l.wedge( vecu, invu ) ), l.newline ),
                concat( r'&= ', l.dot( lr_vwedgeu, invu ), l.newline ),
                concat( r'&= ', vecv, ' - ', l.lr( l.dot( vecv, vecu ) ), invu ) )

        cancel = MathTex( l.lr( l.cancel( l.wedge( vecu, invu ) ) ), tex_template = myTemplate )

        for i in range(2):
           self.play( Write( eq[i] ) )
           self.wait( )
        i = 2
        self.play( AnimationGroup( Write( eq[i] ), Write( eq[i+1] ) ) )
        self.wait( )
        cancel.move_to( eq[i+1] )

        self.play( ReplacementTransform( eq[i+1], cancel ) )
        self.wait( )

        i += 2
        self.play( Write( eq[i] ) )
        self.wait( )

        i += 1
        self.play( Write( eq[i] ) )
        self.wait( )



# vim: et sw=4 ts=4
