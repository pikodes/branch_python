def diviser(a,b):
      c=a/b
      return c
      
try:
      nbre1=float(input("entrez un nombre 1:"))
      nbre2=float(input("entre un nombre 2 :"))
      div=diviser(nbre1,nbre2)
      print(div)
except  ValueError:
      print(" Erreur : les deux arguments doivent être des nombres et retourne None ")      
except ZeroDivisionError:
      print("Erreur : division par zéro impossible et retourne None")
except Exception as e: 
      print(f"Erreur inattendue: {e}") 

