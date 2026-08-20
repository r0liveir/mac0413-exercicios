import pytest
from politica_emprestimo import PoliticaEmprestimo

def test_perfil_inexistente():
    assert pytest.raises(ValueError, PoliticaEmprestimo._validar_perfil, "ESTUDANTE")
    
def test_perfil_existente():
    assert PoliticaEmprestimo._validar_perfil("ALUNO") is None


def test_material_inexistente():
    assert pytest.raises(ValueError, PoliticaEmprestimo._validar_material, "JORNAL")
    
def test_material_existente():
    assert PoliticaEmprestimo._validar_material("LIVRO") is None

@pytest.mark.parametrize("perfil, material, esperado", [
    ("ALUNO", "LIVRO", 14),
    ("ALUNO", "REVISTA", 7),
    ("ALUNO", "MIDIA", 3),
    ("PROFESSOR", "LIVRO", 30),
    ("PROFESSOR", "REVISTA", 14),
    ("PROFESSOR", "MIDIA", 7),
])
def test_prazo_emprestimo_livro_correto(perfil, material, esperado):
    assert PoliticaEmprestimo.prazo_emprestimo(perfil, material) == esperado

@pytest.mark.parametrize("perfil, material, erro", [
    ("DIRETOR", "LIVRO", "Perfil inválido"),
    ("ALUNO", "LAPIS", "Material inválido"),
])
def test_obter_prazo_invalido(perfil, material, erro):
    with pytest.raises(ValueError) as exc:
        PoliticaEmprestimo.prazo_emprestimo(perfil, material)

@pytest.mark.parametrize("perfil, material", [
    ("", ""),
    ("ALUNO", ""),
    ("", "DIRETOR"),
])
def test_obter_prazo_invalido_strings_vazias(perfil, material):
    with pytest.raises(ValueError):
        PoliticaEmprestimo.prazo_emprestimo(perfil, material)

def test_0_dias_atraso_retorna_correto():
    material = "LIVRO"
    dias_atraso = 0
    res = PoliticaEmprestimo.calcular_multa(material, dias_atraso)
    assert res == 0.0

@pytest.mark.parametrize("material, dias_atraso, multa_esperada", [
    ("LIVRO", 1, 1.0),
    ("LIVRO", 10, 10.0),
    ("REVISTA", 10,  15.0),
    ("MIDIA", 10, 30.0),
])
def test_dias_atraso_retorna_correto_dias_normais(material, dias_atraso, multa_esperada):
    res = PoliticaEmprestimo.calcular_multa(material, dias_atraso)
    assert res == multa_esperada

def test_dias_atraso_negativo_retorna_zero():
    assert PoliticaEmprestimo.calcular_multa("LIVRO", -1) == 0.0

@pytest.mark.parametrize("material, dias_atraso, multa_esperada", [
    ("LIVRO", 11, 12.0),
    ("REVISTA", 11,  18.0),
    ("MIDIA", 11, 36.0),
])
def test_dias_atraso_retorna_correto_dias_agravados(material, dias_atraso, multa_esperada):
    res = PoliticaEmprestimo.calcular_multa(material, dias_atraso)
    assert res == multa_esperada

def test_calcular_multa_retorna_erro_material_invalido():
    material = "MATERIAL_INVALIDO"
    with pytest.raises(ValueError) as exc:
        PoliticaEmprestimo.calcular_multa(material, 10)


def test_pode_renovar_caso_sucesso():
    assert PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, False, 0)
    assert PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, 0)

def test_nao_pode_renovar_perfil_invalido():
    perfil = "INVALIDO"
    with pytest.raises(ValueError) as exc:
        PoliticaEmprestimo.pode_renovar(perfil, "REVISTA", 0, False, 0)

def test_nao_pode_renovar_material_invalido():
    material = "INVALIDO"
    with pytest.raises(ValueError) as exc:
        PoliticaEmprestimo.pode_renovar("PROFESSOR", material, 0, False, 0)

def test_renovacoes_realizadas_invalido():
    with pytest.raises(ValueError) as exc:
        PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, -1)

def test_nao_pode_renovar_atraso():
    assert not PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 1, False, 0)

def test_nao_pode_renovar_material_reservado():
    assert not PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, True, 0)

def test_nao_pode_renovar_midia():
    assert not PoliticaEmprestimo.pode_renovar("ALUNO", "MIDIA", 0, False, 0)

def test_nao_pode_renovar_revista_mais_uma():
    assert not PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, 1)
    assert not PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, False, 1)

def test_aluno_nao_pode_renovar_livro_mais_duas():
    assert not PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 0, False, 2)

def test_professor_nao_pode_renovar_livro_mais_tres():
    assert not PoliticaEmprestimo.pode_renovar("PROFESSOR", "LIVRO", 0, False, 3)

def test_pode_renovar_livro():
    assert PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 0, False, 0)
    assert PoliticaEmprestimo.pode_renovar("PROFESSOR", "LIVRO", 0, False, 0)


def test_renovar_revista_permitido():
    assert PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, False, 0) == True
    assert PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, 0) == True

