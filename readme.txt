readdata.py takes data from Geo and converts into a form used by MySQL, inserting it into the correct tables

The created  tables are also displayed as gene.txt expression.txt and probe.txt

Models.py contains a script which logs in to MySQl and querys the avalible data to find a suitable response to an imputted gene ID. 

Search.py uses the script from models.py and attempts to link it with website using cgi forms. However it does not currently work.
