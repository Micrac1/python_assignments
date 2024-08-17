import time

_random_seed = 0

# Nastavi pociatocnu hodnotu seedu (resp. N0 alebo 'stav')
# Spusti sa na zaciatku programu/funkcie
def srand(start):
    # Pripadne kontroly na seed (zaporne cislo, atd.)
    global _random_seed
    _random_seed = start

# Vygeneruje nahodne cislo medzi 0 a RAND_MAX na zaklade seedu (resp. N0 alebo 'stavu')
# Spusti sa lubovolne vela krat po spusteni 'srand(...)'
def rand():
    # povie pythonu ze v tejto funkcii budeme pouzivat globalnu premennu _random_seed
    # premennu _random_seed NEinicializuje!
    global _random_seed
    a = 1103515245
    c = 12345
    m = 2**31
    _random_seed = (a*_random_seed + c) % m

    return _random_seed

RAND_MAX = 2**31

srand(time.time_ns())
# Alternativa s pouzitim sekund s desatinnym miestom (vysledok je pocet ms od Epochy)
# // 1 pouzivame ako 'trik' na zaokruhlenie dole.
# srand((time.time() * 1000) // 1)

def generate_data(n: int, start: int, period: int, minimum: float, maximum: float) -> str:
    global RAND_MAX
    rtrn = "[\n"

    for i in range(0, n):
        val = rand() / (RAND_MAX / (maximum - minimum)) + minimum

        # rtrn += " {\"From\": " + str(start) + ", \"Value:\"" + str(val) + "}"
        rtrn += f" {{ \"From\": {str(start)}, \"Value:\" {str(val)} }}"
        if i + 1 < n:
            rtrn += ","

        rtrn += "\n"
        start += period # Alternativne pouzit start + i * period priamo v stringu

    rtrn += "]\n"
    return rtrn

print(generate_data(15, 100000, 3600, -38.124, 12.412), end = '')