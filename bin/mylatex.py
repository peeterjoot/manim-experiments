def concat( *args, sep = '' ):
    return sep.join( args )

class latex:
    lbr     = r'\left('
    rbr     = r'\right)'
    Bigl    = r'\Bigl'
    Bigr    = r'\Bigr'
    lgr     = r'\langle'
    rgr     = r'\rangle'
    newline = r'\\'

    def doublebr( self, *args, sep = '' ):
        return concat( '{{ ', sep.join( args ), ' }}' )

    def norm( self, *args, sep = '' ):
        return concat( r'\left\lVert{', sep.join( args ), r'}\right\rVert' )

    def norm2( self, *args, sep = '' ):
        return concat( '{', latex.norm( self, sep.join( args ) ), '}^2' )

    def lr( self, *args, sep = '' ):
        return concat( latex.lbr, sep.join( args ), latex.rbr )

    def setlr( self, *args, sep = ',' ):
        return concat( r'\left\{ ', sep.join( args ), r'\right\}' )

    def lrsq( self, *args, sep = '' ):
        return concat( '{', latex.lr( self, sep.join( args ) ), '}^2' )

    def sq( self, *args, sep = '' ):
        return concat( '{', sep.join( args ), '}^2' )

    def frac( self, num, den ):
        return concat( r'\frac{ ', num, ' }{ ', den, ' }' )

    def vec( self, v ):
        #return concat( r'\vec{', v, '}' )
        return concat( r'\mathbf{', v, '}' )

    def hat( self, v ):
        return concat( r'\hat{ \mathbf{', v, '} }' )

    def cancel( self, *args, sep = '' ):
        return concat( r'\cancel{', sep.join( args ), '}' )

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
        return concat( '{', sep.join( args ), '}^{', pow, '}' )

    def inv( self, *args, sep = '' ):
        return concat( r'\frac{1}{ ', sep.join( args ), ' }' )

    def underbrace( self, *args, helptext = '', sep = '' ):
        return concat( r'\underbrace{', sep.join( args ), '}_{', helptext, '}' )

    def gpgrade( self, *args, n = -1, sep = '' ):
        return concat( r'{\left\langle{', sep.join( args ), r'}\right\rangle}_{', str(n), '}' )

    def gpgradezero( self, *args, sep = '' ):
        return concat( r'\left\langle{', sep.join( args ), r'}\right\rangle' )

    def gpgradeone( self, *args, sep = '' ):
        return concat( r'{ \left\langle{', sep.join( args ), r'}\right\rangle }_{1}' )

    def gpgradetwo( self, *args, sep = '' ):
        return concat( r'{ \left\langle{', sep.join( args ), r'}\right\rangle }_{2}' )

    def Proj( self, u, v, op = 'Proj' ):
        return concat( '{', latex.text( self, op ), '}_{', u, '}', latex.lr( self, v ) )

    def Rej( self, u, v):
        return latex.Proj( self, u, v, op = 'Rej' )
