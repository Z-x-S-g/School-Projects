from PyInquirer import prompt, print_json, Separator
from pprint import pprint
from examples import custom_style_2
from os import system
system('clear')

def returning_pmenu():
    print("Okay!, returning to the principal menu")
    system('sleep .35s')
    print(".")
    system('sleep .35s')
    print(".")        
    system('sleep .35s')
    print(".")
    system('clear')


def principal_menu():
    menu = [
        {
            'type' : 'list',
            'name' : 'pmenu',
            'message' : '>= ==Welcome to our digital library== <=',
            'choices' : [
                Separator(),
                '   Add a book at the end of the list',
                '   Remove the last book from the list',
                '   Remove book',
                '   Print the whole list and check it info',
                '   Exit'
            
            ]
        }
    ]
    
    answers = prompt(menu)
    return answers['pmenu']

def cliappend():
    appendB = [
        {
            'type'      : 'input',
            'name'      : 'Title',
            'message'   : 'What is the title of the book?'
        },
        {
            'type'      : 'input',
            'name'      : 'Author',
            'message'   : 'Who is the autor of the book?'
        },
        {
            'type'      : 'input',
            'name'      : 'Edition',
            'message'   : 'What is the edition of the book?'
        },
        {
            'type'      : 'input',
            'name'      : 'Editorial',
            'message'   : 'What is the editorial of the book?',   
        }
    ]

    confirm = [
        {
            'type': 'confirm',
            'message': 'Do you want to add this book to the library?',
            'name': 'continue',
            'default': True,
        }
    ]
    
    answers = prompt(appendB)
    check = prompt(confirm)
    if check['continue'] == True:
        print("Done!")
        returning_pmenu()
        return answers
    else:
        returning_pmenu()


def clipop():
    book = "Daniel"
    popb = [
        {
            'type': 'confirm',
            'message': 'Are you sure you want to delete it?',
            'name': 'continue',
            'default': False,

        }
    ]
    answers = prompt(popb)
    if answers['continue'] == True:
        print("Done the book was removed")
        returning_pmenu()    
    else:
        returning_pmenu()


def cliCheckRm(newlist):
    questions = [
        {
            'type': 'checkbox',
            'qmark': 'o',
            'message': 'Select the books that you want to delete',
            'name': 'remove',
            'choices': newlist,
        }
    ]

    answers = prompt(questions)
    returning_pmenu()
    return answers

def cliAllBooks(blist,reformed_list):
    
    questions = [
       {
            'type': 'list',
            'name': 'books',
            'message': '========== All books ==========',

            'choices':reformed_list,
        }
    ]
    answers = prompt(questions)
    system('clear')
    if answers['books'] =='Exit':
        returning_pmenu()
        return False
    else:
        return answers
    

def cliInfoBook(blist,reformed_list):
    questions = [
       {
            'type': 'list',
            'name': 'books',
            'message': '========== All books ==========',

            'choices':reformed_list,
        }
    ]
    answers = prompt(questions)
    system('clear')
    if answers['books'] == 'Exit':
        returning_pmenu()
        return False
    else:    
        return answers
                

    
    
