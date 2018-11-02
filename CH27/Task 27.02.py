#Task 27.02
#S3CS3 Stefan Yuzhao Heng

import datetime

class libraryItem:
    def __init__(self, t, a, i):
        self.__title = t
        self.__authorArtist = a
        self.__itemID = i
        self.__onLoan = False
        self.__dueDate = datetime.date.today()

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

    def Borrowing(self):
        self.__onLoan = True
        self.__dueDate = self.__dueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__onLoan = False

    def PrintDetails(self):
        print(self.__title,';',self.__authorArtist,';',self.__itemID,';',self.__onLoan,';',self.__dueDate)

class Book(libraryItem):
    def __init__(self, t, a, i):
        libraryItem.__init__(self, t, a, i)
        self.__isRequested = False

    def GetIsRequested(self):
        return(self.__isRequested)

    def SetIsRequested(self):
        self.__isRequested = True
        
class CD(libraryItem):
    def __init__(self, t, a, i):
        libraryItem.__init__(self, t, a, i)

        self.__genre = ""
    def GetGenre(self):
        return(self.__genre)

    def SetGenre(self, g):
        self.__genre = g

'''
C=[]
C.append(CD('And Justice For All','Metallica',123))
C.append(CD('Dark Side Of The Moon','Pink Floyd',234))
C.append(CD('Black Sabbath','Black Sabbath',345))
C.append(CD('hahahha','haha',456))
C.append(CD('hihihi','hihi',567))
B=[]
B.append(Book('12 Rules for Life','Jordan Peterson',678))
B.append(Book('White Fang','Jack London',789))
B.append(Book('I am a book','me',890))
B.append(Book('hi','hahh',111))
for i in C:
    i.PrintDetails()
for i in B:
    i.PrintDetails()
'''
a = Book("rr","aa",3)
a.PrintDetails()