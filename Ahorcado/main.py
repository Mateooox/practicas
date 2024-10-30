import ahorcado
# Juego de ahorcado
ahorcado.printIntro('./Textos/intro.txt')
# Introduzca aqu� las instrucciones para el juego
print("INTRUCCIONES Y REGLAS:\n\nEl juego cuando con dos modos, el primero es para jugar de a dos personas y el segundo para jugar con una palabra aleatoria.\nAl principio de cada ronda tiene que ingresar unicamente una letra\nPara ganar debe de descrubir la palabra secreta, de lo contrario si se queda sin intentos perdera\nCuenta con 8 intentos unicamente\nBuena suerte.")
# Variables globales

letrasIntentadas=''
numeroIntentos = 8
otraVez = 'y'
veces_fal=0
while otraVez == 'y':
            
	# Selecci�n del modo de juego (1: palabra secreta, 2: archivo)
    print('\nSELECCION MODO DE JUEGO:\n\n1.Otro jugador ingresa la palabra\n2.Palabra aleatoria')
	# C�digo ...
    modo_juego="3"
    while modo_juego not in "1,2":
        modo_juego=input("\nIngrese el modo de juego que desea\n")
        if modo_juego not in "1,2":
            print('Ingrese 1 o 2')
    if modo_juego =="1":
        secreta=ahorcado.inputSecret()
        secreta=secreta.lower()
        print("\n"*12)
        ahorcado.figura("./Textos/fase7.txt")
    else:
        palabras=ahorcado.loadWords("./Textos/superHeroes.txt")
        secreta=ahorcado.pickWord(palabras, ",")
	# ...
    ban = 1 # Bandera que indica la culminaci�n de una tanda de turnos
			# ya sea por que el usuario acierta o por que pierde
			
	# Impresi�n de las estad�sticas (Numero de intentos, letras disponibles, palabra secreta (rayas))
	# C�digo ...
    print(f"Numero de intentos:{numeroIntentos}\nLetras disponibles:\n{ahorcado.obtenerLetrasDisponibles(letrasIntentadas)}\nPalabra secreta:\n{ahorcado.obtenerParteAdivinada(secreta,letrasIntentadas)}")
    
	
	# ...
    while ban == 1:
		# Solicitud interactiva de palabras
		# C�digo ...
        var=False
        while var==False:
            print("_"*54)
            car=input("\nIngresa porfavor una letra\n")
            if len(car)==1:
                if ahorcado.verificarLetraIngresada(car, letrasIntentadas)==True:
                    print("La letra ya fue utilizada, intenta nuevamente")
                else:
                    letrasIntentadas+=car
                    var=True
            else:
                print("Un solo caracter porfavor")
                
		# ...
		
		# Verificaci�n de la letra e impresi�n de lo que va de la palabra
		# C�digo ...
        if car not in secreta:
            numeroIntentos-=1
            veces_fal+=1
            nombre=f"./Textos/fase{veces_fal}.txt"
            ahorcado.figura(nombre)
            print("Letra fallida, intenta con otra")
        else:
            ahorcado.figura("./Textos/letra.txt")
        print("\n\n",ahorcado.obtenerParteAdivinada(secreta, letrasIntentadas))
		# ...
		

		
		# Impresi�n del estado del juego (N�mero de intentos, letras disponibles)
		# C�digo ...
        print(f"\nNumero de intentos:{numeroIntentos}\nletras disponibles:\n{ahorcado.obtenerLetrasDisponibles(letrasIntentadas)}")
		
		# ...
		
		# Verificaci�n de la condici�n de finalizaci�n del juego
		# C�digo ...
        if numeroIntentos==0:
            ban=2
            ahorcado.figura("./Textos/muerto.txt")
            print(f"Te quedaste sin intentos, intentalo de nuevo!\nLa palabra secreta era:\n{secreta}")
        if ahorcado.palabraAdivinada(secreta, letrasIntentadas)==True:
            ban=2
            ahorcado.figura("./Textos/Victoria.txt")
            print("\nAdivinaste la palabra\n\n")
	# Inicializar nuevamente las variables que crea necesario...
    veces_fal=0
    numeroIntentos=8
    letrasIntentadas=""
	# Solicitud de nuevo juego
    otraVez = input('Desea jugar otra vez (y/n): \n')  
    otraVez = otraVez.lower()
''' Fin ciclo de nuevo juego '''