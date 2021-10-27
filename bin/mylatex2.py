def concat( *args, sep = '' ):
    return sep.join( args )

class latex:
    # these used to have \left \right's in them, but that causes havoc with manim's colorizer
    # will probably have to adjust with a 'big' command line option instead:
    lbr     = r'('
    rbr     = r')'
    Bigl    = r'\Bigl'
    Bigr    = r'\Bigr'
    lgr     = r'\langle'
    rgr     = r'\rangle'

    newline = r'\\'

    def doublebr( self, *args, sep = '' ):
        return concat( '{{ ', sep.join( args ), ' }}' )

    def norm( self, *args, sep = '' ):
        return concat( r'\lVert{ ', sep.join( args ), r' }\rVert' )

    def norm2( self, *args, sep = '' ):
        return concat( '{ ', latex.norm( self, sep.join( args ) ), ' }^2' )

    def lr( self, *args, sep = '', big = 0 ):
        if big:
            return concat( r'\Bigl( ', sep.join( args ), r' \Bigr)' )
        else:
            return concat( '( ', sep.join( args ), ' )' )

    def setlr( self, *args, sep = ',' ):
        return concat( r'\{ ', sep.join( args ), r' \}' )

    def lrsq( self, *args, big = 0, sep = '' ):
        return concat( latex.lr( self, sep.join( args ), big = big ), '{}^2' )

    def sq( self, *args, sep = '' ):
        return concat( sep.join( args ), '{}^2' )

    def frac( self, num, den ):
        return concat( ' { ', num, r' \over ', den, ' } ' )

    def vec( self, v ):
        return concat( r'\mathbf{', v, '}' )

    def hat( self, v ):
        return concat( r'\mathbf{\hat{', v, '} }' )
        #if v[-1] == '}':
        #    return concat( r'\hat{', v, ' }' )
        #else:
        #    return concat( r'\hat{', v, '}' )

    def cancel( self, *args, sep = '' ):
        return concat( r'\cancel{ ', sep.join( args ), ' }' )

    def text( self, *args, sep = '' ):
        return concat( r'\text{', sep.join( args ), '}' )

    def dot( self, *args, sep = r' \cdot ' ):
        return sep.join( args )

    def det22( self, a, b, c, d ):
        return concat( r'\begin{vmatrix} ', a, ' & ', b, r' \\ ', c, '&', d, r'\end{vmatrix}' )

    def wedge( self, *args, sep = r' \wedge ' ):
        return sep.join( args )

    def cross( self, *args, sep = r' \times ' ):
        return sep.join( args )

    def add( self, *args, sep = ' + ' ):
        return sep.join( args )

    def mult( self, *args, sep = '' ):
        return sep.join( args )

    def sub( self, *args, sep = ' - ' ):
        return sep.join( args )

    def neg( self, *args, sep = '' ):
        return concat( '-', sep.join( args ) )

    def power( self, *args, n='1', sep = '' ):
        return concat( '{ ', sep.join( args ), ' }^{ ', pow, ' }' )

    def inv( self, *args, sep = '' ):
        return concat( r' { 1 \over ', sep.join( args ), ' } ' )

    def underbrace( self, *args, helptext = '', sep = '' ):
        return concat( r'\underbrace{ ', sep.join( args ), ' }_{ ', helptext, ' }' )

    def gpgrade( self, *args, n = -1, sep = '' ):
        return concat( r'{ \langle{ ', sep.join( args ), r' }\rangle }_{ ', str(n), ' }' )

    def gpgradezero( self, *args, sep = '' ):
        return concat( r'\langle{ ', sep.join( args ), r' }\rangle' )

    def gpgradeone( self, *args, sep = '' ):
        return latex.gpgrade( self, sep.join( args ), n = 1 )

    def gpgradetwo( self, *args, sep = '' ):
        return latex.gpgrade( self, sep.join( args ), n = 2 )

    def Proj( self, u, v, op = 'Proj' ):
        return concat( '{ ', latex.text( self, op ), ' }_{ ', u, ' }', latex.lr( self, v ) )

    def Rej( self, u, v):
        return latex.Proj( self, u, v, op = 'Rej' )

# vim: et sw=4 ts=4
