import mysql.connector
import webbrowser

mydb = mysql.connector.connect(
    host="10.1.2.163",
    user="root",
    password="root",
    database="daDB1"
)

if mydb.is_connected():
    # create function for a select database query
    selectDb = "SELECT * FROM userinfo"
    cursor = mydb.cursor()
    cursor.execute(selectDb)
    result = cursor.fetchall()

    p = []

    # html table code
    tbl = "<tr><td>ID</td><td>username</td></tr>"
    p.append(tbl)

    for row in result:
        a = "<tr><td width=50px>%s</td>" % row[0]
        p.append(a)
        b = "<td width=300px>%s</td></tr>" % row[2]
        p.append(b)

    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<h1 align=center> USERS </h1>
<style>
  table {
    font-size: 16px;
  }

  th, td {
    font-size: 14px;
  }
</style>

<table align="center" border = "1">
%s
</table>
</body>
</html>
''' % (''.join(p))

    filename = 'webbrowser.html'

    def main(contents, filename):
        output = open(filename, "w")
        output.write(contents)
        output.close()

    main(contents, filename)
    webbrowser.open(filename)

else:
    print("Connection failed")
