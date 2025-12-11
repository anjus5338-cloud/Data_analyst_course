data = [10,20,30,40,50,5,60]
#Find second largest
#Find second smallest
max = 0
for i in data:
    if i > max:
        max = i
print(max)

min = data[0]
for i in data:
    if i < min:
        min = i
print(min)

ss = data[0]
min = 5
for i in data:
    if i < min and i > ss:
        ss = i
print(ss)

sl = 0
max = 60
for i in data:
    if i < max and i > sl:
        sl = i
print(sl)

data = [10,20,10,30,50,70,90,80]
#average
avg = 0
sum = 0
len = 0
for i in data:
    len += 1
    sum += 1
avg = sum/len
print(avg)

#max
max = 0 
for i in data:
    if i > max:
        max = i
print(max)
#min
min  = data[0]
for i in data:
    if i < min:
        min = i
print(min)
#count the frequency
count = 0
data_2 = {}
for i in data:
    if i in data_2:
        data_2[i] += 1  
    else:
        data_2[i] = 1 
print(data_2)
    




        


        
