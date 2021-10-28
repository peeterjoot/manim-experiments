from helper import *
from helper2 import *

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

        eq2 = MathTex( concat( t_base, '&=', normu, l.newline ),
                       concat( t_height, '&= ', l.norm( l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) ) ), l.newline ) )
        eq2.set_color_by_tex_to_color_map( acolors )


        self.play( Write( VGroup( vproj, vprojl ) ) )
        self.wait( )
        self.play( Write( VGroup( vrej, vrejl ) ) )
        self.wait( )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        self.play( Write( eq2 ) )
        self.wait( 4 )
        # audio: 35:00: +12s

        ar_a = [ t_area, '=', t_base, r' \times ', t_height ]
        ar_0 = [ l.sq( t_area ), '=', l.sq( t_base ), r' \times ', l.sq( t_height ) ]
        ar_1 = [ '=', squ, l.norm2( l.sub( vecv, l.mult( l.lr( l.dot( vecv, hatu ) ), hatu ) ) ) ]
        ar_2 = [ '=', squ, l.lr( l.add( sqv, l.lrsq( l.dot( vecv, hatu ) ) ), l.neg( l.mult( '2', l.lrsq( l.dot( vecv, hatu ) ) ) ), big = 1 ) ]
        ar_3 = [ '=', squ, l.lr( l.sub( sqv, l.lrsq( l.dot( vecv, hatu ) ) ), big = 1 ) ]
        ar_4 = [ '=', squ, sqv, '-', squ, l.lrsq( l.dot( vecv, hatu ) ) ]
        ar_5 = [ '=',
                r' \lVert {{ \mathbf{u} }} \rVert {}^2 \lVert {{ \mathbf{v} }} \rVert {}^2 - ( {{ \mathbf{v} }} \cdot {{ \mathbf{u} }} ){}^2' ]
        eq_a = MathTex( *ar_a )
        eq_a.set_color_by_tex_to_color_map( acolors )
        eq_a.shift( 1.0 * UP + 0.5 * RIGHT )

        eq_0 = MathTex( *ar_0 )
        eq_0.set_color_by_tex_to_color_map( acolors )
        eq_0.shift( 1.05 * UP + 0.5 * RIGHT )

        eq_1 = MathTex( *ar_1 )
        eq_2 = MathTex( *ar_2 )
        eq_3 = MathTex( *ar_3 )
        eq_4 = MathTex( *ar_4 )
        eq_5 = MathTex( *ar_5 )

        self.play( Write( eq_a ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_a, eq_0 ) )
        self.wait( )
        write_aligned( self, eq_0, eq_1, 0.75 * DOWN, acolors )
        self.wait( )
        write_aligned( self, eq_1, eq_2, 0.75 * DOWN, acolors )
        self.wait( )

        eq_3.move_to( eq_2, LEFT )
        eq_3.set_color_by_tex_to_color_map( acolors )
        eq_4.move_to( eq_3, LEFT )
        eq_4.set_color_by_tex_to_color_map( acolors )
        eq_5.move_to( eq_4, LEFT )
        eq_5.set_color_by_tex_to_color_map( acolors )
        self.play( TransformMatchingTex( eq_2, eq_3 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_3, eq_4 ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_4, eq_5 ) )
        self.wait( )


# vim: et sw=4 ts=4
