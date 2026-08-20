import pytest
import politica_emprestimo as pe

# ============================================================================================
# Testes do método _validar_perfil

def test_perfil_inexistente():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo._validar_perfil, "ESTUDANTE")
    
def test_perfil_existente():
    assert pe.PoliticaEmprestimo._validar_perfil("ALUNO") is None
    
# ============================================================================================
# Testes do método _validar_material

def test_material_inexistente():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo._validar_material, "JORNAL")
    
def test_material_existente():
    assert pe.PoliticaEmprestimo._validar_material("LIVRO") is None
    
# ============================================================================================
#  Testes do método prazo_emprestimo
    
def test_prazo_emprestimo_aluno():
    assert pe.PoliticaEmprestimo.prazo_emprestimo("ALUNO", "LIVRO") == 14
    assert pe.PoliticaEmprestimo.prazo_emprestimo("ALUNO", "REVISTA") == 7
    assert pe.PoliticaEmprestimo.prazo_emprestimo("ALUNO", "MIDIA") == 3

def test_prazo_emprestimo_professor():
    assert pe.PoliticaEmprestimo.prazo_emprestimo("PROFESSOR", "LIVRO") == 30
    assert pe.PoliticaEmprestimo.prazo_emprestimo("PROFESSOR", "REVISTA") == 14
    assert pe.PoliticaEmprestimo.prazo_emprestimo("PROFESSOR", "MIDIA") == 7
    
def test_prazo_emprestimo_perfil_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.prazo_emprestimo, "ESTUDANTE", "LIVRO")
    
def test_prazo_emprestimo_material_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.prazo_emprestimo, "ALUNO", "JORNAL")
    
# ============================================================================================
# Testes do método calcular_multa

def test_calcular_multa_material_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.calcular_multa, "JORNAL", 5)
    
def test_calcular_multa_dias_negativos():
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 0) == 0

def test_calcular_multa_livro():
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 0) == 0
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 5) == 5
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 10) == 10
    
def test_calcular_multa_livro_atraso_grande():
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 15) == 20
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 20) == 30
    assert pe.PoliticaEmprestimo.calcular_multa("LIVRO", 25) == 40

def test_calcular_multa_revista():
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 0) == 0
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 5) == 7.5
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 10) == 15

def test_calcular_multa_revista_atraso_grande():
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 15) == 30
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 20) == 45
    assert pe.PoliticaEmprestimo.calcular_multa("REVISTA", 25) == 60

def test_calcular_multa_midia():
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 0) == 0
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 5) == 15
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 10) == 30
    
def test_calcular_multa_midia_atraso_grande():
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 15) == 60
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 20) == 90
    assert pe.PoliticaEmprestimo.calcular_multa("MIDIA", 25) == 120
    
# ============================================================================================
# Testes do método pode_renovar
    
def test_renovar_perfil_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.pode_renovar, "ESTUDANTE", "LIVRO", 0, True, 0)
    
def test_renovar_material_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.pode_renovar, "ALUNO", "JORNAL", 0, True, 0)

def test_renovar_com_num_renovacoes_invalido():
    assert pytest.raises(ValueError, pe.PoliticaEmprestimo.pode_renovar, "ALUNO", "LIVRO", 0, True, -1)
    
def test_renovar_com_atraso():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 1, False, 0) == False

def test_renovar_com_reserva_ativa():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 0, True, 0) == False
    
def test_renovar_midia():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "MIDIA", 0, False, 0) == False
    assert pe.PoliticaEmprestimo.pode_renovar("PROFESSOR", "MIDIA", 0, False, 0) == False
    
def test_renovar_revista_permitido():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, False, 0) == True
    assert pe.PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, 0) == True
    
def test_renovar_revista_negado():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "REVISTA", 0, False, 1) == False
    assert pe.PoliticaEmprestimo.pode_renovar("PROFESSOR", "REVISTA", 0, False, 1) == False
    
    
def test_renovar_livro_permitido():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 0, False, 0) == True
    assert pe.PoliticaEmprestimo.pode_renovar("PROFESSOR", "LIVRO", 0, False, 0) == True
    
def test_renovar_livro_negado():
    assert pe.PoliticaEmprestimo.pode_renovar("ALUNO", "LIVRO", 0, False, 2) == False
    assert pe.PoliticaEmprestimo.pode_renovar("PROFESSOR", "LIVRO", 0, False, 3) == False