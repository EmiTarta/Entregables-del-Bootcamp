print("Hola soy Joselito, tu asistente virtual de Joselito's, estoy aqui para ofrecerte ayuda, en que te puedo ayudar")
print("1. Tengo problemas al iniciar sesion en mi cuenta")
print("2. No recuerdo la contraseña")
print("3. Necesito ayuda para realizar un pedido")
print("4. Informacion sobre delivery")
print("5. Salir")
pregunta = input("-->")
while pregunta != '5':
    if '1' in pregunta:
        pregunta_1 = input("Indicanos mas detalladamente la causa\n-->")
        if 'nombre' in pregunta_1:
            user = input("Indicanos tu nombre de usuario / correo electronico y te enviaremos un mensaje al correo electronico que nos habias proporcionado a la hora de crear la cuenta\n-->")
            if '@' not in user:
                print("No es un correo valido")
            else:
                print("El mensaje se ha enviado correctamente, revisa la carptea de spam")
            break
    elif '2' in pregunta:
        user_2 = input("Indica el correo electronico con el que te diste de alta en Joselito's\n-->")
        if '@' not in user_2:
                print("No es un correo valido")
        else:
            print("El mensaje se ha enviado correctamente, revisa la carptea de spam")
        break
    elif '3' in pregunta:
        print("1. Quiero realizar un pedido")
        print("2. Quiero informacion sobre los alergenos de nuestros productos")
        pregunta_3 = input("Que tipo de ayuda necesitas\n-->")
        if pregunta_3 == '1':
            print("Introduce tu pedido")
            input("-->")
        if pregunta_3 == '2':
            print("Todos nuestros produductos gluten y lactosa")
        break
    elif '4' in pregunta:
        pregunta_4 = print("Que preguntas sobre nuestra opcion de Delivery tienes?")
        print("1. Quiero saber que Joselito's esta mas cerca de mi direccion : pon 1")
        print("2. Quiero saber saber si el envio es gratuito: pon 2")
        print("3. Quiero saber el horario de envios: pon 3")
        preg_4 = input("Ingrese respuesta")
        if "1" in preg_4:
            codigo_postal = input("Ingresa tu codigo postal")
            if codigo_postal == "46001":
                print("Tu Joselito's mas cercano esta en direccion 'Plaza de la Reina, nro. 15'")
                break
            elif codigo_postal == "46002":
                print("Tu Joselito's mas cercano esta en direccion 'C/ Xativa, 21'")
                break
            elif codigo_postal == "46003" or '46004':
                print("Tu Joselito's mas cercano esta en direccion 'C/ Bailen, Estacion AVE Joaquin Sorolla'")
                break
            elif codigo_postal == "46005" or '46006' or '46007':
                print("Tu Joselito's mas cercano esta en direccion 'Centro Comercial El Saler, Avda. Profesor Lopez Pinero, nro. 16, Local 7'")
                break
        if "2" in preg_4:
            print("Nuestros envios tienen un coste de 2 euros")
        if "3" in preg_4:
            print("Nuestros horarios son de 10 a 00hs de lunes a sabado, y de 10 a 20 los domingos")
    else:
        print("No has seleccionado ninguna opcion correcta, vuelve a probar")