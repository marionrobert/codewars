def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

# better solution
def goals(*a):
    return sum(a)
