
start = int(input("enter the x value : "))
end = int(input("enter the y value : "))
for i in range(start,end+1):
    for j in range(1,11): 
        print(f"{i}X{j} = {i*j}")
    
    print("---------------")
