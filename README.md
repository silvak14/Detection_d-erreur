# verification_d-erreur

La detection d'un bit sur l'octet envoye a la fonction parite() se fait a l'aide d'un masque appele masque dailleur.
j'appliquer le ET logique donc si le resultat est 1 c'est que le bit est a 1.

Avec un modulo j'arrive a teste s'il faut ajouter la parite ou non.
Si le nombre de 1 est pair inutile,sinon le OU logique avec 0x80 (10000000),permet de forcer le bit de poid fort a 1, donc on a ajoute la parite.

A retenir que un octet va de 0x00 a 0xff, soit de a 255 en decimal,le dernir bit sert de bit de parite donc un octet peut avoir des valeurs de 0 a 127 seulement.

C'est  a dire que s'il a'agit d'envoi d'un code ASCII,on ne gere pas la table etendue.
Il est possible avec la part des uc de mettre le 9 eme bit dans la trame pour la parite.
