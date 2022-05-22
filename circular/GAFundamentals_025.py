from helper import *

class GAIntro_030( Scene ):
    def construct( self ):

        title = Text( 'Geometric algebra.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        scale = 0.7
        eq = MathTex( r'\text{Given a dot-product space}\, V = \text{Span} \{\mathbf{x}_i | i \in [1,N]\},' ).scale( scale )
        eq1 = MathTex( r'G(V) = \{M \mid M = a_0\, + a_i\, \mathbf{x}_i + a_{ij}\, \mathbf{x}_i \mathbf{x}_j + a_{ijk}\, \mathbf{x}_i \mathbf{x}_j \mathbf{x}_k + \cdots, a_{\mu\cdots\nu} \cdots \in \mathbb{R}\},' ).scale( scale )
        eq2 = MathTex( r'\text{where, for}\, R,S,T \in G(V)' ).scale( scale )

        eq.shift( 2 * UP )
        self.play( Write( eq ) )
        self.wait( 4 )
        eq1.move_to( eq )
        eq1.shift( scale * DOWN )
        self.play( Write( eq1 ) )
        self.wait( 4 )
        eq2.move_to( eq1 )
        eq2.shift( scale * DOWN )
        self.play( Write( eq2 ) )
        self.wait( 4 )

        table = MathTable( [ [r'\text{Associativity of addition}',	       r'R + (S + T) = (R + S) + T'],
                             [r'\text{Commutativity of addition}',	       r'R + S = S + R'],
                             [r'\text{Multiplication is associative}',       r'R(S T) = (R S) T'],
                             [r'\text{Multiplication is distributive}',      r'T(R + S) = T R + T S'],
                             [r'\text{Contraction axiom}',                   r'{\mathbf{x}_i}^2 = \mathbf{x}_i \cdot \mathbf{x}_i'] ], include_outer_lines = True ).scale( 0.60 )
        table.move_to( eq2 )
        table.shift( 2.25 * DOWN )
        self.play( Write( table ) )
        self.wait( 4 )

        fadeall( self )

# vim: et sw=4 ts=4
