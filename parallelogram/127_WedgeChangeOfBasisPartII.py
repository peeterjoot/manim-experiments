from helper import *
from helper2 import *

class WedgeChangeOfBasisPartII( Scene ):
    def construct( self ):
        xcolors = { l.hat('u'): BLUE, l.vec('u'): RED, l.vec('v'): YELLOW, concat( l.vec( 'f' ), '_1' ): BLUE, concat( l.vec( 'f' ), '_2' ): ORANGE }

        o = 1.5 * UP + 6 * LEFT
        alpha = math.sqrt(2)
        beta = 1/math.sqrt(2)
        gamma = math.sqrt(6)/2
        a1 = np.array( [ alpha, 0, 0 ] )
        a2 = np.array( [ beta, gamma, 0 ] )
        vf1 = np.array( [ 1, 0, 0 ] )
        vf2 = np.array( [ 0, 1, 0 ] )
        pts = [ o, o + a1, o + a1 + a2, o + a2 ]
        self.wait( )

        x1 = Arrow( pts[ 0 ], pts[ 1 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x1.set_color( RED )
        x2 = Arrow( pts[ 1 ], pts[ 2 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x2.set_color( YELLOW )
        x3 = Arrow( pts[ 2 ], pts[ 3 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x3.set_color( PURPLE )
        x4 = Arrow( pts[ 3 ], pts[ 0 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x4.set_color( PURPLE )
        poly = Polygon( *pts, color = PURPLE, fill_opacity = 0.5 )

        equv1 = MathTex( vecu, ' = ', l.add( vec_e1, vec_e2 ) )
        equv2 = MathTex( vecv, ' = ', l.add( vec_e2, vec_e3 ) )
        equv1.set_color_by_tex_to_color_map( xcolors )
        equv2.set_color_by_tex_to_color_map( xcolors )

        ul = MathTex( vecu )
        ul.move_to( o + 1.2 * a1 )
        ul.set_color( RED )
        vl = MathTex( vecv )
        vl.set_color( YELLOW )
        vl.move_to( o + 1.1 * (a1 + a2) )
        eg1 = VGroup( ul, x1, equv1 )
        eg2 = VGroup( vl, x2, equv2 )
        eg3 = VGroup( poly, x3, x4 )

        equv1.shift( 5 * LEFT + 0.5 * DOWN )
        where = equv1.get_part_by_tex( l.vec('u') )
        equv2.move_to( where, LEFT )
        equv2.shift( 0.75 * DOWN )
        self.play( AnimationGroup( Write( eg1 ) ) )
        self.play( AnimationGroup( Write( eg2 ) ) )
        self.play( Write( poly ) )
        self.play( AnimationGroup( Write( VGroup( x1, x2, x3, x4 ) ) ) )

        vec_f1     = l.doublebr( l.vec( 'f' ), '_1' )
        vec_f2     = l.doublebr( l.vec( 'f' ), '_2' )
        vec_fi     = l.doublebr( l.vec( 'f' ), '_i' )
        vec_fj     = l.doublebr( l.vec( 'f' ), '_j' )

        f1g = VGroup( Arrow( start = o, end = o + vf1, buff = 0, color = BLUE ), MathTex( vec_f1 ).set_color( BLUE ).move_to( o + vf1 + 0.3 * DOWN ) )
        f2g = VGroup( Arrow( start = o, end = o + vf2, buff = 0, color = ORANGE ), MathTex( vec_f2 ).set_color( ORANGE ).move_to( o + vf2 + 0.3 * LEFT ) )
        uv = l.wedge( vecu, vecv )
        f2e = l.dot( hatu, l.frac( uwedgev, l.norm( uwedgev ) ) )
        eq2a = MathTex( l.text('Let '), vec_f1, ' = ', hatu, ' = ', l.frac( l.add( vec_e1, vec_e2 ), r'\sqrt{2}' ) )
        eq2b = MathTex( l.text('Let '), vec_f2, ' = ', f2e,  ' = ', concat( l.frac('1', r'\sqrt{6}'), l.lr( l.sub( l.add( vec_e1, l.mult( '2', vec_e2 ) ), vec_e1 ) ) ) )
        eq2a.shift( 2.0 * UP + 0 * RIGHT )
        eq2a.set_color_by_tex_to_color_map( xcolors )
        self.play( AnimationGroup( Write( eq2a ), Write( f1g ) ) )
        self.wait( )

        where = eq2a.get_part_by_tex( 'Let' )
        eq2b.move_to( where, LEFT )
        eq2b.shift( 1.5 * DOWN )
        eq2b.set_color_by_tex_to_color_map( xcolors )
        self.play( AnimationGroup( Write( eq2b ), Write( f2g ) ) )
        self.wait( )

        eqp1 = MathTex( vecu, r' = \sqrt{2}', vec_f1 )
        write_aligned( self, equv2, eqp1, 0.75 * DOWN, xcolors, l.vec('v') )
        self.wait( )
        eqp2 = MathTex( vecv, r' = ', r'\frac{\sqrt{2}}{2}', vec_f1, r' + \frac{\sqrt{6}}{2}', vec_f2 )
        write_aligned( self, eqp1, eqp2, 1.00 * DOWN, xcolors, l.vec('u') )
        self.wait( )

        self.play( FadeOut( VGroup( eq2a, eq2b ) ) )
        self.wait( )


        eq3a = MathTex( uwedgev, ' = ', l.add( vec_e12, vec_e13, vec_e23 ) )
        eq3b = MathTex( l.lrsq( uwedgev ), ' = ', '- 3' )
        eq3c = MathTex( uwedgev, ' = ', r'\sqrt{\frac{2 \times 6}{4}}', vec_f1, vec_f2 )
        eq3d = MathTex( l.lrsq( uwedgev ), ' = ', '- 3' )
        eq3a.shift( 1.5 * UP + 2 * RIGHT )
        eq3a.set_color_by_tex_to_color_map( xcolors )
        self.play( Write( eq3a ) )
        self.wait( )
        write_aligned( self, eq3a, eq3b, 0.75 * DOWN + 0.6 * LEFT, xcolors, l.vec('u') )
        self.wait( )
        write_aligned( self, eq3b, eq3c, 1.00 * DOWN + 0.4 * RIGHT, xcolors, l.vec('u') )
        self.wait( )
        write_aligned( self, eq3c, eq3d, 0.75 * DOWN + 0.6 * LEFT, xcolors, l.vec('u') )
        self.wait( )

        self.play( FadeOut( VGroup( eq3a, eq3b, eq3c, eq3d, eqp1, eqp2, equv1, equv2 ) ) )
        t = Text( 'General wedge diagonalization' )
        t.move_to( 3 * UP + 1.5 * RIGHT )
        t.set_color( BLUE )
        self.play( Write( t ) )

        equv0 = MathTex( l.text( 'With ' ), l.norm( uwedgev ), r' = \sqrt{ -', l.lrsq( uwedgev ), ' }' ).scale( 0.75 )
        equv0.set_color_by_tex_to_color_map( xcolors )
        equv0.shift( 4.5 * LEFT + 0 * DOWN )
        self.play( Write( equv0 ) )
        self.wait( )

        equv1 = MathTex( l.setlr( vec_f1, vec_f2 ), ' = ', l.setlr( hatu, f2e, big = 2 ) ).scale( 0.75 )
        write_aligned( self, equv0, equv1, 1 * DOWN, xcolors, 'With' )
        self.wait( )

        equv2 = MathTex( vecu, ' = ', normu, vec_f1, r"= \sum {u'}_i", vec_fi ).scale( 0.75 )
        write_aligned( self, equv1, equv2, 1.25 * DOWN, xcolors, l.vec('f') )
        self.wait( )

        equv3 = MathTex( vecv, ' = ', l.add( l.mult( l.lr( l.dot( vecv, vec_f1 ) ), vec_f1 ), l.mult( l.frac( l.norm( uwedgev ), normu ), vec_f2 ) ), r"= \sum {v'}_i", vec_fi  ).scale( 0.75 )
        write_aligned( self, equv2, equv3, 1.00 * DOWN, xcolors, l.vec('u') )
        self.wait( )

        equv2a = MathTex( uwedgev, concat( r'= \sum_{i < j}', l.det22( 'u_i', 'v_i', 'u_j', 'v_j' ) ), r'\mathbf{e}_i \mathbf{e}_j' )
        equv2a.set_color_by_tex_to_color_map( xcolors )
        equv2a.move_to( t, LEFT )
        equv2a.shift( 1.5 * DOWN + 0.5 * RIGHT )
        self.play( Write( equv2a ) )
        self.wait( )

        equv2b = MathTex( concat( r'= \sum_{1 \le i < j \le 2}', l.det22( "u'_i", "v'_i", "u'_j", "v'_j" ) ), vec_fi, vec_fj )
        write_aligned( self, equv2a, equv2b, 1.5 * DOWN, xcolors )
        self.wait( )

        # can't get this to work with the xcolor Manim color splitting:
        #b1 = l.dot( vecv, vec_f1 )
        #xnormu = l.norm( l.vec( 'u' ) )
        #b2 = l.frac( l.norm( uwedgev ), xnormu )
        #equv2b = MathTex( concat( '=', l.det22( xnormu, '0', b1, b2 ), vec_f1, vec_f2 ) )
        #write_aligned( self, equv2a, equv2b, 0.75 * DOWN, xcolors )
        #self.wait( )

        equv2c = MathTex( '=', normu, l.wedge( vec_f1, l.lr( l.add( l.mult( l.lr( l.dot( vecv, vec_f1 ) ), vec_f1 ), l.mult( l.frac( l.norm( uwedgev ), normu ), vec_f2 ) ), big = 2 ) ) )
        write_aligned( self, equv2b, equv2c, 1.5 * DOWN, xcolors )
        self.wait( )

        equv2d = MathTex( concat( '= ', l.norm( uwedgev ), vec_f1, vec_f2 ) )
        tx_aligned( self, equv2c, equv2d, 0 * DOWN, xcolors )
        self.wait( )



# vim: et sw=4 ts=4
