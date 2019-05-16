
#ex7_6.py  exercise 7.6

food = ["soup", "chips", "fish", "chicken","sausage"]



priceOf = [0.90, 1.00, 2.70, 2.40, 1.20]


print "Item No Item Item Price" 
for i in range (5):
    print i+1,food[i],priceOf[i]
print
for i in range(4):
    priceIncrease = priceOf[i] * 20/100.0
    priceOf[i] = priceOf[i] + priceIncrease


print "Prices have increased by 20%"
print
print "The new prices are:" 
print
print "Item No  Item Item Price" 
for i in range(5):
    print i+1,food[i],priceOf[i]


 


