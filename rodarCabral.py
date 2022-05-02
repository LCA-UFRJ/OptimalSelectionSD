# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:11:09 2019

@author: Lucas
"""

import classes
import funcoes

Automato = classes.Automato
ComposicaoParalela = funcoes.ComposicaoParalela
ComposicaoProduto = funcoes.ComposicaoProduto
DefineEstados = funcoes.DefineEstados
DefineEventos = funcoes.DefineEventos
MontaDictAdjacencias = funcoes.MontaDictAdjacencias
BuscaPorLargura = funcoes.BuscaPorLargura
BuscaPorProfundidade = funcoes.BuscaPorProfundidade
VisitaBuscaPorProfundidade = funcoes.VisitaBuscaPorProfundidade
BuscaPorProfundidadeCompleta = funcoes.BuscaPorProfundidadeCompleta
OrdenacaoTopologica = funcoes.OrdenacaoTopologica
ComponenteFortementeConexo = funcoes.ComponenteFortementeConexo
ParteAcessivel = funcoes.ParteAcessivel
ParteCoacessivel = funcoes.ParteCoacessivel
AlcanceNaoObservavel = funcoes.AlcanceNaoObservavel
Observador = funcoes.Observador
ProcessarAlcanceNaoObservavel = funcoes.ProcessarAlcanceNaoObservavel
Verificador = funcoes.Verificador
VerificadorDiagnosticabilidade = funcoes.VerificadorDiagnosticabilidade
ParteNormal = funcoes.ParteNormal
Renomear = funcoes.Renomear
ComponenteNormal = funcoes.ComponenteNormal
ParteNormalRestrita = funcoes.ParteNormalRestrita
PulaPegaProximo = funcoes.PulaPegaProximo
EliminaEstadosSimilares = funcoes.EliminaEstadosSimilares
PartePosFalha = funcoes.PartePosFalha
ParteComportamentoFalha = funcoes.ParteComportamentoFalha
automatoGf = funcoes.automatoGf
automatoGn = funcoes.automatoGn
automatoGni = funcoes.automatoGni
limpaGni = funcoes.limpaGni
DiagnoseModulosOtimizada = funcoes.DiagnoseModulosOtimizada


def PrincipalCabral():
    estados1 = ["0", "1", "2", "3", "4"]
    eventos1 = ["a", "e", "c", "S1", "g"]
    estadoInicial1 = ["0"]
    EeE1 = [["0", "a", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["2", "c", "4"], ["2", "S1", "3"], ["3", "e", "0"],
            ["4", "g", "3"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["0", "1", "2", "3", "4"]
    eventos2 = ["F", "e", "h", "S1", "S2"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "h", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["1", "F", "4"], ["2", "e", "0"], ["2", "S1", "3"],
            ["3", "S2", "3"], ["4", "h", "4"], ["4", "e", "4"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    estados3 = ["0", "1", "2"]
    eventos3 = ["F", "b", "d", "h"]
    estadoInicial3 = ["0"]
    EeE3 = [["0", "b", "0"], ["0", "h", "1"], ["1", "h", "1"], ["1", "F", "2"], ["2", "h", "2"], ["2", "d", "2"]]
    aut3 = Automato(estados3, eventos3, estadoInicial3, [], EeE3, {})

    estados4 = ["0", "1", "2", "3", "4"]
    eventos4 = ["F", "e", "h"]
    estadoInicial4 = ["0"]
    EeE4 = [["0", "h", "1"], ["0", "e", "0"], ["1", "h", "1"], ["1", "F", "2"], ["1", "e", "0"], ["2", "e", "3"],
            ["3", "e", "3"], ["2", "h", "4"], ["4", "h", "4"]]
    aut4 = Automato(estados4, eventos4, estadoInicial4, [], EeE4, {})

    aut12 = ComposicaoParalela(aut1, aut2)
    aut123 = ComposicaoParalela(aut12, aut3)
    aut1234 = ComposicaoParalela(aut123, aut4)

    Gf = automatoGf(aut1234, ["F"])
    # estadosPosFalha = PartePosFalha(aut1234, ["F"])
    # Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
    # Gf = ParteComportamentoFalha(Gf_mk)

    # F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
    # F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
    # F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
    # F_estadoInicial = ['0|0|0|0|N']

    # Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)

    # Gn2 = ParteNormal(aut1234, ['F'])
    # Gn_2 = automatoGn(aut1234, ['F'])
    # print(Gn.EeE)

    # #Gfi
    # Gf1 = automatoGf(aut1, ['F'])
    # Gf2 = automatoGf(aut2, ['F'])
    # Gf3 = automatoGf(aut3, ['F'])
    # Gf4 = automatoGf(aut4, ['F'])
    #
    # Gf12 = ComposicaoParalela(Gf1, Gf2)
    # Gf123 = ComposicaoParalela(Gf12, Gf3)
    # Gf1234 = ComposicaoParalela(Gf123, Gf4)
    # Gf = Gf1234

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])
    Gn3 = automatoGn(aut3, ['F'])
    Gn4 = automatoGn(aut4, ['F'])

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234
    # print("Gn.eventos")
    # print(Gn.eventos)
    # for ee in Gn.EeE:
    #     print(ee)
    # for ee2 in Gn_2.EeE:
    #     print(ee2)

    # Gnil
    # print("Gnir")
    # aut1n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut1, Gn, ["F"]))
    # aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    # aut2n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut2, Gn, ["F"]))
    # aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))
    # aut3n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut3, Gn, ["F"]))
    # aut3n = limpaGni(automatoGni(aut3, Gn, ["F"]))
    # aut4n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut4, Gn, ["F"]))
    # aut4n = limpaGni(automatoGni(aut4, Gn, ["F"]))
    # aut4n2 = automatoGn(aut4, ["F"])

    # print("aut1n2.EeE")
    # print(aut1n2.EeE)
    # print("aut1n.EeE")
    # print(aut1n.EeE)
    # print("aut2n2.EeE")
    # print(aut2n2.EeE)
    # print("aut2n.EeE")
    # print(aut2n.EeE)
    # print("aut3n2.EeE")
    # print(aut3n2.EeE)
    # print("aut3n.EeE")
    # print(aut3n.EeE)
    # print("aut4n2.EeE")
    # print(aut4n2.EeE)
    # print("aut4n.EeE")
    # print(aut4n.EeE)

    # print(Gn3linha.EeE)
    # print(aut3n.EeE)

    print("renomeados")
    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')
    aut3r = Renomear(Gn3, ['S1', 'S2'], 'R3')
    aut4r = Renomear(Gn4, ['S1', 'S2'], 'R4')
    # aut1r2 = Renomear(aut1n2, ['S1', 'S2'], 'R1')
    # aut2r2 = Renomear(aut2n2, ['S1', 'S2'], 'R2')
    # aut3r2 = Renomear(aut3n2, ['S1', 'S2'], 'R3')
    # aut4r2 = Renomear(aut4n2, ['S1','S2'], 'R4')

    # print("aut1r2.EeE")
    # print(aut1r2.EeE)
    # print("aut1r.EeE")
    # print(aut1r.EeE)
    # print("aut2r2.EeE")
    # print(aut2r2.EeE)
    # print("aut2r.EeE")
    # print(aut2r.EeE)
    # print("aut3r2.EeE")
    # print(aut3r2.EeE)
    # print("aut3r.EeE")
    # print(aut3r.EeE)
    # print("aut4r2.EeE")
    # print(aut4r2.EeE)
    # print("aut4r.EeE")
    # print(aut4r.EeE)

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    ver3 = ComposicaoParalela(aut3r, Gf)
    ver4 = ComposicaoParalela(aut4r, Gf)
    # ver1_2 = ComposicaoParalela(aut1r2, Gf)
    # ver2_2 = ComposicaoParalela(aut2r2, Gf)
    # ver3_2 = ComposicaoParalela(aut3r2, Gf)
    # ver4_2 = ComposicaoParalela(aut4r2, Gf)
    # print("ver1_2.EeE")
    # print(ver1_2.EeE)
    # print("ver1.EeE")
    # print(ver1.EeE)
    # print("ver2_2.EeE")
    # print(ver2_2.EeE)
    # print("ver2.EeE")
    # print(ver2.EeE)
    # print("ver3_2.EeE")
    # print(ver3_2.EeE)
    # print("ver3.EeE")
    # print(ver3.EeE)
    # print("ver4_2.EeE")
    # print(ver4_2.EeE)
    # print("ver4.EeE")
    # print(ver4.EeE)
    # print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    ver13 = ComposicaoParalela(aut1r, ver3)
    ver14 = ComposicaoParalela(aut1r, ver4)
    ver23 = ComposicaoParalela(aut2r, ver3)
    ver24 = ComposicaoParalela(aut2r, ver4)
    ver34 = ComposicaoParalela(aut3r, ver4)

    # triplas
    print("verificadores em tripla")
    ver123 = ComposicaoParalela(aut1r, ver23)
    ver124 = ComposicaoParalela(aut1r, ver24)
    ver134 = ComposicaoParalela(aut1r, ver34)
    ver234 = ComposicaoParalela(aut2r, ver34)

    # quadruplas
    print("verificadores em quadrupla")
    ver1234 = ComposicaoParalela(aut1r, ver234)

    # for e in ver1234.EeE:
    #     print(e)
    diagnose = {}
    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver1'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver2'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver3, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver3'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver4'] = resp[1]
    print(printar)

    # DiagnoseModulosOtimizada(diagnose, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'], [aut1r, aut2r, aut3r, aut4r], [ver1, ver2, ver3, ver4])

    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver12'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver13, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver13'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver14, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver14'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver23, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver23'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver24, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver24'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver34, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver34'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver123, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver123'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver124, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver124'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver134, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver134'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver234, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver234'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver1234, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver1234'] = resp[1]
    print(printar)

    # print(diagnose)

    # print("aut1r.estados")
    # for est in aut1r.estados:
    #     print(est)
    # print("aut2r.estados")
    # for est in aut2r.estados:
    #     print(est)
    # print("aut3r.estados")
    # for est in aut3r.estados:
    #     print(est)
    # print("aut4r.estados")
    # for est in aut4r.estados:
    #     print(est)
    # resp = VerificadorDiagnosticabilidade(ver4_2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    #
    # resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    # print(aut2r.eventos)
    # Gf2 = automatoGf(aut1234, ["F"])
    # #
    # #print(Gf.EeE)
    # #print(Gf2.EeE)
    # #
    # print("EeE Gn")
    # for est in Gn.EeE:
    #     print(est)
    # print("EeE Gn2")
    # for est in Gn2.EeE:
    #     print(est)
    # print("estados Gn")
    # for est in Gn.estados:
    #    if est not in Gn2.estados:
    #        print(est)
    # print("estados Gn2")
    # for est in Gn2.estados:
    #    if est not in Gn.estados:
    #        print(est)

    # print(Gf2.estados)

    # obs = Observador(Gn, ["e", "h"],  ["a","b","c","g","F","S1","S2"])
    # print(obs.estados)
    # print(obs.EeE)
    # aux = []
    # for ee in obs.EeE:
    #     if ee[0] not in aux:
    #         aux.append(ee[0])
    #     if ee[2] not in aux:
    #         aux.append(ee[2])
    #
    # for a in aux:
    #     print(a)
    print("Verificador 1 -> transições:", len(ver1.EeE), " estados: ", len(ver1.estados))
    print("Verificador 2 -> transições:", len(ver2.EeE), " estados: ", len(ver2.estados))
    print("Verificador 3 -> transições:", len(ver3.EeE), " estados: ", len(ver3.estados))
    print("Verificador 4 -> transições:", len(ver4.EeE), " estados: ", len(ver4.estados))
    print("Verificador 12 -> transições:", len(ver12.EeE), " estados: ", len(ver12.estados))
    print("Verificador 13 -> transições:", len(ver13.EeE), " estados: ", len(ver13.estados))
    print("Verificador 14 -> transições:", len(ver14.EeE), " estados: ", len(ver14.estados))
    print("Verificador 23 -> transições:", len(ver23.EeE), " estados: ", len(ver23.estados))
    print("Verificador 24 -> transições:", len(ver24.EeE), " estados: ", len(ver24.estados))
    print("Verificador 34 -> transições:", len(ver34.EeE), " estados: ", len(ver34.estados))
    print("Verificador 123 -> transições:", len(ver123.EeE), " estados: ", len(ver123.estados))
    print("Verificador 124 -> transições:", len(ver124.EeE), " estados: ", len(ver124.estados))
    print("Verificador 134 -> transições:", len(ver134.EeE), " estados: ", len(ver134.estados))
    print("Verificador 234 -> transições:", len(ver234.EeE), " estados: ", len(ver234.estados))
    print("Verificador 1234 -> transições:", len(ver1234.EeE), " estados: ", len(ver1234.estados))

    return ()


def PrincipalCabral2():
    # Synchronous Diagnosis of Discrete-Event Systems 1
    estados1 = ["0", "1", "2", "3"]
    eventos1 = ["a", "b", "d", "S1", "S2", "F"]
    estadoInicial1 = ["0"]
    EeE1 = [["0", "b", "0"], ["0", "F", "1"], ["0", "S2", "2"], ["1", "a", "1"], ["1", "S1", "1"], ["1", "d", "1"],
            ["2", "a", "3"], ["3", "d", "3"], ["3", "b", "2"]]
    marcados1 = ["0", "3"]
    aut1 = Automato(estados1, eventos1, estadoInicial1, marcados1, EeE1, {})

    estados2 = ["0", "1", "2", "3"]
    eventos2 = ["c", "b", "d", "S1", "S2"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "b", "1"], ["0", "S1", "1"], ["0", "S2", "2"], ["1", "c", "0"], ["2", "c", "3"], ["3", "d", "3"],
            ["3", "b", "2"]]
    marcados2 = ["2", "3"]
    aut2 = Automato(estados2, eventos2, estadoInicial2, marcados2, EeE2, {})

    aut12 = ComposicaoParalela(aut1, aut2)

    Gf = automatoGf(aut12, ["F"])
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])

    Gn12 = ComposicaoParalela(Gn1, Gn2)
    Gn = Gn12
    print("Gn.EeE")
    print(Gn.EeE)
    Gn_aux = automatoGn(ComposicaoParalela(aut1, aut2), ["F"])
    print("Gn_aux.EeE")
    print(Gn_aux.EeE)

    # Gnil
    print("Gnir")
    aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))

    print("renomeados")

    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')
    print(aut1r.EeE)
    print(aut2r.EeE)

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)

    print("ver1.EeE")
    print(ver1.EeE)

    print("ver2.EeE")
    print(ver2.EeE)

    print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    print("ver12")
    print(ver12.EeE)

    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)

    print("aut1r.estados")
    for est in aut1r.estados:
        print(est)
    print("aut2r.estados")
    for est in aut2r.estados:
        print(est)

    return ()


def PrincipalCabral3():
    # Synchronous Diagnosis of Discrete-Event Systems 2
    estados1 = ["C0", "C1", "C2", "C3", "C4", "C5", "C6"]
    eventos1 = ["ap", "son", "l", "lon", "soff", "F", "ur", "sr"]
    estadoInicial1 = ["C0"]
    EeE1 = [["C0", "ap", "C1"], ["C1", "son", "C2"], ["C2", "l", "C3"], ["C3", "soff", "C4"], ["C4", "sr", "C0"],
            ["C3", "F", "C5"], ["C5", "soff", "C6"], ["C4", "F", "C6"], ["C3", "lon", "C3"], ["C4", "lon", "C4"],
            ["C5", "lon", "C5"], ["C6", "lon", "C6"], ["C6", "ur", "C6"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
    eventos2 = ["lon", "c", "sr", "ur", "si"]
    estadoInicial2 = ["H0"]
    EeE2 = [["H0", "lon", "H1"], ["H1", "c", "H2"], ["H2", "sr", "H3"], ["H2", "ur", "H3"], ["H3", "si", "H4"],
            ["H4", "lon", "H5"], ["H5", "c", "H6"], ["H6", "sr", "H7"], ["H6", "ur", "H7"], ["H7", "si", "H8"],
            ["H8", "si", "H9"], ["H9", "si", "H0"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    aut12 = ComposicaoParalela(aut1, aut2)

    Gf = automatoGf(aut12, ["F"])

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])

    # print(Gn2.eventos)
    Gn12 = ComposicaoParalela(Gn1, Gn2)

    Gn = Gn12

    # Gnil
    print("Gnir")

    aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))

    print("renomeados")

    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)

    print("ver1.EeE")
    print(ver1.EeE)

    print("ver2.EeE")
    print(ver2.EeE)

    print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)

    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)

    print("aut1r.estados")
    for est in aut1r.estados:
        print(est)
    print("aut2r.estados")
    for est in aut2r.estados:
        print(est)

    return ()


def PrincipalCabral4():
    # synchronous codiagnosability of modular discrete event system
    estados1 = ["0", "1", "2", "3", "4"]
    eventos1 = ["a", "b", "c", "Su", "F"]
    estadoInicial1 = ["0"]
    EeE1 = [["3", "c", "0"], ["1", "F", "4"], ["2", "Su", "3"], ["0", "a", "1"], ["1", "b", "2"], ["4", "c", "4"],
            ["4", "b", "4"], ["4", "a", "4"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["0", "1", "2", "3"]
    eventos2 = ["e", "b", "c", "Su"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "b", "1"], ["1", "Su", "2"], ["2", "e", "3"], ["3", "c", "0"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    aut12 = ComposicaoParalela(aut1, aut2)

    Gf = automatoGf(aut12, ["F"])

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])

    Gn12 = ComposicaoParalela(Gn1, Gn2)
    Gn = Gn12

    # Gnil
    print("Gnir")
    aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))

    print("renomeados")

    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)

    print("ver1.EeE")
    print(ver1.EeE)
    print("ver2.EeE")
    print(ver2.EeE)
    print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)

    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)

    print("aut1r.estados")
    for est in aut1r.estados:
        print(est)
    print("aut2r.estados")
    for est in aut2r.estados:
        print(est)

    return ()


def PrincipalCabral5():
    estados1 = ["0", "1", "2", "3", "4"]
    eventos1 = ["a", "e", "c", "S1", "g"]
    estadoInicial1 = ["0"]
    EeE1 = [["0", "a", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["2", "c", "4"], ["2", "S1", "3"], ["3", "e", "0"],
            ["4", "g", "3"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["0", "1", "2", "3", "4"]
    eventos2 = ["F", "e", "h", "S1", "S2"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "h", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["1", "F", "4"], ["2", "e", "0"], ["2", "S1", "3"],
            ["3", "S2", "3"], ["4", "h", "4"], ["4", "e", "4"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    estados3 = ["0", "1", "2"]
    eventos3 = ["F", "b", "d", "h"]
    estadoInicial3 = ["0"]
    EeE3 = [["0", "b", "0"], ["0", "h", "1"], ["1", "h", "1"], ["1", "F", "2"], ["2", "h", "2"], ["2", "d", "2"]]
    aut3 = Automato(estados3, eventos3, estadoInicial3, [], EeE3, {})

    aut12 = ComposicaoParalela(aut1, aut2)
    aut123 = ComposicaoParalela(aut12, aut3)

    Gf = automatoGf(aut123, ["F"])

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])
    Gn3 = automatoGn(aut3, ['F'])

    Gn12 = ComposicaoParalela(Gn1, Gn2)
    Gn123 = ComposicaoParalela(Gn12, Gn3)
    Gn = Gn123

    # Gnil
    print("Gnir")
    aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))
    aut3n = limpaGni(automatoGni(aut3, Gn, ["F"]))

    print("renomeados")
    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')
    aut3r = Renomear(Gn3, ['S1', 'S2'], 'R3')

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    ver3 = ComposicaoParalela(aut3r, Gf)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    ver13 = ComposicaoParalela(aut1r, ver3)
    ver23 = ComposicaoParalela(aut2r, ver3)

    # triplas
    print("verificadores em tripla")
    ver123 = ComposicaoParalela(aut1r, ver23)

    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver3, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver13, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver23, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver123, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    print(printar)

    print("aut1r.estados")
    for est in aut1r.estados:
        print(est)
    print("aut2r.estados")
    for est in aut2r.estados:
        print(est)
    print("aut3r.estados")
    for est in aut3r.estados:
        print(est)

    return ()


def PrincipalCabralOtimizado():
    estados1 = ["0", "1", "2", "3", "4"]
    eventos1 = ["a", "e", "c", "S1", "g"]
    estadoInicial1 = ["0"]
    EeE1 = [["0", "a", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["2", "c", "4"], ["2", "S1", "3"], ["3", "e", "0"],
            ["4", "g", "3"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["0", "1", "2", "3", "4"]
    eventos2 = ["F", "e", "h", "S1", "S2"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "h", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["1", "F", "4"], ["2", "e", "0"], ["2", "S1", "3"],
            ["3", "S2", "3"], ["4", "h", "4"], ["4", "e", "4"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    estados3 = ["0", "1", "2"]
    eventos3 = ["F", "b", "d", "h"]
    estadoInicial3 = ["0"]
    EeE3 = [["0", "b", "0"], ["0", "h", "1"], ["1", "h", "1"], ["1", "F", "2"], ["2", "h", "2"], ["2", "d", "2"]]
    aut3 = Automato(estados3, eventos3, estadoInicial3, [], EeE3, {})

    estados4 = ["0", "1", "2", "3", "4"]
    eventos4 = ["F", "e", "h"]
    estadoInicial4 = ["0"]
    EeE4 = [["0", "h", "1"], ["0", "e", "0"], ["1", "h", "1"], ["1", "F", "2"], ["1", "e", "0"], ["2", "e", "3"],
            ["3", "e", "3"], ["2", "h", "4"], ["4", "h", "4"]]
    aut4 = Automato(estados4, eventos4, estadoInicial4, [], EeE4, {})

    aut12 = ComposicaoParalela(aut1, aut2)
    aut123 = ComposicaoParalela(aut12, aut3)
    aut1234 = ComposicaoParalela(aut123, aut4)

    Gf = automatoGf(aut1234, ["F"])
    # estadosPosFalha = PartePosFalha(aut1234, ["F"])
    # Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
    # Gf = ParteComportamentoFalha(Gf_mk)

    # F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
    # F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
    # F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
    # F_estadoInicial = ['0|0|0|0|N']

    # Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)

    # Gn2 = ParteNormal(aut1234, ['F'])
    # Gn_2 = automatoGn(aut1234, ['F'])
    # print(Gn.EeE)

    # #Gfi
    # Gf1 = automatoGf(aut1, ['F'])
    # Gf2 = automatoGf(aut2, ['F'])
    # Gf3 = automatoGf(aut3, ['F'])
    # Gf4 = automatoGf(aut4, ['F'])
    #
    # Gf12 = ComposicaoParalela(Gf1, Gf2)
    # Gf123 = ComposicaoParalela(Gf12, Gf3)
    # Gf1234 = ComposicaoParalela(Gf123, Gf4)
    # Gf = Gf1234

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])
    Gn3 = automatoGn(aut3, ['F'])
    Gn4 = automatoGn(aut4, ['F'])

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234
    # print("Gn.eventos")
    # print(Gn.eventos)
    # for ee in Gn.EeE:
    #     print(ee)
    # for ee2 in Gn_2.EeE:
    #     print(ee2)

    # Gnil
    # print("Gnir")
    # aut1n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut1, Gn, ["F"]))
    # aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    # aut2n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut2, Gn, ["F"]))
    # aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))
    # aut3n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut3, Gn, ["F"]))
    # aut3n = limpaGni(automatoGni(aut3, Gn, ["F"]))
    # aut4n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut4, Gn, ["F"]))
    # aut4n = limpaGni(automatoGni(aut4, Gn, ["F"]))
    # aut4n2 = automatoGn(aut4, ["F"])

    # print("aut1n2.EeE")
    # print(aut1n2.EeE)
    # print("aut1n.EeE")
    # print(aut1n.EeE)
    # print("aut2n2.EeE")
    # print(aut2n2.EeE)
    # print("aut2n.EeE")
    # print(aut2n.EeE)
    # print("aut3n2.EeE")
    # print(aut3n2.EeE)
    # print("aut3n.EeE")
    # print(aut3n.EeE)
    # print("aut4n2.EeE")
    # print(aut4n2.EeE)
    # print("aut4n.EeE")
    # print(aut4n.EeE)

    # print(Gn3linha.EeE)
    # print(aut3n.EeE)

    print("renomeados")
    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')
    aut3r = Renomear(Gn3, ['S1', 'S2'], 'R3')
    aut4r = Renomear(Gn4, ['S1', 'S2'], 'R4')
    # aut1r2 = Renomear(aut1n2, ['S1', 'S2'], 'R1')
    # aut2r2 = Renomear(aut2n2, ['S1', 'S2'], 'R2')
    # aut3r2 = Renomear(aut3n2, ['S1', 'S2'], 'R3')
    # aut4r2 = Renomear(aut4n2, ['S1','S2'], 'R4')

    # print("aut1r2.EeE")
    # print(aut1r2.EeE)
    # print("aut1r.EeE")
    # print(aut1r.EeE)
    # print("aut2r2.EeE")
    # print(aut2r2.EeE)
    # print("aut2r.EeE")
    # print(aut2r.EeE)
    # print("aut3r2.EeE")
    # print(aut3r2.EeE)
    # print("aut3r.EeE")
    # print(aut3r.EeE)
    # print("aut4r2.EeE")
    # print(aut4r2.EeE)
    # print("aut4r.EeE")
    # print(aut4r.EeE)

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    ver3 = ComposicaoParalela(aut3r, Gf)
    ver4 = ComposicaoParalela(aut4r, Gf)
    # ver1_2 = ComposicaoParalela(aut1r2, Gf)
    # ver2_2 = ComposicaoParalela(aut2r2, Gf)
    # ver3_2 = ComposicaoParalela(aut3r2, Gf)
    # ver4_2 = ComposicaoParalela(aut4r2, Gf)
    # print("ver1_2.EeE")
    # print(ver1_2.EeE)
    # print("ver1.EeE")
    # print(ver1.EeE)
    # print("ver2_2.EeE")
    # print(ver2_2.EeE)
    # print("ver2.EeE")
    # print(ver2.EeE)
    # print("ver3_2.EeE")
    # print(ver3_2.EeE)
    # print("ver3.EeE")
    # print(ver3.EeE)
    # print("ver4_2.EeE")
    # print(ver4_2.EeE)
    # print("ver4.EeE")
    # print(ver4.EeE)
    # print(Gf.EeE)

    # duplas

    # for e in ver1234.EeE:
    #     print(e)
    diagnose = {}
    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver1'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver2'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver3, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver3'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver4'] = resp[1]
    print(printar)

    DiagnoseModulosOtimizada(diagnose, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'],
                             [aut1r, aut2r, aut3r, aut4r], [ver1, ver2, ver3, ver4])

    # print(diagnose)

    # print("aut1r.estados")
    # for est in aut1r.estados:
    #     print(est)
    # print("aut2r.estados")
    # for est in aut2r.estados:
    #     print(est)
    # print("aut3r.estados")
    # for est in aut3r.estados:
    #     print(est)
    # print("aut4r.estados")
    # for est in aut4r.estados:
    #     print(est)
    # resp = VerificadorDiagnosticabilidade(ver4_2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    #
    # resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    # print(aut2r.eventos)
    # Gf2 = automatoGf(aut1234, ["F"])
    # #
    # #print(Gf.EeE)
    # #print(Gf2.EeE)
    # #
    # print("EeE Gn")
    # for est in Gn.EeE:
    #     print(est)
    # print("EeE Gn2")
    # for est in Gn2.EeE:
    #     print(est)
    # print("estados Gn")
    # for est in Gn.estados:
    #    if est not in Gn2.estados:
    #        print(est)
    # print("estados Gn2")
    # for est in Gn2.estados:
    #    if est not in Gn.estados:
    #        print(est)

    # print(Gf2.estados)

    # obs = Observador(Gn, ["e", "h"],  ["a","b","c","g","F","S1","S2"])
    # print(obs.estados)
    # print(obs.EeE)
    # aux = []
    # for ee in obs.EeE:
    #     if ee[0] not in aux:
    #         aux.append(ee[0])
    #     if ee[2] not in aux:
    #         aux.append(ee[2])
    #
    # for a in aux:
    #     print(a)
    print("Verificador 1 -> transições:", len(ver1.EeE), " estados: ", len(ver1.estados))
    print("Verificador 2 -> transições:", len(ver2.EeE), " estados: ", len(ver2.estados))
    print("Verificador 3 -> transições:", len(ver3.EeE), " estados: ", len(ver3.estados))
    print("Verificador 4 -> transições:", len(ver4.EeE), " estados: ", len(ver4.estados))

    return ()


def PrincipalCabralEsolha():
    estados1 = ["0", "1", "2", "3", "4"]
    eventos1 = ["a", "e", "c", "S1", "g"]
    estadoInicial1 = ["0"]
    EeE1 = [["0", "a", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["2", "c", "4"], ["2", "S1", "3"], ["3", "e", "0"],
            ["4", "g", "3"]]
    aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})

    estados2 = ["0", "1", "2", "3", "4"]
    eventos2 = ["F", "e", "h", "S1", "S2"]
    estadoInicial2 = ["0"]
    EeE2 = [["0", "h", "1"], ["0", "e", "3"], ["1", "S1", "2"], ["1", "F", "4"], ["2", "e", "0"], ["2", "S1", "3"],
            ["3", "S2", "3"], ["4", "h", "4"], ["4", "e", "4"]]
    aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})

    estados3 = ["0", "1", "2"]
    eventos3 = ["F", "b", "d", "h"]
    estadoInicial3 = ["0"]
    EeE3 = [["0", "b", "0"], ["0", "h", "1"], ["1", "h", "1"], ["1", "F", "2"], ["2", "h", "2"], ["2", "d", "2"]]
    aut3 = Automato(estados3, eventos3, estadoInicial3, [], EeE3, {})

    estados4 = ["0", "1", "2", "3", "4"]
    eventos4 = ["F", "e", "h"]
    estadoInicial4 = ["0"]
    EeE4 = [["0", "h", "1"], ["0", "e", "0"], ["1", "h", "1"], ["1", "F", "2"], ["1", "e", "0"], ["2", "e", "3"],
            ["3", "e", "3"], ["2", "h", "4"], ["4", "h", "4"]]
    aut4 = Automato(estados4, eventos4, estadoInicial4, [], EeE4, {})

    aut12 = ComposicaoParalela(aut1, aut2)
    aut123 = ComposicaoParalela(aut12, aut3)
    aut1234 = ComposicaoParalela(aut123, aut4)

    Gf = automatoGf(aut1234, ["F"])
    # estadosPosFalha = PartePosFalha(aut1234, ["F"])
    # Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
    # Gf = ParteComportamentoFalha(Gf_mk)

    # F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
    # F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
    # F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
    # F_estadoInicial = ['0|0|0|0|N']

    # Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)

    # Gn2 = ParteNormal(aut1234, ['F'])
    # Gn_2 = automatoGn(aut1234, ['F'])
    # print(Gn.EeE)

    # #Gfi
    # Gf1 = automatoGf(aut1, ['F'])
    # Gf2 = automatoGf(aut2, ['F'])
    # Gf3 = automatoGf(aut3, ['F'])
    # Gf4 = automatoGf(aut4, ['F'])
    #
    # Gf12 = ComposicaoParalela(Gf1, Gf2)
    # Gf123 = ComposicaoParalela(Gf12, Gf3)
    # Gf1234 = ComposicaoParalela(Gf123, Gf4)
    # Gf = Gf1234

    # Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])
    Gn3 = automatoGn(aut3, ['F'])
    Gn4 = automatoGn(aut4, ['F'])

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234
    # print("Gn.eventos")
    # print(Gn.eventos)
    # for ee in Gn.EeE:
    #     print(ee)
    # for ee2 in Gn_2.EeE:
    #     print(ee2)

    # Gnil
    print("Gnir")
    # aut1n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut1, Gn, ["F"]))
    # aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    # aut2n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut2, Gn, ["F"]))
    # aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))
    # aut3n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut3, Gn, ["F"]))
    # aut3n = limpaGni(automatoGni(aut3, Gn, ["F"]))
    # aut4n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut4, Gn, ["F"]))
    # aut4n = limpaGni(automatoGni(aut4, Gn, ["F"]))
    # aut4n2 = automatoGn(aut4, ["F"])

    # print("aut1n2.EeE")
    # print(aut1n2.EeE)
    # print("aut1n.EeE")
    # print(aut1n.EeE)
    # print("aut2n2.EeE")
    # print(aut2n2.EeE)
    # print("aut2n.EeE")
    # print(aut2n.EeE)
    # print("aut3n2.EeE")
    # print(aut3n2.EeE)
    # print("aut3n.EeE")
    # print(aut3n.EeE)
    # print("aut4n2.EeE")
    # print(aut4n2.EeE)
    # print("aut4n.EeE")
    # print(aut4n.EeE)

    # print(Gn3linha.EeE)
    # print(aut3n.EeE)

    print("renomeados")
    aut1r = Renomear(Gn1, ['S1', 'S2'], 'R1')
    aut2r = Renomear(Gn2, ['S1', 'S2'], 'R2')
    aut3r = Renomear(Gn3, ['S1', 'S2'], 'R3')
    aut4r = Renomear(Gn4, ['S1', 'S2'], 'R4')
    # aut1r2 = Renomear(aut1n2, ['S1', 'S2'], 'R1')
    # aut2r2 = Renomear(aut2n2, ['S1', 'S2'], 'R2')
    # aut3r2 = Renomear(aut3n2, ['S1', 'S2'], 'R3')
    # aut4r2 = Renomear(aut4n2, ['S1','S2'], 'R4')

    # print("aut1r2.EeE")
    # print(aut1r2.EeE)
    # print("aut1r.EeE")
    # print(aut1r.EeE)
    # print("aut2r2.EeE")
    # print(aut2r2.EeE)
    # print("aut2r.EeE")
    # print(aut2r.EeE)
    # print("aut3r2.EeE")
    # print(aut3r2.EeE)
    # print("aut3r.EeE")
    # print(aut3r.EeE)
    # print("aut4r2.EeE")
    # print(aut4r2.EeE)
    # print("aut4r.EeE")
    # print(aut4r.EeE)

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    ver3 = ComposicaoParalela(aut3r, Gf)
    ver4 = ComposicaoParalela(aut4r, Gf)
    # ver1_2 = ComposicaoParalela(aut1r2, Gf)
    # ver2_2 = ComposicaoParalela(aut2r2, Gf)
    # ver3_2 = ComposicaoParalela(aut3r2, Gf)
    # ver4_2 = ComposicaoParalela(aut4r2, Gf)
    # print("ver1_2.EeE")
    # print(ver1_2.EeE)
    # print("ver1.EeE")
    # print(ver1.EeE)
    # print("ver2_2.EeE")
    # print(ver2_2.EeE)
    # print("ver2.EeE")
    # print(ver2.EeE)
    # print("ver3_2.EeE")
    # print(ver3_2.EeE)
    # print("ver3.EeE")
    # print(ver3.EeE)
    # print("ver4_2.EeE")
    # print(ver4_2.EeE)
    # print("ver4.EeE")
    # print(ver4.EeE)
    # print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    ver13 = ComposicaoParalela(aut1r, ver3)
    # ver14 = ComposicaoParalela(aut1r, ver4)
    ver23 = ComposicaoParalela(aut2r, ver3)
    # ver24 = ComposicaoParalela(aut2r, ver4)
    # ver34 = ComposicaoParalela(aut3r, ver4)

    # triplas
    print("verificadores em tripla")
    ver123 = ComposicaoParalela(aut1r, ver23)
    # ver124 = ComposicaoParalela(aut1r, ver24)
    # ver134 = ComposicaoParalela(aut1r, ver34)
    # ver234 = ComposicaoParalela(aut2r, ver34)

    # quadruplas
    print("verificadores em quadrupla")
    # ver1234 = ComposicaoParalela(aut1r, ver234)

    # for e in ver1234.EeE:
    #     print(e)
    diagnose = {}
    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver1'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver2'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver3, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver3'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver4'] = resp[1]
    print(printar)

    # DiagnoseModulosOtimizada(diagnose, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'], [aut1r, aut2r, aut3r, aut4r], [ver1, ver2, ver3, ver4])

    resp = VerificadorDiagnosticabilidade(ver12, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver12'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver13, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver13'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver23, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver23'] = resp[1]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver123, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    printar = [resp[2], resp[1]]
    diagnose['ver123'] = resp[1]
    print(printar)

    # print(diagnose)

    # print("aut1r.estados")
    # for est in aut1r.estados:
    #     print(est)
    # print("aut2r.estados")
    # for est in aut2r.estados:
    #     print(est)
    # print("aut3r.estados")
    # for est in aut3r.estados:
    #     print(est)
    # print("aut4r.estados")
    # for est in aut4r.estados:
    #     print(est)
    # resp = VerificadorDiagnosticabilidade(ver4_2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    #
    # resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    # print(aut2r.eventos)
    # Gf2 = automatoGf(aut1234, ["F"])
    # #
    # #print(Gf.EeE)
    # #print(Gf2.EeE)
    # #
    # print("EeE Gn")
    # for est in Gn.EeE:
    #     print(est)
    # print("EeE Gn2")
    # for est in Gn2.EeE:
    #     print(est)
    # print("estados Gn")
    # for est in Gn.estados:
    #    if est not in Gn2.estados:
    #        print(est)
    # print("estados Gn2")
    # for est in Gn2.estados:
    #    if est not in Gn.estados:
    #        print(est)

    # print(Gf2.estados)

    # obs = Observador(Gn, ["e", "h"],  ["a","b","c","g","F","S1","S2"])
    # print(obs.estados)
    # print(obs.EeE)
    # aux = []
    # for ee in obs.EeE:
    #     if ee[0] not in aux:
    #         aux.append(ee[0])
    #     if ee[2] not in aux:
    #         aux.append(ee[2])
    #
    # for a in aux:
    #     print(a)
    print("Verificador 1 -> transições:", len(ver1.EeE), " estados: ", len(ver1.estados))
    print("Verificador 2 -> transições:", len(ver2.EeE), " estados: ", len(ver2.estados))
    print("Verificador 3 -> transições:", len(ver3.EeE), " estados: ", len(ver3.estados))
    print("Verificador 4 -> transições:", len(ver4.EeE), " estados: ", len(ver4.estados))
    print("Verificador 12 -> transições:", len(ver12.EeE), " estados: ", len(ver12.estados))
    print("Verificador 13 -> transições:", len(ver13.EeE), " estados: ", len(ver13.estados))
    # print("Verificador 14 -> transições:", len(ver14.EeE), " estados: ", len(ver14.estados))
    print("Verificador 23 -> transições:", len(ver23.EeE), " estados: ", len(ver23.estados))
    # print("Verificador 24 -> transições:", len(ver24.EeE), " estados: ", len(ver24.estados))
    # print("Verificador 34 -> transições:", len(ver34.EeE), " estados: ", len(ver34.estados))
    print("Verificador 123 -> transições:", len(ver123.EeE), " estados: ", len(ver123.estados))
    # print("Verificador 124 -> transições:", len(ver124.EeE), " estados: ", len(ver124.estados))
    # print("Verificador 134 -> transições:", len(ver134.EeE), " estados: ", len#(ver134.estados))
    # print("Verificador 234 -> transições:", len(ver234.EeE), " estados: ", len(ver234.estados))
    # print("Verificador 1234 -> transições:", len(ver1234.EeE), " estados: ", len(ver1234.estados))

    return ()






