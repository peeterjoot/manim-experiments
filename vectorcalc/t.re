
# run replacements of peeters_macros.sty elements:
#
# perl -p -i ./t.re filename

s/\\spacegrad/\\boldsymbol{\\nabla}/g;
s/\\B(.)/{{ \\mathbf{$1} }}/g;
s/\\cross/\\times/g;
