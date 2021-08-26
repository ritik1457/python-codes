unit=int(input(" enter total nuber of units"))
total=0
if(unit<100):
    total=unit*0
elif(100<unit and unit>200):
    total=unit*1
elif(200<unit and unit>300):
    total=unit*2
elif(300<unit and unit>400):
    total=unit*3
else:
    total5=unit*4
print("total amount",total)