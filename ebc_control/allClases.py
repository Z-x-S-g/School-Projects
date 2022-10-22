class Book:
    def __init__(self,automatic_id,title,author,edition,editorial):
        self.idbook     =    automatic_id
        self.title      =    title
        self.author     =    author
        self.edition    =    edition
        self.editorial  =    editorial
    def __repr__(self): 
        return str(self.__dict__)
    
    def get_title(self):
        return str(self.title)

    def get_id(self):
        return str(self.idbook)
    
    def get_author(self):
        return str(self.author)
    
    def get_edition(self):
        return str(self.edition)
    
    def get_editorial(self):
        return str(self.editorial)
    def remove(self,title,blist):
        if title == self.title:
            return True 
        else:
            return False

