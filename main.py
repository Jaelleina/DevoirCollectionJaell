# -------question 1

#1. List of strings 
#1. creation de la liste

print("1.-----------liste de 10 elements de type chaine de caracteur------\n")



listes=['Billy','Jeanne','Titi','Milly','Jacky','Marie','Ginette','Moses','Lily','Siella']



print(listes,"\n\n")


#2. changement du  contenu de l'element nO 5

print("2.--------changement du contenu de l'element no5----------\n")

listes[4]='Forte'

print(listes,"\n\n")


#3.cration d' une listse des elements contenant la  lettre "a"

print("3.-------creation d'une list des element contenant la lettre 'a'--------\ n")

liste_copy=[]  
for li in listes:
    if'a' in li:
         
         liste_copy.append(li)

print(liste_copy,"\n\n")



#4.ajouter un element a la fin de la liste

print("------ajouter un  element a la fin de la liste\n-----")


listes.append("yvonne")
print(list,"\n\n")




#5.ajout d l'element a l' index no2 

print("-------ajout d'un element a l'index no2\n-----")

listes.insert(2,'sultan')

print(listes,"\n\n")


#6. suppression de l' element no3

print("-------supression de l'element no3--------\n")

listes.pop(2)

print(listes,"\n\n")

#7.suppression de l'element a l' index no2

print("suppression de l' element a l' index no2\n")

listes.pop(2)

print(listes,"\n\n")

#9. affiche le sens au sens inverse

print("-------afichage en sens inverse de la liste------\n")

listes.reverse()
print(listes,"\n\n")

#10. vider la list

print("------clear the list-------\n")
listes.clear()
print(listes,"\n")

#11. supprime la liste

del listes

#II                      
print("LES TUPLES")

#1. tuple creation
  
print("-------l'occurence de la valeur'3' dans le tuple----\n")

tupl=(2,13,33,2,28,10,45,3,24,3,17)

print(tupl.count(3),"\n\n")

#2. display no5 element

print("----conenu de l' element no5-----\n")

print(tupl[4],"\n\n")

#.3 convert  the tuple into list for sort the tuple

print("tuple ordonnee")

t=list(tupl)
print(type(t))

t.sort()
print(t,"\n\n")

#4. append an element to the tuple 

print("ajout d' un element dans le tuple")

t.append(20)
print(t)

