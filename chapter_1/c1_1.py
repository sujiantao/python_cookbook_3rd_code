
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(shares)
print(price)
print(year)
print(mon)
print(day)

_, shares, price, _ = data
print(shares)
print(price)

s = "Hello"
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)
