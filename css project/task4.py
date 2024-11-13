i = 1 # initializing this variable with a value 1, so that we can use it as condition for while loop

while i < 3 : # this while loop will run as long as i is less then 3, which means 2 times
    print(i) # print the vale of i in each iteration
    i = i + 1 #increasing the value of i by 1
else: # when the condition of while loop will become false then this else block will execute
    print(0) # prints 0

''' explanation : at the begeing the vale of i is 1, while loop checks the condition if 1 is less then 3,which
 is true of at first, so it will print 1 then the vale of i will increse by one to 2,the loop will check the 
 codition again, which will be true agai and it will print 2 because the vale of i is now 2 then then vale of i will 
 again increase by one and become 3, but this time thw condtion of while loop will bw false, becase 3 is not less 
 then 3, hence the while loop will not run again and else block will execute and will print 0. so te expected 
 outcome will be 
 1
 2 
 0 '''