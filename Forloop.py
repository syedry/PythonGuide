values=[20,18,99,51,10]
number=0
sum=0
product=1
for value in values:
    sum+=value
    number+=1
print("1) Sum = "+str(sum)+" and average = "+str(sum/number))

for x in range(1,10):
    product*=x
print("2) Product is "+str(product))

print("3) Intervals are :")
for x in range(0,101,10):
    interval=x
    print(interval)