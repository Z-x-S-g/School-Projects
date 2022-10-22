from functions import *
from cli_functions import *

def connector(blist):
    main_opt = principal_menu()
    if main_opt == '   Add a book at the end of the list':
        #print(cliappend())
        bookList("add",cliappend(),blist)
        connector(blist)
        #Mandar a database
    elif main_opt ==  '   Remove the last book from the list':
        bookList("pop",clipop(),blist)
        connector(blist)
    elif main_opt == '   Remove book':
        bookList("boxRm",None,blist)
        connector(blist)
    elif main_opt ==  '   Print the whole list and check it info':
        bookList("infoAll",None,blist)
        connector(blist)
        #:connector(blist)




    elif main_opt ==  '   Exit':
        system('clear')
        print("Goodbye, and thanks for use our program!")
        exit()



def main():
    blist = []
    b1 = Book("0","El llano en llamas", "Juan Rulfo","2016", "Oceano") 
    b2 = Book("1","Alchemist", "Paulo Cohelo","2016", "Oceano")
    blist.append(b1) 
    blist.append(b2)
    for x in range(2,11):
        newBook = Book(str(x),str(f"libro{x}"),"Daniel Pazos", str(hex(x)), "Oceano" )
        blist.append(newBook)

    connector(blist)
main()


