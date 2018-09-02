# Arithmetic

'''
+
-
*
/
%
**
'''

a = 10
b = 20

res = a + b

res = a**3

# a = 20.17
# b = 56.98

res = a % b

'''
Assignemnt
=
'''

res = 10 + b

'''
Compound assignment
'''

res += a # res = res + a


res **= 2

# Comparision
'''
<
>
<=
>=
==
!=
'''

res1 = a < b
res2 = a < b

res = res1 + res2

print(res)

#Logical
'''
and
or
not

p   q   and     or      not(p)
0   0   0       0       1
0   1   0       1       1
1   0   0       1       0
1   1   1       1       0

'''

res = not(a < b and b > a)

# res = (a < b) ? 10 : 20