from acolorsmath import *

class SummaryTable( Scene ):
    def construct( self ):

        title = Text( 'Summary.' )
        #.scale(0.75)
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )

        table = MathTable( [
             [ r'\text{Operator}',   r'\mathbb{R}^3',                                r'\mathbb{R}^N',                               r'\text{General}' ],
             [ l.Proj( vecu, vecv ), concat( l.lr( l.dot( vecv, hatu ) ), hatu ),    concat( l.lr( l.dot( vecv, hatu ) ), hatu ),   concat( l.lr( l.dot( vecv, vecu ) ), invu ) ],
             [ l.Rej( vecu, vecv ),  l.cross( hatu, l.lr( l.cross( vecv, hatu ) ) ), concat( l.lr( l.wedge( vecv, hatu ) ), hatu ), concat( l.lr( l.wedge( vecv, vecu ) ), invu ) ]
          ], include_outer_lines = True, element_to_mobject = AcolorsMathTex )

        rows = table.get_rows( )
        rows[0].set_color( BLUE )

        table.get_horizontal_lines()[:3].set_color( BLUE )
        table.get_vertical_lines()[:3].set_color( BLUE )
        table.get_horizontal_lines()[:3].set_z_index( 1 )

        self.play( FadeIn( table ) )
        self.wait( 10 )
