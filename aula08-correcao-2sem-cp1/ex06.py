def swap_ends(t):
    if len(t) < 2:
        return t
    return (t[-1],) + t[1:-1] + (t[0],)

print(swap_ends(('a','b','c','d', 'e')))

