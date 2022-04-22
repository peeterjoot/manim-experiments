from manim import *

class Finale( Scene ):
    def construct( self ):
        t = Text( 'Special thanks to' )
        t.move_to( 2.5 * UP + 4 * LEFT )
        t2 = Text( 'sudgylacmoe' )
        t2.next_to( t, DOWN )
        t3 = Text( 'Who generously hand held me through my first Manim baby steps.' ).scale( 0.6 )
        t3.next_to( t2, DOWN )
        t3.shift( 3 * RIGHT )

        t4a = Text( 'Check out:' )
        t4a.set_color( TEAL )
        t4 = Tex("\\verb|http://peeterjoot.com/writing/geometric-algebra-for-electrical-engineers/|").scale( 0.7 )
        t4a.next_to( t3, DOWN )
        t4a.shift( 4 * LEFT )
        t4.next_to( t4a, DOWN )
        t4.shift( 5 * RIGHT )

        g = VGroup( t, t2, t3, t4a, t4 )
        t.set_color( TEAL )
        self.add( g )

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

        self.wait(41)

# vim: et sw=4 ts=4
