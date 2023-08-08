from helper import *

class m80_velocity( Scene ):
    def construct( self ):

        title = Text( 'Application: Kinetic energy.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 10 )

        eq = [ MathTex( concat( r"\mathbf{x}' = r'", hat_r, r"+ r", rhat_prime ) ),
               MathTex( concat( rhat_prime, "=", vec_e3, l.frac( "d", "dt" ), l.lr( r"\cos\theta + j \sin\theta" ) ) ),
               MathTex( concat(             '=', vec_e3, r"j e^{j\theta} \theta' + ", vec_e3, l.frac( 'd j', 'dt' ), r'\sin\theta' ) ),
               MathTex( concat(            r"= \hat{\boldsymbol{\theta}} \theta' + ", vec_e3, vec_e3, vec_e1, r"i e^{i\phi} \phi' \sin\theta" ) ),
               MathTex( concat(            r"= \hat{\boldsymbol{\theta}} \theta' + ", vec_e2, r" e^{i\phi} \phi' \sin\theta" ) ),
               MathTex( concat(            r"= \hat{\boldsymbol{\theta}} \theta' + \hat{\boldsymbol{\phi}} \phi' \sin\theta" ) ) ]

        eq[0].shift( 2 * UP + 0.5 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 10 )

        for i in range(5):
            sh = 1.00 * DOWN + 0.0 * RIGHT
            if i == 1:
                sh += 0.50 * RIGHT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 10 )

        eq2 = [ MathTex( concat( r"\mathbf{x}' = r'", hat_r, r"+ r \hat{\boldsymbol{\theta}} \theta' + r \sin\theta \hat{\boldsymbol{\phi}} \phi' " ) ),
                MathTex( concat( l.frac( "1", "2" ), "m {\mathbf{v}}^2 = ", l.frac( "m", "2" ), l.lr( r"{r'}^2 + r^2 {\theta'}^2 + r^2 \sin^2 \theta {\phi'}^2", big = 1 ) ) ) ]

        eq2[0].shift( 1 * UP )
        self.play( ReplacementTransform( VGroup(*eq), eq2[0] ) )
        self.wait( 10 )

        eq2[1].move_to( eq2[0] ).shift( 2 * DOWN )
        self.play( Write( eq2[1] ) )
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
