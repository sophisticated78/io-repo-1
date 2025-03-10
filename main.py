def zabij_potwora(eliksir: int, olej: int, miecz: int, sila_potwora: int) -> str:
    #Spradzam jaką siłę ma Geralt
    sila_geralta = eliksir + olej + miecz
    # Sprawdzam czy Geralt ma większą siłę niż potwór
    if sila_geralta > sila_potwora:
        return "Geralt zabił potwora"
    else:
        return "Geraltowi nie udało się zabić potwora"

print(zabij_potwora(2, 0, 0, 3)) 
