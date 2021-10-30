from helper import *

class WedgeToDet( Scene ):
    def construct( self ):
        eq = MathTex( concat( r'\text{Let}\,', vecu, '= \sum_{i = 1}^N u_i \mathbf{e}_i, \quad ', vecv, '= \sum_{i = 1}^N v_i \mathbf{e}_i' ) )
        eq.set_color_by_tex_to_color_map( acolors )
        for item in eq:
            self.play( Write( item ) )
        self.wait( )
        self.play( FadeOut( eq ) )

        icolors = { 'i': RED, 'j': BLUE }
        nocolors = { }
        eq2 = MathTex( uwedgev, ' {=} ',
                       l.wedge( l.lr( r'\sum_{ {{i}} = 1}^N u_{{i}} \mathbf{e}_{{i}}', big = 2 ), l.lr( r'\sum_{ {{j}} = 1}^N v_{{i}} \mathbf{e}_{{j}}', big = 2 ) ) )
        eq2.shift( 2 * UP )
        eq2.set_color_by_tex_to_color_map( acolors )
        for item in eq2:
            self.play( Write( item ) )
        self.wait( )

        eq3 = MathTex( r' {=} \sum_{ 1 \le {{i}} , {{j}} \le N} u_{{i}} v_{{j}}', l.lr( r'\mathbf{e}_{{i}} \wedge \mathbf{e}_{{j}}' ) )
        write_aligned( self, eq2, eq3, 1.5 * DOWN, icolors, '{=}' )
        self.wait( )

        eq4 = MathTex( r' {=} \sum_{ {{i}} \ne {{j}} } u_{{i}} v_{{j}}', l.lr( r'\mathbf{e}_{{i}} \wedge \mathbf{e}_{{j}}' ) )
        tx_aligned( self, eq3, eq4, 0.2 * DOWN, icolors, '{=}' )
        self.wait( )

        eq5 = MathTex( r' {=} \sum_{ {{i}} \ne {{j}} } u_{{i}} v_{{j}}', r'\mathbf{e}_{{i}} \mathbf{e}_{{j}}' )
        tx_aligned( self, eq4, eq5, 0.25 * DOWN, icolors, '{=}' )
        self.wait( )

        eq6a = MathTex(  ' {=} ', l.mult( r' \sum_{ {{i}} < {{j}} } u_{{i}} v_{{j}}', r'\mathbf{e}_{{i}} \mathbf{e}_{{j}}' ), '+' )
        eq6b = MathTex(           l.mult( r' \sum_{ {{i}} > {{j}} } u_{{i}} v_{{j}}', r'\mathbf{e}_{{i}} \mathbf{e}_{{j}}' ) )
        eq6c = MathTex(           l.mult( r' \sum_{ {{j}} > {{i}} } u_{{j}} v_{{i}}', r'\mathbf{e}_{{j}} \mathbf{e}_{{i}}' ) )
        g = VGroup( eq6a, eq6b )
        where = eq5.get_part_by_tex( '{=}' )
        eq6a.move_to( where, LEFT )
        eq6a.shift( 0.2 * DOWN )
        eq6b.next_to( eq6a, RIGHT )
        eq6a.set_color_by_tex_to_color_map( icolors )
        eq6b.set_color_by_tex_to_color_map( icolors )
        eq6c.set_color_by_tex_to_color_map( icolors )
        eq6c.move_to( eq6b )
        self.play( ReplacementTransform( eq5, g ) )
        self.wait( )
        self.play( ReplacementTransform( eq6b, eq6c ) )
        self.wait( )

        eq7a = MathTex( r' {=} \sum_{ {{i}} < {{j}} } ( u_{{i}} v_{{j}}', r'\mathbf{e}_{{i}} \mathbf{e}_{{j}} + u_{{j}} v_{{i}}', r'\mathbf{e}_{{j}} \mathbf{e}_{{i}} )' )
        where = eq6a.get_part_by_tex( '{=}' )
        eq7a.move_to( where, LEFT )
        eq7a.shift( 0.2 * DOWN )
        eq7a.set_color_by_tex_to_color_map( icolors )
        self.play( ReplacementTransform( VGroup( eq6a, eq6c ), eq7a ) )
        self.wait( )

        eq7b = MathTex( r' {=} \sum_{ {{i}} < {{j}} } ( u_{{i}} v_{{j}} - u_{{j}} v_{{i}} )', r'\mathbf{e}_{{i}} \mathbf{e}_{{j}}' )
        tx_aligned( self, eq7a, eq7b, 0.2 * DOWN, icolors, '{=}' )
        self.wait( )

        eq8 = MathTex( r' {=} \sum_{ i < j } \begin{vmatrix} u_i & v_i \\ u_j & v_j \end{vmatrix} \mathbf{e}_i \mathbf{e}_j' )
        write_aligned( self, eq7b, eq8, 1.5 * DOWN, nocolors, '{=}' )
        self.wait( )


# vim: et sw=4 ts=4
