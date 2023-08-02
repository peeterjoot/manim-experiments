#from manim import *
from helper import *

class Finale_110( Scene ):
    def construct( self ):
        # This is from sudgy.  I had to tweak the alignment since I don't appear to have ManimBanner2() available.
        #banner = ManimBanner2()
        banner = ManimBanner()
        banner.scale(0.3)
        banner.to_edge(DOWN)
        banner.shift(2 * RIGHT + 0.5 * UP)
        self.play(FadeIn(banner))
        made_with = Tex("Made with ")
        made_with.scale(1.5)
        made_with.next_to(banner, 4 * LEFT, buff = 0.3)
        made_with.align_to(banner.M, DOWN)
        url = Tex("\\verb|https://manim.community|")
        url.next_to(VGroup(made_with, banner), DOWN, buff = -0.2)
        url.shift(0.3*RIGHT + 0.25 * DOWN)
        self.play(AnimationGroup(
            AnimationGroup(banner.expand(), Write(made_with)),
            FadeIn(url),
            lag_ratio = 0.5
        ))
        self.wait( 4 )

        rect = RoundedRectangle( corner_radius=0.3, color=PURE_RED, height=1, width=5 )
        rect.set_fill( PURE_RED, opacity=1.0 )
        rect.move_to( 4 * LEFT + 2 * RIGHT )
        sub = Text( 'Subscribe' ).set_color( WHITE )
        sub.move_to( rect )
        g = VGroup( rect, sub )
        self.play( FadeIn( g ) )
        self.play( g.animate.shift(5.0 * RIGHT + 0 * DOWN), run_time=3, rate_func=linear )
        self.play( FadeOut( g ) )
        self.wait( 4 )

        t1 = Text( 'My blog: ' )
        t1.set_color( TEAL )
        t1.shift( 2.00 * UP + 4.70 * LEFT )
        t2 = Tex("\\verb|https://peeterjoot.com/|") #.scale( 0.7 )
        t2.next_to( t1, DOWN )
        t2.shift( 4 * RIGHT )
        self.play( FadeIn( t1, t2 ) )
        self.wait( 4 )

        t3 = Text( 'My book: ' )
        t3.set_color( TEAL )
        t3.shift( 0.00 * UP + 4.70 * LEFT )
        t4 = Text( 'Geometric Algebra for Electrical Engineers' ).scale( 0.8 )
        t4.next_to( t3, RIGHT )
        t5 = Tex("\\verb|https://peeterjoot.com/gaee/|") #.scale( 0.7 )
        t5.next_to( t3, DOWN )
        t5.shift( 4 * RIGHT )

        self.play( FadeIn( t3, t4, t5 ) )
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
