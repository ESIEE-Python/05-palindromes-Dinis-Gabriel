"""
Aucun module utilisé.
"""
#### Fonction secondaire
CARACSUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZÂÊÎÔÛÄËÏÖÜÀÇÉÈÙâêîôûäëïöüàçéèù',;:!.?-"
CARACREPLACE = "abcdefghijklmnopqrstuvwxyzaeiouaeiouaceeuaeiouaeiouaceeu         "
def ispalindrome(p):
    """
    retourne sir la chaine de caractère est un palindrome ou non.

    arg: string object p.

    return: boolean object True or False.
    """
    # votre code ici
    trtable = str.maketrans(CARACSUP, CARACREPLACE)
    pt = p.translate(tr_table)
    pt = pt.replace(" ", "")
    pale = pt[::-1]
    return pt == pale

#### Fonction principale

def main():
    """
    Test la fonction ispalindrome.

    arg: None.

    return: None.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name == "__main":
    main()