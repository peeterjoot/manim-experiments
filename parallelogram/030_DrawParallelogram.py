from helper import *

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram( Scene ):
    def construct( self ):
        o = np.array( [ -2, -2, 0 ] )
        p1 = np.array( [ 3, 1, 0 ] ) # u
        p2 = np.array( [ 1, 3, 0 ] ) # v
        op1 = o + p1
        op2 = o + p2
        op3 = o + p1 + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED ) # u
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW ) # v

        v1l = MathTex( vecu )
        v2l = MathTex( vecv )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v1l.shift( - 0.3 * p1 )
        v2l.next_to( v2, UP )
        v2l.shift( - 0.3 * p2 )
        v2l.set_color( YELLOW )

        p1cap = p1/ np.linalg.norm( p1 )
        proj = np.dot( p2, p1cap ) * p1cap

        rej = p2 - proj

        v1g = VGroup( v1, v1l )
        v2g = VGroup( v2, v2l )

        v1p = Arrow( start = op2, end = op3, buff = 0, color = RED ) # u'
        v2p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW ) # v'
        parallelogram = [ o, op1, op3, op2 ]
        poly = Polygon( *parallelogram, color = PURPLE, fill_opacity = 0.5 )

        cut = op1 + rej
        recttop = cut - p1
        dashrej = DashedLine( start = op1, end = cut, color = BLUE )
        dashtop = DashedLine( start = cut, end = recttop )
        dashside = DashedLine( start = recttop, end = o, color = BLUE )

        self.play( AnimationGroup( Write( v1g ) ) )
        self.play( AnimationGroup( Write( v2g ) ) )
        self.wait( )
        v1c = v1.copy( )
        v2c = v2.copy( )
        self.add( v1c )
        self.add( v2c )
        self.play( ReplacementTransform( v1c, v1p ) )
        self.wait( )
        self.play( ReplacementTransform( v2c, v2p ) )
        self.wait( 2 )
        # audio: 08:00: +08s

        # https://stackoverflow.com/a/69668382/189270
        poly.set_z_index( v1.z_index - 1 )
        self.play( FadeIn( poly ) )
        self.wait( 4 )

        self.play( Write( dashrej ) )
        self.play( Write( dashtop ) )
        self.play( Write( dashside ) )
        self.wait( 2 )
        self.play( FadeOut( poly ) )
        rectpoints = [ o, op1, op1 + rej, o + rej ]
        rect = Polygon( *rectpoints, color = PURPLE, fill_opacity = 0.5 )
        rect.set_z_index( v1.z_index - 1 )
        self.play( FadeIn( rect ) )
        self.wait( 1 )
        # audio: 23:00: +15s

        self.play( FadeOut( rect ) )
        move = ( -4, 1, 0 )
        a = VGroup( dashrej, dashtop, dashside, v1, v1l, v2, v2l, v1p, v2p ) # , poly
        self.play( a.animate.shift( move ) )
        self.wait( 1 )

        squ        = l.norm2( vecu )
        sqv        = l.norm2( vecv )
        vdotuhatsq = l.lrsq( l.dot( vecv, hatu ) )
        rej        = l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) )

        eq2 = MathTex( l.text( 'base' ), r'& = \Vert', vecu, concat( r'\Vert', l.newline ),
                       l.text( 'height' ), '& = ', concat( l.norm( rej ), l.newline ) )
        eq2[0].set_color( RED )
        eq2[1].set_color( RED )
        eq2[2].set_color( RED )
        eq2[3].set_color( RED )
        eq2[4].set_color( GREEN )
        eq2[5].set_color( GREEN )
        eq2[6].set_color( GREEN )

        vdotuhatsq_dist = l.lrsq( l.dot( vecv, l.lr( normu, hatu ) ) )
        eq = MathTex( l.text( 'Area' ), ' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline, # [0,5]
                      concat( l.sq( l.text( 'Area' ) ), ' &= ', squ, l.norm2( rej ), l.newline ), # 1 + 6
                      concat( '&= ', squ ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2 + 6, 3 + 6
                      concat( '&= ', squ ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4 + 6, 5 + 6
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.mult( squ, vdotuhatsq ) ), l.newline ), # 6 + 6
                      concat( '&= ', l.sub( l.mult( squ, sqv ), vdotuhatsq_dist ), l.newline ), # 7 + 6
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( vdotu ) ), l.newline ) # 8 + 6
                    )
        eq[0].set_color( BLUE )
        eq[2].set_color( RED )
        eq[4].set_color( GREEN )

        oproj = o + proj
        vproj = Arrow( start = o, end = oproj, color = PURPLE, buff = 0 )
        vproj.shift( move )
        vprojl = MathTex( concat( l.lr( l.dot( vecv, hatu ) ), hatu ) )
        vprojl.set_color( PURPLE )
        vprojl.next_to( vproj, DOWN )
        vprojl.shift( 0.2 * ( UP + RIGHT ) )

        vrej = Arrow( start = oproj, end = op2, color = GREEN, buff = 0 )
        vrej.shift( move )
        vrejl = MathTex( concat( vecv, ' - ', l.lr( l.dot( vecv, hatu ) ), hatu ) )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, RIGHT )
        vrejl.shift( 2.0 * UP + 1.5 * LEFT )
        vrejl.shift( ( -0.5, 0, 0 ) )

        self.play( Write( VGroup( vproj, vprojl ) ) )
        self.wait( )
        self.play( Write( VGroup( vrej, vrejl ) ) )
        self.wait( )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        self.play( Write( eq2 ) )
        self.wait( 4 )
        # audio: 35:00: +12s

        eq.shift( 2 * DOWN + 2.4 * RIGHT )
        self.play( AnimationGroup( Write( eq[ 0 ] ), Write( eq[ 1 ] ), Write( eq[ 2 ] ), Write( eq[ 3 ] ), Write( eq[ 4 ] ), Write( eq[ 5 ] ) ) )
        self.wait( 2 )

        ii = 6 - 1
        for i in range( 1 + ii, 4 + ii ):
            self.play( Write( eq[ i ] ) )
            self.wait( 2 )
        self.wait( 2 )
        eq[ 5 + ii ].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[ 3 + ii ], eq[ 5 + ii ] ) )
        self.wait( 3 )

        i = 6 + ii
        eq[ i ].shift( 1.1 * UP )
        self.play( Write( eq[ i ] ) )
        self.wait( 3 )

        i = 7 + ii
        eq[ i ].shift( 1.95 * UP )
        self.play( ReplacementTransform( eq[ i - 1 ], eq[ i ] ) )
        self.wait( 3 )

        i = 8 + ii
        eq[ i ].shift( 2.8 * UP )
        self.play( ReplacementTransform( eq[ i - 1 ], eq[ i ] ) )
        self.wait( 3 )


# vim: et sw=4 ts=4
