#Task 27.02
#S3CS3 Stefan Yuzhao Heng

import datetime

class libraryItem:
    def __init__(self,t,a,i):
        self.__title = t
        self.__authorArtist = a
        self.__itemID = i
        self.__onLoan = False
        self.__dueDate = datetime.date.today()
        self.__borrowerID = None

    def __repr__(self):
        return "ITEM: \n Title: %s;\n Aut/Art: %s;\n ID: %d;\n OnLoan: %s;\n Due: %s;\n Borrower: %s;\n" % (self.__title,self.__authorArtist,self.__itemID,self.__onLoan,self.__dueDate,self.__borrowerID)

    def GetTitle(self):
        return(self.__title)

    def GetAuthor_Artist(self):
        return(self.__authorArtist)

    def GetItemID(self):
        return(self.__itemID)

    def GetOnLoan(self):
        return(self.__onLoan)

    def GetDueDate(self):
        return(self.__dueDate)

    def LoanItem(self,borrowerID):
        self.__onLoan = True
        self.__dueDate = self.__dueDate + datetime.timedelta(weeks=3)
        self.__borrowerID = borrowerID

    def ReturnItem(self):
        self.__onLoan = False

    def PrintDetails(self):
        print(self)

class book(libraryItem):
    def __init__(self,t,a,i):
        libraryItem.__init__(self,t,a,i)
        self.__isRequested = False
        self.__RequestedBy = None

    def GetIsRequested(self):
        return(self.__isRequested)

    def SetIsRequested(self,borrowerID):
        self.__isRequested = True
        self.__RequestedBy = borrowerID

    def RetIsRequested(self):
        self.__isRequested = False

    def GetRequestedBy(self):
        return self.__RequestedBy 

    def PrintDetails(self):
        libraryItem.PrintDetails(self)
        print(" Requ: "+str(self.__isRequested)+";\n RequBy: "+str(self.__RequestedBy)+";\n")
        
class CD(libraryItem):
    def __init__(self, t, a, i):
        libraryItem.__init__(self,t,a,i)
        self.__genre = ""

    def GetGenre(self):
        return(self.__genre)

    def SetGenre(self, g):
        self.__genre = g

class borrower:
    def __init__(self,borrowerName,emailAddress,borrowerID):
        self.__borrowerName = borrowerName
        self.__emailAddress = emailAddress
        self.__borrowerID = borrowerID
        self.__itemsOnLoan = 0 

    def __repr__(self):
        return "BORROWER: \n Name: %s;\n Addr: %s;\n ID: %s;\n LoanNo: %d;\n" %(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

    def GetBorrowerName(self):
        return self.__borrowerName

    def GetEmailAddress(self):
        return self.__emailAddress

    def GetBorrwerID(self):
        return self.__borrowerID

    def GetItemsOnLoan(self):
        return self.__itemsOnLoan 

    def UpdateItemsOnLoan(self,i):
        self.__itemsOnLoan += i

    def PrintDetails(self):
        print(self)

def AddBorrower():
    global borrList 
    global currBorrInd
    currBorrInd += 1
    name = str(input("Borrower name: "))
    email = str(input("Borrower email: "))
    newBorr = borrower(name,email,currBorrInd)
    newBorr.PrintDetails()
    borrList.append(newBorr)

def AddBook():
    global bookList
    global currBookInd
    currBookInd += 1
    title = str(input("Book title: "))
    author = str(input("Book author: "))
    newBook = book(title,author,currBookInd)
    newBook.PrintDetails()
    bookList.append(newBook)

def AddCD():
    global CDList
    global currCDInd
    currCDInd += 1
    title =str(input("CD title: "))
    artist = str(input("CD artist: "))
    newCD = CD(title,artist,currCDInd)
    newCD.PrintDetails()
    CDList.append(newCD)

def BorrowBook():
    borrID = int(input("Borrower ID: "))
    itemID = int(input("Book ID: "))
    bookList[itemID].LoanItem(borrID)
    borrList[borrID].UpdateItemsOnLoan(1)

def ReturnBook():
    borrID = int(input("Borrower ID: "))
    itemID = int(input("Book ID: "))
    bookList[itemID].ReturnItem()
    borrList[borrID].UpdateItemsOnLoan(-1)

def BorrowCD():
    borrID = int(input("Borrower ID: "))
    itemID = int(input("CD ID: "))
    CDList[itemID].LoanItem(borrID)
    borrList[borrID].UpdateItemsOnLoan(1)

def ReturnCD():
    borrID = int(input("Borrower ID: "))
    itemID = int(input("CD ID: "))
    CDList[itemID].ReturnItem()
    borrList[borrID].UpdateItemsOnLoan(-1)

def RequestBook():
    borrID = int(input("Borrower ID: "))
    itemID = int(input("Book ID: "))
    bookList[itemID].SetIsRequested(borrID)

def PrintAll():
    for i in borrList:
        i.PrintDetails()
    for i in bookList:
        i.PrintDetails()
    for i in CDList:
        i.PrintDetails()

def Initialize():
    global borrList
    global bookList
    global CDList
    global currBorrInd
    global currBookInd
    global currCDInd
    borrList = []
    bookList =[]
    CDList = []
    currBorrInd = -1
    currBookInd = -1 
    currCDInd = -1 
    a = book("Don Quijote de la Mancha","Miguel de Cervantes Saavedra",0)
    b = borrower("Stefan","stefan_heng@qq.com",0)
    bookList.append(a)
    borrList.append(b)
    currBookInd += 1
    currBorrInd += 1

def PrintChoices():
    print("1: Add new borrower")
    print("2: Add new book")
    print("3: lu Add new CD")
    print("4: Borrow book")
    print("5: Return book")
    print("6: Borrow CD")
    print("7: Return CD")
    print("8: Request book")
    print("9: Print all")

def ActionLoop():
    dAct = {1:AddBorrower,2:AddBook,3:AddCD,4:BorrowBook,5:ReturnBook,6:BorrowCD,7:ReturnCD,8:RequestBook,9:PrintAll}
    choice = int(input("Input your choice: "))
    if choice == -1:
        print("See ya")
    else:
        dAct[choice].__call__()
        ActionLoop()

def Main():
    global borrList
    global bookList
    global CDList
    global currBorrInd
    global currBookInd
    global currCDInd
    
    Initialize()
    PrintChoices()
    ActionLoop()

print("Welcome to the library")
Main()