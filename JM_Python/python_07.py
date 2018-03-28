# coding=UTF-8
# 面向对象编程
class Person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is',self.name)
p = Person('Swaroop')
print(p) # 输出<__main__.Person object at 0x0000000001E822E8>
p.say_hi()
# 同理
Person('Disy').say_hi()

# 类变量与对象变量
class Robot:
    '''表示有一个带名字的机器人。'''

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self,name):
        '''初始化数据'''
        self.name = name
        print('(Initializing {})'.format(self.name))

        # 当有机器人被创建时
        # 将会增加机器人口数量
        Robot.population += 1

    def die(self):
        '''我挂了'''
        print('{} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {} robots working.'.format(Robot.population))

    def say_hi(self):
        '''来自机器人的诚挚问候

        没问题，你做得到。'''
        print('Greetings, my masters call me {}'.format(self.name))

    @classmethod
    def how_many(cls):
        '''打印出当前的人口数量'''
        print('We have {} robots.'.format(cls.population))

r1 = Robot('faker')
r1.say_hi()
r1.how_many()

r2 = Robot('marin')
r2.say_hi()
r2.how_many()

r1.die()
r1.how_many()
r2.how_many()
Robot.how_many()

r2.die()
r1.how_many()
r2.how_many()
Robot.how_many()

print(Robot.__doc__)
print(Robot.say_hi.__doc__)

# 继承
class SchoolMember:
    '''代表任何学校里的成员'''

    # 类变量
    membersNum = 0

    # 对象变量
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))
        SchoolMember.membersNum += 1

    # 对象方法
    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:{} Age:{}'.format(self.name,self.age),end=' ')

    # 类方法
    @classmethod
    def how_many(cls):
        print('There are {} member in school'.format(cls.membersNum))

class Teacher(SchoolMember):
    '''代表一位老师'''
    teachersNum = 0
    def __init__(self,name,age,course):
        SchoolMember.__init__(self,name,age)
        self.course = course
        print('(Initialized Teacher:{})'.format(self.name))
        Teacher.teachersNum += 1
    def tell(self):
        SchoolMember.tell(self)
        print('Course:{}'.format(self.course))
    @classmethod
    def how_many_t(cls):
        SchoolMember.how_many()
        print('There are {} teachers in school'.format(cls.teachersNum))

class Student(SchoolMember):
    '''代表一位学生'''
    studentsNum = 0
    def __init__(self,name,age,score):
        SchoolMember.__init__(self,name,age)
        self.score = score
        print('(Initialized Student:{})'.format(self.name))
        Student.studentsNum += 1
    def tell(self):
        SchoolMember.tell(self)
        print('Score:{}'.format(self.score))
    @classmethod
    def how_many_s(cls):
        SchoolMember.how_many()
        print('There are {} students in school'.format(cls.studentsNum))

Student.how_many_s()
Teacher.how_many_t()
SchoolMember.how_many()
t1 = Teacher('faker',23,'mid')
s1 = Student('scout',21,'88')
s1.how_many_s()
t2 = Teacher('dade',25,'mid')
s1.how_many_s()
t2.how_many_t()

members = [t1,t2,s1]
for m in members:
    m.tell()
