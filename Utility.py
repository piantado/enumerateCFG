def is_terminal_rule(rhs, cfg):
    # an expansion is terminal if nothing in it appears as a key in cfg
    return all([(x not in cfg) for x in rhs])

def is_nonterminal(x, cfg):
    return isinstance(x,str) and (x in cfg)

# def foldstring(t, sep=" "):
#     if isinstance(t,(list,tuple)):
#         return sep.join([foldstring(x,sep) for x in t])
#     else:
#         return t
#
# def pretty(t):
#     if isinstance(t, (list, tuple)):
#         return "("+("".join([pretty(x) for x in t]))+")"
#     else:
#         return t