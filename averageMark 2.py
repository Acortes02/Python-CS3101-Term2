
#averageMark.py

marks = [0,0,0,0,0.]
print "Please type in 5 marks:"
for i in range(5):
    print "Enter mark", i+1,
    marks[i] = input()

print "\nThese are the marks you entered\n"

for i in marks:
    print i,
   

total = 0.0

for i in marks:
    total = total + i 

average = total/5
print
print "The average mark is ",average
