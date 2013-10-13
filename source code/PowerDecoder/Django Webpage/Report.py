class Report:
    def __init__(self):
        self.Next = []
        self.title = ""
        self.description = ""
        self.data = ""
        
    def __init__(self, Title, Description, Data):
        self.Next = []
        self.title = Title
        self.description = Description
        self.data = Data
        
    def AddNext(self, ob):
        self.Next.append(ob)