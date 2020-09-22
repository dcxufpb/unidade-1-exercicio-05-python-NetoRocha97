import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    global nome_loja
    nome_loja = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório") 
    nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    logradouro = "Av. Projetada Leste"

def test_numero_zero():
    global numero
    numero = 0
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    numero = 500

def test_municipio_vazio():
    global municipio
    municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    municipio = "Campinas"

def test_estado_vazio():
    global estado
    estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    estado = "SP"

def test_cnpj_vazio():
    global cnpj
    cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == '''
'''
