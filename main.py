f = open('myfile.txt','r')  #Open the text file we created in 'read' mode
i = -1      #Setting the value of i to -1
student_names = ["Thomas Shelby", "Arthur Shelby", "John Shelby"]      #Creating a list of students

while True:     #While the condition is true keep running
    i+=1        #Incrementing the value of i
    line = f.readline()     #using the 'readline()' to read every line in the text file
    if not line:
        break
    m1 = line.split(',')[0]     #split each number after ',' and assigning them the value in list
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]

    print(f"Marks of {student_names[i]} in Signal And System are: {m1}")
    print(f"Marks of {student_names[i]} in Microcontroller are: {m2}")
    print(f"Marks of {student_names[i]} in Data Communication are: {m3}")

f.close()
#closing the file