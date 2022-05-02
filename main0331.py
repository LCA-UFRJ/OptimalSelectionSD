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
import rodarAutomatico

from datetime import datetime
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

Otimizada = rodarAutomatico.Otimizada
GfLinha = rodarAutomatico.GfLinha
Inteligente = rodarAutomatico.Inteligente
Exaustiva = rodarAutomatico.Exaustiva
GfLinhaCompleta = rodarAutomatico.GfLinhaCompleta
Todos = rodarAutomatico.Todos
BuscaPorLarguraGfLinha = funcoes.BuscaPorLarguraGfLinha


estados1 = ["0","1","2","3","4"]
eventos1 = ["a","e","c","S1","g"]
estadoInicial1 = ["0"]
EeE1 = [["0","a","1"], ["0","e","3"], ["1","S1","2"], ["2","c","4"], ["2","S1","3"], ["3","e","0"], ["4","g","3"]]
aut1 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})


estados2 = ["0","1","2","3","4"]
eventos2 = ["F","e","h","S1","S2"]
estadoInicial2 = ["0"]
EeE2 = [["0","h","1"], ["0","e","3"], ["1","S1","2"], ["1","F","4"], ["2","e","0"], ["2","S1","3"],  ["3","S2","3"], ["4","h","4"], ["4","e","4"]]
aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})

estados3 = ["0","1","2"]
eventos3 = ["F","b","d","h"]
estadoInicial3 = ["0"]
EeE3 = [["0","b","0"], ["0","h","1"], ["1","h","1"], ["1","F","2"], ["2","h","2"], ["2","d","2"]]
aut3 = Automato(estados3, eventos3, estadoInicial3, [] , EeE3, {})

estados4 = ["0","1","2","3","4"]
eventos4 = ["F","e","h"]
estadoInicial4 = ["0"]
EeE4 = [["0","h","1"], ["0","e","0"], ["1","h","1"], ["1","F","2"], ["1","e","0"], ["2","e","3"],  ["3","e","3"], ["2","h","4"], ["4","h","4"]]
aut4 = Automato(estados4, eventos4, estadoInicial4, [] , EeE4, {})

estados5 = ["0","1","2"]
eventos5 = ["e","h"]
estadoInicial5 = ["0"]
EeE5 = [["0","h","1"], ["0","e","0"], ["1","h","1"], ["1","e","0"]]
aut5 = Automato(estados4, eventos4, estadoInicial4, [] , EeE4, {})

estados6 = ["0","1","2","3","4"]
eventos6 = ["a","e","c","S1","g"]
estadoInicial6 = ["0"]
EeE6 = [["0","a","1"], ["1","S1","2"], ["2","c","4"], ["2","S1","3"], ["3","e","0"], ["4","g","3"]]
aut6 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})

eventos = ["a","e","c","g","h","b","d","F","S1","S2"]
eventosO = ["a","e","c","g","h","b","d"]
eventosF = ["F"]

eventosNO = []#["F","S1","S2"]
for ev in eventos:
  if ev not in eventosO and ev not in eventosNO:
    eventosNO.append(ev)
#print(eventosNO)
eventosR = []
for ev in eventosNO:
  if ev not in eventosF and ev not in eventosR:
    eventosR.append(ev)
#print(eventosR)

aut = [aut1, aut2, aut3, aut4, aut5, aut6, aut3]#, aut4]#, aut5]#, aut6]#, aut1, aut2, aut3, aut4]
juntei = []
autCompleto = aut1
for a in aut:
    if juntei == []:
        autCompleto = a
        juntei.append(a)
    else:
        if a not in juntei:
            juntei.append(a)
            autCompleto = ComposicaoParalela(autCompleto, a)



# TempoInicio = int(round(time.time() * 1000))#datetime.now()
# print("")
# print("Otimizada")
# print("")
# otimizada = Otimizada(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)
#
TempoFimOtimizada = int(round(time.time() * 1000))#datetime.now()
# estadosOtimizada = otimizada[0]
# transicoesOtimizada = otimizada[1]
#
# tempoOtimizada = (TempoFimOtimizada - TempoInicio)
#
# milliseconds = int(round(time.time() * 1000))
# print(milliseconds)
# #print(int(tempoOtimizada))
#
# print(tempoOtimizada, "milissegundos")
# print(estadosOtimizada, "estados")
# print(transicoesOtimizada, "transições")
#
# for k, v in otimizada[3].items():
#   print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
# print("Total: automatos -> ", len(otimizada[3]), ", estados -> ", estadosOtimizada, ", transições -> ", transicoesOtimizada)
#
#
#
print("")
print("Gf'")
print("")
gf_linha = GfLinha(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)

TempoFimGflinha = int(round(time.time() * 1000))#datetime.now()
estadosGflinha = gf_linha[0]
transicoesGflinha = gf_linha[1]

tempoGflinha = (TempoFimGflinha - TempoFimOtimizada)


print(tempoGflinha, "milissegundos")
print(estadosGflinha, "estados")
print(transicoesGflinha, "transições")


for k, v in gf_linha[4].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
for k, v in gf_linha[5].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
print("Total: automatos -> ", len(gf_linha[4])+len(gf_linha[5]), ", estados -> ", estadosGflinha, ", transições -> ", transicoesGflinha)
print("")
print("Inteligente")
print("")
inteligente = Inteligente(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)



TempoFimInteligente = int(round(time.time() * 1000))#datetime.now()
estadosInteligente = inteligente[0]
transicoesInteligente = inteligente[1]

tempoInteligente = (TempoFimInteligente - TempoFimGflinha)

print(tempoInteligente, "milissegundos")
print(estadosInteligente, "estados")
print(transicoesInteligente, "transições", "transições")

for k, v in inteligente[4].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
print("Total: automatos -> ", len(inteligente[4]), ", estados -> ", estadosInteligente, ", transições -> ", transicoesInteligente)
print("")
print("Gf' Completa")
print("")
gf_linhaCopmleta = GfLinhaCompleta(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)

TempoFimGfLinhaCompleta = int(round(time.time() * 1000))#datetime.now()
estadosGfLinhaCompleta = gf_linhaCopmleta[0]
transicoesGfLinhaCompleta = gf_linhaCopmleta[1]

TempoGfLinhaCompleta = (TempoFimGfLinhaCompleta - TempoFimInteligente)


print(TempoGfLinhaCompleta, "milissegundos")
print(estadosGfLinhaCompleta, "estados")
print(transicoesGfLinhaCompleta, "transições")

for k, v in gf_linhaCopmleta[4].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
for k, v in gf_linhaCopmleta[5].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
print("Total: automatos -> ", len(gf_linhaCopmleta[4])+len(gf_linhaCopmleta[5]), ", estados -> ", estadosGfLinhaCompleta, ", transições -> ", transicoesGfLinhaCompleta)
print("")
print("Exaustiva")
print("")
exaustiva = Exaustiva(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)

TempoFimExaustiva = int(round(time.time() * 1000))#datetime.now()
estadosExaustiva = exaustiva[0]
transicoesExaustiva = exaustiva[1]

tempoExaustiva = (TempoFimExaustiva - TempoFimGfLinhaCompleta)


print(tempoExaustiva, "milissegundos")
print(estadosExaustiva, "estados")
print(transicoesExaustiva, "transições")

for k, v in exaustiva[4].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))
print("Total: automatos -> ", len(exaustiva[4]), ", estados -> ", estadosExaustiva, ", transições -> ", transicoesExaustiva)

print("")
print("Todos")
print("")
todos = Todos(aut, autCompleto, eventos, eventosO, eventosNO, eventosR, eventosF)

TempoFimTodos = int(round(time.time() * 1000))#datetime.now()
estadosTodos = todos[0]
transicoesTodos = todos[1]

tempoTodos = (TempoFimTodos - TempoFimExaustiva)


print(tempoTodos, "milissegundos")
print(estadosTodos, "estados")
print(transicoesTodos, "transições")

for k, v in todos[4].items():
  print(k, ": estados -> ", len(v.estados), ", transições -> ", len(v.EeE))

print("Total: automatos -> ", len(todos[4]), ", estados -> ", estadosTodos, ", transições -> ", transicoesTodos)

# print("A busca otimizada foi feita em ", tempoOtimizada, "milissegundos, com ", estadosOtimizada, "estados e ", transicoesOtimizada, "transições.")
# print("As bases encontradas foram:")
# print(otimizada[2][1])

print("A busca Gf' foi feita em ", tempoGflinha, "milissegundos, com ", estadosGflinha, "estados e ", transicoesGflinha, "transições.")
print("As bases encontradas foram:")
print(gf_linha[2])

print("A busca inteligente foi feita em ", tempoInteligente, "milissegundos, com ", estadosInteligente, "estados e ", transicoesInteligente, "transições.")
print("As bases encontradas foram:")
print(inteligente[2])

print("A busca Gf' copmleta foi feita em ", TempoGfLinhaCompleta, "milissegundos, com ", estadosGfLinhaCompleta, "estados e ", transicoesGfLinhaCompleta, "transições.")
print("As bases encontradas foram:")
print(gf_linhaCopmleta[2])

print("A busca exaustiva foi feita em ", tempoExaustiva, "milissegundos, com ", estadosExaustiva, "estados e ", transicoesExaustiva, "transições.")
print("As bases encontradas foram:")
print(exaustiva[2])

print("A busca exaustiva foi feita em ", tempoTodos, "milissegundos, com ", estadosTodos, "estados e ", transicoesTodos, "transições.")
print("As bases encontradas foram:")
print(todos[2])


# print(tempoOtimizada)
# print(estadosOtimizada)
# print(transicoesOtimizada)
# #print("Com relação aos conjuntos com menor cardinalidade houve uma economia no tempo de execução de:", (tempoInteligente-tempoOtimizada/tempoInteligente), "%, na quantidade de estados de :", (estadosInteligente-estadosOtimizada/estadosInteligente), "% e na quantidade de transições de:", transicoesInteligente-transicoesOtimizada/transicoesInteligente,"%")

#print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-tempoOtimizada/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosOtimizada/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesOtimizada/transicoesTodos,"%")

print(tempoGflinha)
print(estadosGflinha)
print(transicoesGflinha)
#print("Com relação aos conjuntos com menor cardinalidade houve uma economia no tempo de execução de:", (tempoInteligente-tempoGflinha/tempoInteligente), "%, na quantidade de estados de :", (estadosInteligente-estadosGflinha/estadosInteligente), "% e na quantidade de transições de:", transicoesInteligente-transicoesGflinha/transicoesInteligente,"%")

print(tempoInteligente)
print(estadosInteligente)
print(transicoesInteligente)

print(TempoGfLinhaCompleta)
print(estadosGfLinhaCompleta)
print(transicoesGfLinhaCompleta)
#print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-TempoGfLinhaCompleta/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosGfLinhaCompleta/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesGfLinhaCompleta/transicoesTodos,"%")

print(tempoExaustiva)
print(estadosExaustiva)
print(transicoesExaustiva)
#print("Com relação a todos os conjuntos que permitem a diagnose houve uma economia no tempo de execução de:", (tempoTodos-tempoExaustiva/tempoTodos), "%, na quantidade de estados de :", (estadosTodos-estadosExaustiva/estadosTodos), "% e na quantidade de transições de:", transicoesTodos-transicoesExaustiva/transicoesTodos,"%")


print(tempoTodos)
print(estadosTodos)
print(transicoesTodos)

# print(TempoInicio)
print(TempoFimOtimizada)
print(TempoFimGflinha)
print(TempoFimInteligente)
print(TempoFimGfLinhaCompleta)
print(TempoFimTodos)