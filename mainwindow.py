from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor
from random import randint
from lista_particulas import Lista_Particulas
from particula import Particula
from pprint import pprint
from algoritmos import puntos_mas_cercanos
from grafos_01 import agregar,get_dicc 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lista_particulas = Lista_Particulas()

        self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)

        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)    

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        
        self.scene = QGraphicsScene()
        self.ui.scene.setScene(self.scene)

        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)
        self.ui.ordenar_id_tabla_pushButton.clicked.connect(self.ordenar_id_tabla)
        self.ui.ordenar_distancia_tabla_pushButton.clicked.connect(self.ordenar_distancia_tabla)
        self.ui.ordenar_velocidad_tabla_pushButton.clicked.connect(self.ordenar_velocidad_tabla)

        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionPuntos_Cercanos.triggered.connect(self.mostrar_puntos_cercanos)
        self.puntos = []

        self.ui.mostrar_grafo_pushButton.clicked.connect(self.mostrar_grafo)
        #self.ui.dibujar_grafo_pushButton.clicked.connect(self.dibujar_grafo)

    @Slot()
    def mostrar_grafo(self):
        for particula in self.lista_particulas:
            agregar(particula.origen_x,particula.origen_y,particula.destino_x,particula.destino_y,int(particula.distancia))
        
        d = get_dicc()
        self.ui.plainTextEdit.clear()
        for key, value in d.items():#Nos retorna llave y valor
            print(key, value)
            a = key
            b = value
            self.ui.plainTextEdit.insertPlainText(str(a))
            self.ui.plainTextEdit.insertPlainText("-->>")
            self.ui.plainTextEdit.insertPlainText(str(b))
            self.ui.plainTextEdit.insertPlainText("\n")

    @Slot()
    def mostrar_puntos_cercanos(self):
        resultado = puntos_mas_cercanos(self.puntos)
        pprint(resultado)
        for punto1,punto2 in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]
            
            self.scene.addLine(x1,y1,x2,y2)

    @Slot()
    def dibujar_puntos(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        puntos = []
        for particula in self.lista_particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r,g,b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x,particula.origen_y,6,6,pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y,6,6,pen)

            x = particula.origen_x
            y = particula.destino_x
            punto = (x,y)
            puntos.append(punto)
            x = particula.origen_y
            y = particula.destino_y
            punto = (x,y)
            puntos.append(punto)

        self.puntos = puntos
        pprint(self.puntos)

    @Slot()
    def ordenar_id(self):
        self.lista_particulas.part.sort(key=lambda x:x.id)
        self.mostrar()

    @Slot()
    def ordenar_distancia(self):
        self.lista_particulas.part.sort(key=lambda x:x.distancia, reverse=True)
        self.mostrar()

    @Slot()
    def ordenar_velocidad(self):
        self.lista_particulas.part.sort(key=lambda x:x.velocidad)
        self.mostrar()

    @Slot()
    def ordenar_id_tabla(self):
        self.lista_particulas.part.sort(key=lambda x:x.id)
        self.mostrar_tabla()

    @Slot()
    def ordenar_distancia_tabla(self):
        self.lista_particulas.part.sort(key=lambda x:x.distancia, reverse=True)
        self.mostrar_tabla()

    @Slot()
    def ordenar_velocidad_tabla(self):
        self.lista_particulas.part.sort(key=lambda x:x.velocidad)
        self.mostrar_tabla()

    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.scene.scale(1.2,1.2)
        else:
            self.ui.scene.scale(0.8,0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.lista_particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r,g,b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x,particula.origen_y,6,6,pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y,6,6,pen)
            self.scene.addLine(particula.origen_x + 3, particula.origen_y + 3, particula.destino_x + 3, particula.destino_y + 3,pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def mostrar_tabla(self):
        self.ui.table.setColumnCount(6)
        header = ["ID","Origen","Destino","Velocidad","Color","Distancia"]
        self.ui.table.setHorizontalHeaderLabels(header)

        self.ui.table.setRowCount(len(self.lista_particulas))

        row = 0
        for particula in self.lista_particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_widget = QTableWidgetItem("("+str(particula.origen_x)+","+str(particula.origen_y)+")")
            destino_widget = QTableWidgetItem("("+str(particula.destino_x)+","+str(particula.destino_y)+")")
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            color_widget = QTableWidgetItem("("+str(particula.red)+","+str(particula.green)+","+str(particula.blue)+")")
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.table.setItem(row,0,id_widget)
            self.ui.table.setItem(row,1,origen_widget)
            self.ui.table.setItem(row,2,destino_widget)
            self.ui.table.setItem(row,3,velocidad_widget)
            self.ui.table.setItem(row,4,color_widget)
            self.ui.table.setItem(row,5,distancia_widget)

            row += 1

    @Slot()
    def buscar_id(self):
        id = int(self.ui.buscar_lineEdit.text())

        encontrado = False
        for particula in self.lista_particulas:
            if id == particula.id:
                self.ui.table.clear()
                self.ui.table.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_widget = QTableWidgetItem("("+str(particula.origen_x)+","+str(particula.origen_y)+")")
                destino_widget = QTableWidgetItem("("+str(particula.destino_x)+","+str(particula.destino_y)+")")
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                color_widget = QTableWidgetItem("("+str(particula.red)+","+str(particula.green)+","+str(particula.blue)+")")
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                row = 0
                self.ui.table.setItem(row,0,id_widget)
                self.ui.table.setItem(row,1,origen_widget)
                self.ui.table.setItem(row,2,destino_widget)
                self.ui.table.setItem(row,3,velocidad_widget)
                self.ui.table.setItem(row,4,color_widget)
                self.ui.table.setItem(row,5,distancia_widget)

                encontrado = True
                return

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'El avion con el identificador "{id}" no fue encontrado'
            )
        
    @Slot()
    def agregar_inicio(self):
        id = self.ui.id_spinBox.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.agregar_inicio(particula)

    @Slot()
    def agregar_final(self):
        id = self.ui.id_spinBox.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.agregar_final(particula)



    @Slot()
    def mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista_particulas))

    @Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if (self.lista_particulas.abrir(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo cargar el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo cargar el archivo " + ubicacion
            )

    @Slot()
    def guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if (self.lista_particulas.guardar(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )