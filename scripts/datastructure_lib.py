"""Ce script contient les classes utilisées pour le prétraitement des données."""



from dataclasses import dataclass
from typing import List
import spacy



# Charger le modèle français de spacy
nlp = spacy.load("fr_core_news_sm")



@dataclass
class Difference:
    """Classe représentant une erreur."""
    mot_errone: str
    ligne: int
    pos_reel:str
    pos_suppose:str



@dataclass
class Ligne:
    """Classe représentant une ligne du fichier de données."""
    ID: str
    charge: str
    outil: str
    n_burst: int
    debut_burst: float
    duree_burst: float
    duree_pause: float
    duree_cycle: float
    pct_burst: float
    pct_pause: float
    longueur_burst: int
    burst: str
    startPos	: str
    endPos: str
    docLength: int
    categ: str
    charBurst: str
    ratio: float
    

@dataclass
class AnLine:
    """Classe représentant une ligne annotée."""
    ID: str
    charge: str
    outil: str
    n_burst: int
    debut_burst: float
    duree_burst: float
    duree_pause: float
    duree_cycle: float
    pct_burst: float
    pct_pause: float
    longueur_burst: int
    burst: str
    startPos	: str
    endPos: str
    docLength: int
    categ: str
    charBurst: str
    ratio: float
    
    erreur: str
    cat_error: str
    token_erronne: str
    lemme: str
    pos_suppose: str
    pos_reel: str
    longueur: int
    contexte: str
    correction: str



@dataclass
class Token:
    """Classe représentant un token du fichier de données."""
    texte: str
    pos_suppose: str
    lemme: str
    erreur: bool
    categ: str
    longueur: int
    contexte: str
    pos_reel: str
    correction: str
    ligne: Ligne
    
    def get_pos_suppose(self):
        """Retourne la pos supposée."""
        doc = nlp(self.texte)
        for token in doc:
            self.pos_suppose = token.pos_
        return self.pos_suppose

    def get_lemme(self):
        """Retourne le lemme."""
        doc = nlp(self.texte)
        for token in doc:
            self.lemme = token.lemma_
        return self.lemme


@dataclass
class Production:
    """Classe représentant une production à chaque nouveau burst."""
    
    ID: str
    charge: str
    outil: str
    n_burst: int
    debut_burst: float
    duree_burst: float
    duree_pause: float
    duree_cycle: float
    pct_burst: float
    pct_pause: float
    longueur_burst: int
    burst: str
    startPos	: str
    endPos: str
    docLength: int
    categ: str
    charBurst: str
    ratio: float
    
    erreur: str
    cat_error: str
    token_erronne: str
    lemme: str
    pos_suppose: str
    pos_reel: str
    longueur: int
    contexte: str
    correction: str
    
    rt: str
    rt_balise: str
   


@dataclass
class Diff:
    """Classe représentant une différence entre 2 chaînes."""
    start: int
    end: int
    difference: str
    
    

@dataclass
class Annotation:
    """Classe représentant une annotation à chaque nouveau burst."""
    
    ID: str
    charge: str
    outil: str
    n_burst: int
    debut_burst: float
    duree_burst: float
    duree_pause: float
    duree_cycle: float
    pct_burst: float
    pct_pause: float
    longueur_burst: int
    burst: str
    startPos	: str
    endPos: str
    docLength: int
    categ: str
    charBurst: str
    ratio: float
    
    erreur: str
    cat_error: str
    token_erronne: str
    lemme: str
    pos_suppose: str
    pos_reel: str
    longueur: int
    contexte: str
    correction: str
    
    nb_char: int
    nb_words: int
    type_operation: str
    nb_deletion: int
    abs_position: str
    rel_position: tuple
    scope: str
    
    rt: str
    rt_balise: str
    
