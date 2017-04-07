'''
Created on Mar 25, 2017

@author: lakinduakash
'''
class Stack:
    
    def __init__(self):
        self.__list=[]
        
    def push(self,item):
        self.__list.append(item)
        
    def pop(self):
        return self.__list.pop()
        
    def isEmpty(self):
        return self.__list==[]
    def size(self):
        return len(self.__list)


class Registry:
    
    def __init__(self):
        self.oStck=Stack()
        
    def printIns(self,postfixE):
        
        so=self.oStck
        j=1
        
        for i in postfixE:
            
            if i.isalpha():
                so.push(i)
                
            elif i=='+':
                od1=so.pop()
                od2=so.pop()
                t='TEMP'+str(j)
                print('LD ',od2)
                print('AD ',od1)
                print('ST ',t)
                so.push(t) 
                j=j+1                   
            elif i=='-':
                od1=so.pop()
                od2=so.pop()
                t='TEMP'+str(j)
                print('LD ',od2)
                print('SB ',od1)
                print('ST ',t)
                so.push(t) 
                j=j+1     
                    
            elif i=='*':
                od1=so.pop()
                od2=so.pop()
                t='TEMP'+str(j)
                print('LD ',od2)
                print('ML ',od1)
                print('ST ',t)
                so.push(t) 
                j=j+1     
                    
            elif i=='/':
                od1=so.pop()
                od2=so.pop()
                t='TEMP'+str(j)
                print('LD ',od2)
                print('DV ',od1)
                print('ST ',t)
                so.push(t) 
                j=j+1     
                    
            else:
                print('Invalid Post-fix expression.')
                
                    
r=Registry()

print("######### INSTRUCTIONS ##########")
print("----------------------------------")
print("LD A which places the operand A into the register")
print("ST A which places the contents of the register into the variable A")
print("AD A which adds the contents of variable A to the register")
print("SB A which subtracts the contents of the variable A from the register")
print("ML A which multiplies the contents of the register by the variable A")
print("DV A which divides the contents of the register by the variable A\n\n")
print('')

postfixE=input("Enter a post-fix expression : ")
print('')
r.printIns(postfixE)



        
        