show = lambda num: print(num(lambda x: x +1)(0))

n0 = lambda s: lambda z: z
n1 = lambda s: lambda z: s(z)
n2 = lambda s: lambda z: s(s(z))
n3 = lambda s: lambda z: s(s(s(z)))
n4 = lambda s: lambda z: s(s(s(s(z))))
func = lambda x: lambda s: lambda z: x(lambda x: s(s(x)))(z)


n0 = func(n0)
n1 = func(n1)
n2 = func(n2)
n3 = func(n3)
n4 = func(n4)

show(n0)
show(n1)
show(n2)
show(n3)
show(n4)