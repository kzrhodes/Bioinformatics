import models

Gene = models.Gene(%s)

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"
print
print "<html><head><TITLE>Results</TITLE></head>"
print "<body><H1>Results</H1>"
print "<table><tr><th>Ke</th><th>Value</th></tr>"

for k in form.keys():
	print"<tr><td>%s</td><td>%s</td></tr>"

print "<table>"

print "</body></html>"
