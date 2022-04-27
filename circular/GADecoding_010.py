from helper import *

class GADecoding_010( Scene ):
    def construct( self ):

        title = Text( 'Unpacking the exponentials.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        eq = [ AcolorsMathTex( concat( vec_e1, vec_e1, ' = ', vec_e2, vec_e2, '= 1' ) ),
               AcolorsMathTex( concat( vec_e1, vec_e2, ' = -', vec_e2, vec_e1 ) ) ]

        eq[0].shift( 1.5 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.40 * LEFT, None )
        self.wait( 5 )

        self.play( FadeOut( *eq ) )

        eq = [ AcolorsMathTex( hat_r, ' = ', vec_e1, r'e^{i\theta}' ),                          # 0
               AcolorsMathTex(        ' = ', vec_e1, l.lr( r'\cos\theta + i \sin\theta' ) ),    # 1
               AcolorsMathTex(        ' = ', vec_e1, r'\cos\theta', '+' ),                      # 2
                   AcolorsMathTex( vec_e1, vec_e1 ),                                            # 3
                   AcolorsMathTex( vec_e2, r'\sin\theta' ) ]                                    # 4

        eq2 = AcolorsMathTex(        ' = ', vec_e1, r'\cos\theta', '+', vec_e2, r'\sin\theta' )

        eq[0].shift( 2 * LEFT + 2 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 4 )
        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.00 * LEFT, None ) # write 1
        self.wait( 4 )
        i = 1
        align_it( self, eq[i], eq[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None, what = '=' )
        eq[3].move_to( eq[2].get_right(), RIGHT )
        eq[3].shift( RIGHT + 0.05 * DOWN )
        eq[4].move_to( eq[3].get_right(), RIGHT )
        eq[4].shift( 1.5 * RIGHT + 0.07 * UP )
        self.play( AnimationGroup( Write( eq[2] ), Write( eq[3] ), Write( eq[4] ) ) )
        self.wait( 4 )
        self.play( Indicate( eq[3] ) )
        self.wait( 4 )
        align_it( self, eq[1], eq2, 0.75 * DOWN + 0.00 * LEFT, m = None, what = '=' )
        self.play( TransformMatchingTex( VGroup( eq[2], eq[3], eq[4] ), eq2 ) )
        self.wait( 4 )

        eq3 = [ AcolorsMathTex( hat_theta, ' = ', hat_r, 'i' ),
                AcolorsMathTex(            ' = ', vec_e1, r'e^{i\theta} i' ),
                AcolorsMathTex(            ' = ', vec_e1, l.lr( r'i \cos\theta - \sin\theta' ) ),
                AcolorsMathTex(            ' = ', vec_e2, r'\cos\theta - ', vec_e1, r'\sin\theta' ) ]

        eq3[0].shift( 2.38 * LEFT + 0.5 * DOWN )
        self.play( Write( eq3[0] ) )
        self.wait( 4 )
        for i in range(3):
            write_aligned( self, eq3[i], eq3[i+1], 0.75 * DOWN + 0.00 * LEFT, None )
            self.wait( 4 )

# vim: et sw=4 ts=4
