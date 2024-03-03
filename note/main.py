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

    def show_note(self):
        self.name = self.ui.list_wid.selectedItems()[0].text()
        self.ui.findnote_btn.setText(self.name)
        self.ui.note_wid.setText(self.notes[self.name]["Text"])


    def save_note(self):
        self.notes[self.ui.findnote_btn.text()]=  {
            'Text':self.ui.note_wid.toPlainText(),
            'Tegs':[]
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

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
