#list
#divisible by 3 or not

age=(12,20,21,24,15,20)
for i in age:
    if i%3==0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 3")



#Square of even numbers in a list

Newage=[x*2 for x in age if x%2==0]
print("The square of even number in the list:" ,Newage)

#Sum of digits of all EVEN numbers in a list

sum = 0
for i in age:
     if i%2==0:
            print("The even numbers are:",i)
            sum+=i
print("The sum of the even numbers is: ",sum)

#Remove duplicate numbers in a list

print ("The list is: ",age) 

# to remove duplicated from list 
newage = [] 
[newage.append(x) for x in age if x not in newage] 

# printing list after removal 
print ("The list after removing duplicates: ",newage) 
 


#Dictionary


hotel_info={
    "Virat Kohli":"5 November 1988",
    "Umesh Yadav":"25 October 1987",
    "Manish Pandey":"10 September 1989",
    "Rohit Sharma": "30 April 1987",
    "Ravindra Jadeja": "6 December 1988",
    "Hardik Pandya":"11 October 1993"

}

def birthdate(a):
    list=hotel_info.keys()
    if a in list:
         print(hotel_info[a])
    else:
         print("Name not present")


a=input("Enter the name: ")
birthdate(a)



