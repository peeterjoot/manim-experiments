from mycolors import *

class m020_isotropic( Scene ):
    def construct( self ):

        title = Text( "Isotropic transformations" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        eq0 = [ cMathTex( r"{{ \mathbf{B} }} = \mu {{ \mathbf{H} }}" ),
                cMathTex( r"{{ \mathbf{D} }} = \epsilon {{ \mathbf{E} }}" ),
                cMathTex( r"\eta = \sqrt{\mu \over \epsilon}" ),
                cMathTex( r"c = 1/\sqrt{\mu \epsilon}" ) ]
        eq0[0].shift( 1.50 * UP + 5 * LEFT )
        self.play( Write( eq0[0] ) )
        self.wait( 1 )
        for i in range(1):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 0.60 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 0.40 * LEFT
            write_aligned( self, eq0[i], eq0[i+1], sh, None )
            self.wait( 1 )
        self.wait( 1 )

        eq = [ cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{E} }} = -{{ \mathbf{M} }} - \mu { \partial {{ \mathbf{H} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \times {{ \mathbf{H} }} = {{ \mathbf{J} }} + \epsilon { \partial {{ \mathbf{E} }} \over \partial t } " ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{E} }} = { \rho \over \epsilon }" ),
               cMathTex( r"{{ \boldsymbol{\nabla} }} \cdot {{ \mathbf{H} }} = { \rho_{\mathrm{m}} \over \mu }" ) ]
        eq[0].shift( 1.50 * UP + 0 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 1 )

        for i in range(3):
            sh = 1.00 * DOWN
            if i == 0:
                sh += 0.00 * DOWN + 1.70 * LEFT
            if i == 1:
                sh += 0.00 * DOWN + 1.40 * LEFT
            if i == 2:
                sh += 0.30 * DOWN + 1.40 * LEFT
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 1 )
        #self.play( FadeOut( VGroup( *eq ) ) )
        self.wait( 1 )

        fadeall( self )

# vim: et sw=4 ts=4
