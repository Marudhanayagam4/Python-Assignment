class MultipleFunctions():
    def Subfields():
        lists= ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech processing", "Natural Language Processing"]
        print("Sub-fields in AI are:", end="\n")
    
        for sub in lists :
            print(sub, end="\n")

    def OddEven():
        num = int(input("Enter a number:"))
        if (num%2==0) :
            print(num, end=" is Even number")
            message="Even number"
        else:
            print(num, end=" is Odd number")
            message="Odd number"
        return message

    def percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        
        Percentage= Total/5
        print("Subject1:",Subject1)
        print("Subject2:",Subject2)
        print("Subject3:",Subject3)
        print("Subject4:",Subject4)
        print("Subject5:",Subject5)
        print("Total:",Total)
        print("Percentage:",Percentage)

    def triangle():
        Height=float(input("Height:"))
        Breadth=float(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area= (Height*Breadth)/2
        print("Area of Triangle:",Area)
        
        Height1=float(input("Height1:"))
        Height2=float(input("Height2:"))
        Breadth=float(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle:",perimeter)

    def Eligible() :
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if(gender=="Male" or gender=="male"):
            if(age<21) :
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
            else:
                print("ELIGIBLE")
                message= "ELIGIBLE"
        else:
            if(age<18):
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
            else:
                print("ELIGIBLE")
                message= "ELIGIBLE"
        return message
