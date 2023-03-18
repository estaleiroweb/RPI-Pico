from machine import Pin
import time

class Set:
    def __setattr__(self, name, value):
        if name=='__dict__': self.__dict__=value
        if name[0:4]=='set_': return None
        try:
            return getattr(self, 'set_'+name)(value)
        except:
            ...
        k=self.__dict__.keys()
        if '_'+name in k or '__'+name in k: return
        print(name)
        try:
            # setattr(self, name, value)
            self.__dict__[name] = value
        except:
            ...
        print(self.__dict__)

class Get:
    def __getattr__(self, name):
        if name[0:4]=='get_': return None
        try:
            return getattr(self, 'get_'+name)()
        except:
            ...
        k=self.__dict__.keys()
        if name in k: return self.__dict__[name]
        name='_'+name
        if name in k: return self.__dict__[name]
        name='_'+name
        if name in k: return self.__dict__[name]
        return None

class Farol(Get):
    # _methods=None
    
    def __init__(self,pinGreen:int,pinYellow:int,pinRed:int,pinButton:'int|None'=None,name:str='Farol'):
        '''Constuctor'''
        # if self._methods==None: 
        #     self._methods=([i for i in dir(self) if i!='__init__' and str(type(getattr(self,i)))=="<class 'bound_method'>"])

        print(name)
        self.__dict__={
            '_name':name,
            '_leds':[Pin(pinGreen, Pin.OUT), Pin(pinYellow, Pin.OUT), Pin(pinRed, Pin.OUT)],
            '_btn':Pin(pinButton, Pin.IN, Pin.PULL_UP) if pinButton!=None else None,
            '_dep':None,
        }
        # self._name=name
        # self._leds=[Pin(pinGreen, Pin.OUT), Pin(pinYellow, Pin.OUT), Pin(pinRed, Pin.OUT)]
        # self._btn=Pin(pinButton, Pin.IN, Pin.PULL_UP) if pinButton!=None else None
        # self._dep=None
        for i in self._leds: i.value(0)
        # print(globals())
        # print(self['setFarol'])
        # print(dir(self))
        print(self.__dict__)
        # print([self.__class__,self.__module__,self.__qualname__])
        

    def set_dep(self, dep:'Farol'):
        '''Config the dependence Farol'''
        self._dep=dep #if type(dep)==Farol else None
        return self
    
    def set_farol(self,val):
        return self
        
    def get_farol(self):
        return 'variavel Farol'

    def setRed(self):
        ...
        
    def moddep(self,dep:'None|Farol|list[Farol]'):
        pass
        
f1=Farol(13,14,15,12,'Farol 1')
f2=Farol(16,17,18,12,'Farol 2')

f1.set_dep(f2)
f2.set_dep(f1)

print(f1.leds)
print(f1.farol)
# farol1=[Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT), Pin(12, Pin.IN, Pin.PULL_UP)] # Green, Yellow, Red, Button
# farol2=[Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), farol1[3]] # Green, Yellow, Red, Button

# def wait(t:int,farol:list[Pin]):
#     ini=time.time()
#     while time.time() - ini <= t and farol[3].value():
#         pass


# while True:
#     print('Green/Red')
#     seFarol(farol1,[1,0,0])
#     seFarol(farol2,[0,0,1])
#     wait(5,farol1)
    
#     print('Yellow/Red')
#     seFarol(farol1,[0,1,0])
#     time.sleep(2)
    
#     print('Red/Green')
#     seFarol(farol1,[0,0,1])
#     seFarol(farol2,[1,0,0])
#     wait(5,farol2)

#     print('Red/Yellow')
#     seFarol(farol2,[0,1,0])
#     time.sleep(2)
 