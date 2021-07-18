class Policy:

    policy = 'Trucaller' # class variables

    def __init__(self,name):
        self.name = name # instance variable

    def say_hi(self):
        print('Hello',self.name)


p = Policy('ankan')

p.say_hi()
print(p.policy)