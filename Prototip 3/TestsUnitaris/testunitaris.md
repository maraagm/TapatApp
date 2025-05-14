
#### 1- Què són els tests unitaris?

Els tests unitaris són proves automatitzades que comproven el funcionament correcte de les unitats més petites d'un programa, com ara funcions o mòduls. Això permet detectar errors en etapes inicials del desenvolupament i facilita el manteniment del codi.


#### 2- Fes una recerca de llibreries de test amb Python.  Com funciona específicament la llibreria unittest de Python?

Python disposa de diverses llibreries per realitzar tests unitaris. Algunes de les més populars són:

- unittest: Inclosa a la llibreria estàndard de Python, proporciona eines per escriure i executar tests.

- pytest: Una llibreria més flexible i avançada que suporta funcionalitats modernes.

- nose2: Un successor de nose amb una integració senzilla.

Sobre unittest, funciona definint classes que hereten de unittest.TestCase. A cada classe s'hi poden afegir mètodes que comencen amb "test_" per definir proves, i assertions per verificar el comportament esperat.


#### 3-  [testsuma.py](testsuma.py) Exercici exemple test.

#### 4- [testfuncions.py](testfuncions.py) Exercici exemple varies  funcions.

#### 5- Fes una Llista de les assertions més importants en unittest i explica per a que  serveixen

- assertEqual(a, b): Verifica que a és igual a b.

- assertNotEqual(a, b): Verifica que a no és igual a b.

- assertTrue(x): Verifica que x és cert.

- assertFalse(x): Verifica que x és fals.

- assertRaises(Error, func, *args): Comprova que func llença un error del tipus especificat.


#### 6-  (prototip3/testBackend.py)  Fes els tests Unitaris dels teus DAO i webservice del prototip 2 que tens a la carpeta prototip 3
