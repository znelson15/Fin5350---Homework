def is_nugget_number(candidate, SIX = 6, NINE = 9, TWENTY = 20):
    for i in range(candidate//SIX + 1):
        for j in range(candidate//NINE + 1):
            for k in range(candidate//TWENTY + 1):
                if(candidate == i * SIX + j * NINE + k * TWENTY):
                    return True
        
    return False
      
     
    
## main
sizes = {'S' : 6, 'M' : 9, 'L' : 20}
SIX = 6
#Keep track of how many candidates in a row are nugget numbers
count = 0
#What is the most recent candidate that was not a nugget number
largest = 0
# Is a given number a nugget number
candidate = SIX

#loop until stopping rule met
while count < SIX:
    if(is_nugget_number(candidate)):
        count += 1
    else:
        largest = candidate
        count = 0
    candidate += 1

print("The largest size that you cannot get is: {0}".format(largest))