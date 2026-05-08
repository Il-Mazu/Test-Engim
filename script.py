import os
import random
import string

def cancella_righe(directory, estensioni=None, perc_lines=5, perc_chars=5):
    if not directory:
        raise ValueError("Directory obbligatoria")
    
    print(f"Sto lavorando sulla directory: {directory}")
    caratteri_casuali = string.ascii_letters + string.digits + string.punctuation

    for cartella, sottocartella, files in os.walk(directory):
        for nome_file in files:
            percorso_completo = os.path.join(cartella, nome_file)
            _, estensione = os.path.splitext(nome_file)

            if estensioni is not None and estensione not in estensioni:
                continue

            try:
                with open(percorso_completo, 'r', encoding='utf-8') as f:
                    righe = f.readlines()
            except Exception as e:
                print(f"Impossibile leggere {nome_file}: {e}")
                continue

            # Gestione file vuoti
            if len(righe) == 0:
                print(f"File vuoto ignorato: {nome_file}")
                continue

            # Cancellazione righe
            n_darimuovere = max(1, int(len(righe) * perc_lines / 100))
            n_darimuovere = min(n_darimuovere, len(righe))  
            indici_darimuovere = set(random.sample(range(len(righe)), n_darimuovere))
            righe = [riga for i, riga in enumerate(righe) if i not in indici_darimuovere]

            # Sostituzione caratteri
            righe_modificate = []
            for riga in righe:
                nuova_riga = ""
                for carattere in riga:
                    if carattere != '\n' and random.random() < perc_chars / 100:
                        nuova_riga += random.choice(caratteri_casuali)
                    else:
                        nuova_riga += carattere
                righe_modificate.append(nuova_riga)

            with open(percorso_completo, 'w', encoding='utf-8') as f:
                f.writelines(righe_modificate)

            print(f"File danneggiato/i: {nome_file}")

# cancella_righe(directory="/path/to/directory")

# cancella_righe(
#    estensioni=[".js", ".txt"],
#    perc_lines=4,
#    perc_chars=6,
#    directory="/path/to/directory"
#)