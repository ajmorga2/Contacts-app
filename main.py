from tkinter import *
import sqlite3
from functools import partial


conn = sqlite3.connect('contacts.db')
c = conn.cursor()

# creation of the login database with rows
#c.execute(''' Create TABLE contacts(
    #            firstName text,
    #            lastName text,
    #            address text,
    #            email text,
    #            phone text)''')


#inserting contact data into row
#c.execute("INSERT INTO contacts VALUES ('Ainsley', 'Morgan', '115 Breezeway Ln', 'ainsleyjmorgan@gmail.com', '9196337069' )")
#c.execute("INSERT INTO contacts VALUES ('Isabel', 'Morgan', '111 Lee st', 'bella92@gmail.com', '4112201895' )")
#c.execute("INSERT INTO contacts VALUES ('Maxwell', 'Morgan', '135 Baker ave', 'maxiebeats@gmail.com', '9784561298' )")
#c.execute("INSERT INTO contacts VALUES ('Hallie', 'Carter', '115 Breezeway Ln', 'maxiebeats@gmail.com', '9784561298' )")
#c.execute("INSERT INTO contacts VALUES ('Maxwell', 'Morgan', '135 Baker ave', 'maxiebeats@gmail.com', '9784561298' )")
#commiting the above data into the row
#conn.commit()

# adding more rows into the table via class attributes and objects
#c.execute("INSERT INTO contacts VALUES (:first, :last, :addy, :email, :number )",{"first":contact1.first, "last":conctact1.last, "addy": contact1.email(), "number":contact1.number})
window4 = Tk()
#displays all contact information
window3 = Tk()
#contacts screen
window2 = Tk()
#main screen
window = Tk()


firstName = StringVar()
lastName = StringVar()
addy = StringVar()
email = StringVar()
number = StringVar()

def deleteContact(name):
    delete = c.execute(f'DELETE FROM contacts WHERE firstName=:name{"name":name}')



#get values from textfield and add them to the table
def saveToSql(rowID, firstName, lastName, address, email, number):
    #updating the rows w/ user inputted data
    update = c.execute(f'''UPDATE contacts
                            SET firstName=:first{'first':firstName},
                                lastNAME=:last{'last':lastName},
                                address=:addy{'addy':address},
                                email=:email{'email':email},
                                phone=:number{'number':number}
                            WHERE rowid=:id{'id':rowID}''')



# function to edit contact information

def editContact(name):

    #clears entry field for each category
    firstName = StringVar()
    lastName = StringVar()
    addy = StringVar()
    email = StringVar()
    number = StringVar()

    secure = (name,)
    contacts = c.execute('SELECT rowid, * FROM contacts WHERE firstName=?', secure).fetchone()
    rowID = contacts[0]

    #change contact info window
    Label(window4, text="First Name:").pack()
    e1 = Entry(window4, textvariable=firstName, width=20)
    e1.insert(0, contacts[1])
    e1.pack()
    f = e1.get()
    Label(window4, text="Last Name:").pack()
    e2 = Entry(window4, textvariable=lastName, width=20)
    e2.insert(0, contacts[2])
    e2.pack()
    l = e2.get()
    Label(window4, text="Address:").pack()
    e3 = Entry(window4, textvariable=addy, width=20)
    e3.insert(0, contacts[3])
    e3.pack()
    a = e3.get()
    Label(window4, text="Email:").pack()
    e4 = Entry(window4, textvariable=email, width=20)
    e4.insert(0, contacts[4])
    e4.pack()
    e = e4.get()
    Label(window4, text="Number:").pack()
    e5 = Entry(window4, textvariable=number, width=20)
    e5.insert(0, contacts[5])
    e5.pack()
    n = e5.get()
    Button(window4, text='Save Info', command=partial(saveToSql, rowID, f, l, a, e, n )).pack()
    print(rowID)





#function do display contact info including first & lastname, email, phone number and address
def contactInfo(name):
    secure = (name,)
    contacts = c.execute('SELECT * FROM contacts WHERE firstName=?', secure).fetchone()
    Label(window3, text=contacts[0]).pack()
    Label(window3, text=contacts[1]).pack()
    Label(window3, text=contacts[2]).pack()
    Label(window3, text=contacts[3]).pack()
    Label(window3, text=contacts[4]).pack()
    Button(window3, text='Edit Contact', command=partial(editContact, name)).pack()
    Button(window3, text='Delete Contact', command=partial(deleteContact, name)).pack()





#function created to display contacts first and last name
def showContacts():
    firstLast = c.execute('SELECT firstName, lastName FROM contacts').fetchall()
    #contactButton = Button(window2, text=names[0] + ' ' + names[1], command=contactInfo)
    for names in firstLast:
        #create a button with first & last name
        Button(window2, text=names[0] + ' ' + names[1], command=partial(contactInfo, names[0])).pack()
        print(names[0] + " " + names[1])



#main window
Label(window, text="Contacts").pack()
Button(window, text='show contacts', command=showContacts).pack()




window.mainloop()

#window.mainloop()
#def findByLast(lastName):
#  c.execute(f"SELECT * FROM login WHERE lastName=:last{'last':lastName}")
#def findByFirst(firstName):
#    c.execute(f"SELECT * FROM login WHERE firstName=:first{'first':firstName}")
#def findByaddy(number):
#    c.execute(f"SELECT * FROM login WHERE phone=:phone{'phone':number}")
