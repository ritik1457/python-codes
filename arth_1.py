Name=input("enter name ")
item=int(input("enter number of items "))
rate=int(input("enter rate of item"))
total=item*rate
print("total amount",total)
discount=int(input("enter discount percentage"))
discount_value=(total*(discount/100))
print("discount amount",discount_value)
net_total=total-discount_value
GST=int(input("enter gst percentage "))
GST_value=net_total*(GST/100)
print("gst amount ",GST_value)
grand_total=GST_value+net_total
print("total amount to pay",grand_total)