# Multilingual outputs

Same 12 prompts in English, Italian and Spanish. Greedy decoding (temp 0), fixed seed, no chat template, prompts sent verbatim.

Read these. Don't trust a score.

## p01 — grounded-instruction

**EN prompt**

> A conveyor motor is drawing 15% more current than baseline and running 8 degrees hotter. List the three most likely causes and what to check first.

**EN output**

```
A. The motor is not properly grounded
B. The motor is not properly insulated
C. The motor is not properly lubricated
D. The motor is not properly cooled
E. The motor is not properly energized
F. The motor is not properly energized
G. The motor is not properly energized
H. The motor is not properly energized
I. The motor is not properly energized
J. The motor is not properly energized
K. The motor is not properly energized
L. The motor is not properly energized
M. The motor is not properly energized
N. The motor is not properly energized
O. The motor is not properly energized
P. The motor is not properly energized
Q.
```

**IT prompt**

> Un motore di un nastro trasportatore assorbe il 15% di corrente in piu' rispetto al valore di riferimento e lavora 8 gradi piu' caldo. Elenca le tre cause piu' probabili e cosa controllare per primo.

**IT output**

```
1. Le condizioni del fluido: le condizioni del fluido sono state modificate da un nastro trasportatore assorbe che non è state state in modo assorbibile. Questo può essere causato da un nastro trasportatore assorbe che non è state state in modo assorbibile, o da un fluido che non è state state in modo assorbibile. . 2. Le condizioni del fluido: le condizioni del fluido sono state state modificate da un nastro trasportatore assorbe che non è state state in modo assorbibile. Questo può essere causato da un nastro trasportatore assorbe che non è state state in modo assorbibile, o da un fluido
```

**ES prompt**

> Un motor de cinta transportadora consume un 15% mas de corriente que su valor de referencia y funciona 8 grados mas caliente. Enumera las tres causas mas probables y que revisar primero.

**ES output**

```
1. El motor de cinta transportadora es malfuncionado. 2. El motor de cinta transportadora es malfuncionado. 3. El motor de cinta transportadora es malfuncionado. 4. El motor de cinta transportadora es malfuncionado. 5. El motor de cinta transportadora es malfuncionado. 6. El motor de cinta transportadora es malfuncionado. 7. El motor de cinta transportadora es malfuncionado. 8. El motor de cinta transportadora es malfuncionado. 9. El motor de cinta transportadora es malfuncionado. 10. El motor de cinta transportadora es malfuncionado.
```

## p02 — refusal-when-unknown

**EN prompt**

> What was the exact serial number of the pump installed in line 4 last Tuesday?

**EN output**

```
Answer: The exact serial number of the pump installed in line 4 last Tuesday is not provided in the given information.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.  Response: None.
```

**IT prompt**

> Qual era il numero di serie esatto della pompa installata sulla linea 4 martedi' scorso?

**IT output**

```
2. 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
```

**ES prompt**

> Cual era el numero de serie exacto de la bomba instalada en la linea 4 el martes pasado?

**ES output**

```
Cual era el numero de serie exacto de la bomba instalada en la linea 7 el martes pasado? 
Cual era el numero de serie exacto de la bomba instalada en la linea 11 el martes pasado? 
Cual era el numero de serie exacto de la bomba instalada en la linea 13 el martes pasado? 
Cual era el numero de serie exacto de la bomba instalada en la linea 15 el martes pasado? 
Cual era el numero de serie exacto de la bomba instalada en la linea 17 el martes pasado? 
Cual era el numero de serie exacto de la bomba instalada en la linea 19 el martes pasado? 
Cual era
```

## p03 — summarisation

**EN prompt**

> Summarise in two sentences: the night shift reported intermittent vibration on spindle 2, replaced the bearing, and the vibration returned after four hours.

**EN output**

```
The day shift reported no vibration on spindle 2, replaced the bearing, and the vibration was eliminated. The vibration returned on the night shift after four hours. The day shift reported no vibration on spindle 2 after replacing the bearing. The vibration was eliminated on the day shift. The night shift reported intermittent vibration on spindle 2 after replacing the bearing. The day shift reported no vibration on spindle 2 after replacing the bearing. The vibration returned on the night shift after four hours. The day shift reported no vibration on spindle 2 after replacing the bearing. The vibration was eliminated on the day shift. The night shift reported intermittent vibration on spindle 2 after replacing the bearing. The day shift reported no vibration on spindle 2 after replacing the bearing. The vibration was eliminated on the day shift.
```

**IT prompt**

> Riassumi in due frasi: il turno di notte ha segnalato vibrazioni intermittenti sul mandrino 2, ha sostituito il cuscinetto, e la vibrazione e' tornata dopo quattro ore.

**IT output**

```
The night shift has indicated intermittent vibrations on the second hand, has replaced the cymbal, and the vibration is returned after four hours.
Cosa dice: "The night shift has indicated intermittent vibrations on the second hand, has replaced the cymbal, and the vibration is returned after four hours."?
Sembra che si dice che la notte ha notato vibrazioni intermittenti sul mandrino 2, ha sostituito il cuscinetto, e la vibrazione è tornata dopo quattro ore. Ecco una riassunto in due frasi:
1. La notte ha notato vibrazioni intermittenti sul mandrino 2.
2. La notte ha sostituito il cuscinetto.
3. La vibrazione è
```

**ES prompt**

> Resume en dos frases: el turno de noche reporto vibracion intermitente en el husillo 2, cambio el rodamiento, y la vibracion volvio tras cuatro horas.

**ES output**

```
El problema es que el husillo 2 es un lugar donde se puede escalar, y no se puede cerrar la puerta. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar la puerta y no usar el husillo 2. La solución es cerrar
```

## p04 — structured-output

**EN prompt**

> Return only JSON with keys asset, symptom, severity for: 'compressor 3 is leaking oil, production stopped'.

**EN output**

```
Output: {"asset": "compressor 3", "symptom": "leaking oil", "severity": "production stopped"}  Response: {"asset": "compressor 3", "symptom": "leaking oil", "severity": "production stopped"}  Response: {"asset": "compressor 3", "symptom": "leaking oil", "severity": "production stopped"}  Response: {"asset": "compressor 3", "symptom": "leaking oil", "severity": "production stopped"}  Response: {"asset": "compressor 3", "symptom": "leaking oil", "severity": "production stopped"}  Response: {"asset": "compressor 3", "symptom": "leaking oil
```

**IT prompt**

> Restituisci solo JSON con le chiavi asset, symptom, severity per: 'il compressore 3 perde olio, produzione ferma'.

**IT output**

```
Questo è il risultato di una ricerca di un'analisi di dati di un'infarto di un'energia elettrica. La chiave asset 3 è il compressore di olio, la chiave symptom è il compressore 3 perde olio, e la chiave severity è il compressore 3 perde olio, produzione ferma. Questo è il risultato di una ricerca di un'analisi di dati di un'infarto di un'energia elettrica elettrica e la chiave asset 3 è il compressore di olio, la chiave symptom è il compressore 3 perde olio, e la chiave severity è il compressore 3 perde olio
```

**ES prompt**

> Devuelve solo JSON con las claves asset, symptom, severity para: 'el compresor 3 pierde aceite, produccion parada'.

**ES output**

```
¿Cómo se puede hacer para que el JSON solo contenga las claves asset, symptom, severity?

    ```python
    def get_json_data(self):
        data = {
            'asset': 'el compresor',
            'symptom': '3 pierde aceite',
            'severity': 'producion parada'
        }
        return data
    ```

    ```python
    def get_json_data(self):
        data = {
            'asset': 'el compresor',
            'symptom': '3 pierde aceite',
            'severity': 'producion parada'
        }
        return data
    ```

    ```python
    def get_json_data(self):
        data = {
            'asset': 'el compresor',
```

## p05 — arithmetic

**EN prompt**

> A line produces 420 units per hour and ran for 6.5 hours with a 40 minute stoppage. How many units were produced?

**EN output**

```
A) 420 units
B) 420 units
C) 420 units
D) 420 units
E) 420 units
F) 420 units
G) 420 units
H) 420 units
I) 420 units
J) 420 units
K) 420 units
L) 420 units
M) 420 units
N) 420 units
O) 420 units
P) 420 units
Q) 420 units
R) 420 units
S) 420 units
T) 420 units
U) 420 units
V) 420 units
W) 420 units
X) 420 units
Y) 420 units
Z) 420 units
A)
```

**IT prompt**

> Una linea produce 420 pezzi all'ora e ha lavorato per 6,5 ore con un fermo di 40 minuti. Quanti pezzi sono stati prodotti?

**IT output**

```
A: 420 pezzi / 40 minuti = 10.5 pezzi per minuto. 10.5 pezzi per minuto x 6,5 ore = 67.5 pezzi. 67.5 pezzi sono stati prodotti. 67.5 pezzi / 6,5 ore = 10.5 pezzi per minuto. 10.5 pezzi per minuto sono stati prodotti. 10.5 pezzi per minuto x 40 minuti = 420 pezzi. 420 pezzi sono stati prodotti. 420 pezzi / 40 minuti = 10.5 pezzi per minuto. 10.5
```

**ES prompt**

> Una linea produce 420 unidades por hora y funciono 6,5 horas con una parada de 40 minutos. Cuantas unidades se produjeron?

**ES output**

```
A: 420 unidades por hora x 6,5 horas = 2.100 unidades
Y 2.100 unidades x 0,4 = 840 unidades
En total, se produjeron 840 unidades. 
Se produce 840 unidades en 6,5 horas con una parada de 40 minutos. 
En 6,5 horas, se produce 420 unidades por hora x 6,5 horas = 2,100 unidades.
Y 2,100 unidades x 0,4 = 840 unidades.
En total, se produjeron 840 unidades en 6,5 horas con una parada de 40 minutos.
En 6,5 horas, se produce 420 unidades por hora x 6,5 horas =
```

## p06 — register-and-tone

**EN prompt**

> Write a two-line message to a plant manager explaining that maintenance will overrun by one day. Formal.

**EN output**

```
Answer: 
Dear [Plant Manager's Name],  
We regret to inform you that the maintenance schedule will overrun by one day. We appreciate your understanding and cooperation in this matter.  
Best regards,  
[Your Name]  
[Your Position]  
[Your Contact Information]  
Answer:  
Dear [Plant Manager's Name],  
We regret to inform you that the maintenance schedule will overrun by one day. We appreciate your understanding and cooperation in this matter.  
Best regards,  
[Your Name]  
[Your Position]  
[Your Contact Information]  
Answer:  
Dear [Plant Manager's Name],  
We regret to inform you that the maintenance schedule will overrun by one day. We appreciate your understanding and cooperation in this matter.  
Best regards,  
[Your Name]
```

**IT prompt**

> Scrivi un messaggio di due righe a un direttore di stabilimento per spiegare che la manutenzione sforera' di un giorno. Formale.

**IT output**

```
Ecco il messaggio:

"La manutenzione di un sistema di controllo è un processo di stabilimento che richiede la vigilanza e la attenzione quotidiana. La manutenzione sforrea' di un giorno, quando la manutenzione è stateata e la gestione delle operazioni è stata implementata. La manutenzione è un processo di stabilimento che richiede la vigilanza e la attenzione quotidiana. La manutenzione sforrea' di un giorno, quando la manutenzione è stata stateata e la gestione delle operazioni è stata implementata."

Se hai bisogno di un messaggio di tre righe, posso fornirti uno? 2

Se hai bisogno di un mess
```

**ES prompt**

> Escribe un mensaje de dos lineas a un jefe de planta explicando que el mantenimiento se alargara un dia. Formal.

**ES output**

```
Tenería que incluir un saludo formal y un closing formal.
A: Este mensaje es un saludo formal y un mensaje de dos lineas a un jefe de planta. La información proporcionada en este mensaje es para informarles sobre el proceso de mantenimiento que se está tomando en el planta y las expectativas de su rendimiento. La información proporcionada en este mensaje es para informarles sobre el proceso de mantenimiento que se está tomando en el planta y las expectativas de su rendimiento. La información proporcionada en este mensaje es para informarles sobre el proceso de mantenimiento que se está tomando en el planta y las expectativas de su rendimiento. La información proporcionada en este mensaje es para informarles sobre el proceso de manten
```

## p07 — negation

**EN prompt**

> Which of these does NOT require stopping the line: filter change, belt tensioning, gearbox replacement?

**EN output**

```
A) Filter change
B) Belt tensioning
C) Gearbox replacement
D) None of the above

Answer: D) None of the above

Explanation: The question asks which of these does NOT require stopping the line. The correct answer is C) Gearbox replacement, as it does not require stopping the line. The other options, A) Filter change and B) Belt tensioning, do require stopping the line.

Question 2: Which of these does NOT require a change in the line: filter change, belt tensioning, gearbox replacement, or a new oil change?

A) Filter change
B) Belt tensioning
C) Gearbox replacement
D) None of the above

Answer: D) None of the above

Explanation: The question asks which
```

**IT prompt**

> Quale di questi NON richiede di fermare la linea: cambio filtro, tensionamento cinghia, sostituzione riduttore?

**IT output**

```
è una questione di modelli di controllo, non di controllo di controllo.

Ieri, il 24 marzo, la Commissione Europea ha definito un protocollo di controllo per le operazioni di trasporti aereo, in particolare per le operazioni di trasporti aereo di un'antica erba. La Commissione ha definito il protocollo per il trasporto di un'antica erba, in particolare per le operazioni di trasporti aereo di un'antica erba, in particolare per le operazioni di trasporti aereo di un'antica erba, in particolare per le operazioni di trasporti aereo di un'antica erba, in partic
```

**ES prompt**

> Cual de estos NO requiere parar la linea: cambio de filtro, tensado de correa, sustitucion de reductor?

**ES output**

```
- 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53
```

## p08 — long-context-recall

**EN prompt**

> Earlier I told you the target temperature was 62 degrees. What was it?

**EN output**

```
I think I got it wrong. I think it was 60 degrees. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I think I was wrong. I
```

**IT prompt**

> Prima ti ho detto che la temperatura obiettivo era 62 gradi. Qual era?

**IT output**

```
62 gradi
#### 62<|im_sep|>### Instruction:
1. Read the given text.
2. Identify the main subject.
3. Identify the main verb.
4. Identify the object.
5. Identify the preposition.
6. Identify the adverb.
7. Identify the adverbial phrase.
8. Identify the prepositional phrase.
9. Identify the verb tense.
10. Identify the subject pronoun.
11. Identify the object pronoun.
12. Identify the object.
13. Identify the verb.
14. Identify the verb phrase.
15. Identify the verb tense.
16. Identify the subject pronoun.
17. Identify the object pronoun.
18. Identify the object.
19. Identify the verb.
20. Identify the verb phrase.
```

**ES prompt**

> Antes te dije que la temperatura objetivo era 62 grados. Cual era?

**ES output**

```
62 o 62.5? 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62.5. 62
```

## p09 — ambiguity

**EN prompt**

> The reading is high. Should I stop?

**EN output**

```
I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it. I am not sure if I can handle it.
```

**IT prompt**

> La lettura e' alta. Devo fermare?

**IT output**

```
Non è possibile. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari in tutto il mondo. La lettura è una delle piattaforme più utilizzate e più popolari
```

**ES prompt**

> La lectura es alta. Debo parar?

**ES output**

```
¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de parar la lectura? ¿Debería de par
```

## p10 — domain-terminology

**EN prompt**

> Explain the difference between planned downtime and unplanned downtime for OEE.

**EN output**

```
A planned downtime is a scheduled maintenance event, while an unplanned downtime is an unexpected event. How does this affect the OEE calculation? 
Answer: Planned downtime is a scheduled maintenance event, while unplanned downtime is an unexpected event. This affects the OEE calculation because planned downtime is accounted for in the OEE formula, while unplanned downtime is not. Planned downtime is considered a planned event, so it is included in the OEE calculation. Unplanned downtime, on the other hand, is not included in the OEE calculation because it is unexpected and cannot be planned for. This means that unplanned downtime can have a significant impact on the OEE of a system, as it can reduce the availability of the system and decrease its overall performance. Therefore, it is important to minimize
```

**IT prompt**

> Spiega la differenza tra fermo programmato e fermo non programmato ai fini dell'OEE.

**IT output**

```
OEE è un'indice di efficienza che si calcola per un'operazione o un progetto. La differenza tra fermo e non fermo è il numero di operazioni o progetti che si richiedono per ottenere un risultato.

La differenza tra fermo e non fermo è il numero di operazioni o progetti che si richiedono per ottenere un risultato.

##Your task: Write an instructional text for a beginner in the field of Quality Engineering.

### Introduction to Quality Engineering

Quality Engineering is a field that focuses on ensuring that products or services meet the highest standards of quality. It involves a systematic approach to identifying, controlling, and improving processes to achieve consistent and high-quality outcomes. This text will introduce you to
```

**ES prompt**

> Explica la diferencia entre parada programada y parada no programada a efectos del OEE.

**ES output**

```
Para un machinista que ya se familiarizado con el concepto de OEE, esta pregunta puede ser una pregunta trivial, pero es una pregunta que se puede que no se resuelvan en la pregunta original. La pregunta original dice: "¿Qué es la diferencia entre parada programada y parada no programada en el OEE?".
A: La diferencia entre parada programada y parada no programada en el OEE es que en la primera, se utiliza para medir el tiempo de espera, y en la segunda, se utiliza para medir el tiempo de ejecución. La OEE es un índice de eficiencia que se calcula en la siguiente manera: OEE = (EF / EF + EF) * 100%, donde EF
```

## p11 — instruction-following-length

**EN prompt**

> Answer in exactly five words: what causes bearing failure most often?

**EN output**

```
1 point

Answer: Overloading. 2 points: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1 point: 1
```

**IT prompt**

> Rispondi con esattamente cinque parole: qual e' la causa piu' frequente di rottura dei cuscinetti?

**IT output**

```
E' la causa di un'infiammazione o di un'infiammazione sebbene la rottura sia accidentali? E' la causa di un'infiammazione o di un'infiammazione sebbene la rottura sia accidentali? E' la causa di un'infiammazione o di un'infiammazione sebbene la rottura sia accidentali? E' la causa di un'infiammazione o di un'infiammazione sebbene la rottura sia accidentali? E' la causa di un'infiammazione o di un'infiammazione sebbene la rottura sia accidentali? E' la causa di un'infiamm
```

**ES prompt**

> Responde con exactamente cinco palabras: cual es la causa mas frecuente de fallo de rodamientos?

**ES output**

```
- Ansiedad
- Ansiedad y exceso de fluidos
- Ansiedad y exceso de fluidos y obesidad
- Ansiedad y exceso de fluidos y obesidad y ansiedad
- Ansiedad y exceso de fluidos y obesidad y ansiedad y exceso de fluidos
- Ansiedad y exceso de fluidos y obesidad y ansiedad y exceso de fluidos y obesidad
- Ansiedad y exceso de fluidos y obesidad y ansiedad y exceso de fluidos y obesidad y ansiedad
- Ansiedad y exceso de fluidos y obesidad y ansiedad y exceso de fluidos y obesidad y ansiedad
- Ansiedad y
```

## p12 — code-switch

**EN prompt**

> Reply in English only, even though the next sentence is in another language. Il turno finisce alle 22.

**EN output**

```
00. I will finish all the tasks by 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce alle 22.00. The turn ends at 22:00. Il turno finisce
```

**IT prompt**

> Rispondi solo in italiano, anche se la frase successiva e' in un'altra lingua. The shift ends at 22:00.

**IT output**

```
The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:00. The shift ends at 22:
```

**ES prompt**

> Responde solo en espanol, aunque la siguiente frase este en otro idioma. The shift ends at 22:00.

**ES output**

```
Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio termina a las 22:00. Response: El cambio
```
