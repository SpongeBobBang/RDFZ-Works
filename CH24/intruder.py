stateList = ["INACTIVE","ACTIVE","ALERT","RINGING"]
actionList = ["pressButton","enterPin","activeSensor"]

class system:
    def __init__(self):
        self.time = 0
        self.state = stateList[0]
        self.action = ""
    
    def displayAction(self):
        print("You can:")
        for i in range(len(actionList)):
            print(i+1,"-",actionList[i])
    
    def action1(self):
        if self.state == stateList[0]:
            self.state = stateList[1]
        self.time += 1
        self.displayStatus()

    def action2(self):
        if self.state != stateList[0]:
            self.state = stateList[0]
        self.time += 1
        self.displayStatus()

    def action3(self):
        if self.state == stateList[1]:
            self.state = stateList[2]
        self.time += 1
        self.displayStatus()
        if self.state == stateList[2]:
            self.state = stateList[3]
            self.time += 2
            self.displayStatus()

    def displayStatus(self):
        print("Current state:",self.state,", Time:",self.time)
        
    def main(self):
        print("Intruder detection system")
        self.displayAction()
        while True:
            self.action = input("Enter your action:")
            if self.action == "1":
                self.action1()
            elif self.action == "2":
                self.action2()
            elif self.action == "3":
                self.action3()
            else:
                print("End")
                break

s=system()
s.main()
