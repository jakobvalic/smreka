from django import forms


class Obrazec_smreka(forms.Form):
    '''Vsebuje 2 obrazca, preko katerih pridobimo višino in orientacijo smreke.'''
    visina = forms.IntegerField(label='Višina smreke', min_value=1, max_value=80)
    orientacija = forms.BooleanField(label='Smreka je obrnejna na glavo', initial=True, required=False)


def smreka_obrat(n):
    '''Vrne seznam, katerega elementi so 'veje' smreke.'''
    sirina = 2*(n - 1) + 1
    presledek = 0
    smreka = []
    for i in range(n):
        veja = presledek * ' ' + sirina * '*' + presledek * ' '
        sirina -= 2
        presledek += 1
        smreka.append(veja)
    return smreka