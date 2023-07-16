"""
Ce module contient des fonctions utiles pour effectuer une classification non supervisé avec K-means sur un corpus de compétences issus de 30 métiers du secteur de l'informatique.

Auteur: Jeremy Fouquet
Version: 1.0
Date: 16-07-2023
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('french'))  # Mots vides en français
vectorizer = TfidfVectorizer()



def importData(fileName) :
    """
    Importe les données à partir d'un fichier CSV.

    Args:
        fileName (str): Le nom du fichier CSV à importer.

    Returns:
        pandas.DataFrame: Les données importées sous forme de dataframe.
    """
    train = pd.read_csv(fileName, sep=",")
    return train

def cleanData(train) :
    """
    Nettoie les données en appliquant des transformations sur la colonne 'competences' du dataframe.

    Args:
        train (pandas.DataFrame): Le dataframe contenant les données à nettoyer.
    """
    train['competences'] = train['competences'].apply(lambda x: ' '.join([word for word in word_tokenize(x.lower()) if word.isalpha() and word not in stop_words]))

def vectorizedData(train) :
    """
    Effectue la vectorisation des données textuelles.

    Args:
        train (pandas.DataFrame): Le dataframe contenant les données à vectoriser.

    Returns:
        scipy.sparse.csr_matrix: La matrice creuse représentant les données vectorisées.
    """
    X = vectorizer.fit_transform(train['competences'])
    return X

def kmeanData(k, X) :
    """
    Effectue le clustering des données en utilisant l'algorithme K-means.

    Args:
        k (int): Le nombre de clusters à former.
        X (scipy.sparse.csr_matrix): La matrice creuse représentant les données.

    Returns:
        sklearn.cluster.KMeans: L'objet K-means entraîné sur les données.
    """
    kmeans = KMeans(n_clusters=k, n_init='auto') # n_init = Nombre d'initialisations pour l'algorithme K-means
    kmeans.fit(X)
    train['cluster'] = kmeans.labels_ # Attribution des clusters aux métiers
    return kmeans

def predictJobs(kmeans, train) :
    """
    Prédit le(s) métier(s) associé(s) à une liste de compétences.

    Args:
        kmeans (sklearn.cluster.KMeans): L'objet K-means entraîné sur les données.
        train (pandas.DataFrame): Le dataframe contenant les données.

    """
    # exemple_nouvelles_competences = "excel. programmation web. langage python, SQL, javascript.  connaissance du logiciel de design figma. connaissance de git. Anglais intermediaire. Autonome et de bonne capacité d'analyse"
    nouvelles_competences = input("Veuillez saisir une liste de compétences : ")
    # Prétraitement de la nouvelle liste de competences
    nouvelle_competences_preprocessed = ' '.join([word for word in word_tokenize(nouvelles_competences.lower()) if word.isalpha() and word not in stop_words])
    # Vectorisation de la nouvelle iste de competences
    nouvelle_competences_vectorized = vectorizer.transform([nouvelle_competences_preprocessed])
    # Prédiction du cluster pour la nouvelle iste de competences
    nouveau_cluster = kmeans.predict(nouvelle_competences_vectorized)[0]
    # Recherche des métiers associés au cluster prédit
    metiers_associes = train[train['cluster'] == nouveau_cluster]['metier'].unique()
    print("Métier prédit :", metiers_associes)

if __name__ == "__main__":
    # exemple de competences = "exploration de données. visualisation de données. Big data. data mining. sql. excel. tableau. R. analyse des données. développement de tableaux de bord. python. création de rapport. suivi statistiques. Analyse du comportement des clients. collecte de données. analyse de données de ventes"
    train = importData("train.csv")
    cleanData(train)
    X = vectorizedData(train)
    kmeans = kmeanData(8, X)
    predictJobs(kmeans, train)