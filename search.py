# -*- coding: iso-8859-1 -*-
#imports models script
import models

Gene = models.Gene(%s)

#imports cgi programmes
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
#displays the data ouput to the website

print "Content-Type: text/html" #html stuff is following
print #blank line, end of headers
print "<html><head><TITLE>Results</TITLE></head>"
print "<body><H1>Results</H1>"
print "<table><tr><th>Ke</th><th>Value</th></tr>"

for k in form.keys():
	print"<tr><td>%s</td><td>%s</td></tr>"

print "<table>"

print "</body></html>"
