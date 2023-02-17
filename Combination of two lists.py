import random

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

results = [("sajjad", "soghra"), ("abdollah", "minoo") , ("sobhan", "hane")]

combined_list = [] 
  
while len(boys) > 0 and len(girls) > 0: 
    index1 = random.randrange(0, len(boys)) 
    index2 = random.randrange(0, len(girls)) 
      
    combined_list.append((boys[index1], girls[index2])) 
      
    boys.pop(index1) 
    girls.pop(index2) 
  
print (combined_list)





