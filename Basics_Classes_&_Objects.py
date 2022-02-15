print('''
01. Arithmatic Programming : Addition, Multiplication, Division, Substraction and Power of Number.
                                                                                                         ''')

class Arithmetic_Operations:

    def add(self):
        a = 10
        b = 20
        print("Addition            : ",a,"+",b,"=",a+b)

    def mul(self):
        a = 10
        b = 20
        print("Multiplication      : ",a,"*",b,"=",a*b)

    def div(self):
        a = 25 
        b = 2
        print("Division in Decimal : ",a,"/",b," =",a/b)
        print("Simple Division     : ",a,"//",b,"=",a//b)

    def sub(self):
        a = 10
        b = 20
        print("Substraction        : ",a,"-",b,"=",a-b)

    def pow(self):
        a = 25
        b = 2
        print(a,"to the power",b,"  : ",a**b)

obj = Arithmetic_Operations()
obj.add()
obj.mul()
obj.div()
obj.sub()
obj.pow()


print('''

02. Python program to calculate the Area of - Triangle, Rectangle, Square and Circle
                                                                                    ''')

class Area:

    def triangle(self):
        b = 10
        h = 12
        print("Area of Triangle  : 0.5 * base * height = 0.5 *",b,"*",h,"=",0.5*b*h)

    def rectangle(self):
        l = 10
        w = 20
        print("Area of Rectangle : length * width      =",l,"*",w,"=",l*w)

    def square(self):
        s = 4
        print("Area of Square    : side * side         =",s,"*",s,"=",s*s)

    def circle(self):
        r = 5
        print("Area of Circle    : pi * r * r          = 3.14 *",r,"*",r,"=",3.14*r*r)


obj1 = Area()
obj1.triangle()
obj1.rectangle()
obj1.square()
obj1.circle()

print('''

03. Python program to calculate Volume of - Cuboid, Cube, Cone & Cylinder.
                                                                                     ''')
class Vol:

    def cuboid(self):
        l = 10
        w = 10
        h = 10
        print("Volume of Cuboid   : length * width * height               =",l,"*",w,"*",h,"=",l*w*h)

    def cube(self):
        s = 5
        print("Volume of Cube     : side * side * side                    =",s,"*",s,"*",s,"=",s**3)

    def cone(self):
        r = 5
        h = 10
        print("Volume of Cone     : pi * radius * radius * ( height \ 3 ) = 3.14 *",r,"*",r,"* (",h,"/ 3 ) =",3.14*(r**2)*(h/3))

    def cylinder(self):
        r = 5
        h = 8
        print("Volume of Cylinder : pi * radius * radius * height         = 3.14 *",r,"*",r,"*",h,"=",3.14*(r**2)*h)

obj2 = Vol()
obj2.cuboid()
obj2.cube()
obj2.cone()
obj2.cylinder()

print('''

04. Python Program to Convert - kilometre to meter & Celcius to Fahrenheit
                                                                            ''')

class conversion:
    def km_to_m(self):
        km = 1
        print(km,"kilometre       = ",km*1000,"meter",)
    
    def Cel_to_Fah(self):
        c = 25
        print(c,"degree celsius = ",( c * 1.8 ) + 32,"degree fahrenheit")

obj3 = conversion()
obj3.km_to_m()
obj3.Cel_to_Fah()

print('''                                                                                       
                                                                                                
05. Python Program to Swap two variables                                                       
                                                                                            ''')
class swap:
    def swap(self):
        x = 25
        y = 50
        print("Before Swapping x =",x,"& y =",y)
        z = x
        x = y
        y = z
        print("After Swapping  x =",x,"& y =",y)

obj4 = swap()
obj4.swap()

print('''

06. Python Program to Reverse Three Digit Number                          
                                                                                ''')
class rev:
    def rev(self):
        num = 123
        rem = num % 10
        num1 = num // 10
        rem1 = num1 % 10
        num2 = num1 // 10
        rev = rem * 100 + rem1 * 10 + num2
        print("Three Digit Number",num,"Reverse to",rev)

obj5 = rev()
obj5.rev()

print('''                                                                                   
                                                                                                
07. Python Program to Calculate ( a + b ) ^ 2  &  ( a - b ) ^ 2                          
                                                                                 ''')
class Expression:
    def exp(self):
        a = 4
        b = 3
        ans1 = ( a**2 + 2*a*b + b**2 )
        print("(",a,"+",b,") ^ 2 =",ans1)
        ans2 = ( a**2 - 2 * a * b + b**2 )
        print("(",a,"-",b,") ^ 2 =",ans2)

obj6 = Expression()
obj6.exp()