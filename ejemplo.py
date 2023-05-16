
#contrasenia='p123'
#pass_ingresado=input('ingrese contraseña')
#print ('la contraseña es correcta  ') if contrasenia==pass_ingresado else print('la contraseña es incorrecto')
#p1=int(input('ing n1'))
#p2=int(input('ing n2'))

#if p1==p2-3:
#    print ('el prime es igual al segundo-3')
#elif p1<p2:
#    print('el primero es menor al segundo')
#else:
 #   print('el segundo es menor al primero')


# ...if <condicion> else ...

#while <condicion>:
#<bloque codigo>
#--------
#numeros=[14,45,5,123,1,4,9,15,25]
#v=0
#while v!=5:
 #   v=numeros.pop()
  #  print (v)

#interacciones= int(input('ingrese nrsw a ingresar:'))
#suma=0
#while interacciones:
 #   valor=int(input('ing nro:'))
  #  suma+=valor
  #  if suma >=100:
  #      break
  #  interacciones-=1
#else:
 #   print('pase por el else')
#print ('la suma de valores es',suma)
# break rompe el bucle
# cotinue no ejecuta el codigo en esa interaccion
# pass simular q hay codigo

#-----FOR
'''lista=[10,9,8]
for n in lista:
    print(n)

for numero in range(10):
    print (numero)'''

# ------archivos
'''aa=open('mihobbie.txt','a')
for n in range (1,4):
    aa.write(input(f'ingrese su hobbie numero {n}:') + '\n')
aa.close()'''

'''with open('mihobbie.txt','a') as aa:
    for n in range (1,4):
        aa.write(input(f'ingrese su hobbie numero {n}:') + '\n')'''

#lectura readline lee 1 linea, readlines crea una lista de todos

'''a=open('mihobbie.txt','r')
ta=a.readlines()
print(ta)
a.close'''

#ubicar puntero seek
'''a=open('mihobbie.txt','r')
print(a.read())
print ('-----')
a.seek(0)
print(a.read())
print ('-----')
a.close'''

# JSON -> JS OBJECT NOTATION
'''lista=[1,2]
mi_dic={
    'clave1':1,
    'clave2':2,
    'lista':lista,
}

import json
with open ('test.json','w') as f:
    json.dump (mi_dic,f,indent=4)'''

#leer
import json
with open ('test.json','r') as f:
    datos=json.load(f)
    print(datos)
    print(type(datos))
