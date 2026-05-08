import os
import random
import string

def cancella_righe (directory, estensioni=None, perc_line=5, perc_chars=5 ):
    if not directory:
        raise ValueError("Directory obbligatoria")
    print(f"Sto lavorando sulla directory: {directory}")
    for cartella, sottocartella, files in os.walk(directory):
        for nome_file in files:
            percorso_completo =os.path.join(cartella, nome_file)
            
            _, estensione = os.path.splitext(nome_file)
        
        if estensioni is not None and estensione not in estensioni:
            continue
        
        with open(percorso_completo, 'r') as f:
            righe=f.readlines()

        print(f"File: {nome_file}, righe trovate: {len(righe)}")

cancella_righe(directory="/home/ilmazu/Progetti/Test Engim/Test", estensioni=[".txt"])