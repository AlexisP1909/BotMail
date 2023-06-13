listeTotaux = [
    (0,12),
    (1,6),
    (2,13)
]
ordreJoursTrav = [x[0] for x in sorted(listeTotaux, key=lambda tup: tup[1], reverse=True)]
dictParcsRange = {dictParcs.keys()[k]:dictParcs.values()[k] for i in ordreJoursTrav}