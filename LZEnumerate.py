from IntegerizedStack import *
from Utility import *
from Node import Node

from copy import deepcopy
import BasicEnumerate

def possible_lz_targets(nt, T):
    # return a list of possible subtrees of t that LZ could reference
    # usually we will want these to be complete subtrees involving more than
    # one rule. Also we will return them in order of frequency, from high to low,
    # so that we preferentially enumerate the high-frequency subtrees
    out = []
    if T is not None:
        for t in T:
            if (t not in out) and (len(t) >= 3) and t.complete and t.nt == nt: ## NOTE: This is extremely inefficient
                out.append(t)
    return out

def from_int(nt, n, cfg, root=None):
    # provide the n'th expansion of nonterminal nt

    # count up the number of terminals
    nterminals = sum([is_terminal_rule(rhs, cfg) for rhs in cfg[nt]])

    # We have a choice here -- we could first cod enonterminals or we could first code previous trees
    # If we do trees first, they will be used earlier in the enumerations, which I guess more interesting
    lz_targets = possible_lz_targets(nt, root)

    if n < len(lz_targets): # we are coding an LZ target
        return deepcopy(lz_targets[n]) # must deepcopy
    elif n-len(lz_targets) < nterminals:
        # check if n is coding a terminal, but remember to subtract len(lz_targets)
        return Node(nt, cfg[nt][n-len(lz_targets)])
    else:
        # Use n to be what's leftover after trying to code lz_targets and terminals
        n = n - len(lz_targets) - nterminals

        # n-nterminals should be an IntegerizedStack where we
        i = IntegerizedStack(n)

        # how many nonterminal rules
        nnonterminals = len(cfg[nt]) - nterminals

        # i first encodoes which *non*-terminal
        which = i.modpop(nnonterminals)
        rhs = cfg[nt][nterminals+which]

        # count up how many on the rhs are nonterminals
        # and divide i into that many integers
        t = i.split(sum( is_nonterminal(r,cfg) for r in rhs))

        # A little subtlety: we have to store whether the node
        # is "complete" so we can know whether to use it in
        # recursive calls
        out = Node(nt)
        out.complete = False
        for r in rhs:
            if is_nonterminal(r,cfg):
                out.children.append(from_int(r, t.pop(0), cfg, root if root is not None else out))
            else:
                out.children.append(r)
        out.complete = True
        return out

if __name__ == "__main__":

    cfg = {
        "S": [("NP", "VP")],
        "NP": [("n",), ("d", "n"), ("d", "AP", "n"), ("NP", "PP")],
        "AP": [("a",), ("a", "AP")],
        "PP": [("p", "NP"), ],
        "VP": [("v",), ("v", "NP"), ("v", "S"), ("VP", "PP")]
    }


    # print(from_int("S", 0))
    for i in range(10000):
        t = from_int("S", i, cfg)
        b = BasicEnumerate.from_int("S", i, cfg)

        # print only the trees that are different (rendered as scheme different)
        if t.as_scheme() != b.as_scheme():
            print(i, t.terminals(), b.terminals(), "\\\\")

        # print(i, b.terminals())
        # for x in b:
        #     print("\t", x)
        # print(i, BasicEnumerate.from_int("S",i))


