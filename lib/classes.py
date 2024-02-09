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
            promedio = sum(self.calif)/len(self.calif)
        except Exception as e:
            print(f"error desconocido:{e}")
        return promedio
   
    def  __str__ (self):
        return f"{self.matricula},{self.nombre},{self.edad},{self.calif},{self.promedio}"

    #  .............heredar................

class alumnograduado(alumno):
    def __init__(self, matricula, nombre, edad, graduado,fecha, tesis):
        super().__init__(matricula, nombre, edad)
        self.graduado = graduado
        self.fecha = fecha
        self.tesis = tesis
        pass
    def chkGrad(self):
        promedio = self.promedio()
        if promedio <= 6:
            print("\033[31m si \033[0m")
        else:
            print( "n/a")
        pass

    
#--..-----imprimir parte 2 -----
   # def printalum(alumnograduado):
    #print(f"Nombre Completo:{self.nombre} edad:{self.edad} matricula:{self.matricula} graduado el:{self.fecha}con Tesis:{self.tesis}")
    #return 
        
 

