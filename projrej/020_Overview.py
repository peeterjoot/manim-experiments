from helper import *

class Overview( Scene ):
    def construct( self ):
        t = Text( "Outline." )
        t.set_color( BLUE )
        t.shift( 3 * UP )
        self.add( t )

        blist = BulletedList( "Trick: Multiplication by one on the left,",
                              "Multiplication by one on the right,",
                              "Justify the projection and rejection identifications.",
                              "Conventional vector algebra equivalents,",
                              "Show that projection and rejection are perpendicular,",
                              "Show that the rejection multivector has no grade three components.",
                              "Cross product rejection representation in 3D,",
                              "Summary of relationships.",
                              height = 2.5 )
        blist.shift( 0.5 * DOWN )
        for item in blist:
            self.play( Write( item ) )

        self.wait( )


# vim: et sw=4 ts=4
