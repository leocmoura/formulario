from cProfile import label
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.models.passagem import Passagem
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'origem':'Origem:', 'destino':'Destino', 'data_ida':'Data de ida:', 'data_volta':'Data de volta:', 'informacoes':'Informações:', 'classe_viagem':'Classe de vôo:'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker()
        }

    # origem = forms.CharField(label='Origem', max_length=100)
    # destino = forms.CharField(label='Destino', max_length=100)
    # data_ida = forms.DateField(label='Ida', widget=DatePicker)
    # hora_ida = forms.TimeField(label='Hora_ida')
    # data_volta = forms.DateField(label='Volta', widget=DatePicker)
    # hora_volta = forms.TimeField(label='Hora_volta')
   
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_numero(origem, 'origem', lista_de_erros)
        campo_tem_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_data_pesquisa(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
        