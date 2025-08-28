angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
  
    if 90 in (angle1, angle2, angle3):
        print("This is a Right Triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("This is an Obtuse Triangle")
    else:
        print("This is an Acute Triangle")
else:
    print("These angles do not form a valid triangle")