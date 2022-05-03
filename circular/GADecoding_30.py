from helper import *

class GADecoding_30( Scene ):
    def construct( self ):

        title = Text( 'Exponential unit vector representation.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        req = [ MathTex( concat( hat_r, ' = ', vec_e1, r'\cos\theta + ', vec_e2, r'\sin\theta' ) ),
                MathTex( concat(        ' = ', vec_e1, r'\cos\theta + ', vec_e1, vec_e1, vec_e2, r'\sin\theta' ) ),
                MathTex( concat(        ' = ', vec_e1, l.lr( r'\cos\theta + ', vec_e1, vec_e2, r'\sin\theta' ) ) ),
                MathTex( concat(        ' = ', vec_e1, l.lr( r'\cos\theta + i \sin\theta' ) ) ),
                MathTex( concat(        ' = ', vec_e1, r'e^{i\theta}' ) ) ]

        teq = [ MathTex( concat( hat_theta, ' = ', vec_e2, r'\cos\theta - ', vec_e1, r'\sin\theta' ) ),
                MathTex( concat(            ' = ', vec_e2, r'\cos\theta - ', vec_e2, vec_e2, vec_e1, r'\sin\theta' ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta - ', vec_e2, vec_e1, r'\sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta + ', vec_e1, vec_e2, r'\sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, l.lr( r'\cos\theta + i \sin\theta' ) ) ),
                MathTex( concat(            ' = ', vec_e2, r'e^{i\theta}' ) ) ]

        teq2 = [ MathTex( concat( hat_theta, ' = ', hat_r, 'i' ) ),
                 MathTex( concat(            ' = ', vec_e1, r'e^{i\theta} i' ) ),
                 MathTex( concat(            ' = ', vec_e1, r'i e^{i\theta}' ) ),
                 MathTex( concat(            ' = ', vec_e2, r'e^{i\theta}' ) ) ]

        req[0].shift( UP )
        self.play( Write( req[0] ) )
        self.wait( 4 )
        for i in range(4):
            write_aligned( self, req[i], req[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        req2 = MathTex( concat( hat_r, ' = ', vec_e1, r'e^{i\theta}' ) )
        req2.move_to( 5 * LEFT + 1 * UP )
        self.play( Transform( VGroup(*req), req2 ) )
        self.wait( 4 )

        teq[0].shift( UP )
        self.play( Write( teq[0] ) )
        self.wait( 5 )
        for i in range(5):
            write_aligned( self, teq[i], teq[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        teq3 = MathTex( concat( hat_theta, ' = ', vec_e2, r'e^{i\theta}' ) )
        teq3.move_to( 5 * LEFT + 0 * UP )
        self.play( Transform( VGroup(*teq), teq3 ) )
        self.wait( 4 )

        teq2[0].shift( UP )
        self.play( Write( teq2[0] ) )
        self.wait( 5 )
        for i in range(3):
            write_aligned( self, teq2[i], teq2[i+1], 0.75 * DOWN + 0.00 * LEFT, m = None )
            self.wait( 4 )

        teq4 = MathTex( concat( ' =',  hat_r, 'i' ) )
        teq4.move_to( teq3, RIGHT )
        teq4.shift( RIGHT )
        self.play( AnimationGroup( FadeOut( *teq2 ),
                                   Write( teq4 ) ) )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
