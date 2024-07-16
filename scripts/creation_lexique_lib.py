"""Ce script permet de créer un lexique de référence à partir des textes finaux."""



from pathlib import Path
import spacy



# Charger le modèle français de spacy
nlp = spacy.load("fr_core_news_sm")



def get_filenames(chemin_dossier: str) -> list[Path]:
    """Renvoie la liste de tous les fichiers textes d'un dossier.

    Parameters
    ----------
    chemin_dossier : str
        chemin du dossier contenant les fichiers textes

    Returns
    -------
    list
        liste des fichiers textes du dossier.
    """
    dossier = Path(chemin_dossier)
    return list(dossier.glob('*.txt'))



# Stocker la liste des fichiers textes dans la variable file_liste
file_liste = get_filenames("../data/TextesFinaux_txt")



def obtenir_lexique(file_liste: list) -> list:
    """Crée un lexique contenant tous les mots présents dans les fichiers textes.

    Parameters
    ----------
    file_liste : str
        liste de fichiers textes

    Returns
    -------
    list
        liste de tous les mots présents dans les fichiers textes.
    """
    lexique = []
    for file in file_liste:
        with open(file, 'r') as lecture_fichier:
            lecture = lecture_fichier.readlines()
            for line in lecture:
                line = line.strip()
                mots = nlp(line)
                for mot in mots:
                    mot = mot.text.lower()   # on recupère le text sinon problème il recupère des attributs mots de spacy
                    if mot not in lexique :
                        lexique.append(mot)
                    else :
                        pass
    return lexique
