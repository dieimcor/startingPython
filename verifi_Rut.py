rut=int(input("Ingrese su rut para verificar que sea válido: "))
vrut=str(rut)
cont=2
xrut=rut
urut=rut
truecont=0
res=0
while(cont!=8) and (truecont!=2) and (urut!=0):
    if cont>=2:
        xrut=urut%10
        #print("El ultimo digito es: ",xrut)
        suma=xrut*cont
        #print(suma)
        res=res+suma
        #print(res)
        urut=urut/10
        urut=urut//1
        urut=int(urut)
        #print("el rut sin el ultimo digito es: ",urut)
        cont=cont+1
    if cont>7:
        cont=2
        truecont=truecont+1
compr=res%11
compr=11-compr
if (compr==10):
    print("Su rut es: ",rut," - K")
else:
    print("Su rut es: ",rut,"-",compr)
