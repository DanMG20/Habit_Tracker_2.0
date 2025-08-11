from datetime import datetime
from datetime import timedelta
import locale
# Establecer el locale a español (puede variar según el sistema operativo)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
class Fechas():
    def __init__(self, db_objeto):
        self.db_objeto = db_objeto
        self.DIA_HOY = datetime.now()

    def encabezados_fechas(self):
            #CONSTANTESs
            
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
            texto_semana_encabezado = "Semana " + str(SEMANA_CORRIENTE)
            texto_dia_encabezado = "HOY," + dia + str(self.DIA_HOY.day)
            return texto_dia_encabezado,texto_semana_encabezado,mes_encabezado,ANIO_CORRIENTE

    def inicio_semana(self):
        # Ajustar el inicio de la semana al domingo
            inicio_semana = self.DIA_HOY - timedelta(days=(self.DIA_HOY.weekday() + 1) % 7)
            return inicio_semana
    
    def dias_actuales(self): 
        dias_actuales = []
        for dia_indic in range(7):  # Del domingo (0) al sábado (6)
                dia_semana = self.inicio_semana() + timedelta(days=dia_indic)
                dias_actuales.append(dia_semana.day)
        return dias_actuales