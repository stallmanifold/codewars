import collections as coll


def dbl_linear(n):
    u = 1
    q2, q3 = coll.deque(), coll.deque()

    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        
        if u == q2[0]: 
            u = q2.popleft()
        if u == q3[0]: 
            u = q3.popleft()
        
    return u
