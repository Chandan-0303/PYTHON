def Add(n1,n2):
    ans = 0
    ans = n1 + n2
    
    return ans

def main():
    print("Enter first number:")
    num1 = int(input())
    
    print("Enter second number:")
    num2 = int(input())
    
    ret = Add(num1,num2)
    print("Addition is",ret)

if __name__ =="__main__":
    main()