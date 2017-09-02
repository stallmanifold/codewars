def duplicate_count(s):
    return len([c for c,k in set(((c, s.lower().count(c)) for c in s.lower() if c.isalnum())) if k != 1])
