Ce este:

Jocul standard de ruleta ruseasca, cu cateva modificari.

Cum functioneaza:

Se importa modulele tkinter, random si os. Se declara variabila fereastra care va servi drept fereastra principala (root) a aplicatiei. I se atribiue un nume si o dimensiune. Se creeaza un label cu numele jocului si se plaseaza in fereastra principala folosind pack(). Parametrii functiei pack() asigura ca labelul se va extinde odata cu fereastra. Se creeaza functiile de alegere pentru butoane care functioneaza identic: primesc ca parametru stringul optiune si in functie de valoarea acestuia ('da' sau 'nu') ruleaza o alta functie/instruciune sau inchid fereastra popup deschisa. Se observa utilizarea lambda cu rolul de a impacheta o intreaga functie intr-o instructiune compacta ce poate fi transmisa ca parametru butonului. Se definesc functiile de joc. Functia easy doar creeaza o fereastra care contine un label si doua butoane cu optiunea de a iesi sau nu din popupul creat. Functia medium face aproape acelasi lucru, dar este necesara utilizarea functiei randrange() pentru generarea unui numar aleatroiu intre 1 si 6 (principiul de functionare al ruletei). Consecintele "pierderii" jocului in functia medium() sunt reprezentate printr-o fereastra cu un label si doua butoane care dau optiunile de continuare cu acelasi joc sau revenirea la meniu. Functia hard() este identica doar ca daca jocul este "pierdut" se va rula un bloc de cod care foloseste functia makedirs() din modulul os (acest bloc de cod face o "infinitate" de foldere in C: utilizand un while true). Urmeaza declararea butoanelor din meniul principal care primesc ca argumente culoarea, textul, dimensiunea si functia (cu lambda) pe care o vor avea ca instructiune. Totul este afisat cu pack(). Ultima linie este ce face fereastra principala si tot ce se intampla in ea sa se comporte ca o aplicatie prin functia mainloop().

Cum se ruleaza:

Fisierul main.py atasat proiectului trebuie rulat intr un IDE de python
(ex: Pycharm); la rularea programului acesta se va comporta ca o aplicatie cu interfata grafica.

Programul se ruleaza folosind comanda py ./main.py in windows powershell (se atrage atentia asupra faptului ca programul nu este compatibil decat cu sistemul de operare windows, deci prezentarea unei comenzi de rulare pentru linux sau macos ar fi inutila)

Precizari:

Este necesara instalarea in prealabil a modulelor tkinter, random si os.

Referinte:

https://docs.python.org/3/library/tkinter.html
https://github.com/py2exe/py2exe/blob/master/docs/py2exe.freeze.md
https://pyinstaller.org/en/v4.8/usage.html
https://docs.python.org/3/library/random.html
https://stackoverflow.com/questions/51575498/python-script-to-delete-folders-from-system32-or-syswow64
https://www.w3schools.com/python/python_lambda.asp
https://www.youtube.com/watch?v=tpwu5Zb64lQ
https://github.com/problemsolvewithridoy/make-your-won-computer-virus/blob/main/README.md
