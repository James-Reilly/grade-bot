import os
import re


def main():
	print("Welcome to Grader 1.0!")

	#Get the Path of th directory to grade
	path = input("Enter Path: ")
	
	while not (os.path.isdir(path)):
		path = input("Path does not exist please try again: ")
		
	"""#Get grading python or java
	com = input("Are you grading python or java? (python/java): "):
	while not (com == "python" or com == "java"):
		com = input("Not valid language please try again (python/java): "):
	"""

	neededFiles = input("Enter location of other files needed (.java) ")
	neededFiles = path + "/" + neededFiles
	while not (os.path.isdir(neededFiles)):
		inputFiles = input("Location does not exist please try again: ")
		inputFiles = path + "/" + inputFiles

	"""
	gradeType = input("Is the program run using a main driver, piped .txt input or .txt as an argument? (m/p/a): "):
	while(gradeType == "m" or gradeType =="p" or gradeType == "a"):
		gradeType = input("Please try again. (m/p/a): "):

	if(gradeType == "m"):
		mainDriver(com, path)
	else if (gradeType == "p"):
		pipedInput(com, path)
	else:
		textArg(com, path)

	"""

	inputFiles = input("Enter location of input (.txt) files: ")
	inputFiles = path + "/" + inputFiles
	while not (os.path.isdir(inputFiles)):
		inputFiles = input("Location does not exist please try again: ")
		inputFiles = path + "/" + inputFiles

	solOutput = input("Enter location of solution output (.txt) files: ")
	solOutput = path + "/" + solOutput
	while not (os.path.isdir(solOutput)):
		solOutput = input("Location does not exist please try again: ")
		solOutput = path + "/" + solOutput

	

	main = input("Name of Main java class (not including .java): ")
	


	while(True):
		student = findAndCompileStudent(path, neededFiles, inputFiles)
		runTests(student,main,inputFiles)
		compareOutputs(solOutput, student)

		again = input("Run again with same config? (y/n): ")
		if again == 'y':
			continue
		break
"""
def mainDriver(com, path):
	main = input("Name of Main " + com + " File: ")
	command = com + " " + main
	extra = ""
"""

"""
@param path - The path to the directory of the lab being graded
@param neededFiles - path to the directory to the files needed to run the program
@param inputFiles - path to the input textFiles

"""
def findAndCompileStudent(path, neededFiles, inputFiles):
	while(True):
		stu = str(input("Enter Student to Grade (Folder Name): "))
		stu = path + "/" + stu
		if(os.path.isdir(stu)):
			print("Student Exists! Compiling Code!")
			break
		else:
			print("Student does not exist try again!")

	for file in os.listdir(neededFiles):
		os.system("cp " + str(neededFiles) + "/" + file + " " + stu)
	os.system("find " + stu + " -name '*.java' | xargs javac")

	for file in os.listdir(inputFiles):
		os.system("cp " + str(inputFiles) + "/" + file + " " + stu)
	return stu


"""
@param stu - The path to the students directory
@param main - Name of the main driver file
@param inputFiles - path to the input textFiles

Calls diff on the students output vs the faculty output
"""		
def runTests(stu, main, inputFiles):
	os.system("mkdir " + stu + "/stu-output")
	os.system("find stu-output -name '*.txt' | xargs rm")
	num = -1
	command = "java -classpath " + stu + " " + main + " "
	for file in os.listdir(inputFiles):
		number = re.search(r'\d+', file).group()
		print(str(number))
		print("RUNNING " + file)
		os.system(command + inputFiles + "/" + str(file) + " > "+ stu +"/stu-output/output" + str(number) +".txt")
	
"""
@param sol - Location of the solution files
@param path - The path to the students directory

Calls diff on the students output vs the faculty output
"""		
def compareOutputs(sol, path):

	for solfile in os.listdir(sol):
		for stufile in os.listdir(path + "/stu-output"):
			if ".txt" not in stufile:
				continue
			number = re.search(r'\d+', solfile).group()
			stuNumber = re.search(r'\d+', stufile).group()
			if not number == stuNumber:
				continue

			print("Comparing Test " + number)
			os.system("diff " + path + "/stu-output/" + str(stufile) + " " + sol + "/" + str(solfile))
			input("Continue?")


main()
