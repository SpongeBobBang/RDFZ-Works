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
        return "Item: \n Title: %s;\n Aut/Art: %s;\n ID: %d;\n OnLoan: %s;\n Due: %s;\n Borrower: %s;\n" % (self.__title,self.__authorArtist,self.__itemID,self.__onLoan,self.__dueDate,self.__borrowerID)

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

class Book(libraryItem):
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
        return "Borrower: \n Name: %s;\n Addr: %s;\n ID: %s;\n LoanNo: %d;\n" %(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

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
        print(self)

a = Book("Don Quijote de la Mancha","Miguel de Cervantes Saavedra",208032)
b = borrower("Stefan","stefan_heng@qq.com",182406)
a.PrintDetails()
b.PrintDetails()

def ActionBorrow(currBook,currBorr):
    currBook.LoanItem(currBorr.GetBorrwerID())
    currBorr.UpdateItemsOnLoan()
    currBook.SetIsRequested(currBorr.GetBorrwerID())

ActionBorrow(a,b)
a.PrintDetails()
b.PrintDetails()