class alumno:

    def __init__(self ,matricula,nombre,edad,):
        self.matricula=matricula
        self.nombre=nombre
        self.edad=edad
        self.calif= []
        
    
        pass
   
    def setCalif(self, calif):
        self.calif.append(calif)
        
        return calif
    
    def Setpromedio(self):

        ZeroDivisionError
        try:
            promedio =sum(self.calif)/len(self.calif)
        except Exception as e:
            print(f"Error: {e}")    
        return promedio
    
    

    #def  __str__ (self):
    # return f"{self.matricula}|{self.nombre}|{self.edad}|{self.calif}"

    #  .............heredar................

class alumnograduado(alumno):
    def __init__(self, matricula, nombre, edad):
        super().__init__(matricula, nombre, edad)
        self.graduado=None 
        self.fecha = None
        self.tesis = None
        pass

    def set_graduado(self,graduado, fecha,tesis):
        self.graduado=graduado
        self.fecha = fecha
        self.tesis = tesis


    def chkGrad(self):
        promedio = self.promedio()

        if promedio <= 6:
            graduado = "No"
        else:
            graduado = "Si"
        return graduado
    
    def chckFecha(self):
        promedio = self.promedio()
        
        fecha = ""
        if promedio <= 5.9:
            fecha = "N/A"
        else:
            fecha = self.fecha
        
        return fecha
   
    def  __str__ (self):
       return f"{self.matricula}| {self.nombre}|{self.edad}   |{self.calif} ||{self.graduado}    |{self.fecha}      |{self.tesis}"
    

#--..-----imprimir parte 2 -----
   # def printalum(alumnograduado):
    #print(f"Nombre Completo:{self.nombre} edad:{self.edad} matricula:{self.matricula} graduado el:{self.fecha}con Tesis:{self.tesis}")
    #return 

 

