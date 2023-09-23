from IntegerizedStack import *
from Utility import *
from Node import *

def from_int(nt, n, cfg):
    # provide the n'th expansion of nonterminal nt

    # count up the number of terminals
    nterminals = sum([is_terminal_rule(rhs, cfg) for rhs in cfg[nt]])

    # check if n is coding a terminal
    if n < nterminals:
        return Node(nt, cfg[nt][n])
    else:
        # n-nterminals should be an IntegerizedStack where we
        # uppop the children
        i = IntegerizedStack(n - nterminals)

        # how many nonterminal rules
        nnonterminals = len(cfg[nt]) - nterminals

        # i first encodoes which *non*-terminal
        which = i.modpop(nnonterminals)
        #print("#", nt, n, nterminals, nnonterminals, which, cfg[nt])
        rhs = cfg[nt][nterminals+which]

        # count up how many on the rhs are nonterminals
        # and divide i into that many integers
        t = i.split(sum( is_nonterminal(r,cfg) for r in rhs))

        # now we can expand all of the children
        children = []
        for r in rhs:
            if is_nonterminal(r,cfg):
                children.append(from_int(r,t.pop(0), cfg))
            else:
                children.append(Node(r))
        return Node(nt, children)

if __name__ == "__main__":

    ## NOTE: that in cfg, the terminal rules must be ordered first
    # cfg = {
    #     "S": [("o"), ("S", "S")]
    # }
    cfg = {
        "S": [("NP", "VP")],
        "NP": [("n",), ("d", "n"), ("d", "AP", "n"), ("NP", "PP")],
        "AP": [("a",), ("a", "AP")],
        "PP": [("p", "NP"), ],
        "VP": [("v",), ("v", "NP"), ("v", "S"), ("VP", "PP")]
    }
    # cfg = {
    #     "BOOL":   [("<", "NUMBER", "NUMBER"), ("=", "NUMBER", "NUMBER"), ("FORALL", "VAR", "BOOL"), ("NOT", "BOOL"), ("OR", "BOOL", "BOOL")],
    #     "NUMBER": [("0",), ("VAR",), ("S", "NUMBER"), ("+", "NUMBER", "NUMBER"), ("*", "NUMBER", "NUMBER")],
    #     "VAR":    [("x",), ("VAR", "*")]
    # }
    # cfg = {
    #     "S": [("a", "b"), ("a", "S", "b")]
    # }

    unq = set()
    for i in range(100000):
        t = from_int("S", i, cfg)

        tstr = str(t)
        assert(tstr not in unq)
        unq.add(tstr)

        print(i, "&", t.terminals(), "\\\\")
        # print(i, t.as_scheme())

