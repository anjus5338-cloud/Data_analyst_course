def test(a,b):
    if a>b:
        return a
    else:
        return b
result1 = test(2,5)
result2 = test(10,3)
result3 = test(result1,result2)
print(result1)
print(result2)
print(result3)