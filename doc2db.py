from docx import Document
import re


class Subject:

    def __init__(self, sub_code, sub_name, sub_abbre, sub_time, teacher, map_id, is_lab):
        self.sub_code = sub_code
        self.sub_name = sub_name
        self.sub_abbre = sub_abbre
        self.sub_time = sub_time
        self.teacher_code = teacher
        self.map_id = map_id
        self.is_lab = is_lab


class ClassRoom:

    def __init__(self, subject, room_no, section):
        self.subject = subject
        self.room_no = room_no
        self.section = section


wordDoc = Document("5TH_TT_WITH_TUTORIAL.docx")
text = []
time_tables = []
class_rooms = []
subjects = []
for info in wordDoc.paragraphs:
        text.append(info.text)
for table in wordDoc.tables:
    class_room = "3a"
    for row in table.rows:
        for cell in row.cells:
            time_tables.append(cell.text)
for item in text:
    if "CS" in item and "." in item:
        arr = re.split("[\t]+", str(item))
        sub_abbre = re.split("^[0-9]?\. ", arr[0])[1]
        sub_code = arr[1].strip()
        sub_name = arr[2].strip()
        teacher = arr[3].strip()
        
        print(sub_abbre, sub_code, sub_name, teacher, sep=" ")
    print("")
# for info in time_tables:
    # print(info)
