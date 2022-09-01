list = []
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    l = int(input())

    list.append(l)
print("INPUT",list)
print("Output")
for num in list:
     
    if num >= 0:
        print(num, end = " ")