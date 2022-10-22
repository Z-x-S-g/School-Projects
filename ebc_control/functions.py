from allClases import * 
from cli_functions import cliAllBooks, cliInfoBook, principal_menu, cliCheckRm
#Creation of all book lists by genre
def bookList(opt,func,blist):
    if opt == "add":
        title = func['Title']
        author = func['Author']
        edition = func['Edition']
        editorial = func['Editorial']
        giveid = len(blist)

        while(blist.count(giveid) > 0):
            giveid += 1
        
        newbook = Book(str(giveid),title,author,str(edition),editorial)
        blist.append(newbook)
    
    
    if opt == "pop":
        blist.pop()
    if opt == "boxRm":
        newlist = []
        llate = []
        for books in range(len(blist)):
            titleBook = dict(name = blist[books].get_title())
            newlist.append(titleBook)
            llate.append(blist[books].get_title())
        answers = cliCheckRm(newlist)
        rm = list(answers['remove'])
        v = range(len(blist))
        for llate in rm:
            for i in v:
                if blist[i].remove(llate,blist) == True:
                    del blist[i]
                    break
                else:
                    pass
                
        #r = range(len(blist))
        #print(r)

    if opt == "infoAll":
        getBooks(blist,func)


def getBooks(blist,answer):
    newlist = []
    if answer != None:
        
        for book in range(len(blist)):
            if blist[book].get_title() == answer['books']:
                newlist.append('====================')
                newlist.append("|----ID-------- "+str(blist[book].get_id()) ) 
                newlist.append("|---Title------ "+blist[book].get_title())
                newlist.append("|---Author----- "+blist[book].get_author())
                newlist.append("|--Edition----- "+blist[book].get_edition())
                newlist.append("|-Editorial---- "+blist[book].get_editorial())
                newlist.append('====================')
            else:
                newlist.append((blist[book].get_title()))
        newlist.append('Exit')
        answer = cliInfoBook(blist,newlist)
        if answer == False:
            pass
        else:
            getBooks(blist,answer)
    elif answer == None:
        for book in range(len(blist)):
            newlist.append((blist[book].get_title()))
        newlist.append('Exit')
        answer = cliAllBooks(blist,newlist) #return answer
        if answer == False:
            pass
        else:
            getBooks(blist,answer)
    else: 
        for book in range(len(blist)):
            newlist.append((blist[book].get_title()))
        newlist.append('Exit')
        answer = cliAllBooks(blist,newlist)
        if answer == False:
            pass
        else:
            getBooks(blist,answer)


#print(bookList())  

