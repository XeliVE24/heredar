class alumno:

    def __init__(self ,matricula,nombre,edad,):
        self.matricula=matricula
        self.nombre=nombre
        self.edad=edad
        pass

    def Calificaciones(self,cal1=None,cal2=None,cal3=None,cal4=None,cal5=None):
        self.cal1=cal1
        self.cal2=cal2
        self.cal3=cal3
        self.cal4=cal4
        self.cal5=cal5
   
    def  __str__ (self):
        return f"{self.matricula},{self.nombre},{self.edad},{self.cal1},{self.cal2},{self.cal3},{self.cal4},{self.cal5},{self.promedio},{self.graduado},{self.fecha},{self.tesis}"

    def Promedio(self):
        ZeroDivisionError
        try:
            self.promedio=((self.cal1+self.cal2+self.cal3+self.cal4+self.cal5)/5)
        except Exception as e:
         print(f"error desconocido:{e}")
    
        return
    
    def Graduado(self):
        if self.promedio >= 6:
            return "si"
        else:
            return "n/a"
    

        
 

