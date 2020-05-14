import csv
import os
import glob
import subprocess

droidfile = input("Please enter filepath of DROID CSV: ") #this line lets you state the DROID CSV which contains files you want to validate identifying as extension
droidfile = droidfile.strip('"')
output = os.path.basename(os.path.normpath(droidfile))
output = output.replace(".csv","") + "_validator_output"
extension = []
outputlist = []
count = int(1)


with open(droidfile, 'rt') as f: #reads the CSV file and takes the filepath and method columns, if the file has identified by extension only it will add the filepath of that file to a list
	reader = csv.reader(f)
	for row in reader:
		filepath = row[3]
		method = row[5]
		if method == 'Extension':
			extension.append(filepath)

if not os.path.exists(output): #output directory is created in bin and is the name of the droid csv export with _validator_output added 
      os.makedirs(output)

for file in extension: #runs validator over files, if filename already exists it adds an incremental number to the output filename
	fileoutput = os.path.basename(os.path.normpath(file))
	if os.path.exists(output+ "\\" + fileoutput+ ".txt"):
		fileoutput = fileoutput + "[" + str(count) + "]"
		command = "validate.bat " + '"' + file + '"'+ " > " + '"' + output + "\\" + fileoutput + ".txt" + '"'
		count += 1
		subprocess.run(command)
	else:
		command = "validate.bat " + '"' + file + '"'+ " > " + '"' + output + "\\" + fileoutput + ".txt" + '"'
		subprocess.run(command)
	

for file in glob.glob(output+"/*"): #generates a list of all files in output folder, if it contains invalid UTF8 characters it will print the output filename to the console, as well as add to a list which will be exported to a csv file called errorfiles.csv create in bin directory
	with open(file, 'r') as f:
		if 'Valid OK' in f.read():
			pass
		else:
			file = (os.path.basename(os.path.normpath(file)))
			file = file[:-4]
			print (file + " is not UTF8 valid")
			outputlist.append(file)

with open("errorfiles.csv", "w") as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter='\n')
    wr.writerow(outputlist)

