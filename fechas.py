from datetime import datetime
from datetime import timedelta
import locale
import json
# Establecer el locale a español (puede variar según el sistema operativo)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
class Fechas():
    def __init__(self, db_objeto):
        self.db_objeto = db_objeto
        self.DIA_HOY = datetime.now()
        self.dia_hoy_variable = datetime.now()

    def encabezados_fechas(self):
            #CONSTANTES
            FECHA_MANANA = datetime.now() + timedelta(days=1)
            DIA_MANANA =FECHA_MANANA.day
            SEMANA_CORRIENTE =FECHA_MANANA.isocalendar().week
            MES_CORRIENTE = datetime.now().strftime("%B")
            ANIO_CORRIENTE = datetime.now().year
            # Aqui cambiamos el inicio de la semana a domingo
            dia_semana_domingo = (datetime.now().weekday() + 1) % 7
            # aqui calculamos el dia de inicio de semana que seria el domingo
            domingo = datetime.now()- timedelta(days=dia_semana_domingo)
            if dia_semana_domingo == 0:
                dia = " Domingo "
            elif dia_semana_domingo == 1:
                dia = " Lunes "
            elif dia_semana_domingo == 2:
                dia = " Martes "
            elif dia_semana_domingo == 3:
                dia = " Miercoles "
            elif dia_semana_domingo == 4:
                dia = " Jueves "
            elif dia_semana_domingo == 5:
                dia = " Viernes "
            elif dia_semana_domingo == 6:
                dia = " Sábado "
            mes_encabezado = MES_CORRIENTE
            texto_semana_encabezado = "Semana " + str((self.dia_hoy_variable+timedelta(days=1)).isocalendar().week)
            texto_dia_encabezado = "HOY," + dia + str(self.DIA_HOY.day)
            return texto_dia_encabezado,texto_semana_encabezado,mes_encabezado,ANIO_CORRIENTE

    def inicio_semana(self):
        # Ajustar el inicio de la semana al domingo
            inicio_semana = self.dia_hoy_variable - timedelta(days=(self.dia_hoy_variable.weekday() + 1) % 7)
            return inicio_semana
    
    def dias_actuales(self): 
        dias_actuales = []
        for dia_indic in range(7):  # Del domingo (0) al sábado (6)
                dia_semana = self.inicio_semana() + timedelta(days=dia_indic)
                dias_actuales.append(dia_semana)
        
        return dias_actuales
    #----------------------------------------------CALCULO RENDIMIENTO--------------------------------------
    def calcular_rendimiento_semanal(self):
        """
        Calcula y guarda el rendimiento semanal de cumplimiento de hábitos en porcentaje,
        sin contar días anteriores a la creación del hábito y sin contar días no configurados para ejecución.
        """
        ejecuciones = self.db_objeto.cargar_ejecuciones()

        # Ajustar el inicio de la semana al domingo
        inicio_semana = self.inicio_semana()
        fin_semana = inicio_semana + timedelta(days=6)

        habitos_totales = 0
        habitos_cumplidos = 0

        for habit in self.db_objeto.habitos:
            fecha_creacion = datetime.strptime(habit["Fecha_creacion"], "%Y-%m-%d").date()

            # Iterar por cada día de la semana
            for dia_indic in range(7):
                dia_semana = inicio_semana + timedelta(days=dia_indic)
                dia_semana_str = dia_semana.strftime("%Y-%m-%d")
                dia_ejecucion = habit["dias_ejecucion"][dia_indic]

                # Ignorar días antes de la fecha de creación
                if dia_semana.day < fecha_creacion.day:
                    continue

                if dia_ejecucion == 1:  # Día en el que el hábito debe ejecutarse
                    habitos_totales += 1
                    # Verificar si se cumplió
                    ejecucion = next(
                        (e for e in ejecuciones if
                        e["nombre_habito"] == habit["nombre_habito"] and e["fecha_ejecucion"] == dia_semana_str),
                        None
                    )
                    if ejecucion and ejecucion["completado"]:
                        habitos_cumplidos += 1

        rendimiento = (habitos_cumplidos / habitos_totales * 100) if habitos_totales > 0 else 0
        rendimiento_redondeado = round(rendimiento)
        rendimiento_data = {
            "inicio_semana": inicio_semana.strftime("%Y-%m-%d"),
            "fin_semana": fin_semana.strftime("%Y-%m-%d"),
            "rendimiento": rendimiento
        }

        self.guardar_rendimiento_semanal(rendimiento_data)
        return rendimiento_redondeado
    
    def guardar_rendimiento_semanal(self, rendimiento_data):
        """
        Guarda el rendimiento semanal en un archivo JSON.
        """
        try:
            with open("json\\rendimiento_semanal.json", "r") as file:
                rendimientos = json.load(file)
        except FileNotFoundError:
            rendimientos = []

        # Agregar el nuevo rendimiento
        rendimientos.append(rendimiento_data)

        # Guardar en el archivo
        with open("json\\rendimiento_semanal.json", "w") as file:
            json.dump(rendimientos, file, indent=4)

    def semana_siguiente(self):
         if self.dia_hoy_variable > (self.DIA_HOY +timedelta(weeks=1)):
                print("Ya no se puede avanzar mas")
         else:
             self.dia_hoy_variable = self.dia_hoy_variable + timedelta(weeks=1)

    def semana_anterior(self): 
        if self.db_objeto.habitos:
            # Convertir las fechas a objetos date y tomar la más antigua
            fechas = [
                datetime.strptime(h["Fecha_creacion"], "%Y-%m-%d").date()
                for h in self.db_objeto.habitos
            ]
            fecha_inicial = min(fechas)
        else:
            fecha_inicial = self.DIA_HOY.date()

        if self.dia_hoy_variable.date() <= fecha_inicial:
            print("ya no se puede avanzar más")
        else:
            self.dia_hoy_variable -= timedelta(weeks=1)
         
        
