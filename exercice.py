#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    nbr=len(string)
    nbr= nbr/2
    if int(nbr):
        print('Le nombre de caractères est pair')
    else:
        print('Le nombre de caractères est impair')
def remove_third_char(string: str) -> str:
    premiers=string[0:2]
    derniers=string[3:len(string)]
    return (premiers+derniers)

#Option 1
def replace_char(string: str, old_char: str, new_char: str) -> str:
  for i in range(len(string)):
      if string[i] == old_char:
        return(string[0:6]+ 'z' +string[7:len(string)])

def get_number_of_char(string: str, char: str) -> int:
    char='1'
    if char in string:
        return(True)
    else:
        return(False)


def get_number_of_words(sentence: str, word: str) -> int:
    word="doo"
    if word in sentence:
       return()


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
