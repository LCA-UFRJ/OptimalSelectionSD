# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:11:09 2019

@author: Lucas
"""

import classes
import funcoes
import execucao
import exemploprincipal
import exemplo8modulos
# import execucao2
# import execucao3
# import execucao4
#import rodar
#import rodarCabral
import rodarAutomatico

#from datetime import datetime
import time



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
BuscaExaustivaArvore = funcoes.BuscaExaustivaArvore
BuscaGfLinhaArvore = funcoes.BuscaGfLinhaArvore
MontaGniCabral = funcoes.MontaGniCabral

Otimizada = rodarAutomatico.Otimizada #busca com foco nas interseções (ainda nao provado e por isso nao utilizado)
GfLinha = rodarAutomatico.GfLinha #busca com os verificadores parciais, primeiramente pela cardinalidade
Inteligente = rodarAutomatico.Inteligente #busca exaustiva, primeiramente por cardinalidade
Exaustiva = rodarAutomatico.Exaustiva #busca exaustiva, desconsiderando os modulos que contem uma base
ExaustivaArvore = rodarAutomatico.ExaustivaArvore #busca exaustiva, utilizando o método da arvore
GfLinhaCompleta = rodarAutomatico.GfLinhaCompleta #busca por todas as bases minimas utilizando os verificadores parciais
GfLinhaArvore = rodarAutomatico.GfLinhaArvore #busca com os verificadores parciais, utilizando o metodo da arvore
Todos = rodarAutomatico.Todos #busca por todos os verificadores, inclusive os que ja possuem base conhecida
BuscaPorLarguraGfLinha = funcoes.BuscaPorLarguraGfLinha

exemploPrincipal = exemploprincipal.exemploPrincipal()
exemplo8modulos = exemplo8modulos.exemplo8modulos()

#ret = exemploPrincipal()
# estados1 = ["0","1","2","3","4"]
# eventos1 = ["a","e","c","S1","g"]
# estadoInicial1 = ["0"]
# EeE1 = [["0","a","1"], ["0","e","3"], ["1","S1","2"], ["2","c","4"], ["2","S1","3"], ["3","e","0"], ["4","g","3"]]
# aut1 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})
#
#
# estados2 = ["0","1","2","3","4"]
# eventos2 = ["F","e","h","S1","S2"]
# estadoInicial2 = ["0"]
# EeE2 = [["0","h","1"], ["0","e","3"], ["1","S1","2"], ["1","F","4"], ["2","e","0"], ["2","S1","3"],  ["3","S2","3"], ["4","h","4"], ["4","e","4"]]
# aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})
#
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
#
# estados5 = ["0","1","2"]
# eventos5 = ["e","h"]
# estadoInicial5 = ["0"]
# EeE5 = [["0","h","1"], ["0","e","0"], ["1","h","1"], ["1","e","0"]]
# aut5 = Automato(estados5, eventos5, estadoInicial5, [] , EeE5, {})
#
# estados6 = ["0","1","2","3","4"]
# eventos6 = ["a","e","c","S1","g"]
# estadoInicial6 = ["0"]
# EeE6 = [["0","a","1"], ["1","S1","2"], ["2","c","4"], ["2","S1","3"], ["3","e","0"], ["4","g","3"]]
# aut6 = Automato(estados6, eventos6, estadoInicial6, [] , EeE6, {})
#
# eventos = ["a","e","c","g","h","b","d","F","S1","S2"]
# eventosO = ["a","e","c","g","h","b","d"]
# eventosF = ["F"]
#
# eventosNO = []#["F","S1","S2"]
# for ev in eventos:
#   if ev not in eventosO and ev not in eventosNO:
#     eventosNO.append(ev)
# #print(eventosNO)
# eventosR = []
# for ev in eventosNO:
#   if ev not in eventosF and ev not in eventosR:
#     eventosR.append(ev)
# #print(eventosR)
#
# aut = [aut1, aut2, aut3, aut4]#, aut3, aut2, aut4, aut1]#, aut5, aut6, aut3]#, aut4]#, aut5]#, aut6]#, aut1, aut2, aut3, aut4]
# juntei = []
# autCompleto = aut1
# for a in aut:
#     if juntei == []:
#         autCompleto = a
#         juntei.append(a)
#     else:
#         if a not in juntei:
#             juntei.append(a)
#             autCompleto = ComposicaoParalela(autCompleto, a)
#
#
#
# # TempoInicio = int(round(time.time() * 1000))#datetime.now()
# # print("")
# # print("Otimizada")
# # print("")
# # otimizada = Otimizada(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
# #
# TempoFimOtimizada = int(round(time.time() * 1000))#datetime.now()
# # estadosOtimizada = otimizada[0]
# # transicoesOtimizada = otimizada[1]
# #
# # tempoOtimizada = (TempoFimOtimizada - TempoInicio)
# #
# # milliseconds = int(round(time.time() * 1000))
# # print(milliseconds)
# # #print(int(tempoOtimizada))
# #
# # print(tempoOtimizada, "milissegundos")
# # print(estadosOtimizada, "estados")
# # print(transicoesOtimizada, "transições")
# #
# # for k, v in otimizada[3].items():
# #   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# # print("Total: automatos -> ", len(otimizada[3]), ", estados -> ", estadosOtimizada, ", transições -> ", transicoesOtimizada)
# #
# #
# #
# print("")
# print("Gf'")
# print("")
# gf_linha = GfLinha(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
# TempoFimGflinha = int(round(time.time() * 1000))#datetime.now()
# estadosGflinha = gf_linha[0]
# transicoesGflinha = gf_linha[1]
#
# tempoGflinha = (TempoFimGflinha - TempoFimOtimizada)
#
#
# print(tempoGflinha, "milissegundos")
# print(estadosGflinha, "estados")
# print(transicoesGflinha, "transições")
#
#
# for k, v in gf_linha[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# for k, v in gf_linha[5].items():
#   #retirado 20220313
#   #if k[3:] not in gf_linha[7].keys():
#     print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", gf_linha[6], ", estados -> ", estadosGflinha, ", transições -> ", transicoesGflinha)
# print("")
# print("Inteligente")
# print("")
# inteligente = Inteligente(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
#
#
# TempoFimInteligente = int(round(time.time() * 1000))#datetime.now()
# estadosInteligente = inteligente[0]
# transicoesInteligente = inteligente[1]
#
# tempoInteligente = (TempoFimInteligente - TempoFimGflinha)
#
# print(tempoInteligente, "milissegundos")
# print(estadosInteligente, "estados")
# print(transicoesInteligente, "transições", "transições")
#
# for k, v in inteligente[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", len(inteligente[4]), ", estados -> ", estadosInteligente, ", transições -> ", transicoesInteligente)
# print("")
# print("Gf' Completa")
# print("")
# gf_linhaCompleta = GfLinhaCompleta(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
# TempoFimGfLinhaCompleta = int(round(time.time() * 1000))#datetime.now()
# estadosGfLinhaCompleta = gf_linhaCompleta[0]
# transicoesGfLinhaCompleta = gf_linhaCompleta[1]
#
# TempoGfLinhaCompleta = (TempoFimGfLinhaCompleta - TempoFimInteligente)
#
#
# print(TempoGfLinhaCompleta, "milissegundos")
# print(estadosGfLinhaCompleta, "estados")
# print(transicoesGfLinhaCompleta, "transições")
#
# for k, v in gf_linhaCompleta[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# for k, v in gf_linhaCompleta[5].items():
#   #returado 20220313
#   # if k[3:] not in gf_linhaCompleta[7].keys():
#     print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", gf_linhaCompleta[6], ", estados -> ", estadosGfLinhaCompleta, ", transições -> ", transicoesGfLinhaCompleta)
# print("")
# print("Exaustiva")
# print("")
# exaustiva = Exaustiva(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
# TempoFimExaustiva = int(round(time.time() * 1000))#datetime.now()
# estadosExaustiva = exaustiva[0]
# transicoesExaustiva = exaustiva[1]
#
# tempoExaustiva = (TempoFimExaustiva - TempoFimGfLinhaCompleta)
#
#
# print(tempoExaustiva, "milissegundos")
# print(estadosExaustiva, "estados")
# print(transicoesExaustiva, "transições")
#
# for k, v in exaustiva[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", len(exaustiva[4]), ", estados -> ", estadosExaustiva, ", transições -> ", transicoesExaustiva)
#
# print("")
# print("Exaustiva Arvore")
# print("")
# exaustivaArvore = ExaustivaArvore(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
# TempoFimExaustivaArvore = int(round(time.time() * 1000))#datetime.now()
# estadosExaustivaArvore = exaustivaArvore[0]
# transicoesExaustivaArvore = exaustivaArvore[1]
#
# tempoExaustivaArvore = (TempoFimExaustivaArvore - TempoFimExaustiva)
#
#
# print(tempoExaustivaArvore, "milissegundos")
# print(estadosExaustivaArvore, "estados")
# print(transicoesExaustivaArvore, "transições")
#
# for k, v in exaustivaArvore[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", len(exaustivaArvore[4]), ", estados -> ", estadosExaustivaArvore, ", transições -> ", transicoesExaustivaArvore)
#
# print("")
# print("Gf' Arvore")
# print("")
# gf_linhaArvore = GfLinhaArvore(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
# #
# TempoFimGfLinhaArvore = int(round(time.time() * 1000))#datetime.now()
# estadosGfLinhaArvore = gf_linhaArvore[0]
# transicoesGfLinhaArvore = gf_linhaArvore[1]
# #
# TempoGfLinhaArvore = (TempoFimGfLinhaArvore - TempoFimExaustivaArvore)
# #
# #
# print(TempoGfLinhaArvore, "milissegundos")
# print(estadosGfLinhaArvore, "estados")
# print(transicoesGfLinhaArvore, "transições")
#
# print("")
# print("Todos")
# print("")
# todos = Todos(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
# TempoFimTodos = int(round(time.time() * 1000))#datetime.now()
# estadosTodos = todos[0]
# transicoesTodos = todos[1]
#
# tempoTodos = (TempoFimTodos - TempoFimGfLinhaArvore)
#
#
# print(tempoTodos, "milissegundos")
# print(estadosTodos, "estados")
# print(transicoesTodos, "transições")
#
# for k, v in todos[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
#
# print("Total: automatos -> ", len(todos[4]), ", estados -> ", estadosTodos, ", transições -> ", transicoesTodos)
#
#
# #
# for k, v in gf_linhaArvore[4].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# for k, v in gf_linhaArvore[5].items():
#   #retirado 20220313 LR
#   #if k[3:] not in gf_linhaArvore[7].keys():
#     print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", gf_linhaArvore[6], ", estados -> ", estadosGfLinhaArvore, ", transições -> ", transicoesGfLinhaArvore)
# #
#
#
# # print("A busca otimizada foi feita em ", tempoOtimizada, "milissegundos, com ", estadosOtimizada, "estados e ", transicoesOtimizada, "transições.")
# # print("As bases encontradas foram:")
# # print(otimizada[2][1])
#
# print("A busca Gf' foi feita em ", tempoGflinha, "milissegundos, com ", estadosGflinha, "estados e ", transicoesGflinha, "transições.")
# print("As bases encontradas foram:")
# print(gf_linha[2])
#
# print("A busca inteligente foi feita em ", tempoInteligente, "milissegundos, com ", estadosInteligente, "estados e ", transicoesInteligente, "transições.")
# print("As bases encontradas foram:")
# print(inteligente[2])
#
# print("A busca Gf' copmleta foi feita em ", TempoGfLinhaCompleta, "milissegundos, com ", estadosGfLinhaCompleta, "estados e ", transicoesGfLinhaCompleta, "transições.")
# print("As bases encontradas foram:")
# print(gf_linhaCompleta[2])
#
# print("A busca exaustiva foi feita em ", tempoExaustiva, "milissegundos, com ", estadosExaustiva, "estados e ", transicoesExaustiva, "transições.")
# print("As bases encontradas foram:")
# print(exaustiva[2])
#
# print("A busca exaustiva foi feita em ", tempoTodos, "milissegundos, com ", estadosTodos, "estados e ", transicoesTodos, "transições.")
# print("As bases encontradas foram:")
# print(todos[2])
#
# print("A busca Gf' arvore foi feita em ", TempoGfLinhaArvore, "milissegundos, com ", estadosGfLinhaArvore, "estados e ", transicoesGfLinhaArvore, "transições.")
# print("As bases encontradas foram:")
# print(gf_linhaArvore[2])
#
# print("A busca exaustiva arvore foi feita em ", tempoExaustivaArvore, "milissegundos, com ", estadosExaustivaArvore, "estados e ", transicoesExaustivaArvore, "transições.")
# print("As bases encontradas foram:")
# print(exaustivaArvore[2])
#
#
#
# # print(tempoOtimizada)
# # print(estadosOtimizada)
# # print(transicoesOtimizada)
# # #print("Com relação aos conjuntos com menor cardinalidade houve uma economia no tempo de execução de:", (tempoInteligente-tempoOtimizada/tempoInteligente), "%, na quantidade de estados de :", (estadosInteligente-estadosOtimizada/estadosInteligente), "% e na quantidade de transições de:", transicoesInteligente-transicoesOtimizada/transicoesInteligente,"%")
#
# #print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-tempoOtimizada/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosOtimizada/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesOtimizada/transicoesTodos,"%")
#
# print(tempoGflinha)
# print(estadosGflinha)
# print(transicoesGflinha)
# #print("Com relação aos conjuntos com menor cardinalidade houve uma economia no tempo de execução de:", (tempoInteligente-tempoGflinha/tempoInteligente), "%, na quantidade de estados de :", (estadosInteligente-estadosGflinha/estadosInteligente), "% e na quantidade de transições de:", transicoesInteligente-transicoesGflinha/transicoesInteligente,"%")
#
# print(tempoInteligente)
# print(estadosInteligente)
# print(transicoesInteligente)
#
# print(TempoGfLinhaCompleta)
# print(estadosGfLinhaCompleta)
# print(transicoesGfLinhaCompleta)
# #print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-TempoGfLinhaCompleta/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosGfLinhaCompleta/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesGfLinhaCompleta/transicoesTodos,"%")
#
# print(tempoExaustiva)
# print(estadosExaustiva)
# print(transicoesExaustiva)
# #print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-tempoExaustiva/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosExaustiva/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesExaustiva/transicoesTodos,"%")
#
#
# print(tempoTodos)
# print(estadosTodos)
# print(transicoesTodos)
#
# print(TempoGfLinhaArvore)
# print(estadosGfLinhaArvore)
# print(transicoesGfLinhaArvore)
# #print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-TempoGfLinhaCompleta/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosGfLinhaCompleta/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesGfLinhaCompleta/transicoesTodos,"%")
#
# print(tempoExaustivaArvore)
# print(estadosExaustivaArvore)
# print(transicoesExaustivaArvore)
#
#
# # print(TempoInicio)
# print(TempoFimOtimizada)
# print(TempoFimGflinha)
# print(TempoFimInteligente)
# print(TempoFimGfLinhaCompleta)
# print(TempoFimTodos)
#
#
#
# print("TempoGfLinhaCompleta")
#
# print(TempoGfLinhaCompleta)
#
# print("tempoExaustiva")
#
# print(tempoExaustiva)
# print("TempoGfLinhaArvore")
#
# print(TempoGfLinhaArvore)
#
# print("tempoExaustivaArvore")
#
# print(tempoExaustivaArvore)
#
# #
# # #testes apagar depois
# # # exemplo 3.5
# # estados1 = ["C0", "C1", "C2", "C3", "C4", "C5", "C6"]
# # eventos1 = ["ap", "son", "l", "lon", "soff", "F", "ur", "sr"]
# # estadoInicial1 = ["C0"]
# # EeE1 = [["C0", "ap", "C1"], ["C1", "son", "C2"], ["C2", "l", "C3"], ["C3", "soff", "C4"], ["C4", "sr", "C0"],
# #         ["C3", "F", "C5"], ["C5", "soff", "C6"], ["C4", "F", "C6"], ["C3", "lon", "C3"], ["C4", "lon", "C4"],
# #         ["C5", "lon", "C5"], ["C6", "lon", "C6"], ["C6", "ur", "C6"]]
# # aut1 = Automato(estados1, eventos1, estadoInicial1, [], EeE1, {})
# #
# # estados2 = ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
# # eventos2 = ["lon", "c", "sr", "ur", "si"]
# # estadoInicial2 = ["H0"]
# # EeE2 = [["H0", "lon", "H1"], ["H1", "c", "H2"], ["H2", "sr", "H3"], ["H2", "ur", "H3"], ["H3", "si", "H4"],
# #         ["H4", "lon", "H5"], ["H5", "c", "H6"], ["H6", "sr", "H7"], ["H6", "ur", "H7"], ["H7", "si", "H8"],
# #         ["H8", "si", "H9"], ["H9", "si", "H0"]]
# # aut2 = Automato(estados2, eventos2, estadoInicial2, [], EeE2, {})
# #
# #
# # aut12=ComposicaoParalela(aut1, aut2)
# #
# # Gf = automatoGf(aut12, ["F"])
# # Gn1 = automatoGn(aut1, ['F'])
# # Gn2 = automatoGn(aut2, ['F'])
# # Gn12 = ComposicaoParalela(Gn1, Gn2)
# # Gn = Gn12
# # #Gnil
# # print("Gnir")
# # aut1n = Gn1#limpaGni(automatoGni(aut1, Gn, ["F"]))
# # aut2n = Gn2#limpaGni(automatoGni(aut2, Gn, ["F"]))
# #
# # gn1a = automatoGn(aut1, "F")
# # gn2a = automatoGn(aut2, "F")
# # gn = ComposicaoParalela(gn1a, gn2a)
# # gn1 = MontaGniCabral(gn1a, 1, [gn1a, gn2a], gn, ["F"])
# # gn2 = MontaGniCabral(gn2a, 2, [gn1a, gn2a], gn, ["F"])
# #
# # aut1n = gn1#limpaGni(automatoGni(aut1, Gn, ["F"]))
# # aut2n = gn2#limpaGni(automatoGni(aut2, Gn, ["F"]))
# #
# #
# # aut1r = Renomear(aut1n, ['ur', 'S2'], 'R1')
# # aut2r = Renomear(aut2n, ['ur', 'S2'], 'R2')
# #
# # ver1 = ComposicaoParalela(Gf, aut1r)
# # ver2 = ComposicaoParalela(Gf, aut2r)
# #
# #
# # ver12 = ComposicaoParalela(ver1, ver2)
# #
# # print(VerificadorDiagnosticabilidade(ver1, ['urR1', 'urR2']))
# # print(VerificadorDiagnosticabilidade(ver2, ['urR1', 'urR2']))
# # print(VerificadorDiagnosticabilidade(ver12, ['urR1', 'urR2']))
# # for ee in ver1.EeE:
# #     print(ee)
# #
# # for ee in ver2.EeE:
# #     print(ee)
# #
# # for es in ver1.estados:
# #     print(es)
# #
# # for es in ver2.estados:
# #     print(es)
# #
# # for ef in Gf.EeE:
# #     print(ef)
# # for en in Gn.EeE:
# #     print(en)
# #
# # print(len(ver1.estados))
# # print(len(ver2.estados))
# # print(len(ver1.EeE))
# # print(len(ver2.EeE))
# # print(len(ver12.estados))
# # print(len(ver12.EeE))
#
# # #exemplos 3.1 e 3.2
# # estados2 = ["0","1","2","3","4"]
# # eventos2 = ["F","e","h","S1"]
# # estadoInicial2 = ["0"]
# # EeE2 = [["0","h","1"], ["0","e","3"], ["1","S1","2"], ["1","F","4"], ["2","e","0"], ["2","S1","3"],  ["3","e","0"], ["4","h","4"], ["4","e","4"]]
# # aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})
# #
# # gf = automatoGf(aut2, "F")
# # print(gf.EeE)
# #
# # gn = automatoGn(aut2, "F")
# #
# # gr = Renomear(gn, ["S1"], "R1")
# #
# # gv = ComposicaoParalela(gr, gf)
# #
# # print("gn.EeE")
# # for e in gn.EeE:
# #     print(e)
# #
# # print("gf.EeE")
# # for e in gf.EeE:
# #     print(e)
# #
# # print("gr.EeE")
# # for e in gr.EeE:
# #     print(e)
# #
# # print("gv.EeE")
# # for e in gv.EeE:
# #     print(e)
# # for s in gv.estados:
# #     print(s)
#
# # exemplo 3.3
# # estados1 = ["0","1","2","3"]
# # eventos1 = ["F","a","b", "c","S1"]
# # estadoInicial1 = ["0"]
# # EeE1 = [["0","a","1"], ["0","F","3"], ["1","c","2"], ["2","b","1"], ["3","b","0"], ["3","S1","0"]]
# # aut1 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})
# #
# # estados2 = ["0","1","2"]
# # eventos2 = ["b", "d","S1"]
# # estadoInicial2 = ["0"]
# # EeE2 = [["0","d","1"], ["0","S1","2"], ["1","b","1"], ["2","b","0"]]
# # aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})
# #
# # g=ComposicaoParalela(aut1, aut2)
# # #gn = automatoGn(g, "F")
# # gn1a = automatoGn(aut1, "F")
# # gn2a = automatoGn(aut2, "F")
# # gn = ComposicaoParalela(gn1a, gn2a)
# #
# # gn1 = MontaGniCabral(gn1a, 1, [gn1a, gn2a], gn, ["F"])
# # gn2 = MontaGniCabral(gn2a, 2, [gn1a, gn2a], gn, ["F"])
# #
# # for e in g.EeE:
# #     print(e)
# #
# # for e in gn.EeE:
# #     print(e)
# #
# # for e in gn1.EeE:
# #     print(e)
# #
# #
# # for e in gn2.EeE:
# #     print(e)
#
# #
# # # exemplo 3.4
# # estados1 = ["0","1","2","3","4"]
# # eventos1 = ["F","a","b", "d","Su"]
# # estadoInicial1 = ["0"]
# # EeE1 = [["0","a","2"], ["0","b","1"], ["1","a","2"], ["2","Su","3"], ["3","d","0"], ["2","F","4"], ["4","b","4"], ["4","d","4"]]
# # aut1 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})
# #
# # estados2 = ["0","1","2","3"]
# # eventos2 = ["b", "c", "d","e", "Su"]
# # estadoInicial2 = ["0"]
# # EeE2 = [["0","b","1"], ["0","e","0"], ["1","c","2"], ["2","b","2"], ["2","Su","3"], ["3","d","0"]]
# # aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})
# # g=ComposicaoParalela(aut1, aut2)
# # #gn = automatoGn(g, "F")
# # gn1a = automatoGn(aut1, "F")
# # gn2a = automatoGn(aut2, "F")
# # gn = ComposicaoParalela(gn1a, gn2a)
# # gn1 = MontaGniCabral(gn1a, 1, [gn1a, gn2a], gn, ["F"])
# # gn2 = MontaGniCabral(gn2a, 2, [gn1a, gn2a], gn, ["F"])
# #
# # gf = automatoGf(g, "F")
# #
# # gr1 = Renomear(gn1, ["Su"], "R1")
# # gr2 = Renomear(gn2, ["Su"], "R2")
# #
# # gr = ComposicaoParalela(gr1, gr2)
# # gv = ComposicaoParalela(gf, gr)
# # for e in g.EeE:
# #     print(e)
# # for e in gn.EeE:
# #     print(e)
# # for e in gn1.EeE:
# #     print(e)
# # for e in gn2.EeE:
# #     print(e)
# # for e in gr1.EeE:
# #     print(e)
# # for e in gr2.EeE:
# #     print(e)
# # for e in gf.EeE:
# #     print(e)
# # for e in gr.EeE:
# #     print(e)
# #
# # for e in gv.EeE:
# #     print(e)
