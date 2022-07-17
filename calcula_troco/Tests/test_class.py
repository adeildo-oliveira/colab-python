from calcula_troco_com_cedula import ClaculaTrocoComCedula

def test_deve_retornar_troco_20():
    troco = ClaculaTrocoComCedula()
    resultado = troco.troco_com_cedula(100, 80)

    assert resultado[0] == 20

def test_deve_retornar_troco_80():
    troco = ClaculaTrocoComCedula()
    resultado = troco.troco_com_cedula(100, 20)

    assert resultado[0] == 50
    assert resultado[1] == 20
    assert resultado[2] == 10

def test_deve_retornar_troco_com_varias_cedulas():
    troco = ClaculaTrocoComCedula()
    resultado = troco.troco_com_cedula(100, 10.50)

    assert resultado[0] == 50
    assert resultado[1] == 20
    assert resultado[2] == 10
    assert resultado[3] == 5
    assert resultado[4] == 2
    assert resultado[5] == 2
    assert resultado[6] == 0.5
    assert sum(resultado) == 89.5