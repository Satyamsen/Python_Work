# 3. WAP to take orders from Customer in Restuarant.

# Name of the Customer: 
# Table No.:
# List of Items:
# 1.     Rs.
# 2.     Rs.
# 3.     Rs.
# ....n.

# Order: 
# Qty:
# Would you like to add anything (Y/N): 
# #If Yes,  
# Order:
# Qty:
# #If No,
# Your Total billed amount : Rs. 
# Thank You, for your visit.

n=input("Enter Your Name :")
print("Table No : 10")
l1={"Listofitems":{
    'Paneer Kulche':'190',
    'Biryani':'100',
    'Chole Kulche':'190',
    'Daaltadka':'130'}}

print("List of Items ")

a=l1['Listofitems']
for i in a:
    print(i,"=",a[i])

o=input("enter your order :")
quantity={'1':'Full','2':'half'}
for i in a:
    if i==o:
        for j in quantity:
            print(quantity[j])
    else:
        print("Sorry")
        break
        



            
    