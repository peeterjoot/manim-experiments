from manim import *

class Finale_150( Scene ):
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

        t4a = Text( 'My book: ' )

        t4a.set_color( TEAL )
        t4a.shift( 1.00 * UP + 4.70 * LEFT )

        t4b = Text( 'Geometric Algebra for Electrical Engineers' ).scale( 0.8 )
        t4b.next_to( t4a, RIGHT )

        t4 = Tex("\\verb|http://peeterjoot.com/gaee/|") #.scale( 0.7 )
        t4.next_to( t4a, DOWN )
        t4.shift( 4 * RIGHT )

        g = VGroup( t4, t4a, t4b )
        self.play( FadeIn( g ) )
        self.wait( 4 )

# vim: et sw=4 ts=4
