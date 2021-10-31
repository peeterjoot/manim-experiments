#from sys import *
#sys.path.append(r'../bin')
from concat import *

class latex2:
    # these used to have \left \right's in them, but that causes havoc with manim's colorizer
    # will probably have to adjust with a 'big' command line option instead:
    lbr     = r'('
    rbr     = r')'
    Bigl    = r'\Bigl'
    Bigr    = r'\Bigr'
    Biggl   = r'\Biggl'
    Biggr   = r'\Biggr'
    lgr     = r'\langle'
    rgr     = r'\rangle'

    newline = r'\\'

    def doublebr( self, *args, sep = '' ):
        return concat( '{{ ', sep.join( args ), ' }}' )

    def norm( self, *args, sep = '' ):
        return concat( r'\Vert ', sep.join( args ), r' \Vert' )

    def sqrt( self, *args, sep = '' ):
        return concat( r'\sqrt{', sep.join( args ), '}' )

    def norm2( self, *args, sep = '' ):
        return concat( latex2.norm( self, sep.join( args ) ), ' {}^2' )

    def lr( self, *args, sep = '', big = 0 ):
        if big > 1:
            return concat( latex2.Biggl, '( ', sep.join( args ), ' ', latex2.Biggr, ')' )
        elif big:
            return concat( latex2.Bigl, '( ', sep.join( args ), ' ', latex2.Bigr, ')' )
        else:
            return concat( '( ', sep.join( args ), ' )' )

    def setlr( self, *args, sep = ',', big = 0 ):
        if big > 1:
            return concat( latex2.Biggl, r'\{ ', sep.join( args ), ' ', latex2.Biggr, r'\}' )
        elif big:
            return concat( latex2.Bigl, r'\{ ', sep.join( args ), ' ', latex2.Bigr, r'\}' )
        else:
            return concat( r'\{ ', sep.join( args ), r' \}' )

    def lrsq( self, *args, big = 0, sep = '' ):
        return concat( latex2.lr( self, sep.join( args ), big = big ), '{}^2' )

    def sq( self, *args, sep = '' ):
        return concat( sep.join( args ), '{}^2' )

    def pow( self, *args, n = 0, sep = '' ):
        return concat( sep.join( args ), '{}^{', str(n), '}' )

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
        return concat( r'\begin{vmatrix}', a, '&', b, r'\\', c, '&', d, r'\end{vmatrix}' )

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
        return concat( r'\langle ', sep.join( args ), r' \rangle', '{}_{ ', str(n), ' }' )

    def gpgradezero( self, *args, sep = '', big = 0 ):
        if big > 1:
            return concat( latex2.Biggl, r'\langle ', sep.join( args ), latex2.Biggr, r'\rangle' )
        elif big:
            return concat( latex2.Bigl, r'\langle ', sep.join( args ), latex2.Bigr, r'\rangle' )
        else:
            return concat( r'\langle ', sep.join( args ), r' \rangle' )

    def gpgradeone( self, *args, sep = '' ):
        return latex2.gpgrade( self, sep.join( args ), n = 1 )

    def gpgradetwo( self, *args, sep = '' ):
        return latex2.gpgrade( self, sep.join( args ), n = 2 )

    def Proj( self, u, v, op = 'Proj' ):
        return concat( '{ ', latex2.text( self, op ), ' }_{ ', u, ' }', latex2.lr( self, v ) )

    def Rej( self, u, v):
        return latex2.Proj( self, u, v, op = 'Rej' )

# vim: et sw=4 ts=4
