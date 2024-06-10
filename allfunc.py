class func():
    def displayai():
     list=['Machine Learning','Neural Networks','Vision Robotics','Speech Processing','Natural Language Processing']
     print('Sub-fields in AI are:')  
     for i in list:
        print(i) 

    def oddreven():
      num=int(input("enter the number:")) 
      if num%2==0:
        print('number is even')
       
      else:
        print("number is odd")

    def eligible():
        gender=str(input("enter your gender"))
        age=int(input("enter your age"))
        if gender.lower()=='male' and age>=21:
            print("Eligible for marriage")
        elif gender.lower()=='female' and age>=18:
            print("Eligible for marriage")
        else:
            print("not eligible for marriage")

    def percentage():
        sub1=int(input("subject 1 :"))
        sub2=int(input("subject 2 :"))
        sub3=int(input("subject 3 :"))
        sub4=int(input("subject 4 :"))
        sub5=int(input("subject 5 :"))
        print("total",sub1+sub2+sub3+sub4+sub5)
        perce=((sub1+sub2+sub3+sub4+sub5)/500)*100
        print("your percentage is:",perce) 
     
    def peri():
        h=int(input("height:"))
        b=int(input("breadth:"))
        print('Area formula: (Height*Breadth)/2')
        area=(h*b)/2
        print('area of a triangle:',area)
        h1=int(input("height1:"))  
        h2=int(input("height2:"))  
        b1=int(input("breadth1:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=h1+h2+b1
        print("perimeter of triangle:",perimeter)