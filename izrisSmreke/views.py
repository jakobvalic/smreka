from django.shortcuts import render

from .forms import Obrazec_smreka, smreka_obrat

def izris_smreke(request, visina=10, orientacija=True):
    opis = "Navzdol " if orientacija else "Navzgor "
    smreka = smreka_obrat(visina)
    smreka = smreka if orientacija else smreka[::-1] # Pravilno orientiran izris smreke
    spremenljivke = {'naslov': 'Izris smreke', 'smreka':smreka, 'opis':opis}
    return render(request, 'izris.html', spremenljivke)

def pridobi_visino(request):
    # Uporabnik je vpisal podatke in pritisnil gumb
    if request.method == 'POST':
        obrazec = Obrazec_smreka(request.POST)
        if obrazec.is_valid():
            visina = obrazec.cleaned_data['visina']
            orientacija = obrazec.cleaned_data['orientacija']
            return izris_smreke(request, visina, orientacija)
    else: # Prazen obrazec
        obrazec = Obrazec_smreka
    return render(request, 'visina.html', {'obrazec':obrazec})






