dSpeed = int(input("what was your average speed in km/h?\n"))
Roadspeed = 60
Roadspeed = int(input("what was the allowed speed on the road?\n"))

if dSpeed>60:
    points = (dSpeed - Roadspeed) //5
    print("your points:" , points)
    
if points>12:
        print("time to go to jail")

else:
    print("ok")

    