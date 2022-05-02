# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:11:09 2019

@author: Lucas
"""

class Automato: 
  def __init__(self, estados, eventos, estadoInicial = [], estadosMarcados = [] , EeE = [], adjacentes = {}, ): 
    self.estados = estados 
    self.adjacentes = adjacentes 
    self.eventos = eventos 
    self.EeE = EeE 
    self.estadosMarcados = estadosMarcados 
    self.estadoInicial = estadoInicial 
  def RelacionaEstadoEvento(self, estados, eventos, EeE = [], adjacentes = {}): 
    self.estados = estados 
    self.adjacentes = adjacentes 
    self.eventos = eventos 
    self.EeE = EeE 
    #contador = 0 
    for estado in estados: 
      atual = "" 
      atual = estado 
      mensagem = "" 
      mensagem = "Para o estado %s digite os eventos e para qual estado o automato ira dentre os eventos:" % estado 
      for evento in eventos: 
        mensagem += evento 
      print(mensagem) 
      for evento in eventos: 
        ev = evento 
        est = "" 
        invalido = True 
        while invalido: 
          est = input("Ocorrendo evento %s o automato ira para o estado:" % ev) 
          if est in estados: #adjacentes[contador]: 
            invalido = False 
            self.EeE.append([atual,ev,est]) 
          elif est == "": 
            print("evento %s inativo no estado %s" % (ev, estado))
            invalido = False        
          else: 
            print("O estado indicado não existe no automato em questão. Os possiveis sao:") 
          #print(estados)#adjacentes[contador]) 
        
      #contador += 1 
    return(self.EeE)
  def MontaListaAdjacencias(self, estados, eventos, EeE = [], adjacentes = {}): 
    self.estados = estados 
    self.adjacentes = adjacentes 
    self.eventos = eventos 
    self.EeE = EeE 
    contador = 0
    #adjacentes = {}
    aux = []
    print(len(self.EeE))
    #for ee in self.EeE:
    while contador < len(EeE):
        print(EeE)
        if EeE[contador][0] in self.adjacentes:
            aux = self.adjacentes.get(EeE[contador][0])
            print(self.adjacentes.get(EeE[contador][0]))
            aux.append(EeE[contador][2])
            self.adjacentes.update({EeE[contador][0]:aux})
            print("atualizei chave %s com o atributo %s" % (EeE[contador][0], EeE[contador][2]))
        else:
            lista = []
            lista.append(EeE[contador][2])
            self.adjacentes.update({EeE[contador][0]:lista})
            print("inseri chave %s e atributo %s" % (EeE[contador][0], EeE[contador][2]))
        contador += 1
    return(self.adjacentes)
    #return(self.EeE)

  def DefineEstadosMarcados(self, estados, estadosMarcados = []): 
    self.estados = estados 
    self.estadosMarcados = estadosMarcados 
    aindaAdicionando = True  
    while aindaAdicionando:
      est = input("defina um estado que será marcado, se não for adicionar mais pressione ENTER") 
      if est in self.estadosMarcados: #adjacentes[contador]: 
        print("estado já está na lista de estados marcados")
        print(self.estadosMarcados) 
      elif est == "": 
        print("estados marcados finalizados")
        print(estadosMarcados)
        aindaAdicionando = False        
      elif est not in estados:
        print("estado inválido, os estados disponíveis são:")
        print(estados)
      else:  
        estadosMarcados.append(est) 
        print("O estado foi adicionado") 
        print(estadosMarcados)#adjacentes[contador]) 
    return(estadosMarcados)
      #contador += 1 
    
  def DefineEstadoInicial(self, estados): 
    self.estados = estados 
    estadoInicial = [] 
    est = input("defina um estado inicial") 
    if est not in estados:
      print("estado inválido, os estados disponíveis são:")
      print(estados)
    else:  
      estadoInicial.append(est) 
      print("O estado foi adicionado") 
      print(estadoInicial)#adjacentes[contador]) 
    return(estadoInicial)
    

def DefineEstados():
  estados = []
  aindaAdicionando = True
  while aindaAdicionando:
    est = input("defina um estado, se não for adicionar mais pressione ENTER") 
    if est in estados: #adjacentes[contador]: 
      print("estado já está na lista de estados")
      print(estados) 
    elif est == "": 
      print("estados adicionados")
      print(estados)
      aindaAdicionando = False        
    else:
      estados.append(est) 
      print("O estado foi adicionado") 
      print(estados)#adjacentes[contador]) 
  return(estados) 

def DefineEventos():
  eventos = []
  aindaAdicionando = True
  while aindaAdicionando:
    ev = input("defina um evento, se não for adicionar mais pressione ENTER") 
    if ev in eventos: #adjacentes[contador]: 
      print("estado já está na lista de estados")
      print(eventos) 
    elif ev == "": 
      print("eventos adicionados")
      print(eventos)
      aindaAdicionando = False        
    else:
      eventos.append(ev) 
      print("O evento foi adicionado") 
      print(eventos)#adjacentes[contador]) 
  return(eventos) 


#estados = ["1","2","3","4","5","6"]
#adjacencias = [["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"],["1","2","3","4","5","6"]]
#eventos = ["a","b","c","d"]
#EeE = [["1","a","2"], ["1","b","3"], ["2","a","5"], ["3","d","2"]]

#aut = Automato(estados, eventos, EeE, {})
#adj = {}
#adj = aut.MontaListaAdjacencias(estados, eventos, EeE)

estados = DefineEstados()
eventos = DefineEventos()
aut = Automato(estados, eventos, [], {})
EeE = []
EeE = aut.RelacionaEstadoEvento(estados, eventos, [], {})
adj = {}
adj = aut.MontaListaAdjacencias(estados, eventos, EeE)
estIni = aut.DefineEstadoInicial(estados)
estMarc = aut.DefineEstadosMarcados(estados, [])