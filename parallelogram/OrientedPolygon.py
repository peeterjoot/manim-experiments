from helper import *


def OrientedPolygon( *vertices, c0, c1, c2, f, d1, d2, tex, r ):
    n = len( vertices )

    #print( vertices )

    poly = Polygon( *vertices, color = c0 , fill_opacity = f )
    g = VGroup( poly )

    if tex:
        v1 = MathTex( vec_v1 )
        v1.set_color( c1 )
        v2 = MathTex( vec_v2 )
        v2.set_color( c2 )
        g = g + VGroup( v1, v2 )

    for i in range( n ):
        a = Arrow( vertices[ i ], vertices[ ( i + 1 ) % n ], buff = 0, max_tip_length_to_length_ratio = r )
        if i == 0:
            if tex:
                v1.next_to( a, d1 )
            a.set_color( c1 )
        elif i == 1:
            if tex:
                v2.next_to( a, d2 )
            a.set_color( c2 )
        else:
            a.set_color( c0 )
        g.add( a )

    return g


# vim: et sw=4 ts=4
