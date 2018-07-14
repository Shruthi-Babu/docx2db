from docx import Document
from boltons import iterutils
import sqlite3


conn = sqlite3.connect('Docs/5a.db') #db exclusive for 5a
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS classes (day TEXT, slot TEXT, room TEXT, mapid TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS faculty(fid TEXT, name TEXT, tag TEXT,designation TEXT, qualification TEXT, phoneno TEXT, emailid TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS slot(slotnumber TEXT,timings TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS subjects(mapid TEXT, fid TEXT, sem TEXT,sub TEXT)''')

c.execute('''SELECT * INTO 5a.slot FROM 2017e.slot''') #tried to copy the original 'slot' table into 'slot' for 5A, but not working!!



wordDoc = Document("Docs/5a.docx") #doc containing TT of 5A only so that its easier to access subjects individually
text = []
time_tables = []
class_rooms = []
subjects = []
TABLE = [[]]
for table in wordDoc.tables:
    class_room = "5a"
    for row in table.rows:
        for cell in row.cells:
            time_tables.append(cell.text)
#print time_tables
TABLE = iterutils.chunked(time_tables , 16) #creates a 2D list from the availabe 1D list
for i in range(len(TABLE)):
    print(TABLE[i])
    
#The number of columns that are getting displayed is different for each TT, hence split the doc class wise.
