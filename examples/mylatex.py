def concat(*args, sep=''):
    return sep.join(args)

class latex:
    lbr      = r'\left('
    rbr      = r'\right)'
    nextline = r'\\'
    def mknorm(self, *args, sep = ''):
        return concat( r'\left\lVert{', sep.join(args), r'}\right\rVert' )
    def mknorm2(self, *args, sep = ''):
        return concat( r'{', latex.mknorm( self, sep.join(args) ), r'}^2' )
    def lr(self, *args, sep = ''):
        return concat( r'\left( ', sep.join(args), r' \right)' )
    def lrsq(self, *args, sep = ''):
        return concat( r'{', latex.lr( self, sep.join(args) ), r'}^2' )
    def sq(self, *args, sep = ''):
        return concat( r'{', sep.join(args), r'}^2' )
    def vec(self, v):
        return concat( r'\vec{', v, r'}' )
    def hat(self, v):
        return concat( r'\hat{', v, r'}' )
    def cancel(self, *args, sep = ''):
        return concat( r'\cancel{', sep.join(args), r'}' )
    def text(self, *args, sep = ''):
        return concat( r'\text{', sep.join(args), r'}' )
    def dot(self, *args, sep = r' \cdot '):
        return sep.join(args)
    def wedge(self, *args, sep = r' \wedge '):
        return sep.join(args)
    def gpgrade(self, *args, n=-1, sep = ''):
        return concat( r'{\left\langle{', sep.join(args), r'}\right\rangle}_{', n, '}' )
    def gpgradezero(self, *args, sep = ''):
        return concat( r'\left\langle{', sep.join(args), r'}\right\rangle' )
