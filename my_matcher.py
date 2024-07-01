# noinspection DuplicatedCode
def boyer_moore(T, P):
    """
    Boyer-Moore algoritam pretrage

    Funkcija poredi odgovarajuće karaktera teksta i šablona koji
    se traži sa desna nalevo. Svako nepoklapanje pomera startnu
    poziciju pretrage za broj koraka koji se računa na osnovu
    poslednjeg pojavljivanja nepoklopljenog karaktera iz teksta u šablonu.
    Složenost: O(nm+s), gde su n i m dužine teksta odnosno šablona koji se
    traži, a s predstavlja dužinu alfabeta.

    Argumenti:
    - `T`: tekst koji se pretražuje
    - `P`: šablon koji se traži
    """
    t = len(T)
    p = len(P)

    if p == 0:
        return 0

    pattern_tabel = {}
    for i in range(p):
        pattern_tabel[P[i]] = i

    t_tracker = p-1
    p_tracker = p-1

    while t_tracker < t:
        if P[p_tracker] == T[t_tracker]:
            if p_tracker == 0:
                return t_tracker
            else:
                p_tracker -= 1
                t_tracker -= 1
        else:
            j = pattern_tabel.get(T[t_tracker], -1)
            t_tracker += p - min(p_tracker, j + 1)
            p_tracker = p-1

    return -1


def generate_table(P):
    """
    Funkcija generiše tabelu poklapanja za KMP algoritam

    Tabela poklapanja beleži maksimalnu dužinu tzv. `proper`
    prefiksa stringa koji je ujedno i njegov sufiks.

    Argument:
    - `P`: string čija se tabela generiše
    """
    p = len(P)
    table = [0] * p

    j = 0
    i = 1

    while i < p:
        if P[i] == P[j]:
            table[i] = j+1
            i += 1
            j += 1
        elif j > 0:
            j = table[j - 1]
        else:
            i += 1

        return table


def kmp(T, P):
    t = len(T)
    p = len(P)

    if p == 0:
        return [0]

    table = generate_table(P)

    t_tracker = 0
    p_tracker = 0

    found = []
    while t_tracker < t:
        if P[p_tracker] == T[t_tracker]:
            if p == p_tracker + 1:
                found.append(t_tracker - p + 1)
                p_tracker = table[p_tracker - 1]
            else:
                p_tracker += 1
                t_tracker += 1
        elif p_tracker > 0:
            p_tracker = table[p_tracker - 1]
        else:
            t_tracker += 1

    return found


if __name__ == '__main__':
    text = 'abaabccbcabbabaab'
    pattern = 'abba'
    print(boyer_moore(text, pattern))
    print(kmp(text, pattern))
