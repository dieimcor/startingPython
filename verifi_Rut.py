rut=int(input("Ingrese su rut para verificar que sea válido: "))
vrut=str(rut)
cont=2
xrut=rut
urut=rut
res=0
while(urut!=0):
    if cont>=2:
        xrut=urut%10
        suma=xrut*cont
        res=res+suma
        urut=urut/10
        urut=urut//1
        urut=int(urut)
        cont=cont+1
    if cont>7:
        cont=2
compr=res%11
compr=11-compr
if (compr==10):
    print("Su rut es: ",rut," - K")
elif compr==11:
    print("Su rut es: ",rut," - 0")
else:
    print("Su rut es: ",rut,"-",compr)
