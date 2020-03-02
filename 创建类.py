class Student:  #Student类：包含成员变量和成员方法
    def __init__(self,mname,mnumber):  #构造方法，用于创建对象
        self.name = mname      #定义成员变量
        self.number = mnumber
        self.Course_Grade = {}
        self.GPA = 0
    def getInfo(self):           #获取姓名和学号方法
        print(self.name,self.number)

s1 = Student("wang","317000010")   #创建s1对象
s1.getInfo()
s2 = Student("zhang","317000011")   #创建s2对象
s2.getInfo()

#变量值的修改
class Student:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.gpa = 0

    def getInfo(self):
        print(self.name,self.number)

    def setGpa(self,gpa):
        self.gpa = gpa

s3 = Student("Li","31000013")
s3.setGpa(3.5)

print("我的名字是"+s3.name+",学号为"+s3.number,",平均绩点为",s3.gpa)
