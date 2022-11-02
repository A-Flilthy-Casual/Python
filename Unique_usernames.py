#created by Roman Sanchez October 5th 2022

#usernames is a dictornay the first part is the key the second part is the pair assigned to that key
#here is the given example data
#this data is given as a dictornary itself it has two keys in it 
#they are students and active both of which are arrays
data = {
    "students":["Roman Sanchez","Roman Sanchez","Jeorge Vasquez","Jeorge Vasquez"],
    "active":[True,True, True, True]
    
}
#add to the dictonary a new key called usernames to Store
#usernames in a array also known as a list in python
data["usernames"]=[]


def remove_inacctive():
    #this function takes the data from keys of students and active
    
    #This function begins by parsing the array under the key known as active
    #however since I'm deleting elements of the array I have to start at the end
    #otherwise I might miss some
    i=len(data["active"])-1
    while (i>=0):
        if data["active"][i]==False:
            del data["students"][i]
            del data["active"][i]
            i-=1
        else:
            i-=1

def find_space(x):
    #this function searches the students array until it finds a space
    #it then returns the index value of where the space is +1 because we only want to print the first 5 letters of the last name
    #it also takes in a variable x so you can tell it which part of the array to search
    
    
        return int(data["students"][x].find(' '))+1
        
        
    

def find_dupes():
#This function finds and replaces duplicate usernames
#it does so by parsing through the array and counting each time it does it
# by default it adds to the set seen each time we compare the set named seen to our array usernames
# if we get a hit for a duplicate then we remove the last value of that string, then replace it with the numerical value
#that tells which duplicate number it is
#The tricky part to this is making a integer in this case the variable count into a string
#if we didn't convert it first the computer throws an error
    seen = set()
    count=2
    for i, e in enumerate(data["usernames"]):
        if e in seen:
            data["usernames"][i] =data["usernames"][i][:-1]
            data["usernames"][i]=data["usernames"][i]+str(count)
            count+=1
        else:
            seen.add(e)
    
            
def create_username():
    #call the function that removes all inactive users so all thats left is to make usernames
    remove_inacctive()
    
    #iterate through the students names to make a username
    count2=0
    for i in data["students"]:
        #in the array attached to the key username find the first 
        #blank space then take the 5 charachters that follow it and add them to the array in the appopriate index position
        #then also add the first 3 charachters of the array attached to key username at the correct index position
        #this weir if condition is there because I was having trouble making the variable i plug into 
        #the function find space increase by one each time.
        if 0==0:
            data["usernames"].append(i[find_space(count2):find_space(count2)+5]+i[0:3])
            count2+=1
    
    #make all the usernames lowercase
    #I don't think using indexing with range is appreciated in python, but I'm too used to c and c++
    for x in range(len(data["usernames"])):
        data["usernames"][x]=data["usernames"][x].lower()
    #now that we have a array of usernames time to run the function to find and change duplicates
    find_dupes()

#the function was defined earlier but we still need to actually use or call it
create_username()
#print the dictonary data to the terminal to make sure our function did what we wanted
print(data)