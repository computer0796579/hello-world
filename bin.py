def div_by_two(n):
    """Return n // 2 and n % 2."""
    return n // 2, n % 2

def bin_v1(n):
    """Convert a number to the binary string."""
    q, r = div_by_two(n)
    s = []
    s.append(r)
    while q > 0:
        q, r = div_by_two(q)
        s.append(r)
    for _ in s[::-1]:
        print(_, end='')
