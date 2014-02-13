from random import randint


class Osob:
    def __init__(self, param1, param2, param3, param4):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.itog = self.param1 + self.param2 + self.param3 + self.param4

    def show(self):
        print self.param1,self.param2, self.param3, self.param4

class Population:
    def __init__(self):
        self.list=[]
        for i in range(6):
            self.list.append(Osob(randint(1,20),randint(1,20),randint(1,20),randint(1,20)))

    def mix(self,num1,num2):
        param1 = max(self.list[num1].param1,self.list[num2].param1)
        param2 = max(self.list[num1].param2,self.list[num2].param2)
        param3 = max(self.list[num1].param3,self.list[num2].param3)
        param4 = max(self.list[num1].param4,self.list[num2].param4)
        result = Osob(param1, param2, param3, param4)
        return result

    def generation(self):
        result = []
        self.list.sort(key = lambda x: x.itog)
        result.append(self.mix(2,3))
        result.append(self.mix(2,4))
        result.append(self.mix(2,5))
        result.append(self.mix(3,4))
        result.append(self.mix(3,5))
        result.append(self.mix(4,5))
        result.sort(key = lambda x: x.itog)
        self.list = result

    def show(self):

        for i in self.list:
            print self.list.index(i)+1,  i.itog




population = Population()
print 'basic population'
population.show()

for i in range(10):
    print 'genetation' + str(i+2)
    population.generation()
    population.show()
    if population.list[0].itog==population.list[5].itog:
        print 'no more reason to continue'
        break


