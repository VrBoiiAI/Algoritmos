import os
import time

os.system('cls')

#EMPIEZAN FUNCIONES
#EMPIEZAN FUNCIONES
#EMPIEZAN FUNCIONES
#EMPIEZAN FUNCIONES
#EMPIEZAN FUNCIONES

x=0
y=0
dosNumU = "Ingrese el primer numero: "
dosNumD = "Ingrese el segundo numero: "
unNum = "Ingrese el numero para calcular:"


def sum():
     
     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)

     answ = x+y
     answ = str(answ)
     x= str(x)
     print(nom +", el resultado de la suma es de: " + (answ))

def res():

     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)

     answ = x-y
     answ = str(answ)
     print(nom +", el resultado de la resta es de: " + (answ))

def mul():

     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)
     
     answ = x*y
     answ = str(answ)
     print(nom +", el resultado de la multiplicacion es de: " + (answ))

def div():

     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)
     
     answ = x/y
     answ = str(answ)
     print(nom +", el resultado de la division es de: " + (answ))

def divEnt():

     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)
     
     div = int(x/y)
     answ = str(div)
     print(nom +", el resultado de la division entera es de: " + (answ))

def resid():

     x = input(dosNumU)
     y = input(dosNumD)
     x = float(x)
     y = float(y)
     
     answ = x%y
     answ = str(answ)
     print(nom +", el residuo de la division es de: " + (answ))

def elev():

     x = input(unNum)
     x = float(x)
     
     answ = x**2
     answ = str(answ)
     x = str(x)
     print(nom +", el resultado de elevar "+x+" al cuadrado es de: " + (answ))

def raiz():

     x = input(unNum)
     x = float(x)
     
     answ = x**0.5
     answ = str(answ)
     x = str(x)
     print(nom +", la raiz cuadrada de "+x+" es igual a: "+(answ))

while True:

    def ite():
        rep = input("Desea realizar otra operacion? (y/n)")
        if rep == y or rep == y:
            break


    os.system('cls')
    nom = input("Por favor ingrese su nombre: ")
    op = ""
    op = input( "\na) Calcular volumen\nb) Calcular area\nc) Calcular perimetro (Figuras regulares)\nd) Operaciones basicas \n\n" + nom + ", que operacion desea realizar? \n")

        #EMPIEZAN VOLUMENES
        #EMPIEZAN VOLUMENES
        #EMPIEZAN VOLUMENES
        #EMPIEZAN VOLUMENES
        #EMPIEZAN VOLUMENES

    if op == "a" or op == "A":

        os.system('cls')
        op = input( "\na) Cubo\nb) Cilindro\nc) Cono\nd) Piramides...\ne) Prismas...\n\n" + nom + ", que volumen desea calcular? \n")


        if op == "a" or op == "A":

            os.system('cls')
            l = input("Ingrese la medida del lado del cubo: ")
            l = float(l)
            vol = l*l*l
            vol = str(vol)
            print("El volumen del cubo es de: "+vol+"u³")
            ite()

        elif op == "b" or op == "B":

            os.system('cls')
            r = input("Ingrese la medida del radio del circulo(La base): ")
            r = float(r)
            h = input("Ingrese la medida de la altura del cilindro: ")
            h = float(h)
            b = (r*r)*3.141592
            vol = b * h
            vol = str(vol)
            print("El volumen del cilindro es de: "+vol+"u³")

        elif op == "c" or op == "C":

            os.system('cls')
            r = input("Ingrese la medida del radio del circulo(La base): ")
            r = float(r)
            h = input("Ingrese la medida de la altura del cono: ")
            h = float(h)
            b = (r*r)*3.141592
            vol = (b * h)/3
            vol = str(vol)
            print("El volumen del cilindro es de: "+vol+"u³")

        elif op == "d" or op == "D":

            os.system('cls')
            op = input("\na) Cuadrado\nb) Pentagono\nc) Hexagono\n\n" + nom + ", cual es la base de la piramide? \n")


            if op == "a" or op == "A":
                    
                os.system('cls')
                l = input("Ingrese la medida de un lado cuadrado: ")
                l = float(l)
                h = input("Ingrese la medida de la altura de la piramide: ")
                h = float(h)
                vol = (((l*l)*h)/3)
                vol = str(vol)
                print("El volumen de la piramide es de: " + vol + "u³")

            elif op == "b" or op == "B":
                    
                os.system('cls')
                l = input("Ingrese la medida de un lado del pentagono: ")
                l = float(l)
                ap = input("Ingrese la medida del apotema del pentagono: ")
                ap = float(ap)
                h = input("Ingrese la medida de la altura de la piramide: ")
                h = float(h)
                b = ((l*5)*ap)/2
                vol = b * h /3
                vol = str(vol)
                print("El volumen de la piramide es de: " + vol + "u³")

            elif op == "c" or op == "C":

                os.system('cls')
                l = input("Ingrese la medida de un lado del hexagono: ")
                l = float(l)
                ap = input("Ingrese la medida del apotema del hexagono: ")
                ap = float(ap)
                h = input("Ingrese la medida de la altura de la piramide: ")
                h = float(h)
                b = 3*l*ap
                vol = b * h /3
                vol = str(vol)
                print("El volumen de la piramide es de: " + vol + "u³")

            else:
                os.system('cls')
                print("Respuesta no valida, renicie el programa.")

        elif op == "e" or op == "E":

            os.system('cls')
            op = input("\na) Cuadrado\nb) Pentagono\nc) Hexagono\n\n" + nom + ", cual es la base del prisma? \n")


            if op == "a" or op == "A":
                    
                os.system('cls')
                l = input("Ingrese la medida de un lado del cuadrado: ")
                l = float(l)
                h = input("Ingrese la medida de la altura del prisma: ")
                h = float(h)
                vol = (l*l)*h
                vol = str(vol)
                print("El volumen del prisma es de: " + vol + "u³")

            elif op == "b" or op == "B":
                    
                os.system('cls')
                l = input("Ingrese la medida de un lado del pentagono: ")
                l = float(l)
                ap = input("Ingrese la medida del apotema del pentagono: ")
                ap = float(ap)
                h = input("Ingrese la medida de la altura del prisma: ")
                h = float(h)
                b = ((l*5)*ap)/2
                vol = b * h
                vol = str(vol)
                print("El volumen del prisma es de: " + vol + "u³")

            elif op == "c" or op == "C":

                os.system('cls')
                l = input("Ingrese la medida de un lado del hexagono: ")
                l = float(l)
                ap = input("Ingrese la medida del apotema del hexagono: ")
                ap = float(ap)
                h = input("Ingrese la medida de la altura del prisma: ")
                h = float(h)
                b = 3*l*ap
                vol = b * h
                vol = str(vol)
                print("El volumen del prisma es de: " + vol + "u³")

            else:
                os.system('cls')
                print("Respuesta no valida, renicie el programa.")

        #TERMINAN VOLUMENES
        #TERMINAN VOLUMENES
        #TERMINAN VOLUMENES
        #EMPIEZAN AREAS
        #EMPIEZAN AREAS
        #EMPIEZAN AREAS

    elif op == "b" or op == "B":
            
        os.system('cls')
        op = input( "\na) Circulo\nb) Triangulo\nc) Pentagono\nd) Hexagono\ne) Figuras de 4 lados...\n\n" + nom + ", que area desea calcular? \n")


        if op == "a" or op == "A":

            os.system('cls')
            r = input("Ingrese la medida del radio del circulo: ")
            r = float(r)
            A = r*r*3.141592
            A = str(A)
            print("El area del circulo es de: " + A + "u²")

        elif op == "b" or op == "B":

            os.system('cls')
            b = input("Ingrese la medida de la base del triangulo: ")
            b = float(b)
            h = input("Ingrese la medida de la altura del triangulo: ")
            h = float(h)
            A = b * h /2
            A = str(A)
            print("El area del triangulo es de: " + A + "u²")

        elif op == "c" or op == "C":

            os.system('cls')
            l = input("Ingrese la medida de un lado del pentagono: ")
            l = float(l)
            ap = input("Ingrese la medida del apotema del pentagono: ")
            ap = float(ap)
            A = ((l*5)*ap)/2
            A = str(A)
            print("El area del pentagono es de: "+A+"u²")

        elif op == "d" or op == "D":

            l = input("Ingrese la medida de un lado del hexagono: ")
            l = float(l)
            ap = input("Ingrese la medida del apotema del hexagono: ")
            ap = float(ap)
            A = 3*l*ap
            A = str(A)
            print("El area del hexagono es de: "+A+"u²")

        elif op == "e" or op == "E":

            os.system('cls')
            op = input("\na) Cuadrado, Rectangulo, Paralelogramos\nb) Rombo\nc) Trapecio\n\n" + nom + ", cual es la figura que quieres calcular? \n")


            if op == "a" or op == "A":
                    
                os.system('cls')
                b = input("Ingrese la medida de la base del cuadrilatero: ")
                b = float(b)
                h = input("Ingrese la medida de la altura del cuadrilatero: ")
                h = float(h)
                A = b*h
                A = str(A)
                print("El area del cuadrilatero es de: " + A + "u²")

            elif op == "b" or op == "B":
                    
                os.system('cls')
                d1 = input("Ingrese la medida de la diagonal mayor del rombo: ")
                d1 = float(d1)
                d2 = input("Ingrese la medida de la diagonal menor del rombo: ")
                d2 = float(d2)
                A = 0.5 * d1 * d2
                A = str(A)
                print("El area del rombo es de: " + A + "u²")
                    
            elif op == "c" or op == "C":

                os.system('cls')
                b1 = input("Ingrese la medida de la base mayor del trapecio: ")
                b1 = float(b1)
                b2 = input("Ingrese la medida de la base menor del trapecio: ")
                b2 = float(b2)
                h = input("Ingrese la medida de la altura del trapecio: ")
                h = float(h)
                A = (b1 + b2) * h *0.5
                A = str(A)
                print("El area del trapecio es de: " + A + "u²")

            else:
                os.system('cls')
                print("Respuesta no valida, renicie el programa.")

        #TERMINAN AREAS
        #TERMINAN AREAS
        #TERMINAN AREAS
        #EMPIEZAN PERIMETROS
        #EMPIEZAN PERIMETROS
        #EMPIEZAN PERIMETROS

    elif op == "c" or op == "C":

        os.system('cls')
        numLados = input("Ingrese el numero de lados de la figura: ")
        numLados = int(numLados)
        b = input("Ingrese la medida de un lado de la figura: ")
        b = int(b)
        p = b * numLados
        p = str(p)
        print(nom + ", el perimetro de la figura es de: " + p + "u")
            
    elif op == "d" or op == "D":

        os.system('cls')
        op = input("\na) Suma\nb) Resta\nc) Multiplicacion\nd) Division...\ne) Elevar al cuadrado\nf) Raiz Cuadrada\n\n" + nom + ", Que operacion desea realizar? \n")


        if op == "a" or op == "A":

            sum()

        elif op == "b" or op == "B":

            res()

        elif op == "c" or op == "C":

            mul()

        elif op == "d" or op == "D":

            op = input("\na) Division\nb) Division Entera\nc) Residuo\n\n" + nom + ", Que operacion desea realizar? \n")


            if op == "a" or op == "A":

                div()

            elif op == "b" or op == "B":

                divEnt()

            elif op == "c" or op == "C":

                resid()

        elif op == "e" or op == "E":

            elev()

        elif op == "f" or op == "F":

            raiz()
                
        else:
            
            os.system('cls')
            print("Respuesta no valida, renicie el programa.")

    else:
            os.system('cls')
            print("Respuesta no valida, renicie el programa.")