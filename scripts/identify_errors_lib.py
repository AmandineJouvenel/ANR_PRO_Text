"""Ce script permet de détecter tous les mots qui ne sont pas dans le lexiques constitué à partir des textes finaux."""



from datastructure_lib import Ligne, Token, Difference
import csv
from typing import List
from creation_lexique_lib import obtenir_lexique, get_filenames
import spacy



# Cahrger le modèle français de spacy
nlp = spacy.load("fr_core_news_sm")



def ouverture_csv(file: str) -> List[Ligne]:
    """Ouvre un fichier csv et retourne une liste de lignes.

    Parameters
    ----------
    file : str
        fichier csv ou tsv contenant les données originales non annotées

    Returns
    -------
    list
        liste des lignes du fichier.
    """

    # Ouvrir le fichier
    with open (file, 'r', encoding='utf-8') as f:
        
        # S'adapter au format (csv ou tsv)
        if file.endswith('.csv') : 
            delim = ','
        if file.endswith('.tsv') : 
            delim = '\t'
        reader = csv.reader(f, delimiter=delim) ## le delimiter de notre csv c'est des tabs
        next(reader, None)

        # Initialiser une liste pour stocker les lignes non annotées
        liste_lignes = []

        # Parcourir chaque ligne du fichier
        for row in reader:

            line = Ligne(
                ID=row[0],
                charge=row[1],
                outil=row[2],
                n_burst=int(row[3]),
                debut_burst=float(row[4].replace(',', '.')) if row[4] else None,
                duree_burst=float(row[5].replace(',', '.')) if row[5] else None,
                duree_pause=float(row[6].replace(',', '.')) if row[6] else None,
                duree_cycle=float(row[7].replace(',', '.')) if row[7] else None,
                pct_burst=float(row[8].replace(',', '.')) if row[8] else None,
                pct_pause=float(row[9].replace(',', '.')) if row[9] else None,
                longueur_burst=int(row[10]),
                burst=row[11],
                startPos=int(row[12]),
                endPos=int(row[13]),
                docLength=int(row[14]),
                categ=row[15],
                charBurst=row[16],
                ratio=float(row[17].replace(',', '.')) if row[17] else None
                
                )

            liste_lignes.append(line)

        return liste_lignes



def clean_lines(liste_lignes: List[Ligne]) -> List[Ligne]:
    """Nettoie les lignes de la liste.

    Parameters
    ----------
    liste_lignes : list
        liste des lignes du fichier contenant les données originales non annotées

    Returns
    -------
    list
        liste des lignes nettoyées.
    """
    for ligne in liste_lignes:
        ligne.charBurst = ligne.charBurst.replace("␣"," ")
    return liste_lignes



def compare_data_lexique(liste_lignes: List[Ligne], lexique: List[str]) -> list:
    """Compare les données avec le lexique et retourne une liste d'erreurs.

    Parameters
    ----------
    liste_lignes : list
        liste des lignes du fichier contenant les données originales non annotées nettoyées
    lexique : list
        liste des mots issus des documents finaux

    Returns
    -------
    list
        liste des mots n'appartenant pas au lexique.
    """
    n = 0
    liste_erreurs = []
    for ligne in liste_lignes:
        mots_originaux = nlp(ligne.charBurst)
        mots_originaux = ligne.charBurst.split()

        for mot in mots_originaux:
            if mot.text!=" " and mot.text.lower() not in lexique:
                erreur = Difference(mot, n, "Unknown", mot.pos_)
                liste_erreurs.append(erreur)
                n += 1
    return liste_erreurs



def main():
    liste_lignes = ouverture_csv("CLEAN_csv_planification.tsv")
    
    file_list = get_filenames("../data/TextesFinaux_txt")
    lexique = obtenir_lexique(file_list)
    liste_lignes = clean_lines(liste_lignes)

    liste_erreurs = compare_data_lexique(liste_lignes, lexique)

    print("Ligne\tMot erroné\tPos réel\tPos supposé\n")
    for error in liste_erreurs:

        print(f"{error.ligne}\t{error.mot_errone}\t{error.pos_reel}\t{error.pos_suppose}")

if __name__ == "__main__":
    main()
