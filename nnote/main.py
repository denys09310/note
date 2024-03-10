import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_main_w


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_main_w()
        self.ui.setupUi(self)
        self.read_notes()
        self.ui.list_wid.addItems(self.notes)
        self.ui.list_wid.itemClicked.connect(self.show_note)
        self.ui.savenote_btn.clicked.connect(self.save_note)
        self.ui.createnote_btn.clicked.connect(self.create_note)
        self.ui.delatenote_btn.clicked.connect(self.delete_note)
        self.ui.createteg_btn.clicked.connect(self.add_tag)
        self.ui.deleteteg_btn.clicked.connect(self.delete_teg)
        self.ui.saveteg_btn.clicked.connect(self.search_by_teg)

    def show_note(self):
        self.name = self.ui.list_wid.selectedItems()[0].text()
        self.ui.findnote_btn.setText(self.name)
        self.ui.note_wid.setText(self.notes[self.name]["Text"])
        self.ui.teg_wid.clear()
        self.ui.teg_wid.addItems(self.notes[self.name]["Tegs"])


    def save_note(self):
        tags = []
        for i in range(self.ui.teg_wid.count()):
            tags.append(self.ui.teg_wid.item(i).text())


        self.notes[self.ui.findnote_btn.text()]=  {
            'Text':self.ui.note_wid.toPlainText(),
            'Tegs':tags
        }
        with open("notes.json","w",encoding="utf-8") as file:
            json.dump(self.notes, file)
        self.ui.list_wid.clear()
        self.ui.list_wid.addItems(self.notes)
    def clear(self):
        self.ui.findnote_btn.clear()
        self.ui.note_wid.clear()

    def create_note(self):
        self.clear()

    def read_notes(self):
        try:
            with open("notes.json",'r',encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
             self.notes = {
                "First note":{
                    "Text" : "It's first text ",
                 "Tegs":[]
                }
            }
    def delete_note(self):
        try:
            del self.notes [self.name]
            self.clear()
            self.ui.list_wid.clear()
            self.ui.list_wid.addItems(self.notes)
            self.save_note()
        except:
            print('Eror404')
    def add_tag(self):
        tag_name = self.ui.findteg_btn.text()
        if tag_name !="":
            if tag_name not in self.notes[self.name]["Tegs"]:
                self.notes[self.name]["Tegs"].append(tag_name)
                self.ui.teg_wid.clear()
                self.ui.teg_wid.addItems(self.notes[self.name]["Tegs"])
    
    def delete_teg(self):
        if self.ui.teg_wid.selectedItems():
            tag_name = self.ui.teg_wid.selectedItems()[0].text()
            if tag_name  in self.notes[self.name]["Tegs"]:
                self.notes[self.name]["Tegs"].remove(tag_name)
                self.ui.teg_wid.clear()
                self.ui.teg_wid.addItems(self.notes[self.name]["Tegs"])
    
    def search_by_teg(self):
        tag = self.ui.findteg_btn.text()
        if tag:
            matching_notes = []
            for note_name in self.notes:
                if tag in self.notes[note_name]["Tegs"]:
                    matching_notes.append(note_name)
        
        self.ui.list_wid.clear()
        self.ui.list_wid.addItems(matching_notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
