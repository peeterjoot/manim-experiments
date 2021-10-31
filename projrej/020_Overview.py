from helper import *

class Overview( Scene ):
    def construct( self ):
        blist = BulletedList( "Multiplication by one on the left,",
                              "Multiplication by one on the right,",
                              "Conventional vector algegra equivalents,",
                              "Show that projection and rejection are perpendicular,",
                              "Show that the rejection multivector has no grade three components.",
                              height = 2 )
        for item in blist:
            self.play( Write( item ) )

        self.wait( )


# vim: et sw=4 ts=4
