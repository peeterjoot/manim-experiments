from helper import *

class Overview( Scene ):
    def construct( self ):
        blist = BulletedList( "Multiplication by one on the right.",
                              "Multiplication by one on the left.",
                              height = 3 )
        for item in blist:
            self.play( Write( item ) )

        self.wait( )


# vim: et sw=4 ts=4
