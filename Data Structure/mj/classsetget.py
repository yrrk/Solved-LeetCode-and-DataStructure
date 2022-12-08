class Students:
    def __init__(self) -> None:
        self.classroom={}
        self.attendence={}

    def set_marks(self,key,value):
        self.classroom[key]=value
    
    def get_marks(self,key):
        return self.classroom[key]


class StudAttendance(Students):
    def __init__(self) -> None:
        super().__init__()


    def set_attendance(self,key,value):
        self.attendence[key]=value

    def get_attendance(self,key):
        return self.attendence[key]



#Without inheritance
# inwk=Students()
# inwk.set_marks("yaksh",20)
# inwk.set_marks("mj",25)
# inwk.set_marks("hansil",3)
# inwk.set_marks("rahul",10)
# inwk.set_marks("jagdish",0)
# print(inwk.get_marks("mj"))


#With inheritance
DusviClass=StudAttendance()
DusviClass.set_attendance("yaksh",True)
DusviClass.set_marks("yaksh",20)
DusviClass.set_attendance("mj",False)
DusviClass.set_marks("mj",30)
DusviClass.set_attendance("hansil",False)
DusviClass.set_marks("hansil",2)
DusviClass.set_attendance("rahul",True)
DusviClass.set_marks("rahul",12)
DusviClass.set_attendance("Jagdish",False)
DusviClass.set_marks("jagdish",-20)
print(DusviClass.get_attendance("mj"))
print(DusviClass.get_marks("mj"))