from django.shortcuts import redirect
from random import choice

paises = ['Colombia', 'Peru', 'Mexico']


class PaisMiddleware():
    def process_request(self, request):
        pass
        # pais = choice(paises)
        # if pais == 'Mexico':
        #     return redirect('http://mejorando.la')