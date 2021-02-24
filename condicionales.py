# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:28:30 2021

@author: PedroLuis
"""
# Ejercicio 1
vcami = float(input('Digite el valor de la unidad de la camisa: $'))
cantcami = int(input('Digite la cantidad de camisas: '))
tcamisa = cantcami * vcami

if cantcami >= 3:
    vpagarcami = tcamisa - (tcamisa * 0.30)
else:
    vpagarcami = tcamisa - (tcamisa * 0.10)

print(f'El valor total a pagar es : ${vpagarcami:,} ')


# Ejercicio 2
vcompra = float(input('Digite el valor de la compra: $'))
num = int(input('Digite un numero: '))
if num >= 74:
    tcompra = vcompra - (vcompra * 0.20)
else:
    tcompra = vcompra - (vcompra * 0.15)

print(f'El valor a pagar con descuento es : ${tcompra:,} ')


# Ejercicio 3
vmonto = float(input('Digite el valor del monto: $'))
if vmonto > 50000:
    pcuota = (vmonto * 0.02)
    print('La cuota a pgar del monto es de 2%')
else:
    pcuota = (vmonto * 0.03)
    print('La cuota a pgar del monto es de 3%')

print(f'El valor de la cuota es : ${pcuota,} ')


# Ejercicio 4
ganancia = float(input('Digite la ganancia diaria: $'))
ptsuno = int(input('Digite numero de puntos de contamacion dia 1: '))
ptsdos = int(input('Digite numero de puntos de contamacion dia 2: '))
ptstres = int(input('Digite numero de puntos de contamacion dia 3: '))
ptscuatro = int(input('Digite numero de puntos de contamacion dia 4: '))
ptscinco = int(input('Digite numero de puntos de contamacion dia 5: '))

prome = (ptsuno + ptsdos + ptstres + ptscuatro + ptscinco) / 5

if prome >= 170:
    print('Tendra una sancion de parar la produccion por una semana y multa')
    multa = ganancia - (ganancia * 0.50)
    print('El valor a descontar por la multa diariamente es: ${multa:,} ')
else:
    print('No tendra sancion ni multas')


# Ejercicio 5
valorcate = float(input('Digite valor del carro o terreno : $'))
increte = float(input('Digiteel incremento anual del terreno : %'))
devaluau = float(input('Digiteel devaluacion anual del carro : %'))

inc = (((valorcate * increte) / 100) * 3) / 2
dec = ((valorcate * devaluau) / 100) * 3

if dec < inc:
    print('Conviene comprar el carro')
else:
    print('Conviene comprar el terreno')


# Ejercicio 6
cantpc = int(input('Digite cantidad de pc a comprar: '))
valorpc = 11000
total = valorpc * cantpc

if cantpc < 5:
    pagarpc = total - (total * 0.10)
if cantpc >= 5 and cantpc <= 10:
    pagarpc = total - (total * 0.20)
if cantpc > 10:
    pagarpc = total - (total * 0.40)

print(f'El valor total a pagar con descuento es : ${pagarpc:,} ')


# Ejercicio 7
marcaap = int(input('Digite la marca del aparato: '))
valorap = float(input('Digite el valor del aparto: $'))

if valorap >= 2000:
    vdap = valorap - (valorap * 0.10)
if marcaap == 'nosy':
    vdapm = valorap - (valorap * 0.05)

totalap = (vdap + vdapm)
taparato = totalap + (totalap * 0.16)

print(f'El valor a pagar del aparato con iva incluido es : ${taparato:,} ')


# Ejercicio 8
npieza = int(input('Digite número de piezas: '))
vpieza = float(input('Digite el valor por unidad de pieza: $'))

tv = vpieza * npieza
if tv > 500000:
    inver = tv * 0.55
    prest = tv * 0.30
    credi = tv * 0.15
else:
    inver = tv * 0.70
    prest = 0
    credi = tv * 0.30

inte = credi * 0.20
print(f'El valor de la cantidad a invertir es : ${inver,} ')
print(f'El valor del prestamo es : ${prest:,} ')
print(f'El valor del credito es : ${credi:,} ')
print(f'El valor del interes es : ${inte:,} ')


# Ejercicio 9
primernum = int(input('Digite primer número: '))
segundonum = int(input('Digite segundo número: '))

if primernum == segundonum:
    res = primernum * segundonum
    print('Se multiplicaron los números, el resultado es: ', res)
if primernum > segundonum:
    res = primernum - segundonum
    print('Se restaron los números, el resultado es: ', res)
else:
    res = primernum + segundonum
    print('Se sumaron los números, el resultado es: ', res)


# Ejercicio 10
numuno = int(input('Digite numero 1: '))
numdos = int(input('Digite numero 2: '))
numtres = int(input('Digite numero 3: '))

if numuno > numdos and numuno > numtres:
    print('El numero 1 es mayor :', numuno)
if numdos > numuno and numdos > numtres:
    print('El numero 2 es mayor :', numdos)
if numtres > numdos and numtres > numuno:
    print('El numero 3 es mayor :', numtres)
















