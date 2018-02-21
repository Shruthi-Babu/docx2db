from docx import Document
import re


class Subject:

    def __init__(self, sub_code, sub_name, teacher, map_id, sem):
        self.sub_code = sub_code
        self.sub_name = sub_name
        self.teacher_code = teacher
        self.is_lab = Subject.is_lab()
        self.sem = sem

    @staticmethod
    def is_lab(self):
        return True

    def generate_map_id(self):

        return

    def generate_fid(self):

        return


class ClassRoom:

    def __init__(self, map_id, room_no, day):
        self.map_id = map_id
        self.room_no = room_no
        self.day = day

    def find_slot(self, slot):
        self.slot = slot
        return


wordDoc = Document("test_files/5TH_TT_WITH_TUTORIAL.docx")
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
        sub_code = re.split("[0-9]?\.", arr[0])[1]
        sub_name = arr[2].strip()
        teacher = arr[3].strip()
        print(sub_code, "Subject:"+sub_name, "Teacher:"+teacher, sep=" ")
    print("")
# for info in time_tables:
    # print(info)
