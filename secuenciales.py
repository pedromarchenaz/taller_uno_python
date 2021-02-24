# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:51:55 2021

@author: PedroLuis
"""
# Ejercicio 1 ***********************
vp1 = float(input('Digite el valor de la persona 1: '))
vp2 = float(input('Digite el valor de la persona 2: '))
vp3 = float(input('Digite el valor de la persona 3: '))

total = vp1 + vp2 + vp3
pp1 = (vp1/total) * 100
pp2 = (vp2/total) * 100
pp3 = (vp3/total) * 100

print(f'El porcentaje invertido de la persona 1 es: {pp1} %')
print(f'El porcentaje invertido de la persona 2 e: {pp2} %')
print(f'El porcentaje invertido de la persona 3 es: {pp3} %')


# Ejercicio 2 ***********************
vs = float(input('Digite el valor de su sueldo: $'))
canth = int(input('Digite cuantos hijos tiene: '))

vb = canth * 80000
mt = vs + vb

print(f'El valor de la bonificacion es : ${vb:,} ')
print(f'El valor total a pagar es : ${mt:,} ')


# Ejercicio 3 ***********************
vi = float(input('Digite el valor inicial: $'))
sf = (vi * 0.015) + vi
print(f'El valor del saldo final es : ${sf:,} ')


# Ejercicio 4 ***********************
cmc = int(input('Digite la cantidad de metros cuadrados: '))
valort = cmc * 80000
cuotai = valort * 0.35
resto = valort - cuotai
vcuota = resto / 12

print(f'El valor de la cuota inicial es : ${cuotai:,} ')
print(f'El valor total de cada cuota es : ${vcuota:,} ')


# Ejercicio 5 ***********************
sb = float(input('Digite el valor de su sueldo base: $'))
dpp = sb * 0.01
dss = sb * 0.04
dsf = sb * 0.005
dch = sb * 0.05
td = dpp + dss + dsf + dch
tp = sb - td

print(f'El valor del descuento de la politica publica es : ${dpp:,} ')
print(f'El valor del descuento del seguro social es : ${dss:,} ')
print(f'El valor del descuento del seguro forzoso es : ${dsf:,} ')
print(f'El valor del descuento de la caja de ahorros es : ${dch:,} ')
print(f'El valor total a pagar al trabajador es : ${tp:,} ')


# Ejercicio 6 ***********************
cpala = int(input('Digite la cantidad de palabras: '))
tcenti = int(input('Digite el tamaño en centimetros: '))
ncolores = int(input('Digite el número de colores: '))

vcpala = cpala * 20000
vtcenti = tcenti * 15000
vncolores = ncolores * 25000
taviso = vcpala + vtcenti + vncolores

print(f'El valor total a pagar por el aviso es : ${taviso:,} ')


# Ejercicio 7 ***********************
cano = int(input('Digite la cantidad de años laborados: '))
if cano > 1:
    vbono = (120000 * cano) - 20000
else:
    vbono = 100000

print(f'El valor del bono por año es : ${vbono:,} ')


# Ejercicio 8 ***********************
chora = int(input('Digite la cantidad de horas laboradas: '))
vatotal = chora * 20000
desccda = vatotal * 0.05
vapagar = vatotal - desccda

print(f'El valor del descuento es : ${desccda:,} ')
print(f'El valor total a pagar es : ${vapagar:,} ')


# Ejercicio 9 ***********************
montoini = float(input('Digite el valor delmonto inicial: $'))
montofin = float(input('Digite el valor del monto final: $'))
montollamada = montoini - montofin
montototal = (montollamada * 0.20) + montollamada
saldo = montoini - montototal

print(f'El valor total de la llamada es : ${montototal:,} ')
print(f'El valor de su saldo actual es : ${saldo:,} ')


# Ejercicio 10 ***********************
cantfoto = int(input('Digite la cantidadde fotos del rollo: '))
vfoto = cantfoto * 1500
vpagarfo = (vfoto * 0.16) + vfoto

print(f'El valor total a pagar con el iva es : ${vpagarfo:,} ')


# Ejercicio 11 ***********************
presuh = float(input('Digite el valor del presupuesto del hospital: $'))
gine = presuh * 0.40
trau = presuh * 0.30
pedi = presuh * 0.30

print(f'Presupuesto para ginecologia es : ${gine:,} ')
print(f'Presupuesto para traumatología es : ${trau:,} ')
print(f'Presupuesto para pediatria es : ${pedi:,} ')


# Ejercicio 12 ***********************
cantpeli = int(input('Digite la cantidadde de peliculas: '))
if cantpeli > 1:
    descpeli = cantpeli - 1
    tppeli = descpeli * 1500
else:
    tppeli = cantpeli * 1500

print(f'El valor total a pagar por las peliculas es : ${tppeli:,} ')


# Ejercicio 13 ***********************
nperfa = int(input('Digite la cantidadde de personas de la familia: '))
vtour = (nperfa * 25000)
montotour = (vtour * 0.12) + vtour

print(f'El valor total a pagar con el iva incluido es : ${montotour:,} ')


# Ejercicio 14 ***********************
cantdias = int(input('Digite la cantidadde de dias (varios dias): '))
vthotel = (cantdias * 200000) - 100000

print(f'El valor total a pagar es : ${vthotel:,} ')


# Ejercicio 15 ***********************
valorpresta = float(input('Digite el valor del prestamo: $'))
tpresta = (valorpresta * 0.24) + valorpresta
cuotaes = (tpresta / 2) / 4
cuotaor = (tpresta / 2) / 20

print(f'El valor de cada una de las 4 cuotas especial es : ${cuotaes:,} ')
print(f'El valor de cada una de las 20 cuotas ordinaris es : ${cuotaor:,} ')









