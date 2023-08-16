# StudentsMarksSheet
The given code snippet reads data from a text file named "myfile.txt" and processes it to extract and display marks for different subjects associated with a list of student names. The code starts by opening the file in read mode and initializing a counter variable i to keep track of the current student's index.

A list named student_names is defined, containing the names of students. These names correspond to the order in which the students' marks are expected to be present in the file.

Inside the main loop, the code reads each line from the file using the readline() method. If the line is empty (indicating the end of the file), the loop terminates.

The line is split using the comma (',') delimiter, and the extracted values are assigned to the variables m1, m2, and m3, representing the marks in different subjects for the current student.

The code then prints out the marks along with the corresponding student's name for each subject. It uses the extracted marks and the student's name from the student_names list to create informative output messages.

After processing all the lines in the file, the file is closed to free up system resources
