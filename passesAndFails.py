
#passesAndFails.py

name = ["","","","","",""]
marks = [0,0,0,0,0,0]


print "Please type in 6 names and marks:"
for i in range(6):
    print "Enter name", i + 1,
    name[i] = raw_input()
    print "Enter mark", i + 1,
    marks[i] = input()

print
print "These are the passes and fails:"
print

for i in range(6):
    print name[i],":",
    if marks[i] >= 40:
        print "Pass"
    else:
        print "Fail"

#0utput


#Please type in 6 names and marks:
#Enter name 1 yasmin
#Enter mark 1 90
#Enter name 2 jamie
#Enter mark 2 55
#Enter name 3 Dave
#Enter mark 3 39
#Enter name 4 Imran
#Enter mark 4 41
#Enter name 5 Jenie
#Enter mark 5 40
#Enter name 6 Pat
#Enter mark 6 85

#These are the passes and fails:

#yasmin : Pass
#jamie : Pass
#Dave : Fail
#Imran : Pass
#Jenie : Pass
#Pat : Pass
