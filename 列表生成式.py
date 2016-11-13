L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [a.upper() for a in L1 if isinstance(a,str)]
print(L2)
