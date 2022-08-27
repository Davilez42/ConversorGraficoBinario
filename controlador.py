
def factorial(x:int):
    if x==0:
        return 1
    else : 
      return  x * factorial(x-1)    



def ciclo(n,x):
    print(n)
    
    if n<x:
        if n==x:
            return x
        else:
            return ciclo(n+1,x)
    else:
         if n==x:
            return x
         else:
            return ciclo(n-1,x)    
        

         



def convertiraBinario(numero):
    if(numero==0):
        return ""

    if(numero%2==0):
        
        return  convertiraBinario((numero/2)) +"0"
    
    else:

        return convertiraBinario(int(numero/2))+ "1"
    
    




def convertiraDecimal(numero):
    
    if type(numero)==int:
        lista = [z for z in str(numero)]
        n= len(lista)
        k = int(lista.pop(0))
        resultado = k*2**(n-1)
        return resultado + convertiraDecimal(lista)
        
    if type(numero)==list:
        if len(numero)==0:
            return 0
        m = numero
        n= len(numero)
        k = int(m.pop(0))
        resultado = k*2**(n-1)
        return resultado + convertiraDecimal(m)
        
     
        
  