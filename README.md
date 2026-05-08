# Test-Engim

La logica dello script è la seguente

Viene usato os.walk per analizzare ogni file presente in una cartella, inclusi quelli nelle sottocartelle

se il file ha l'estensione specificata o non è stata specificata alcuna estensione viene letto e modificato

la cancellazione di righe avviene in questo modo

    -viene calcolato il numero di righe da rimuovere in base alla percentuale e con un minimo di 1, e assicurandosi che non si rimuovano più righe di quelle esistenti

    -vengono poi selezionate in modo casuale le righe da rimuovere

la sostituzione casuale dei caratteri invece

    -per ogni riga rimanente, itera sui caratteri

    -se il carattere è valido viene sostituito da un carattere casuale che può essere una lettera un numero o della punteggiatura

Infine viene sovrascritto il file originale e stampato un resoconto dei file ritoccati