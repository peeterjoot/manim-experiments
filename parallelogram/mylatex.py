def concat( *args, sep = '' ):
    return sep.join( args )

class latex:
    lbr      = r'\left('
    rbr      = r'\right)'
    nextline = r'\\'

    def norm( self, *args, sep = '' ):
        return concat( r'\left\lVert{', sep.join( args ), r'}\right\rVert' )

    def norm2( self, *args, sep = '' ):
        return concat( '{', latex.norm( self, sep.join( args ) ), '}^2' )

    def lr( self, *args, sep = '' ):
        return concat( latex.lbr, sep.join( args ), latex.rbr )

    def lrsq( self, *args, sep = '' ):
        return concat( '{', latex.lr( self, sep.join( args ) ), '}^2' )

    def sq( self, *args, sep = '' ):
        return concat( '{', sep.join( args ), '}^2' )

    def vec( self, v ):
        return concat( r'\vec{', v, '}' )

    def hat( self, v ):
        return concat( r'\hat{', v, '}' )

    def cancel( self, *args, sep = '' ):
        return concat( r'\cancel{', sep.join( args ), '}' )

    def text( self, *args, sep = '' ):
        return concat( r'\text{', sep.join( args ), '}' )

    def dot( self, *args, sep = r' \cdot ' ):
        return sep.join( args )

    def wedge( self, *args, sep = r' \wedge ' ):
        return sep.join( args )

    def add( self, *args, sep = ' + ' ):
        return sep.join( args )

    def mult( self, *args, sep = '' ):
        return sep.join( args )

    def sub( self, *args, sep = ' - ' ):
        return sep.join( args )

    def neg( self, *args, sep = '' ):
        return concat( '-', sep.join( args ) )

    def underbrace( self, *args, helptext = '', sep = '' ):
        return concat( r'\underbrace{', sep.join( args ), '}_{', helptext, '}' )

    def gpgrade( self, *args, n = -1, sep = '' ):
        return concat( r'{\left\langle{', sep.join( args ), r'}\right\rangle}_{', n, '}' )

    def gpgradezero( self, *args, sep = '' ):
        return concat( r'\left\langle{', sep.join( args ), r'}\right\rangle' )

    def Proj( self, u, v, op = 'Proj' ):
        return concat( '{', latex.text( self, op ), '}_{', u, '}', latex.lr( self, v ) )

    def Rej( self, u, v):
        return latex.Proj( self, u, v, op = 'Rej' )
