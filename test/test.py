import sqlite3
#connect() permet de se connecter
connexion = sqlite3.connect('D:/workspace/python/test/test/jobs.db')
#cursor() 
curseur = connexion.cursor() #creation du curseur
query="select major from recent_grads;"
#print('1 '+ str(curseur.fetchone()))
curseur.execute(query) #exécute la requête SQL situé dans la viriable query et ce curseur convertit les résultats en t-uples pour ls stocker en local
#print('2 '+ str(curseur.fetchone()))
result1=curseur.fetchone() #Chercher le premier résultat dans la variable locale 
result2=curseur.fetchone() #Chercher le seuxième résultat dans la variable locale
next_five_results=curseur.fetchmany(5)
all_results=curseur.fetchall()
print(result1)
print(result2)
print(next_five_results)
print(all_results[0:5])



