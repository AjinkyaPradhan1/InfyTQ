class Instructor:

    def __init__(self):
        self.__name = None
        self.__techSkills = None
        self.__experience = None
        self.avgfeed = None

    def set_name(self,name):
        self.__name = name

    def set_techSkills(self,techSkills):
        self.__techSkills = techSkills

    def set_experience(self,experience):
        self.__experience = experience

    def set_avgfeed(self,avgfeed):
        self.__avgfeed = avgfeed

    def get_name(self):
        return self.__name 

    def get_techSkills(self):
        return self.__techSkills 

    def get_experience(self):
        return self.__experience 

    def get_avgfeed(self):
        return self.__avgfeed 

    def check_eligibility(self):
        if self.__experience>3 and self.__avgfeed>=4.5:
            return True
        elif self.__experience<3 and self.__avgfeed<4:
            return True
        else:
            return False

    def allocate_course(self,techSkills):
        if ((techSkills==self.__techSkills) or (techSkills== 'CSE')):
            return True
        else:
            return False


    







