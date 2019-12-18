# utf8validatorbatch
To run utf8validator(https://github.com/digital-preservation/utf8-validator) over a DROID CSV export file and identify any non-utf8 files which identify by extension only

Download the UTF8 validator and run script from the bin folder, it will prompt you to add a filepath to the DROID csv export you want to check. The script will then run the utf8 validator over all files identifying by 'extension' in DROID export. 

It will save all output from the validator to an output folder which will be created in the bin directory and called the same name as the DROID export with '_validator_output' added

If file contains invalid UTF8 characters it will print the output filename to the console, as well as add to a list which will be exported to a csv file called errorfiles.csv created in the bin directory
