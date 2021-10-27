from time import process_time_ns
import pika
import pageviewapi
from datetime import date
#Contar la cantidad de visitas de la pagina.

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#El consumidor utiliza el exchange 'log'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    caracteres = "()"
    body2 = str(body).replace("wikipedia","")
    body2 = body2.replace("b","")
    body2 = body2.replace("'","")
    body2 = body2.replace(" ","")
    body2 = body2.replace("(","")
    body2 = body2.replace(")","")
    print("Visitas a la pagina de wikipedia: ",body2)

    #Obtener la fecha de hoy
    fecha = date.today()
    fechaformateada = "" + str(fecha.year) + str(fecha.month) + str(fecha.day) 
    vistas = pageviewapi.per_article('es.wikipedia', body2, '20010115', fechaformateada,
                        access='all-access', agent='all-agents', granularity='daily')


    #[{'project': 'es.wikipedia', 'article': 'paris', 'granularity': 'daily', 'timestamp': '2015111300', 'access': 'all-access', 'agent': 'all-agents', 'views': 2}]
    vistas2 = vistas['items']
    #print(vistas2)
    suma = 0
    for i in vistas2:
        suma+= i['views']
    print("visitas totales:" + str(suma))

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()