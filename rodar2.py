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

def Principal2():
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

    aut12=ComposicaoParalela(aut1, aut2)
    # aut123=ComposicaoParalela(aut12, aut3)
    # aut1234=ComposicaoParalela(aut123, aut4)

    Gf = automatoGf(aut12, ["F"])
    # estadosPosFalha = PartePosFalha(aut1234, ["F"])
    # Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
    # Gf = ParteComportamentoFalha(Gf_mk)


    #F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
    #F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
    #F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
    # F_estadoInicial = ['0|0|0|0|N']

    #Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)


    # Gn2 = ParteNormal(aut1234, ['F'])
    #Gn_2 = automatoGn(aut1234, ['F'])
    #print(Gn.EeE)

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


    #Gni
    Gn1 = automatoGn(aut1, ['F'])
    Gn2 = automatoGn(aut2, ['F'])
    # Gn3 = automatoGn(aut3, ['F'])
    # Gn4 = automatoGn(aut4, ['F'])

    # print(Gn2.eventos)
    Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    Gn = Gn12
    # print("Gn.eventos")
    # print(Gn.eventos)
    # for ee in Gn.EeE:
    #     print(ee)
    # for ee2 in Gn_2.EeE:
    #     print(ee2)


    #Gnil
    print("Gnir")
    # #aut1n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut1, Gn, ["F"]))
    aut1n = limpaGni(automatoGni(aut1, Gn, ["F"]))
    # #aut2n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut2, Gn, ["F"]))
    aut2n = limpaGni(automatoGni(aut2, Gn, ["F"]))
    # #aut3n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut3, Gn, ["F"]))
    # aut3n = limpaGni(automatoGni(aut3, Gn, ["F"]))
    # #aut4n2 = EliminaEstadosSimilares(ParteNormalRestrita(aut4, Gn, ["F"]))
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

    #print(Gn3linha.EeE)
    #print(aut3n.EeE)

    print("renomeados")

    aut1r = Renomear(aut1n, ['S1', 'S2'], 'R1')
    aut2r = Renomear(aut2n, ['S1', 'S2'], 'R2')
    # aut3r = Renomear(aut3n, ['S1', 'S2'], 'R3')
    # aut4r = Renomear(aut4n, ['S1', 'S2'], 'R4')

    # aut1r = Renomear(aut1n, ['S1','S2'], 'R1')
    # aut2r = Renomear(aut2n, ['S1','S2'], 'R2')
    # aut3r = Renomear(aut3n, ['S1','S2'], 'R3')
    # aut4r = Renomear(aut4n, ['S1','S2'], 'R4')
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


    #unitarios
    print("verificadores unitarios")
    ver1 = ComposicaoParalela(aut1r, Gf)
    ver2 = ComposicaoParalela(aut2r, Gf)
    # ver3 = ComposicaoParalela(aut3r, Gf)
    # ver4 = ComposicaoParalela(aut4r, Gf)
    # ver1_2 = ComposicaoParalela(aut1r2, Gf)
    # ver2_2 = ComposicaoParalela(aut2r2, Gf)
    # ver3_2 = ComposicaoParalela(aut3r2, Gf)
    # ver4_2 = ComposicaoParalela(aut4r2, Gf)

    # print("ver1_2.EeE")
    # print(ver1_2.EeE)
    print("ver1.EeE")
    print(ver1.EeE)
    # print("ver2_2.EeE")
    # print(ver2_2.EeE)
    print("ver2.EeE")
    print(ver2.EeE)
    # print("ver3_2.EeE")
    # print(ver3_2.EeE)
    # print("ver3.EeE")
    # print(ver3.EeE)
    # print("ver4_2.EeE")
    # print(ver4_2.EeE)
    # print("ver4.EeE")
    # print(ver4.EeE)
    print(Gf.EeE)

    #duplas
    print("verificadores em dupla")
    ver12 = ComposicaoParalela(aut1r, ver2)
    # ver13 = ComposicaoParalela(aut1r, ver3)
    # ver14 = ComposicaoParalela(aut1r, ver4)
    # ver23 = ComposicaoParalela(aut2r, ver3)
    # ver24 = ComposicaoParalela(aut2r, ver4)
    # ver34 = ComposicaoParalela(aut3r, ver4)

    # #triplas
    # print("verificadores em tripla")
    # ver123 = ComposicaoParalela(aut1r, ver23)
    # ver124 = ComposicaoParalela(aut1r, ver24)
    # ver134 = ComposicaoParalela(aut1r, ver34)
    # ver234 = ComposicaoParalela(aut2r, ver34)
    #
    #
    # #quadruplas
    # print("verificadores em quadrupla")
    # ver1234 = ComposicaoParalela(aut1r, ver234)

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
    # resp = VerificadorDiagnosticabilidade(ver4_2, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    #
    # resp = VerificadorDiagnosticabilidade(ver4, ['S1R1', 'S2R1', 'S1R2', 'S2R2', 'S1R3', 'S2R3', 'S1R4', 'S2R4'])
    #
    # print(resp)
    #print(aut2r.eventos)
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
    return()