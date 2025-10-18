import math

while True:
    c = input("=== GeoCalc Mini ===\n1.Square 2.Rectangle 3.Triangle 4.Circle 5.Trapezoid 6.Cylinder 0.Exit\nChoose: ")
    if c=='0' or c.lower()=='exit':
        print("Goodbye!")
        break
    
    elif c=='1':
        s=float(input("Side: "))
        print(f"Area={s*s:.2f}, Perimeter={4*s:.2f}")
    elif c=='2':
        a=float(input("Length: "))
        b=float(input("Width: "))
        print(f"Area={a*b:.2f}, Perimeter={2*(a+b):.2f}")
    elif c=='3':
        a=float(input("Side a: "))
        b=float(input("Side b: "))
        c_=float(input("Side c: "))
        s=(a+b+c_)/2
        print(f"Area={math.sqrt(s*(s-a)*(s-b)*(s-c_)):.2f}, Perimeter={a+b+c_:.2f}")
    elif c=='4':
        r=float(input("Radius: "))
        print(f"Area={math.pi*r*r:.2f}, Circumference={2*math.pi*r:.2f}")
    elif c=='5':
        a=float(input("Base1: "))
        b=float(input("Base2: "))
        h=float(input("Height: "))
        s1=float(input("Side1: "))
        s2=float(input("Side2: "))
        print(f"Area={((a+b)/2*h):.2f}, Perimeter={a+b+s1+s2:.2f}")
    elif c=='6':
        r=float(input("Radius: "))
        h=float(input("Height: "))
        print(f"Surface Area={2*math.pi*r*(r+h):.2f}, Volume={math.pi*r*r*h:.2f}")
    else:
        print("Invalid choice!")
