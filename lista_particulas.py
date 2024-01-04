from particula import Particula 
import json

class Lista_Particulas:
    def __init__(self) -> None:
        self.__particula = []

    def __str__(self) -> str:
        return "".join(
            str(v)+"\n" for v in self.__particula
        )

    def __len__(self):
        return(
            len(self.__particula)
        )

    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particula):
            particulas = self.__particula[self.cont]
            self.cont += 1
            return particulas
        
        else:
            raise StopIteration

    def __lt__(self,other):
        return self.part.id < other.id


    def agregar_final(self, particula: Particula):
        self.__particula.append(particula)

    def agregar_inicio(self, particula: Particula):
        self.__particula.insert(0, particula)

    def mostrar(self):
        for i in self.__particula:
            print(i)
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista = json.load(archivo)

                # ** --> para que cada llave rerpresente el nombre del atributo
                # Y lo coloque en el lugar correspondiente
                self.__particula = [Particula(**particula) for particula in lista]

                return 1
        except:
            pass

        try:
            with open(ubicacion,"r") as archivo:
                lista = json.load(archivo)
                self.__particula = [
                    Particula(
                        particula["id"],
                        particula["origen"]["x"],
                        particula["origen"]["y"],
                        particula["destino"]["x"],
                        particula["destino"]["y"],
                        particula["velocidad"],
                        particula["color"]["red"],
                        particula["color"]["green"],
                        particula["color"]["blue"]
                    ) for particula in lista
                ]
            return 1
        except:
            return 0

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                lista = [particula.to_dict() for particula in self.__particula]
                print(lista)
                json.dump(lista, archivo, indent=4)
                return 1
                #archivo.write(str(self))

        except:
            return 0

    @property
    def part(self):
        return self.__particula

    def lista_ordenar_id(self):
        self.__particula.sort()

    