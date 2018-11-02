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
        self.__borrowerID = ""

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
        print(self.__title,';',self.__authorArtist,';',self.__itemID,';',self.__onLoan,';',self.__dueDate)

class Book(libraryItem):
    def __init__(self,t,a,i):
        libraryItem.__init__(self,t,a,i)
        self.__isRequested = False

    def GetIsRequested(self):
        return(self.__isRequested)

    def SetIsRequested(self):
        self.__isRequested = True

    def PrintDetails(self):
        libraryItem.PrintDetails(self)
        print(self.__isRequested)
        
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
        return "Name: %s; Addr: %s; ID: %s; onLoan: %d" %(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

    def GetBorrowerName(self):
        return self.__borrowerName

    def GetEmailAddress(self):
        return self.__emailAddress

    def GetBorrwerID(self):
        return self.__borrowerID

    def GetItemsOnLoan(self):
        return self.__itemsOnLoan 

    def UpdateItemsOnLoan(self):
        self.__itemsOnLoan += 1

    def PrintDetails(self):
        print(self.__borrowerName,";",self.__emailAddress,";",self.__borrowerID,";",self.__itemsOnLoan)

a = Book("Don Quijote de la Mancha","Miguel de Cervantes Saavedra",208032)
a.PrintDetails()
b = borrower("Stefan","stefan_heng@qq.com",182406)
b.PrintDetails()

def ActionBorrow(currBook,currBorr):
    currBook.LoanItem(currBorr.GetBorrwerID())
    currBorr.UpdateItemsOnLoan()

ActionBorrow(a,b)
a.PrintDetails()
b.PrintDetails()