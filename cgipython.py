#!/usr/local/Python-3.7/bin/python
import pymysql
import sys
import cgi
import mysql.connector
import cgitb
cgitb.enable()

myuser = "cwill96"
mypassword = "#"

# print content-type
print("Content-type: text/html\n")
print('''<style>


#miRNA td, #miRNA th {
  border: 1px solid #ddd;
  padding: 8px;
}

#miRNA tr:nth-child(even){background-color: #A9A9A9;}

#miRNA tr:hover {background-color: #FF4500;}

#miRNA th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #DCDCDC;
  color: white;
}
</style>
</head>''')
print("<body>")


print("""
<html>
<title>Search miRNA by Target</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-flat.css">
<body>

<div class="w3-container w3-dark-grey">
  <h2>miRNAs that target</h2>
  <p>Get a list of all miRNAs that target the genes you enter by name and score.</p>
</div>


<body>
""")

print("""
<form class="w3-panel w3-light-grey w3-leftbar" name="miRNA" action="https://bioed.bu.edu/cgi-bin/students_20/cwill96/hw04" method="post">
Gene Name: <input type="text" name="Search_term"><br>
<label for="Score">Score:</label>
  		<input type="text" id="Score" name="Score"><br>
<input type="submit" class="w3-btn w3-ripple w3-round-xxlarge w3-hover-deep-orange w3-dark-grey" value="Submit" />
</form>
""")

form = cgi.FieldStorage()

if form:
	# get the values from the form for single-value fields
	# note that the names in quotes match the names of the fields in the form above
	reskeyword  = form.getvalue("Search_term")
	testa = form.getvalue("Score")
	#if reskeyword is not empty
	if reskeyword: 
		# print the keyword to the html
		print("<table id=miRNA>")
		print("<tr><th>Name of miRNA</th><th>Score</th></tr>")
	
		#now, get access to the database and send a query looking for all professors 
		#who's research contains the keyword
		
		#import module to connect to a mysql database
		import mysql.connector
		
		#create the connection with login details
		connection = mysql.connector.connect(host='bioed.bu.edu', user=myuser, password=mypassword, database='miRNA', port='4253')
		
		#the cursor sends and receives information from the database
		cursor = connection.cursor()

		#this is the SQL query
		query = "select miRNA.name, score from gene natural join targets join miRNA using (mid) where gene.name regexp '%s' and score <'%s'" %(reskeyword,testa)
		print("""Query used in database: <br />"""+ query + "<br /><br /> Searching by entered Gene Name:'%s' <br /> & entered Score:'%s' <br /><br />""" %(reskeyword,testa))
		 
		#execute the query
		cursor.execute(query)

		#rows receives the results of the query
		rows = cursor.fetchall()

		print("""Results: <br />""")
		for row in rows:
			print("<tr><td>%s</td><td>%f</td></tr>" % (row[0], row[1]))
else:
	print('Waiting for you to enter something.....')
	
#end the html code
print("""
</body>
</html>
""") 
