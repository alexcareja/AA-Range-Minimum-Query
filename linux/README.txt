README

Instructiuni
  Algoritmii si testarea lor necesita Python 3.6+ instalat(sau orice verisune
 mai noua).
  Pentru testarea CORECTITUDINII algoritmilor trebuie executat in terminal
 "make" sau "make test". Pentru testarea EFICIENTEI algoritmilor trebuie
 executat in terminal comanda "make speed" care va lua toti algoritmii si ii va
 supune unui test cu N = 15 000(elemente in vector) si M = 15 000(interogari).

Fisiere
->node.py - contine clasa Node folosita in implementarea arborilor
->input_class.py - contine clasa Input care realizeaza citirea din fisier
->farach_colton_bender.py - contine implemenarea solutiei ce foloseste
 Catesian Tree & Farach-Colton and Bender algorihm
->rmq_spare.py - implementarea solutiei Sparse Table
->segment_tree.py - implementarea solutiei Segment Tree
->rmq_banal.py - functia banala ce raspunde in O(n) unei interogari
->generator_date_in.py - generatorul de teste de intrare
->generator_ref.py - generatorul de referinte, care foloseste rmq_banal pentru
 generarea respunsurilor corecte
->test_algo.py - programul care testeaza testele. Primeste argument in linia de
 comanda. Lista de argumente valide: "sparse", "cartesian", "segment". In
 functie de argument, va supune algoritmul respectiv testelor 0-9 (test10.in
 este folosit la speed test). Make test sau make va testa toate cele 3 solutii.
->speed_test.py - programul care testeaza eficienta in timp a solutiilor de
 rezolvare a RMQ. Lista de argumente valide: "sparse", "cartesian", "segment",
 "basic". La fel ca mai sus, se va rula speed test pe solutia respectiva.
 Bonus: aici am inclus si testarea eficientei solutiei banale, care se poate
 vedea daca rulati "make speed_basic". Speed_test foloseste test10.in ca input
 (N = 15 000, M = 15 000) pentru a putea evidentia eficienta algoritmului
 optim asimptotic(Farach-Colton and Bender).

Observatii
**Testarea eficientei algoritmului lui Farach-Colton si a solutiei Segment Tree
 se va efectua relativ rapid(sub 2 secunde), insa testarea solutiei care 
 foloseste Sparse Table poate dura oriune intre 30 si 180 de secunde, in functie
 de performantele masinii. Totodata, solutia Sparse Table va aloca o matrice de
 15 000 x 15 000 de intregi reprezentati pe 4 bytes care vor ocupa aproximativ
 1GB de memorie RAM.
**Testarea eficientei solutiei banale va dura intre 5 si 20 de secunde, insa nu
 este necesara testarea ei, daca nu doriti.
