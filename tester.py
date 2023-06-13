from datetime import datetime
parcs = [
    {"dateEntretien":datetime(2020,5,4)},
    {"dateEntretien":datetime(2020,6,4)},
    {"dateEntretien":datetime(2020,7,4)},
    {"dateEntretien":datetime(2020,8,4)}
]

parcs.sort(key=lambda x: x["dateEntretien"])
#print(parcs)