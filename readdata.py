#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#defines file containing dataset
infile='database.uncompressed'

#opens the file containing dataset
fh = open(infile)

line= fh.readline()
while line[:20] != '!dataset_table_begin':
    line=fh.readline()

header= fh.readline().strip()
colnames={}

index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.
genefile=open('gene.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probe.txt', 'w')

#splits the data from the tables into seperate, defined colums
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

#a function to create new rows when required
def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"

#takes data from dataset and adds it to created files
def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
rows=0    

#try/except for error checking
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
	rows=rows+1
    except:
	pass

#closes created files
genefile.close()
probefile.close()
expressionfile.close()

#displays the number of created rows
print '%s rows processed'%rows
    
