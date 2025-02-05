class Notebook:
    def __init__(self, notes):
        self.notes = notes

    def read(self, date):
        try:
            return self.notes[date]
        except (KeyError):
            return []
        
notes = {
    "20.02.2002": ["Something happened"],
    "21.02.2002": ["Nothing happened", "Absolutely nothing happened"],
    "22.02.2002": ["Happened nothing", "Happened absolutely nothing"],
}
    
notebook = Notebook(notes)
print(notebook.read("20.02.2002"))
print(notebook.read("19.02.2002"))