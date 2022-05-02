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


def Rodar4():
    # synchronous codiagnosabilityof modular discrete event system
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

    # estados3 = ["0","1","2"]
    # eventos3 = ["F","b","d","h"]
    # estadoInicial3 = ["0"]
    # EeE3 = [["0","b","0"], ["0","h","1"], ["1","h","1"], ["1","F","2"], ["2","h","2"], ["2","d","2"]]
    # aut3 = Automato(estados3, eventos3, estadoInicial3, [] , EeE3, {})
    #
    # estados4 = ["0","1","2","3","4"]
    # eventos4 = ["F","e","h"]
    # estadoInicial4 = ["0"]
    # EeE4 = [["0","h","1"], ["0","e","0"], ["1","h","1"], ["1","F","2"], ["1","e","0"], ["2","e","3"],  ["3","e","3"], ["2","h","4"], ["4","h","4"]]
    # aut4 = Automato(estados4, eventos4, estadoInicial4, [] , EeE4, {})

    aut12 = ComposicaoParalela(aut1, aut2)
    # aut123=ComposicaoParalela(aut12, aut3)
    # aut1234=ComposicaoParalela(aut123, aut4)

    Gf = automatoGf(aut12, ["F"])
    # estadosPosFalha = PartePosFalha(aut1234, ["F"])
    # Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
    # Gf = ParteComportamentoFalha(Gf_mk)

    # F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
    # F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
    # F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
    # F_estadoInicial = ['0|0|0|0|N']

    # Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)

    # Gn2 = ParteNormal(aut1234, ['F'])
    Gn = automatoGn(aut12, ['F'])
    # print(Gn.EeE)

    # Gni
    print("Gnir")
    # aut1n = EliminaEstadosSimilares(ParteNormalRestrita(aut1, Gn, ["F"]))
    aut1n = automatoGni(aut1, Gn, ["F"])
    # print(aut1n3.EeE)
    # aut1n=automatoGn(aut1, ["F"])
    print(aut1n.EeE)
    # aut2n = EliminaEstadosSimilares(ParteNormalRestrita(aut2, Gn, ["F"]))
    aut2n = automatoGni(aut2, Gn, ["F"])
    # aut2n=automatoGn(aut2, ["F"])
    # aut3n = EliminaEstadosSimilares(ParteNormalRestrita(aut3, Gn, ["F"]))
    # aut3n2 = automatoGni(aut3, Gn, ["F"])
    # aut4n = EliminaEstadosSimilares(ParteNormalRestrita(aut4, Gn, ["F"]))
    # aut4n2 = EliminaEstadosSimilares(automatoGni(aut4, Gn, ["F"]))

    # print(aut1n3.EeE)
    # print(aut2n2.EeE)
    # print(Gn3linha.EeE)
    # print(aut3n.EeE)

    print("renomeados")
    aut1r = Renomear(aut1n, ['Su'], 'R1')
    aut2r = Renomear(aut2n, ['Su'], 'R2')
    # aut3r = Renomear(aut3n, ['S1','S2'], 'R3')
    # aut4r = Renomear(aut4n, ['S1','S2'], 'R4')

    # unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    # ver3 = ComposicaoParalela(aut3r, Gf)
    # ver4 = ComposicaoParalela(aut4r, Gf)

    # print(Gf.EeE)

    # duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    # ver13 = ComposicaoParalela(aut1r, ver3)
    # ver14 = ComposicaoParalela(aut1r, ver4)
    # ver23 = ComposicaoParalela(aut2r, ver3)
    # ver24 = ComposicaoParalela(aut2r, ver4)
    # ver34 = ComposicaoParalela(aut3r, ver4)

    # triplas
    # print("verificadores em tripla")
    # ver123 = ComposicaoParalela(aut1r, ver23)
    # ver124 = ComposicaoParalela(aut1r, ver24)
    # ver134 = ComposicaoParalela(aut1r, ver34)
    # ver234 = ComposicaoParalela(aut2r, ver34)

    # quadruplas
    # ver1234 = ComposicaoParalela(aut1r, ver234)

    print("diagnose")
    resp = VerificadorDiagnosticabilidade(ver1, ['urR1', 'urR2'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver2, ['urR1', 'urR2'])
    printar = [resp[2], resp[1]]
    print(printar)
    resp = VerificadorDiagnosticabilidade(ver12, ['urR1', 'urR2'])
    printar = [resp[2], resp[1]]
    print(printar)

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
    return ()