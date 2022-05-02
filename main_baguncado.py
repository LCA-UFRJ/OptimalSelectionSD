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
MontaListaAdjacencias = funcoes.MontaListaAdjacencias
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

#Diagnostico = funcoes.Diagnostico

#adjacencias1 = [["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"]]
#estados1 = ["1","2","3","4","5","6"]
#eventos1 = ["a","b","c","d","e", "F"]
#EeE1 = [["1","a","2"], ["1","b","3"], ["2","c","5"], ["2","d","1"], ["3","d","2"]]
#estadoInicial1 = ["1"]
#aut1 = Automato(estados1, eventos1, estadoInicial1, [] , EeE1, {})

#estados2 = ["1","2","3","4","5","6"]
#eventos2 = ["a","b","d","e"]
#EeE2 = [["1","a","2"], ["1","e","4"], ["2","d","1"], ["3","b","6"]]
#estadoInicial2 = ["1"]
#aut2 = Automato(estados2, eventos2, estadoInicial2, [] , EeE2, {})





#EeEfull = [["1","a","2"], ["1","b","3"], ["1","c","5"], ["1","d","4"], ["2","a","1"], ["2","b","3"], ["2","c","5"], ["2","d","4"], ["3","a","1"], ["3","b","2"], ["3","c","5"], ["3","d","4"], ["4","a","2"], ["4","b","3"], ["4","c","5"], ["4","d","1"], ["5","a","2"], ["5","b","3"], ["5","c","1"], ["5","d","2"], ["6","a","2"], ["6","b","3"], ["6","c","5"], ["6","d","4"], ["3","F","6"]]
#adj1 = MontaListaAdjacencias(estados1, eventos1, EeE1)
#adjFull = MontaListaAdjacencias(estados1, eventos1, EeEfull)

EeE1 = []

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

#print(12)
aut12=ComposicaoParalela(aut1, aut2)
#print(123)
aut123=ComposicaoParalela(aut12, aut3)
#print(1234)
aut1234=ComposicaoParalela(aut123, aut4)
#print(aut1234.EeE)


#aut123 = Automato(["0|0|0", "0|0|1", "0|1|1", "0|4|2", "1|0|0", "1|0|1", "1|1|1", "1|4|2", "2|2|1", "3|2|1", "3|3|0", "3|3|1", "3|4|2", "4|2|1"], ["a", "e", "c", "S1", "g", "F", "h", "S2", "b", "d"], ["0|0|0"], [], [["0|0|0", "a", "1|0|0"], ["0|0|0", "b", "0|0|0"], ["0|0|1", "a", "1|0|1"], ["0|0|0", "h", "0|1|1"], ["0|0|1", "h", "0|1|1"], ["0|1|1", "a", "1|1|1"], ["0|1|1", "F", "0|4|2"], ["0|4|2", "a", "1|4|2"], ["0|4|2", "d", "0|4|2"], ["0|4|2", "h", "0|4|2"], ["0|0|0", "e", "3|3|0"], ["0|0|1", "e", "3|3|1"], ["0|4|2", "e", "3|4|2"], ["1|0|0", "b", "1|0|0"], ["1|0|0", "h", "1|1|1"], ["1|0|1", "h", "1|1|1"], ["1|1|1", "S1", "2|2|1"], ["1|1|1", "F", "1|4|2"], ["1|4|2", "h", "1|4|2"], ["1|4|2", "d", "1|4|2"], ["2|2|1", "c", "4|2|1"], ["2|2|1", "S1", "3|3|1"], ["3|2|1", "e", "0|0|1"], ["3|3|0", "S2", "3|3|0"], ["3|3|0", "b", "3|3|0"], ["3|3|1", "S2", "3|3|1"], ["3|4|2", "h", "3|4|2"], ["3|4|2", "d", "3|4|2"], ["3|4|2", "e", "0|4|2"], ["4|2|1", "g", "3|2|1"]],{})
#print(aut123.EeE)
#Gf_mk = Automato(aut1234.estados, aut1234.eventos, ["0|0|0|0"], ["0|4|2|2",  "1|4|2|2", "0|4|2|4", "3|4|2|3", "1|4|2|4",  "0|4|2|3", "1|4|2|3"],aut1234.EeE)
#Gf = ParteCoacessivel(Gf_mk)
#print(Gf.EeE)

F_estados = ['0|0|0|0|N', '0|0|1|0|N', '0|1|1|1|N', '0|4|2|2|Y', '0|4|2|3|Y', '0|4|2|4|Y', '1|0|0|0|N', '1|0|1|0|N', '1|1|1|1|N', '1|4|2|2|Y', '1|4|2|3|Y', '1|4|2|4|Y', '2|2|1|1|N', '3|2|1|1|N', '3|4|2|3|Y', '4|2|1|1|N']
F_eventos = ['a', 'e', 'c', 'S1', 'g', 'F', 'h', 'S2', 'b', 'd']
F_EeE = [['0|0|0|0|N', 'a', '1|0|0|0|N'], ['0|0|0|0|N', 'b', '0|0|0|0|N'], ['0|0|1|0|N', 'a', '1|0|1|0|N'], ['0|0|0|0|N', 'h', '0|1|1|1|N'], ['0|0|1|0|N', 'h', '0|1|1|1|N'], ['0|1|1|1|N', 'a', '1|1|1|1|N'], ['0|1|1|1|N', 'F', '0|4|2|2|Y'], ['0|4|2|2|Y', 'a', '1|4|2|2|Y'], ['0|4|2|3|Y', 'a', '1|4|2|3|Y'], ['0|4|2|4|Y', 'a', '1|4|2|4|Y'], ['0|4|2|2|Y', 'd', '0|4|2|2|Y'], ['0|4|2|3|Y', 'd', '0|4|2|3|Y'], ['0|4|2|4|Y', 'd', '0|4|2|4|Y'], ['0|4|2|2|Y', 'h', '0|4|2|4|Y'], ['0|4|2|4|Y', 'h', '0|4|2|4|Y'], ['0|4|2|2|Y', 'e', '3|4|2|3|Y'], ['0|4|2|3|Y', 'e', '3|4|2|3|Y'], ['1|0|0|0|N', 'b', '1|0|0|0|N'], ['1|0|0|0|N', 'h', '1|1|1|1|N'], ['1|0|1|0|N', 'h', '1|1|1|1|N'], ['1|1|1|1|N', 'S1', '2|2|1|1|N'], ['1|1|1|1|N', 'F', '1|4|2|2|Y'], ['1|4|2|2|Y', 'h', '1|4|2|4|Y'], ['1|4|2|4|Y', 'h', '1|4|2|4|Y'], ['1|4|2|2|Y', 'd', '1|4|2|2|Y'], ['1|4|2|3|Y', 'd', '1|4|2|3|Y'], ['1|4|2|4|Y', 'd', '1|4|2|4|Y'], ['2|2|1|1|N', 'c', '4|2|1|1|N'], ['3|2|1|1|N', 'e', '0|0|1|0|N'], ['3|4|2|3|Y', 'd', '3|4|2|3|Y'], ['3|4|2|3|Y', 'e', '0|4|2|3|Y'], ['4|2|1|1|N', 'g', '3|2|1|1|N']]
F_estadoInicial = ['0|0|0|0|N']

Gf = Automato(F_estados, F_eventos, F_estadoInicial, [], F_EeE)


Gn = ParteNormal(aut1234, ['F'])
#print(Gn.EeE)



#estados1n = ["0","1","2","31","32","4"]
#eventos1n = ["a","e","c","S1","g"]
#estadoInicial1n = ["0"]
#EeE1n = [["0","a","1"], ["0","e","31"], ["1","S1","2"], ["2","c","4"], ["2","S1","31"], ["32","e","0"], ["4","g","32"]]
#aut1n = Automato(estados1n, eventos1n, estadoInicial1n, [] , EeE1n, {})
#aut1r = Renomear(aut1n, ['S1','S2'], 'R1')
#print(aut1r.estados)
#print(aut1r.eventos)
#print(aut1r.EeE)


#estados2n = ["0","1","2","3"]
#eventos2n = ["e","h","S1","S2"]
#estadoInicial2n = ["0"]
#EeE2n = [["0","h","1"], ["0","e","3"], ["1","S1","2"], ["2","e","0"], ["2","S1","3"],  ["3","S2","3"]]
#aut2n = Automato(estados2n, eventos2n, estadoInicial2n, [] , EeE2n, {})
#aut2r = Renomear(aut2n, ['S1','S2'], 'R2')
#print(aut2r.estados)
#print(aut2r.eventos)
#print(aut2r.EeE)


#estados3n = ["0","1","2"]
#eventos3n = ["b","d","h"]
#estadoInicial3n = ["0"]
#EeE3n = [["0","b","0"], ["0","h","1"], ["1","h","1"]]
#aut3n = Automato(estados3n, eventos3n, estadoInicial3n, [] , EeE3n, {})
#aut3r = Renomear(aut3n, ['S1','S2'], 'R3')
#print(aut3r.estados)
#print(aut3r.eventos)
#print(aut3r.EeE)


#estados4n = ["0","01","1"]
#eventos4n = ["e","h"]
#estadoInicial4n = ["0"]
#EeE4n = [["0","h","1"], ["0","e","01"], ["1","e","0"]]
#aut4n = Automato(estados4n, eventos4n, estadoInicial4n, [] , EeE4n, {})
#aut4r = Renomear(aut4n, ['S1','S2'], 'R4')
#print(aut4r.estados)
#print(aut4r.eventos)
#print(aut4r.EeE)


#Gn1 = ComponenteNormal(aut1, Gn)
#Gn1r = Renomear(Gn1, ['S1','S2'], 'R1')
#Gn1 = ComposicaoParalela(aut1, Gn)
#Gn1 = ParteNormal(Gn1, "F")
#Gn1 = Automato(Gn1.estados, aut1.eventos, Gn1.estadoInicial, Gn1.estadosMarcados, Gn1.EeE)


#print(Gn1.EeE)
#print(Gn1.eventos)

#Gn2 = ComponenteNormal(aut2, Gn)
#Gn2r = Renomear(Gn2, ['S1','S2'], 'R2')
#Gn2 = ComposicaoParalela(aut2, Gn)
#Gn2 = ParteNormal(Gn2, "F")
#Gn2 = Automato(Gn2.estados, aut2.eventos, Gn2.estadoInicial, Gn2.estadosMarcados, Gn2.EeE)
#print(Gn21.EeE)
#print(Gn2.EeE)

#Gn3 = ComponenteNormal(aut3, Gn)
#Gn3r = Renomear(Gn3, ['S1','S2'], 'R3')
#Gn3 = ComposicaoParalela(aut3, Gn)
#Gn3 = ParteNormal(Gn3, "F")
#Gn3 = Automato(Gn3.estados, aut3.eventos, Gn3.estadoInicial, Gn3.estadosMarcados, Gn3.EeE)
#print(Gn3.EeE)

#Gn4 = ComponenteNormal(aut4, Gn)
#Gn4r = Renomear(Gn4, ['S1','S2'], 'R4')
#Gn4 = ComposicaoParalela(aut4, Gn)
#Gn4 = ParteNormal(Gn4, "F")
#Gn4 = Automato(Gn4.estados, aut4.eventos, Gn4.estadoInicial, Gn4.estadosMarcados, Gn4.EeE)
#print(Gn4.EeE)

#Gni
print("Gnir")
Gn1linha = ParteNormalRestrita(aut1, Gn, "F")
aut1n = EliminaEstadosSimilares(Gn1linha)
Gn2linha = ParteNormalRestrita(aut2, Gn, "F")
aut2n = EliminaEstadosSimilares(Gn2linha)
Gn3linha = ParteNormalRestrita(aut3, Gn, "F")
aut3n = EliminaEstadosSimilares(Gn3linha)
Gn4linha = ParteNormalRestrita(aut4, Gn, "F")
aut4n = EliminaEstadosSimilares(Gn4linha)

print("renomeados")
aut1r = Renomear(Gn1linha, ['S1','S2'], 'R1')
aut2r = Renomear(Gn2linha, ['S1','S2'], 'R2')
aut3r = Renomear(Gn3linha, ['S1','S2'], 'R3')
aut4r = Renomear(Gn4linha, ['S1','S2'], 'R4')


#unitarios
print("verificadores unitarios")
ver1 = ComposicaoParalela(aut1r, Gf)
ver2 = ComposicaoParalela(aut2r, Gf)
ver3 = ComposicaoParalela(aut3r, Gf)
ver4 = ComposicaoParalela(aut4r, Gf)

#print(ver1.EeE)
#resp = Diagnostico(ver1)
#resp = VerificadorDiagnosticabilidade(ver1, ['S1R1','S2R1'])
#resp = VerificadorDiagnosticabilidade(ver2, ['S1R2','S2R2'])
#resp = VerificadorDiagnosticabilidade(ver3, ['S1R3','S2R3'])
#resp = VerificadorDiagnosticabilidade(ver4, ['S1R4','S2R4'])
#print(ver2.EeE)
#print(ver3.EeE)
#print(ver4.EeE)


#duplas
print("verificadores em dupla")
ver12 = ComposicaoParalela(aut1r, ver2)
ver13 = ComposicaoParalela(aut1r, ver3)
ver14 = ComposicaoParalela(aut1r, ver4)
ver23 = ComposicaoParalela(aut2r, ver3)
ver24 = ComposicaoParalela(aut2r, ver4)
ver34 = ComposicaoParalela(aut3r, ver4)

#triplas
print("verificadores em tripla")
ver123 = ComposicaoParalela(aut1r, ver23)
ver124 = ComposicaoParalela(aut1r, ver24)
ver134 = ComposicaoParalela(aut1r, ver34)
ver234 = ComposicaoParalela(aut2r, ver34)


#quadruplas
print("verificadores em quadrupla")
ver1234 = ComposicaoParalela(aut1r, ver234)

print("diagnose")
resp = VerificadorDiagnosticabilidade(ver3, ['S1R1','S2R1','S1R2','S2R2','S1R3','S2R3','S1R4','S2R4'])

print(resp)



#conf12 = ComposicaoParalela(aut1n, aut2n)
#conf123 = ComposicaoParalela(conf12, aut3n)
#conf1234 = ComposicaoParalela(conf123, aut4n)


estadosPosFalha = PartePosFalha(aut1234, ["F"])

#print(estadosPosFalha)
#print(aut1234.eventos)
#Gf_mk = Automato(aut1234.estados, aut1234.eventos, ["0|0|0|0"], ["0|4|2|2",  "1|4|2|2", "0|4|2|4", "3|4|2|3", "1|4|2|4", "0|4|2|3", "1|4|2|3"],aut1234.EeE)
Gf_mk = Automato(aut1234.estados, aut1234.eventos, aut1234.estadoInicial, estadosPosFalha,aut1234.EeE)
Gf_ = ParteCoacessivel(Gf_mk)
for g_ in Gf_.EeE:
  print(g_)

#for g in Gf.EeE: 
#  print(g)
  

#autN = ParteNormal(aut1, "F")
#T1 = ComposicaoParalela(autN, Gn)


#EeET1 = ComponenteNormal(aut4, Gn, "F")
#print("teste1")
#print(EeET1.EeE)
#for ee in T1.EeE:
  #print(ee)

#print("iniciar Teste")
#Gnlinha = ParteNormalRestrita(aut4, Gn, "F")
#EliminaEstadosSimilares(Gnlinha)

#for ee in Gnlinha.EeE:
  #print(ee)

#for est in Gnlinha.estados:
  #print(est)
#print("teste finalizado!")
#print("Gn1")
#for ee in aut1n.EeE:
#  print(ee)


#print(conf1234.EeE)
#for ee in conf1234.EeE:
  #print(ee)
#print(Gn.EeE)
#for ee in Gn.EeE:
  #print(ee)










#for ee in ver1234.EeE:
#  print(ee)
#for ee in ver1234.EeE:
#  print(ee[0])
#for ee in ver1234.EeE:
#  print(ee[1])
#for ee in ver1234.EeE:
#  print(ee[2])

#montar verificador
#MontaListaAdjacencias(estados, eventos, EeE = [], adjacentes = {})
#ComponenteFortementeConexo(listaAdjacencias = {}, estado1 = "", estado2 = "", estados = [])
#print(ver3.EeE)
####Exemplo

#estadosEx = ["0","1","2","3","4","5","6"]
#eventosEx = ["a","b","c","su","sf"]
#EeEEx = [["0","a","1"], ["1","b","2"], ["1","c","2"], ["2","a","2"], ["2","c","2"], ["1","sf","3"], ["3","b","4"], ["4","c","5"], ["5","a","6"], ["6","su","6"]]
#estadoInicialEx = ["0"]
#autEx = Automato(estadosEx, eventosEx, estadoInicialEx, ["3","4","5","6"] , EeEEx, {})

#autAcessivel = ComposicaoProduto(aut1, aut2)
#autFull = Automato(estados1, eventos1, estadoInicial1, ["1","2","3","6"] , EeEfull, {})
#autObs = Observador(autFull, ["a","b","c"], ["d"])
#0AlcanceNaoObservavel("1", ["a","b","c"], EeE1, ["d"])
#[['1|1', 'a', '2|2'], ['1|3', 'b', '3|6'], ['2|2', 'd', '1|1'], ['3|2', 'd', '2|1']]
#BuscaPorLargura(adjFull, "1", estados1)

#retornoAutGV = Verificador(autEx, [["a","b"], ["a","c"]], ["sf"])
#autGV = retornoAutGV[0]
#eventosRenomeados = retornoAutGV[1]

#adj1 = MontaListaAdjacencias(autGV.estados, autGV.eventos, autGV.EeE, {})

#print(ComponenteFortementeConexo(adj1, '2|N|2|N|6|Y', '2|N|2|N|5|Y', autGV.estados))

#resposta = VerificadorDiagnosticabilidade(autGV, eventosRenomeados)
#print(resposta)

#ParteAcessivel(aut1)
#autCoacessivel = ParteCoacessivel(autEx)
#print(autCoacessivel.estados)
#ret = ComponenteFortementeConexo(adj1, "1", "6", estados1)
#retorno = BuscaPorProfundidade(adjFull, "1", estados1)
#BuscaPorProfundidadeCompleta(adj1, "1", estados1)
#OrdenacaoTopologica(adj1, "1", estados1)
#BuscaPorProfundidade(adj1, "1", estados1)
#aut = Automato(estados, eventos, EeE, {})
#adj = {}
#adj = aut.MontaListaAdjacencias(estados, eventos, EeE)

#estados = DefineEstados()
#eventos = DefineEventos()
#aut = Automato(estados1, eventos1, [], {})
#EeE = []
#EeE = aut.RelacionaEstadoEvento(estados, eventos, [], {})
#adj = {}
#adj = aut.MontaListaAdjacencias(estados, eventos, EeE)
#estIni = aut.DefineEstadoInicial(estados)
#estMarc = aut.DefineEstadosMarcados(estados, [])