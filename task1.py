my_list = input().split()
a = int(input())
result=[]
for i in range(1, a+1):
     for j in my_list:      
         result.append(f'{j}{i}')
        
print((result))