from helper import *

class WedgeChangeOfBasisPartII( Scene ):
    def construct( self ):
        o = 2 * UP + 6 * LEFT
        alpha = math.sqrt(2)
        beta = 1/math.sqrt(2)
        gamma = math.sqrt(6)/2
        a1 = np.array( [ alpha, 0, 0 ] )
        a2 = np.array( [ beta, gamma, 0 ] )
        vf1 = np.array( [ 1, 0, 0 ] )
        vf2 = np.array( [ 0, 1, 0 ] )
        pts = [ o, o + a1, o + a1 + a2, o + a2 ]
        #self.play( FadeIn( p ) )
        self.wait( )

        x1 = Arrow( pts[ 0 ], pts[ 1 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x1.set_color( RED )
        x2 = Arrow( pts[ 1 ], pts[ 2 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x2.set_color( GREEN )
        x3 = Arrow( pts[ 2 ], pts[ 3 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x3.set_color( PURPLE )
        x4 = Arrow( pts[ 3 ], pts[ 0 ], buff = 0, max_tip_length_to_length_ratio = 0.3 )
        x4.set_color( PURPLE )
        poly = Polygon( *pts, color = PURPLE, fill_opacity = 0.5 )

        eq = MathTex( vecu, ' &= ', l.add( vec_e1, vec_e2 ), l.newline,
                      vecv, ' &= ', l.add( vec_e2, vec_e3 ), l.newline )

        ul = MathTex( vecu )
        ul.move_to( o + 1.2 * a1 )
        ul.set_color( RED )
        vl = MathTex( vecv )
        vl.set_color( GREEN )
        vl.move_to( o + 1.1 * (a1 + a2) )
        eg1 = VGroup( ul, x1 )
        eg2 = VGroup( vl, x2 )
        for i in range( 4 ):
            eg1 += eq[i]
            eq[i].set_color( RED )
        for i in range( 4, 8 ):
            eg2 += eq[i]
            eq[i].set_color( GREEN )
        eg3 = VGroup( poly, x3, x4 )

        eq.shift( 5 * LEFT + 0.5 * DOWN )
        self.play( AnimationGroup( Write( eg1 ) ) )
        self.play( AnimationGroup( Write( eg2 ) ) )
        self.play( Write( poly ) )
        self.play( AnimationGroup( Write( VGroup( x1, x2, x3, x4 ) ) ) )

        uv = l.wedge( vecu, vecv )
        f2e = l.dot( hatu, l.frac( uwedgev, l.norm( uwedgev ) ) )
        #              0               1   2       3     4      5                                       6
        eq2 = MathTex( l.text('Let '), vec_f1, ' &= ', hatu, ' = ', l.frac( l.add( vec_e1, vec_e2 ), r'\sqrt{2}' ), l.newline,
                       l.text('Let '), vec_f2, ' &= ', f2e,  ' = ', concat( l.frac('1', r'\sqrt{6}'), l.lr( l.sub( l.add( vec_e1, l.mult( '2', vec_e2 ) ), vec_e1 ) ) ), l.newline )
        #              7               8   9       10    11     12                                      13
        eq2.shift( 2.0 * UP + 2.0 * RIGHT )
        eq2[1].set_color( BLUE )
        eq2[2].set_color( BLUE )
        eq2[3].set_color( BLUE )
        eq2[8].set_color( YELLOW )
        eq2[9].set_color( YELLOW )
        eq2[10].set_color( YELLOW )
        f1g = VGroup( Arrow( start = o, end = o + vf1, buff = 0, color = BLUE ), MathTex( vec_f1 ).set_color( BLUE ).move_to( o + vf1 + 0.3 * DOWN ) )
        f2g = VGroup( Arrow( start = o, end = o + vf2, buff = 0, color = YELLOW ), MathTex( vec_f2 ).set_color( YELLOW ).move_to( o + vf2 + 0.3 * LEFT ) )
        self.play( Write( eq2[0:6] ), Write( f1g ) )
        self.wait( )
        self.play( Write( eq2[7:13] ), Write( f2g ) )
        self.wait( )

        eqp = MathTex( concat( vecu, ' &= ', l.mult( r'\sqrt{2}', vec_f1 ), l.newline ),
                       concat( vecv, ' &= ', l.add( l.mult( r'\frac{\sqrt{2}}{2}', vec_f1 ),
                                                 l.mult( r'\frac{\sqrt{6}}{2}', vec_f2 ) ), l.newline ) )
        eqp[0].set_color( RED )
        eqp[1].set_color( GREEN )
        eqp.move_to( eq )
        eqp.shift( 2 * DOWN + 0.5 * RIGHT )
        self.play( Write( eqp ) )
        self.wait( )

        eq3 = MathTex( concat( uwedgev, ' &= ', l.add( vec_e12, vec_e13, vec_e23 ), l.newline ),
                       concat( l.lrsq( uwedgev ), ' &= - 3', l.newline ),
                       concat( uwedgev, r' &= \sqrt{\frac{2 \times 6}{4}}', vec_f1, vec_f2, l.newline ),
                       concat( l.lrsq( uwedgev ), ' &= - 3', l.newline ) )
        eq3.shift( 1.5 * DOWN + 2 * RIGHT )
        for i in eq3:
            self.play( Write( i ) )
            self.wait( )
        self.wait( 2 )

        self.play( FadeOut( VGroup( eq3, eqp, eq, eq2 ) ) )
        t = Text( 'General wedge diagonalization' )
        b1 = l.dot( vecv, vec_f1 )
        b2 = l.frac( l.norm( uwedgev ), normu )
        eq = MathTex( concat( l.setlr( vec_f1, vec_f2 ), ' &= ', l.setlr( hatu, f2e ), l.newline ),
                      concat( vecu, ' &= ', normu, vec_f1, l.newline ),
                      concat( vecv, ' &= ', l.add( l.mult( l.lr( l.dot( vecv, vec_f1 ) ), vec_f1 ), l.mult( l.frac( l.norm( uwedgev ), normu ), vec_f2 ) ), l.newline ),
                      concat( uwedgev, r'&='),
                      concat( r'\sum_{i < j} ', l.det22( 'u_i', 'v_i', 'u_j', 'v_j' ), r'\mathbf{e}_i \mathbf{e}_j', l.newline ),
                          r'&= ', concat( l.det22( normu, '0', b1, b2 ), vec_f1, vec_f2, l.newline ),
                          r'&= ', concat( l.norm( uwedgev ), vec_f1, vec_f2, l.newline ) )
        t.move_to( 3 * UP + 1 * RIGHT )
        t.set_color( BLUE )
        self.play( Write( t ) )
        eq.shift( 1.25 * DOWN )
        for i in range( 5 ):
            self.play( Write( eq[i] ) )
        self.wait( 2 )
        eq[6].shift( 1.5 * UP )
        self.play( ReplacementTransform( eq[4], eq[6] ) )
        self.wait( 2 )
        eq[8].shift( 3 * UP )
        self.play( ReplacementTransform( eq[6], eq[8] ) )
        self.wait( )


# vim: et sw=4 ts=4
