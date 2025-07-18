from datetime import datetime
from datetime import timedelta
import locale
# Establecer el locale a español (puede variar según el sistema operativo)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
class fechas():
    def encabezados_fechas():
            #CONSTANTES
            DIA_HOY = datetime.now().day
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
            texto_dia_encabezado = "HOY," + dia + str(DIA_HOY)
            return texto_dia_encabezado,texto_semana_encabezado,mes_encabezado,ANIO_CORRIENTE



