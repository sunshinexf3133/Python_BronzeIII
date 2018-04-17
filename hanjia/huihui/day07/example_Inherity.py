#coding:utf-8
#继承
#开发一款游戏，其中涉及人类玩家和计算机玩家。
#1.假设有两类玩家：人和计算机。主要差别在于，人通过键盘输入走法，
#而计算机使用函数生成走法。除此之外，这两类玩家相同，他们都有名称和得分
#2.编写的Human类用于表示人类玩家，为此，一种方法是通过复制并粘贴新建
#Player类的一个拷贝，再添加让玩家走棋的方法make_move(self)。
#另一种更佳的做法是使用继承。我们让Human类继承Player类的所有变量和方法，
#这样就不需要再次编写他们了
#3.在python中，pass语句表示：“什么都不做”
#4.(重写方法)继承的一个小瑕疵是，h的字符串表示为Player，但更为准确的
#说法应该是Human，为了修复这种问题，可给Human定义方法__repr__:
#players.py

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
    #pass
    def __repr__(self) :
        return 'Human(%s)'%str(self)

if __name__ == "__main__" :
    p = Player('LLL')
    print str(p)
    p.incr_score()
    print p
    p.reset_score()
    print p
    print'--------------fengexian1--------------'
    h = Human('HHH')
    print h
    h.incr_score()
    print h
    h.reset_score()
    print h
    #print p
