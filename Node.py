

class Node:
    def __init__(self, nt, children=None):
        self.nt = nt
        self.children = [] if children is None else children
        self.complete = False # this is a flag we use in generation to see if we are complete yet

    def __str__(self, use_nt=True):
        if len(self.children) == 0:
            return self.nt
        else:
            return "("+self.nt+" "+" ".join(str(n) for n in self.children)+")"

    def as_scheme(self, use_nt=True):
        # similar to __str__ but no nonterminal names
        if len(self.children) == 0:
            return self.nt
        else:
            return "("+" ".join((n.as_scheme() if isinstance(n,Node) else n) for n in self.children)+")"

    def terminals(self,sep=""):
        if len(self.children) == 0:
            return self.nt
        else:
            return sep.join( (x.terminals() if isinstance(x,Node) else str(x)) for x in self.children)

    def __len__(self):
        return 1 + sum(len(x) for x in self.children)

    def __iter__(self):
        yield self
        for x in self.children:
            yield from x

