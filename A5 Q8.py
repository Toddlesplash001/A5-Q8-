random_list = []
for i in range(1,11):
    num = int(input("Enter the integer "))
    random_list.append(num)
positive_number = 0
negative_number = 0
odd_number = 0
even_number = 0
for i in range(0,10):
    if random_list[i]>=0:
        positive_number+=1
    elif random_list[i]<0:
        negative_number+=1
    if random_list[i]%2 == 0:
        even_number+=1
    else:
        odd_number+=1
print("The number of positive integers are",positive_number)
print("The number of negative integers are",negative_number)
print("The number of odd integers are",odd_number)
print("The number of even integers are",even_number)
for i in random_list:
    count = random_list.count(i)
    a = 0
    while a< count:
        random_list.remove(i)
        a =a +1
    print("Number of occurences of",i,"is",count)
    
