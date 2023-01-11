# Opening a file
file = open("team7.txt", "w")

team_members = ["Naruto \n", "Sasuke \n", "Sakura \n"]
sensei = "Kakashi \n"

# Writing a string to file
file.write(sensei)

# Writing multiple strings at a time
file.writelines(team_members)

# Closing file
file.close()

# Checking if the data is written to file or not
file = open("team7.txt", "r")
print(file.read())

file.close()