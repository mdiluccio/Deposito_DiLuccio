class Punto:
    
    def __init__(self, x,y):
        self.x = x 
        self.y = y
    
   
    def muovi(self, dx, dy):
        self.x = dx
        self.y = dy
       # print(dx, dy)
        
    """@classmethod
    def distanza_da_origine(cls):"""
        
 
punto1 = Punto(4,5)  
print("Prima", punto1.x, punto1.y)  
punto1.muovi(3,6)
print("Dopo",punto1.x, punto1.y) 

        
    
        