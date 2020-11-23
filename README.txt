This package is to check an entered insulin gene sequence with the original sequence and give an output of the different SNPs and their positions in a dictionary if found. After that, it will check if these SNPs are found in a built database or not. You will find the needed code for building the database attached and all what you need is to run it once if there is a problem with the attached database after deleting it. 

The file for building database is named BuildingDatabase_MS_161219_V4.py 

To check your code for retrieving info from database based on the entered dictionary, please check FixCheckingPositions_MS_161219_V1.py, it should give you the same output in figure(9) in the attached report.

First Step needed by running the main code file, named FinalCode.py, is to enter the path of the sequence you want to check. After that, the program will continue working and give you an output of the clinical significance of SNPs if found. 

There is a file named SNP_Detection.py which is a module with different functions that together will give the SNPs and their positions as output
First function is compile to parse the entered file to extract the sequence. The output of this function will be passed on to another function named check to make sure that you entered the write sequence that do not have any insertion or deletion.If you entered the wrong file, you will be asked to enter another file.

After checking the file, the output of check will be passed on to the Hashtable function to form the hashfunction and form the hashtable. You will find all the details for the hashfunction in the report and the presentation. The Hashtable function will be used also on the original file which named insulin.fasta

The two hastables are compared using diff function to extract the different hash values that will be passed on to SNPs function to give the the different SNPs and their positions in a dictionary which will be later checked in the database for its clinical pathogenicity

If you want to check the code there is also a file named isoform insulin.txt which have SNPs in position 0,4,464 

For further information about the coding, please check the attached report. If anything is not clear enough, do not hesitate to contact us and you can find our emails written in the report itself.


This Module was done by Mayar Mansour and Muhammad Esadany
