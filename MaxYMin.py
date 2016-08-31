largest, smallest = None, None

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        if largest is None or int(num) > largest:
            largest = int(num)
        if smallest is None or int(num) < smallest:
            smallest = int(num)
    except ValueError:
        print ("")

print ("Invalid input")
print "Maximum is {}".format(largest)
print "Minimum is {}".format(smallest)





		
		

	
	
	
