class Automato:
    def __init__(self, estados, eventos, estadoInicial=[], estadosMarcados=[], EeE=[], adjacentes={}):
        self.estados = estados
        self.adjacentes = adjacentes
        self.eventos = eventos
        self.EeE = EeE
        self.estadosMarcados = estadosMarcados
        self.estadoInicial = estadoInicial

    def RelacionaEstadoEvento(self, estados, eventos, EeE=[], adjacentes={}):
        self.estados = estados
        self.adjacentes = adjacentes
        self.eventos = eventos
        self.EeE = EeE
        # contador = 0
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
                    if est in estados:  # adjacentes[contador]:
                        invalido = False
                        self.EeE.append([atual, ev, est])
                    elif est == "":
                        print("evento %s inativo no estado %s" % (ev, estado))
                        invalido = False
                    else:
                        print("O estado indicado não existe no automato em questão. Os possiveis sao:")
                        # print(estados)#adjacentes[contador])

            # contador += 1
        return (self.EeE)

    def DefineEstadosMarcados(self, estados, estadosMarcados=[]):
        self.estados = estados
        self.estadosMarcados = estadosMarcados
        aindaAdicionando = True
        while aindaAdicionando:
            est = input("defina um estado que será marcado, se não for adicionar mais pressione ENTER")
            if est in self.estadosMarcados:  # adjacentes[contador]:
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
                print(estadosMarcados)  # adjacentes[contador])
        return (estadosMarcados)
        # contador += 1

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
            print(estadoInicial)  # adjacentes[contador])
        return (estadoInicial)

