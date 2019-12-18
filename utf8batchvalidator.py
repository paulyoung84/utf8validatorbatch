import csv
import os
import glob

droidfile = input("Please enter filepath of DROID CSV: ")
output = os.path.basename(os.path.normpath(droidfile))
output = output.replace(".csv","") + "_validator_output" 
if not os.path.exists(output):
      os.makedirs(output)
extension = []
outputlist = []
count = int(1)


with open(droidfile, 'rt') as f: #this line lets you state the DROID CSV which contains files you want to validate identifying as extension
	reader = csv.reader(f)
	for row in reader:
		filepath = row[3]
		method = row[5]
		if method == 'Extension':
			extension.append(filepath)

if not os.path.exists(output):
      os.makedirs(output)

for file in extension:
	fileoutput = os.path.basename(os.path.normpath(file))
	if os.path.exists(output+ "\\" + fileoutput+ ".txt"):
		fileoutput = fileoutput + "[" + str(count) + "]"
		command = "validate.bat " + '"' + file + '"'+ " > " + output + "\\" + '"' + fileoutput +'"' + ".txt"
		count += 1
		os.system(command)
	else:
		command = "validate.bat " + '"' + file + '"'+ " > " + output + "\\" + '"' + fileoutput +'"' + ".txt"
		os.system(command)
	

for file in glob.glob(output+"/*"):
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

