from bojovnik import Bojovník
from kostka import Kostka
from arena import Aréna
from mag import Mág

kostka10 = Kostka(10)
zalgoren = Bojovník("Zalgoren", 60, 20, 10, kostka10)
gandalf = Mág("Gandalf", 45, 15, 12, kostka10, 30, 45)
arena = Aréna(zalgoren, gandalf, kostka10)

arena.zápas()








