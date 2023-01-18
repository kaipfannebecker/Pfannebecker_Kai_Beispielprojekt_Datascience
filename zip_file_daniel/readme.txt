Folgendes, ich bräuchte mal deine Einschätzung. Ich habe ein Programm geschrieben, 
was über die CSV Daten in einem Ordner iteriert, aus diesen ein paar Werte ausließt 
und diese dann zusammen mit dem Namen der Datei in eine neue Tabelle schreibt. 
Ich bekomme im Ende also pro Durchlauf ein Tupel. Funktioniert soweit auch, 
allerdings vertauscht er bei einigen Zeilen die beiden Werte (d. H. der Wert, 
der eigentlich in Spalte A landen soll, landet auf einmal in Spalte B und umgekehrt).

Da das ganze bei mehrmaligen Durchläufen mit gleichen Ausgangsdaten und gleichem Programm 
jeweils unterschiedliche Zeilen betrifft, halte ich das ganze für ein Speicherproblem. Die 
drei .jpgs sind Bildschirmfotos des Outputs der drei Durchläufe. Die grauen Zellen mit NAN 
sind die, deren Werte vertauscht wurden. Sie unterscheiden sich von Durchlauf zu Durchlauf.

Hast du irgendeine andere Idee was das sein könnte und/oder wie ich das löse?

