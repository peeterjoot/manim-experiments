from helper import *

class Overview( Scene ):
    def construct( self ):
        blist = BulletedList( "Parallelogram area (visually, algebraic)",
                              "Projection and rejection (geometric algebra)",
                              "Parallelogram area (GA)",
                              "Determinant structure of the wedge product",
                              "Orientation and signed areas",
                              height = 3 )
        for item in blist:
            self.play( Write( item ) )

        self.wait( )


# vim: et sw=4 ts=4
