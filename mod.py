class human:
   
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
        print(self.__name)
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age
        print(self.__age)
        
class employee:
    
    def __init__(self,salary,company):
        self.__salary=salary
        self.__company=company
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        self.__salary=salary
        print(self.__salary)
    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self,company):
        self.__company=company
        print(self.__company)
        
class teacher(human,employee):
    def __init__(self,name,age,salary,company,pay):
        human.__init__(self,name,age)
        employee.__init__(self,salary,company)
        self.pay=pay
    def salarystmt(self):
        return self.salary+self.pay
    def info(self):
        print(f"Teacher's name is {self.name}, she is {self.age} years, get {self.salarystmt()} salary, works at {self.company}")

    def report(self,file):
        file1=open(file,"w")
        a=(f"Teacher's name is {self.name}, she is {self.age} years, get {self.salarystmt()} salary, works at {self.company}")
        file1.write(a)