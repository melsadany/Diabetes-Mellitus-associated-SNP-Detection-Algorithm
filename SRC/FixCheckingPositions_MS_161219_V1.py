##This is to check the positions found in the entered sequence. These positions are saved in a dictionary and will be checked whether present or not in the database.

import sqlite3 as litem

#As a checking step for this part, you can define the dictionary keys and values as below 
dict={
    4 : ['A', 'C'],
    266 : ['C', 'G']
    }

#The dict defined below is a step to check that the code gives the write output for an empty dictionary.
##dict = {
##    }

flag1 = False
##flag1 here is to check whether the dictionary has keys or not meaning there're SNPs found or not

for position in dict.keys():
    flag1 = True
    con = lite.connect("INSULIN_SNPs.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Seqinfo")
    rows = cur.fetchall()
    flag=0
##    flag here is to count 
    cursor = con.execute("SELECT * from Seqinfo WHERE Position =?", (int(position),))
    if cursor:
        for row in cursor:
            if int(position) == row[4]:
                value_of_position = dict[position]
                if value_of_position[1] == row[3]:
                    print("The entered sequence that has a SNP at position: ", position, "is ", row[1], "SNP")
                    flag +=1
    if flag == 0:
        print("The entered sequence that has a SNP at position: ", position, "has undefined clinical pathogenicity")
if flag1== False:
    print("The entered sequence has no SNPs")
