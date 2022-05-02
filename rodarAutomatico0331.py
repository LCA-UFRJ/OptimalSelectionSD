# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:11:09 2019

@author: Lucas
"""

import classes
import funcoes
import execucao
# import execucao2
# import execucao3
# import execucao4
import rodar
import rodarCabral

from datetime import datetime

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
Rodar = execucao.Rodar
DiagnoseModulosOtimizada = funcoes.DiagnoseModulosOtimizada
SequenciaAteAquiLargura = funcoes.SequenciaAteAquiLargura
SequenciaAteAquiProfundidade = funcoes.SequenciaAteAquiProfundidade
MontaGfLinha = funcoes.MontaGfLinha
TesteGfLinha = funcoes.TesteGfLinha
AdicionaModuloEDiagnostica = funcoes.AdicionaModuloEDiagnostica
BuscaOtimizada = funcoes.BuscaOtimizada
BuscaGfLinha = funcoes.BuscaGfLinha
BuscaInteligente = funcoes.BuscaInteligente
BuscaExaustiva = funcoes.BuscaExaustiva
BuscaGfLinhaCompleta = funcoes.BuscaGfLinhaCompleta
BuscaTodos = funcoes.BuscaTodos
BuscaPorLarguraGfLinha = funcoes.BuscaPorLarguraGfLinha


def Otimizada(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")
    # aut1n = limpaGni(automatoGni(aut1, Gn, eventosF))
    # aut2n = limpaGni(automatoGni(aut2, Gn, eventosF))
    # aut3n = limpaGni(automatoGni(aut3, Gn, eventosF))
    # aut4n = limpaGni(automatoGni(aut4, Gn, eventosF))

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    #print("renomeados")
    # aut1r = Renomear(aut1n, eventosR,'R1') #['S1','S2'], 'R1')
    # aut2r = Renomear(aut2n, eventosR, 'R2') #['S1','S2'], 'R2')
    # aut3r = Renomear(aut3n, eventosR, 'R3') #['S1','S2'], 'R3')
    # aut4r = Renomear(aut4n, eventosR, 'R4') #['S1','S2'], 'R4')

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    #print("verificadores unitarios")
    # ver1 = ComposicaoParalela(aut1r, Gf)
    # ver2 = ComposicaoParalela(aut2r, Gf)
    # ver3 = ComposicaoParalela(aut3r, Gf)
    # ver4 = ComposicaoParalela(aut4r, Gf)

    verUni = []
    automatosVerDict = {}

    # automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaOtimizada(automatosVerDict, autR, verUni, eventosRenomeados)
    estadosOtimizada = 0
    eventosOtimizada = 0
    for k, v in automatosVerDict.items():
        estadosOtimizada = estadosOtimizada + len(v.estados)
        eventosOtimizada = eventosOtimizada + len(v.EeE)

    return [estadosOtimizada, eventosOtimizada, ret[0], ret[1]]


def GfLinha(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    #print("renomeados")

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    contEstados = 0
    contEventos = 0
    #print("verificadores unitarios")

    verUni = []
    automatosVerDict = {}

    automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaGfLinha(automatosVerDict, autR, verUni, eventosRenomeados)

    bases = []
    for k,v in ret[1].items():
        if v['diagnostico'] == ['Linguagem gerada é diagnosticável']:
            bases.append(k)

    #print("gflinhadict")
    #print("")
    #print(ret[2])
    estadosGfLinha = 0
    eventosGfLinha = 0
    for k, v in ret[0].items():
        estadosGfLinha = estadosGfLinha + len(v.estados)
        eventosGfLinha = eventosGfLinha + len(v.EeE)

    for k, v in ret[2].items():
        estadosGfLinha = estadosGfLinha + len(v.estados)
        eventosGfLinha = eventosGfLinha + len(v.EeE)

    # for k, v in ret[2].items():
    #     if "gf'" in k:
    #         print(k)
    #         print(v.estados)
    #         print(v.EeE)




    return [estadosGfLinha, eventosGfLinha, bases, ret, ret[0], ret[2]]


def Inteligente(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    #print("renomeados")

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    #print("verificadores unitarios")

    verUni = []
    automatosVerDict = {}

    automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaInteligente(automatosVerDict, autR, verUni, eventosRenomeados)

    bases = []
    for k, v in ret[1].items():
        if v['diagnostico'] == ['Linguagem gerada é diagnosticável']:
            bases.append(k)

    estadosInteligente = 0
    eventosInteligente = 0
    for k, v in ret[0].items():
        estadosInteligente = estadosInteligente + len(v.estados)
        eventosInteligente = eventosInteligente + len(v.EeE)
    return [estadosInteligente, eventosInteligente, bases, ret, ret[0]]


def Exaustiva(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    #print("verificadores unitarios")

    verUni = []
    automatosVerDict = {}

    automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaExaustiva(automatosVerDict, autR, verUni, eventosRenomeados)

    bases = []
    for k, v in ret[1].items():
        if v['diagnostico'] == ['Linguagem gerada é diagnosticável']:
            bases.append(k)

    estadosExaustiva = 0
    eventosExaustiva = 0
    for k, v in ret[0].items():
        estadosExaustiva = estadosExaustiva + len(v.estados)
        eventosExaustiva = eventosExaustiva + len(v.EeE)

    return [estadosExaustiva, eventosExaustiva, bases, ret, ret[0]]


def GfLinhaCompleta(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    #print("verificadores unitarios")

    verUni = []
    automatosVerDict = {}

    automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaGfLinhaCompleta(automatosVerDict, autR, verUni, eventosRenomeados)

    bases = []
    for k, v in ret[1].items():
        if v['diagnostico'] == ['Linguagem gerada é diagnosticável']:
            bases.append(k)

    estadosGfLinhaCompleto = 0
    eventosGfLinhaCompleto = 0
    for k, v in ret[0].items():
        estadosGfLinhaCompleto = estadosGfLinhaCompleto + len(v.estados)
        eventosGfLinhaCompleto = eventosGfLinhaCompleto + len(v.EeE)

    for k, v in ret[2].items():
        estadosGfLinhaCompleto = estadosGfLinhaCompleto + len(v.estados)
        eventosGfLinhaCompleto = eventosGfLinhaCompleto + len(v.EeE)

    return [estadosGfLinhaCompleto, eventosGfLinhaCompleto, bases, ret, ret[0], ret[2]]


def Todos(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF):
    Gf = automatoGf(autCompleto, eventosF)

    automatosGn = []
    automatosDict = {}
    cont = 1
    for a in aut:
        nome = "Gn" + str(cont)
        Gn = automatoGn(a, eventosF)
        automatosGn.append(Gn)
        automatosDict[nome] = Gn
        cont = cont + 1

    #print(automatosDict)

    # Gn12 = ComposicaoParalela(Gn1, Gn2)
    # Gn123 = ComposicaoParalela(Gn12, Gn3)
    # Gn1234 = ComposicaoParalela(Gn123, Gn4)
    # Gn = Gn1234

    # aut = [aut1, aut2, aut3, aut4]
    junteiGn = []
    autGnCompleto = automatosDict["Gn1"]
    for a in automatosDict.values():
        if junteiGn == []:
            autGnCompleto = a
            junteiGn.append(a)
        else:
            if a not in junteiGn:
                junteiGn.append(a)
                autGnCompleto = ComposicaoParalela(autGnCompleto, a)
    Gn = autGnCompleto

    #print("Gnir")

    autN = []
    automatosNDict = {}
    cont = 1
    for a in aut:
        nome = "aut" + str(cont) + "n"
        autn = limpaGni(automatoGni(a, Gn, eventosF))
        autN.append(autn)
        automatosNDict[nome] = autn
        cont = cont + 1

    #print(automatosNDict)

    autR = []
    automatosRDict = {}
    cont = 1
    eventosRenomeados = []
    for a in automatosNDict.values():
        nome = "aut" + str(cont) + "r"
        autr = Renomear(a, eventosR, "R" + str(cont))  # limpaGni(automatoGni(a, Gn, eventosF))
        autR.append(autr)
        automatosRDict[nome] = autr
        cont = cont + 1
        for ev in eventosR:
            evNovo = ev + "R" + str(cont)
            if evNovo not in eventosRenomeados:
                eventosRenomeados.append(evNovo)

    #print(eventosRenomeados)
    #print(automatosRDict)

    #print("verificadores unitarios")

    verUni = []
    automatosVerDict = {}

    automatosVerDictGlobal = {}
    cont = 1
    for a in automatosRDict.values():
        nome = "ver" + str(cont)
        ver = ComposicaoParalela(a, Gf)  # Renomear(a, eventosR, "R"+str(cont))#limpaGni(automatoGni(a, Gn, eventosF))
        verUni.append(ver)
        automatosVerDict[nome] = ver
        cont = cont + 1

    #print(automatosVerDict)
    ret = BuscaTodos(automatosVerDict, autR, verUni, eventosRenomeados)

    bases = []
    for k, v in ret[1].items():
        if v['diagnostico'] == ['Linguagem gerada é diagnosticável']:
            bases.append(k)

    estadosTodos = 0
    eventosTodos = 0
    for k, v in ret[0].items():
        estadosTodos = estadosTodos + len(v.estados)
        eventosTodos = eventosTodos + len(v.EeE)

    return [estadosTodos, eventosTodos, bases, ret, ret[0]]