def marcar_multiplos_n(criba,n,tamano):
    for i in range(n+n,tamano+1,n): #empieza en n+n, hasta tamano+1,de n en n for(i=n+n;i<=tamano+1;i=n+n) 
        criba[i]=False
        
"""def es_primo(criba,n):
    return criba[n]"""
def es_primo(criba,n):
    return criba[n]

def cribar(criba,tamano):
    raiz=int(tamano**0.5)+1
    global lista_primos
    #for i in range(2,raiz+1):
    for i in range(2,tamano):
        if es_primo(criba,i):
            lista_primos.append(i)
            marcar_multiplos_n(criba,i,tamano)

def crear_criba(tamano):
    criba=[True]*(tamano+1)
    criba[0]=criba[1]=False
    return criba

"""def crear_list_primos(criba):
    lista_primos=[]
    for x,y in enumerate(criba):
        if y==True:
            lista_primos.append(x)
    return lista_primos"""

if _name_ == '_main_':
    lista_primos=[]
    tamano=1_000_000
    criba=crear_criba(tamano)
    cribar(criba,tamano)
    #print(crear_list_primos(criba))
    print(lista_primos)