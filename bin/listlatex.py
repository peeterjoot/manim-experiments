# This class has latex construction methods that do not concatenate everything into a single string, but instead produce lists (i.e. with items that can be 
# colored separately)

def concat( *args, sep = '' ):
    return sep.join( args )

class latex:
    leftb     = ( r'( ' )
    rightb    = ( r' )' )
    newline   = ( r'\\' )
    cdot      = ( r' \cdot ' )
    plus      = ( r' + ' )
    minus     = ( r' - ' )
    wedgeop   = ( r' \wedge ' )
    sqop      = ( r'{}^2' )
    rVert     = ( r'\rVert' )
    lVert     = ( r'\lVert' )

    def norm( self, *args ):
        return latex.lVert + args + latex.rVert

    def norm2( self, *args ):
        return latex.norm( self, args ) + latex.sqop

    def lr( self, *args ):
        return (latex.leftb, *args, latex.rightb)

    def lrsq( self, *args ):
        return latex.lr( self, args ) + latex.sqop

    def sq( self, *args ):
        return args + latex.sqop

    def vec( self, v ):
        return ( concat( r'\vec{', v, '}' ) )

    def hat( self, v ):
        return ( concat( r'\hat{', v, '}' ) )

    #def cancel( self, *args, join=False, sep='' ):
    #    if join:
    #        return ( concat( r'\cancel{', sep.join( args ), '}' )
    #    else:
    #        return ( r'\cancel{' ) + args + ( '}' )

    def text( self, *args, sep = '' ):
        return [ concat( r'\text{', sep.join( args ), '}' ) ]

    def binaryop( self, *args, op='BOP' ):
        rc = args[0]
        for it in args[1:]:
            rc = rc + op + it
        return rc

    def unaryoop( self, *args, op='UOP' ):
        return op + args

    def dot( self, *args ):
        return latex.binaryop( self, *args, latex.cdot )

    def wedge( self, *args ):
        return latex.binaryop( self, *args, latex.wedgeop )

    def add( self, *args ):
        return latex.binaryop( self, *args, latex.plus )

    def sub( self, *args ):
        return latex.binaryop( self, *args, latex.minus )

    def neg( self, *a ):
        return latex.unaryop( self, latex.minus )

    #def underightbace( self, *args, helptext = '', sep = '' ):
    #    return concat( r'\underightbace{', sep.join( args ), '}_{', helptext, '}' )
    #def gpgrade( self, *args, n = -1, sep = '' ):
    #    return concat( r'{\left\langle{', sep.join( args ), r'}\right\rangle}_{', n, '}' )
    #def gpgradezero( self, *args, sep = '' ):
    #    return concat( r'\left\langle{', sep.join( args ), r'}\right\rangle' )

    def Proj( self, u, v, op = 'Proj' ):
        return ( r'{\text{Proj}}_', u, '(', v, ')' )

    def Rej( self, u, v):
        return ( r'{\text{Rej}}_', u, '(', v, ')' )
