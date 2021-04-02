import requests
import json
import os
os.chdir('/Users/gshanmu2/Documents/python/Mouser/')

def keep(todo):
    is_complete = todo["completed"]
    #print("IS_COMPLETE: "+str(is_complete))
    #print("users"+str(users))
    #print("has_max_count_bbefore"+has_max_count)x
    has_max_count = str(todo["userId"]) in users
    #print("has_max_count_after" + has_max_count)
    return is_complete and has_max_count


#Determine which user completed most task


url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url, verify=False)

#print(response.text)


todos = response.json()

print(todos)



#Json_res =  json.loads(response.text)
#print(type(Json_res))

#print(Json_res[1])
#print(Json_res[1]["userId"])

#print(todos[:10])


# Map of userId to number of complete TODOs for that user
todos_by_user = {}


for todo in todos:
    #print(todo["userId"]+""+(todo["completed"]))
    #print("{},{},{},{}".format(todo['userId'], todo['id'], todo['title'],todo['completed']))
    #print(todo['userId'])
    #print(todos_by_user[todo["userId"]])
    print(todo["completed"])
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
            #print(todos_by_user)
        except KeyError:
         # This user has not been seen. Set their count to 1.
             todos_by_user[todo["userId"]] = 1
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

print(top_users)


# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

print("max_completed: " +str(max_complete))


users = []
for user, num_complete in top_users:
    print("{},{}".format(user, num_complete))
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(max_users)

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)



