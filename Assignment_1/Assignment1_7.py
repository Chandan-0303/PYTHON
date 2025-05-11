def Divisible(num):
    if((num % 5)==0):
        print("true")
    else:
        print("false")    
def main():
    print("Enter number : ")
    value = int(input()) 
    
    Divisible(value)  
     
if __name__ =="__main__":
    main()