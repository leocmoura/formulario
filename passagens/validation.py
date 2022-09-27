def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destinos são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'
        
def campo_tem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se tem numero no campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números'
        
def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se data de ida é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que de ida'

def data_ida_menor_data_pesquisa(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se data da pesquisa é maior que data viagem"""
    if data_pesquisa > data_ida:
        lista_de_erros['data_ida'] = f'Data inválida: não da pra viajar no tempo!! HOJE: {data_pesquisa}'