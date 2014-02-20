# -*- coding: iso-8859-1 -*-
'''Classes to represent our gene expression objects'''

import MySQLdb

#class allows script to login to personal MySQL with created tables
class DBHandler():
    connection=None
    dbname='kzrhodes'
    dbuser='kzrhodes'
    dbpassword='fluttershy'
    
    def __init__(self):
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, \
user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

    def cursor(self):
	return DBHandler.connection.cursor()

#class which keeps the data created from search function
class Gene():
    gene_symbol=''
    gene_title=''
    gene_id=''
    probelist=[]

    def __init__(self,geneid):
	self.gene_id=geneid

	#logs into MySQL
        db=DBHandler()
	cursor=db.cursor()
	sql='select gene_title, gene_symbol from gene where gene_id=%s'
	cursor.execute(sql,(geneid,))

	#query database
	#get result and populate the class fields.
	result=cursor.fetchone()

	self.gene_title	=result[0]
        self.gene_symbol=result[1]
        #locates matching probes
        probesql='select probe_name from probe where gene=%s'
	#fill in the blanks yourself
	cursor.execute(probesql,(geneid,))

	#fills probe list
	for result in cursor.fetchall():
  	    self.probelist.append(result[0])



