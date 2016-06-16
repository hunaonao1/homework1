# import requests
# from bs4 import BeautifulSoup
import random
import re
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'huzihao')

    strb = '\n\rhello huzihao\r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    print 3, stra.startswith('hel')
    print 4, stra.endswith('hel')
    print 5,stra+strb
    print 6,len(stra)
    print 7,'-'.join(['a','b','c'])
    print 8,strb.split(' ')
    print 9,strb.find('zi')

def demo_peration():
    print 1, 5/2
    print 2, 1<2,5>2
    print 3, 2<<3
    print 4, 4^6
    x=2
    y=3.4
    print x,y,type(x),type(y)

def demo_buildinfunction():
    print 1,max(2,3),min(5,6)
    print 2,len('xxx'),len([1,2,3])
    print 3,range(1,10,2)
    print 5,dir(list)
    x=2
    print 6,eval('x+3')
    print 7,chr(65),ord('a')
    print 8,divmod(11,3)

def demo_controlflow():
    score=65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 'C'
    while score<100:
        print score
        score+=10
    score=65
    for i in range(0,10,2):
        if i==0:
            pass #do_special
        if i<5:
            continue
        print 3,i
        if i==6:
            break

def demo_list():
    lista=[1,2,3]#vector
    print 1, lista
    listb=['a','1','b','1.1']
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,'a'in listb
    listb.insert(0,'www')
    print 7,listb
    listb.pop(1)
    print 8,listb
    listb.reverse()
    print 9,listb
    listb.sort()
    print 10,listb

    tuplea=(1,2,3)
    listaa=[1,2,3]
    listaa.append(4)
    print 11,listaa

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def demo_dict():
    dicta={4:16,1:1,2:4,3:9}
    print 1, dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1)
    #for map<int,int>::iterator it =x.begin();it!=end()
    for key,value in dicta.items():
        print 'key-value:',key,value
    dictb={'+':add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*']='x'
    print 6,dictb
    del dicta[1]
    print 7,dicta

def demo_set():
    seta=set((1,2,3))
    setb=set((2,3,4))
    print 1,seta
    print 2,seta.intersection(setb),seta&setb
    print 3,seta-setb
    print 4,seta|setb,seta.union(setb)
    seta.add('x')
    print 5,seta.difference(setb)

class User:
    type='USER'
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def __repr__(self):
        return 'Im'+self.name+' '+str(self.uid)

class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid,group):
        User.__init__(self,name,uid)
        self.group = name

    def __repr__(self):
        return 'Im' + self.name + ' ' + str(self.uid)+ ' ' + self.group

class Guest(User):
    type = 'GUEST'

    #def __init__(self, name, uid):
        #User.__init__(self,name,uid)

    def __repr__(self):
        return 'Im guest' + self.name + ' ' + str(self.uid)
def create_user(type):
    if type=='USER':
        return User('u1',1)
    elif type=='ADMIN':
        return Admin('a1',101,'g1')
    else:
        return Guest('gu1',201)

def demo_exception():
    try:
        print 2/1
        #if type=='c':
        raise Exception('Raise Error')
    except Exception as e:
        print 'error:',e
    finally:
        print 'clean up'

def demo_random():
    #random.seed(1)
    print 1,int(random.random()*100)
    print 2,random.randint(0,200)
    print 3,random.choice(range(0,100))
    print 4,random.sample(range(0,100),5)
    a=[2,3,4,5,6,7]
    random.shuffle(a)
    print 5,a

def demo_re():
    str='abc123def12gh15'
    p1=re.compile('[\d]+')
    p2=re.compile('[\d]')
    print 1, p1.findall(str)
    print 2, p2.findall(str)

    str='a@163.com;b@gmail.com;c@qq.com;d@163.com;z@qq.xom'
    p3=re.compile('[\w]+@[^qq]+\.com')
    print 3, p3.findall(str)

    str='<html><h>title</h><body>xxx</body></html>'
    p4=re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    p5=re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5, p5.findall(str)

    str='xx2016-06-11yy'
    p6=re.compile('\d{4}-\d{2}-\d{2}')
    print 6, p6.findall(str)

if __name__ == '__main__':
    print 'hello songying'
    #demo_string()
    #demo_peration()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    #demo_set()
    '''
    user1=User('u1',1)
    print 1,user1
    admin1=Admin('a1',1,'g1')
    print 2,admin1
    print create_user('GUESY')
    demo_exception()
    '''
    #demo_random()
    demo_re()