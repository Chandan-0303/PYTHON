def Display(num):
    for i in range(num):
        print("* ",end=" ")
    
def main():
    print("Enter number : ")
    value = int(input())
    
    Display(value)  
     
if __name__ =="__main__":
    main()