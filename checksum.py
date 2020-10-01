#!/usr/bin/env python3



def somme_fletcher(texte):
	checksum1 = []
	checksum2 = []
	somme = 0

	#le tableau checksum1

	for i in texte:

		#ord()La fonction qui va retourner la valeur ASCII
 
		valeur = ord(i)
		somme += valeur
		checksum1.append(somme % 65535)

	# le tableau checksum2

	counter = 0
	somme = 0
	for i in texte:
		somme += checksum1[counter]
		checksum2.append(somme % 65535)
		counter += 1

	#Pour faire retourner un dictionnaire des deux checksums

	return {'checksum1':checksum1,'checksum2':checksum2}

#Pour afficher les 2 tableaux

def afficher_tableau(res):
	liste = ['checksum1','checksum2']
	for nom in liste:
		print("| ",nom," |")
		for i in res[nom]:
			print(i,"\n")

#Pour inserer le texte  commme argument

def main():
	import sys
	if len(sys.argv) != 2:
		print("Inserez un texte en argument")
		return -1
	tableau = somme_fletcher(sys.argv[1])
	afficher_tableau(tableau)


if __name__ == "__main__":
	main()
