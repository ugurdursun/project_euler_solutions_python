import math


def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

if __name__=='__main__':

    for i in reversed(range(100,1000)):
        for j in reversed(range(100,1000)):
            a = int(i*j)
            if a == rev(a):

                 print(a) 

             
            
            
                                 
        
        
    
    
        
        

