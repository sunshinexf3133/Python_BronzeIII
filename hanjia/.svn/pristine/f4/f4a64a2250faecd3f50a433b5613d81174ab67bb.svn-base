#coding:utf-8
#多态
#创建一个名为Undercut的简单游戏。在这个游戏中，
#两个玩家同时选择一个1-10的整数，如果一个玩家选择
#的整数比对方选择的整数小1，则该玩家获胜，否则算打平。
#例如，如果A和B一起玩游戏Undercut，且他们选择的数字
#分别为9和10，则A获胜；如果他们分别选择4和7，则打成平手
#也可以两个电脑玩家一起玩，或两个人类玩家一起玩
#example_Polymorphism.py

import random

class Player :
    def __init__(self,name) :
        self._name = name
        self._score = 0

    def reset_score(self) :
        self._score = 0

    def incr_score(self) :
        self._score = self._score + 1

    def get_name(self) :
        return self._name

    def __str__(self) :
        return  "name = %s,score = %s" %(self._name,self._score)

    def __repr__(self) :
        return 'Player(%s)'%str(self)

class Human(Player) :
    def __repr__(self) :
        return 'Human(%s)' %str(self)

    def get_move(self) :
        while True :
            try :
                n = int(raw_input('%s move (1-10):'%self.get_name()))
                if 1 <= n <= 10 :
                    return n
                else :
                    print('Oops!')
            except :
                print('Oops!')

class Computer(Player) :
    def __repr__(self) :
        return 'Computer(%s)' %str(self)

    def get_move(self) :
        return random.randint(1,10)

def play_undercut(p1,p2) :
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print("%s move:%s" %(p1.get_name(),m1))
    print("%s move:%s" %(p2.get_name(),m2))
    if m1 == m2 - 1 :
        p1.incr_score()
        return p1,p2,'%s wins!' %p1.get_name()
    elif m2 == m1 - 1:
        p2.incr_score()
        return p1,p2,'%s wins!' %p2.get_name()
    else :
        return p1,p2,'draw:no winner'

if __name__ == "__main__" :
    c = Computer('CCC')
    h = Human('HHH')
    print play_undercut(c,h)
