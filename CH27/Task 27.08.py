#Task 27.08
#S3CS3 Stefan Yuzhao Heng

class assessment:
	def __init__(self,t,m):
		self.__assessmentTitle = t
		self.__maxMarks = m 

	def __repr__(self):
		return "Assessment title: %s; Max marks: %s;" % (self.__assessmentTitle,self.__maxMarks)

	def PrintDetails(self):
		print(self)

class lesson:
	def __init__(self,t,d,r):
		self.__lessonTitle = t
		self.__duration = d
		self.__requireLab = r

	def __str__(self):
		return "Lesson title: %s; Duration: %s; LabRequired: %s;" % (self.__lessonTitle,self.__duration,self.__requireLab)

	def PrintDetails(self):
		print(self)

class course:
	def __init__(self,t,m):
		self.__courseTItle = t
		self.__maxStudents = m
		self.__lessonNo = 0
		self.__courseLesson = []
		self.__courseAssessment = assessment

	def AddAssessment(self,t,m):
		self.__courseAssessment = assessment(t,m)

	def AddLesson(self,t,d,r):
		self.__lessonNo += 1
		self.__courseLesson.append(lesson(t,d,r))

	def PrintDetails(self):
		print("Course title:",self.__courseTItle)
		print("Max students:",self.__maxStudents)
		print(self.__courseAssessment)
		for i in range(self.__lessonNo):
			self.__courseLesson[0].PrintDetails()

a = course("Computer Science",40)
a.AddAssessment("Programming",100)
a.AddLesson("Top-down Design",60,True)
a.PrintDetails()