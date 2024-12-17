#clients = {"Durand Luc": [{"Adresse":["Résidence les Prés","4 Rue des Pinsons"]},{"CP":"05000"},{"Ville":"Gap"}]}


clients={"Nom":"Durand Luc","Adresse":["Résidence les Prés","4 Rue des Pinsons"],"CP":"05000","Ville":"Gap"}

for element in clients.items():
    print(clients, ":", element)