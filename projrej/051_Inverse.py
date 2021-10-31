from helper import *

class 051_Inverse( Scene ):
    def construct( self ):

        title = Tex( 'The vector inverse.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( Write( title ) )

        eq = MathTex( concat( r'Lemma: ', invu, '=', l.frac( vecu, uu ) ) ) 
        eq.move_to( what_to_prove, DOWN )
        eq.shift( 2 * DOWN )
        eq.set_color_by_tex_to_color_map( acolors )
        self.play( Write( eq ) )
        self.wait( 2 )

        eq2 = MathTex( concat( l.lr( vecu, invu, big = 2), '&=', vecu, l.frac( vecu, uu ), l.newline ),
                       concat( '&=', l.frac( uu, uu ), l.newline ),
                       concat( '&= 1', l.newline ) )
        eq2.move_to( eq, DOWN )
        eq2.shift( 4 * DOWN )
        eq2.set_color_by_tex_to_color_map( acolors )
        for i in eq2:
            self.play( Write( i ) )
            self.wait( 2 )
        self.play( FadeOut( eq2 ) )

        eq3 = MathTex( concat( l.lr( invu, vecu, big = 2), '&=', vecu, l.frac( vecu, uu ), l.newline ),
                       concat( '&=', l.frac( uu, uu ), l.newline ),
                       concat( '&= 1', l.newline ) )
        eq3.move_to( eq, DOWN )
        eq3.shift( 4 * DOWN )
        eq3.set_color_by_tex_to_color_map( acolors )
        for i in eq3:
            self.play( Write( i ) )
            self.wait( 2 )
        self.play( FadeOut( VGroup( eq3, eq ) ) )
        self.wait( 2 )

        eqx = MathTex( concat( uu, '=', l.dot( vecu, vecu ), '=', l.sq( l.norm( vecu ) ) ) )
        eqx.set_color_by_tex_to_color_map( acolors )
        self.play( Write( eqx ) )
        self.wait( 2 )
        self.play( FadeOut( eqx ) )

        eqy = MathTex( concat( invu, '=', vecu, l.pow( l.norm( vecu ), n = -2 ), '=', hatu, l.pow( l.norm( vecu ), n = -1 ) ) )
        eqy.set_color_by_tex_to_color_map( acolors )
        self.play( Write( eqy ) )
        self.wait( 2 )


# vim: et sw=4 ts=4
