import classes

Automato = classes.Automato


def Observador(aut, eventosO, eventosUO):
    autAcessivel = ParteAcessivel(aut)

    EeE = autAcessivel.EeE

    estadoInicialObs = AlcanceNaoObservavel(autAcessivel.estadoInicial[0], eventosO, autAcessivel.EeE, eventosUO)
    EeEObs = []
    for ee in EeE:
        estPartida = AlcanceNaoObservavel(ee[0], eventosO, EeE, eventosUO)
        estPtd = ee[0]
        estAlc = ee[2]
        for ev in EeE:
            if ev[0] in estPartida:
                if ev[0] not in estPtd:
                    estPtd = estPtd + "_" + ev[0]
        listaEstPtd = estPtd.split("_")
        for eptd in listaEstPtd:
            for e in EeE:
                if e[0] == eptd and e[1] == ee[1]:
                    addEstUO = AlcanceNaoObservavel(e[2], eventosO, EeE, eventosUO)
                    listaAddEstUO = addEstUO.split("_")
                    for estUO in listaAddEstUO:
                        if estUO not in estAlc:
                            estAlc = estAlc + "_" + estUO
        if ee[1] not in eventosUO:
            EeEObs.append([estPtd, ee[1], estAlc])
    estadosMarcadosObservador = []
    adjacentesObs = {}
    autObservador = Automato(aut.estados, aut.eventos, estadoInicialObs, estadosMarcadosObservador, EeEObs,
                             adjacentesObs)
    # print(EeEObs)
    return (autObservador)


def AlcanceNaoObservavel(estado="", eventosO=[], EeE=[], eventosUO=[]):
    estadosAnalisados = []
    filaEstados = []
    estadoAtual = [estado]
    processar = []
    estadoObservador = estado
    filaEstados.append(estado)
    while len(filaEstados):
        retorno = ProcessarAlcanceNaoObservavel(filaEstados[0], eventosO, EeE, eventosUO, filaEstados,
                                                estadosAnalisados, estadoObservador)
        filaEstados = retorno[0]
        estadosAnalisados = retorno[1]
        filaEstados.remove(filaEstados[0])
        estadoObservador = retorno[2]
    return (estadoObservador)


def ProcessarAlcanceNaoObservavel(estado="", eventosO=[], EeE=[], eventosUO=[], filaEstados=[], estadosAnalisados=[],
                                  estadoObservador=""):
    estadoAtual = [estado]
    processar = []
    for ee in EeE:
        if ee[0] == estado:
            processar.append(ee)
    for ee in processar:
        if ee[1] in eventosUO:
            if ee[2] not in estadoObservador:
                estadoObservador = estadoObservador + "_" + ee[2]
                if ee[2] not in filaEstados and ee[2] not in estadosAnalisados:
                    filaEstados.append(ee[2])
    if estadoAtual not in estadosAnalisados:
        estadosAnalisados.append(estadoAtual[0])
    return ([filaEstados, estadosAnalisados, estadoObservador])


def ComposicaoParalela(aut1, aut2):
    estados1 = aut1.estados
    estados2 = aut2.estados
    # print(aut1.estadoInicial[0])
    # print(aut2.estadoInicial[0])

    paraleloInicial = [aut1.estadoInicial[0] + "|" + aut2.estadoInicial[0]]
    paraleloEstados = []
    paraleloEventos = []
    paraleloEeE = []
    paraleloMarcados = []
    estadoAtual = ""
    for est1 in estados1:
        for est2 in estados2:
            estadoAtual = est1 + "|" + est2
            paraleloEstados.append(estadoAtual)
            if est1 in aut1.estadosMarcados or est2 in aut2.estadosMarcados:
                if estadoAtual not in paraleloMarcados:
                    paraleloMarcados.append(estadoAtual)
    for ev in aut1.eventos:
        if ev not in paraleloEventos:
            paraleloEventos.append(ev)
    for ev in aut2.eventos:
        if ev not in paraleloEventos:
            paraleloEventos.append(ev)
    for ev1 in aut1.EeE:
        for ev2 in aut2.EeE:
            adicionar12 = []
            adicionar1 = []
            adicionar2 = []
            adicionarL1 = []
            adicionarL2 = []
            # if ev1[0]=='31' or ev2[0]=='1|4|2|2|Y':
            # print(ev1)
            # print(ev2)
            # print(ev1[0] + "-" + ev2[0] + "-" + ev1[1] + "-" + ev2[1])
            if ev1[1] in aut2.eventos and ev2[1] in aut1.eventos and ev1[1] == ev2[1]:
                adicionar12 = [ev1[0] + "|" + ev2[0], ev1[1], ev1[2] + "|" + ev2[2]]
            if ev1[1] not in aut2.eventos:
                adicionar1 = [ev1[0] + "|" + ev2[0], ev1[1], ev1[2] + "|" + ev2[0]]
                adicionarL1 = [ev1[0] + "|" + ev2[2], ev1[1], ev1[2] + "|" + ev2[2]]
            if ev2[1] not in aut1.eventos:
                adicionar2 = [ev1[0] + "|" + ev2[0], ev2[1], ev1[0] + "|" + ev2[2]]
                adicionarL2 = [ev1[2] + "|" + ev2[0], ev2[1], ev1[2] + "|" + ev2[2]]
                # oensar nos autolacos
            # if ev1[0] == ev1[2] and ev1[1] not in aut2.eventos:
            #  adicionarL1 = [ev1[0] + "|" + ev2[2], ev1[1], ev1[0] +"|" + ev2[2]]
            # if ev2[0] == ev2[2] and ev2[1] not in aut1.eventos:
            #  adicionarL2 = [ev1[2] + "|" + ev2[0], ev2[1], ev1[2] +"|" + ev2[2]]
            # adicionar e criar o analogo
            if adicionar12 not in paraleloEeE and adicionar12 != []:
                paraleloEeE.append(adicionar12)
            if adicionar1 not in paraleloEeE and adicionar1 != []:
                paraleloEeE.append(adicionar1)
            if adicionar2 not in paraleloEeE and adicionar2 != []:
                paraleloEeE.append(adicionar2)
            if adicionarL1 not in paraleloEeE and adicionarL1 != []:
                paraleloEeE.append(adicionarL1)
            if adicionarL2 not in paraleloEeE and adicionarL2 != []:
                paraleloEeE.append(adicionarL2)
            # print(adicionar)

    # for pEst in paraleloEstados:
    #     estados = pEst.split("|")
    #     if estados[0] in aut1.estadosMarcados or estados[1] in aut2.estadosMarcados:
    #         if pEst not in paraleloMarcados:
    #             paraleloMarcados.append(pEst)

    autParaleloFull = Automato(paraleloEstados, paraleloEventos, paraleloInicial, paraleloMarcados, paraleloEeE, {})
    # print(paraleloEventos)
    # print(paraleloEeE)
    autAcessivel = ParteAcessivel(autParaleloFull)
    return (autAcessivel)


def ComposicaoProduto(aut1, aut2):
    estados1 = aut1.estados
    estados2 = aut2.estados
    produtoInicial = [aut1.estadoInicial[0] + "|" + aut2.estadoInicial[0]]
    produtoEstados = []
    produtoEventos = []
    produtoEeE = []
    estadoAtual = ""
    for est1 in estados1:
        for est2 in estados2:
            estadoAtual = est1 + "|" + est2
            produtoEstados.append(estadoAtual)
    for ev1 in aut1.eventos:
        for ev2 in aut2.eventos:
            if ev1 not in produtoEventos and ev1 == ev2:
                produtoEventos.append(ev1)
    for ev1 in aut1.EeE:
        for ev2 in aut2.EeE:
            adicionar = []
            if ev1[1] == ev2[1]:
                adicionar = [ev1[0] + "|" + ev2[0], ev1[1], ev1[2] + "|" + ev2[2]]
            if adicionar not in produtoEeE and adicionar != []:
                produtoEeE.append(adicionar)
    autProdutoFull = Automato(produtoEstados, produtoEventos, produtoInicial, [], produtoEeE, {})

    autAcessivel = ParteAcessivel(autProdutoFull)
    return (autAcessivel)


def DefineEstados():
    estados = []
    aindaAdicionando = True
    while aindaAdicionando:
        est = input("defina um estado, se não for adicionar mais pressione ENTER")
        if est in estados:  # adjacentes[contador]:
            print("estado já está na lista de estados")
            print(estados)
        elif est == "":
            print("estados adicionados")
            print(estados)
            aindaAdicionando = False
        else:
            estados.append(est)
            print("O estado foi adicionado")
            print(estados)  # adjacentes[contador])
    return (estados)


def DefineEventos():
    eventos = []
    aindaAdicionando = True
    while aindaAdicionando:
        ev = input("defina um evento, se não for adicionar mais pressione ENTER")
        if ev in eventos:  # adjacentes[contador]:
            print("estado já está na lista de estados")
            print(eventos)
        elif ev == "":
            print("eventos adicionados")
            print(eventos)
            aindaAdicionando = False
        else:
            eventos.append(ev)
            print("O evento foi adicionado")
            print(eventos)  # adjacentes[contador])
    return (eventos)


def MontaDictAdjacencias(estados, eventos, EeE=[], adjacentes={}):
    contador = 0
    aux = []
    while contador < len(EeE):
        if EeE[contador][0] in adjacentes:
            aux = adjacentes.get(EeE[contador][0])
            aux.append(EeE[contador][2])
            adjacentes.update({EeE[contador][0]: aux})
        else:
            lista = []
            lista.append(EeE[contador][2])
            adjacentes.update({EeE[contador][0]: lista})
        contador += 1
    return (adjacentes)


def BuscaPorLargura(dictAdjacencias={}, estado="", estados=[]):
    estadosAlcancados = []
    filaEstados = []
    situacaoEstado = {}
    situacaoEstado.clear()
    # print("situacaoEstado")
    # print(situacaoEstado)
    d = 0
    ds = {}
    pi = {}
    for est in estados:
        situacaoEstado.update({est: 0})
        # print(situacaoEstado)
        ds.update({est: ["nulo"]})
        pi.update({est: ["nulo"]})
    pi.update({estado: []})
    ds.update({estado: d})
    situacaoEstado.update({estado: 1})
    filaEstados.append(estado)
    while len(filaEstados):
        # print(filaEstados)
        u = filaEstados[0]
        d = ds.get(u)
        if u in dictAdjacencias:
            for v in dictAdjacencias[u]:
                # if u == "0|0|0|0":
                # print(u)
                # print(v)
                # print(situacaoEstado)
                if situacaoEstado.get(v) == 0:
                    situacaoEstado.update({v: 1})
                    ds.update({v: ds.get(u) + 1})
                    pi.update({v: u})
                    filaEstados.append(v)
                # if u == "1|0|0|0":
                #  print(u)
                #  print(v)
                #  print(situacaoEstado)

        situacaoEstado.update({u: 2})
        filaEstados.remove(u)
    dictAdjacencias.clear()
    # situacaoEstado.clear()
    return (ds)


def ParteCoacessivel(automato):
    adj1 = {}
    adj1.clear()
    adj1 = MontaDictAdjacencias(automato.estados, automato.eventos, automato.EeE)
    estC = {}
    coacessiveis = []
    EeEcoacessiveis = []
    for estado in automato.estados:
        baux = False
        if estado not in estC.keys():
            baux = False
            estC[estado] = False
        else:
            baux = estC[estado]
        if baux == False:
            ret1 = BuscaPorProfundidade(adj1, estado, automato.estados, 0, {}, {}, {})
            for marcado in automato.estadosMarcados:
                alcancaMarcado = ret1[1].get(marcado)
                if alcancaMarcado == 2:
                    estC[estado] = True
                    coacessiveis.append(estado)
                # print(alcancaMarcado)
    for EeE in automato.EeE:
        if (EeE[0] in coacessiveis) and (EeE[2] in coacessiveis):
            EeEcoacessiveis.append(EeE)
    autCoacessivel = Automato(coacessiveis, automato.eventos, automato.estadoInicial, automato.estadosMarcados,
                              EeEcoacessiveis, {})

    return (autCoacessivel)


def ParteComportamentoFalha(automato):
    adj1 = {}
    adj1.clear()
    cfEstados = []
    cfEstadosMarcados = []
    EeEcfMarcados = []
    for est in automato.estados:
        if est in automato.estadosMarcados:
            cfEstados.append(est + "|Y")
            cfEstadosMarcados.append(est + "|Y")
        else:
            cfEstados.append(est + "|N")
        for ee in automato.EeE:
            if ee[0] in automato.estadosMarcados:
                partida = ee[0] + "|Y"
            else:
                partida = ee[0] + "|N"
            if ee[2] in automato.estadosMarcados:
                chegada = ee[2] + "|Y"
            else:
                chegada = ee[2] + "|N"
            EeEcfMarcados.append([partida, ee[1], chegada])

    adj1 = MontaDictAdjacencias(cfEstados, automato.eventos, EeEcfMarcados)
    estC = {}
    coacessiveis = []
    EeEcoacessiveis = []

    for estado in cfEstados:
        baux = False
        if estado not in estC.keys():
            baux = False
            estC[estado] = False
        else:
            baux = estC[estado]
        if baux == False:
            ret1 = BuscaPorProfundidade(adj1, estado, cfEstados, 0, {}, {}, {})
            for marcado in cfEstadosMarcados:
                alcancaMarcado = ret1[1].get(marcado)
                if alcancaMarcado == 2:
                    estC[estado] = True
                    if estado not in coacessiveis:
                        coacessiveis.append(estado)
                # print(alcancaMarcado)
    for EeE in EeEcfMarcados:
        if (EeE[0] in coacessiveis) and (EeE[2] in coacessiveis):
            if EeE not in EeEcoacessiveis:
                EeEcoacessiveis.append(EeE)
    autCoacessivel = Automato(coacessiveis, automato.eventos, [automato.estadoInicial[0] + "|N"], cfEstadosMarcados,
                              EeEcoacessiveis, {})

    return (autCoacessivel)


def ComponenteFortementeConexo(dictAdjacencias={}, estado1="", estado2="", estados=[]):
    isCFC = False
    caminho1 = []
    caminho2 = []
    # print(dictAdjacencias)
    # print(estado1)
    # print(estado2)
    # print(estados)
    if estado1 != estado2:
        ret1 = BuscaPorProfundidade(dictAdjacencias, estado1, estados, 0, {}, {}, {})
        ret2 = BuscaPorProfundidade(dictAdjacencias, estado2, estados, 0, {}, {}, {})
        alcancaEst2 = ret1[1].get(estado2)
        alcancaEst1 = ret2[1].get(estado1)
        # print(ret1[4])
        # print(ret2[4])

        if alcancaEst1 and alcancaEst2:
            isCFC = True
            proximo1 = estado1
            while proximo1 != []:
                # print(caminho1)
                # print(proximo1)
                caminho1.append(proximo1)
                proximo1 = ret2[4].get(proximo1)
                # print(caminho1)
                # print(proximo1)
                # print("------")
            proximo2 = estado2
            while proximo2 != []:
                # print(caminho2)
                # print(proximo2)
                caminho2.append(proximo2)
                proximo2 = ret1[4].get(proximo2)
                # print(caminho2)
                # print(proximo2)
                # print("------")
                # print(caminho2)
                # print(proximo2)

            # print(ret1[0])
            # print(ret1[1])
            # print(ret1[2])
            # print(ret1[3])
            # print(alcancaEst1)

            # print(alcancaEst2)
    # print(caminho1)
    # print(caminho2)
    return [isCFC, caminho1, caminho2]


def BuscaPorProfundidade(dictAdjacencias={}, estado="", estados=[], d=0, ds={}, pi={}, situacaoEstado={}):
    # print(estado)
    estadosAlcancados = []
    filaEstados = []
    if d == 0:
        for est in estados:
            situacaoEstado.update({est: 0})
            ds.update({est: ["nulo"]})
            pi.update({est: ["nulo"]})
    pi.update({estado: []})
    memoria = []
    if situacaoEstado.get(estado) == 0:
        retorno = VisitaBuscaPorProfundidade(situacaoEstado, d, ds, pi, dictAdjacencias, estado, estados, memoria)
        d = retorno[0]
        ds = retorno[1]
        pi = retorno[2]
        situacaoEstado = retorno[3]
        # print(situacaoEstado)
        memoria = retorno[4]
    return ([estadosAlcancados, situacaoEstado, d, ds, pi])


def VisitaBuscaPorProfundidade(situacaoEstado, d, ds, pi, dictAdjacencias, estado, estados, memoria):
    cMemo = 0
    if dictAdjacencias.get(estado):
        while cMemo < len(dictAdjacencias.get(estado)):
            memoria.append(estado)
            cMemo += 1
    else:
        memoria.append(estado)
    situacaoEstado.update({estado: 1})
    d += 1
    ds.update({estado: d})
    if estado in dictAdjacencias:
        for v in dictAdjacencias[estado]:
            if situacaoEstado.get(v) == 0:
                pi.update({v: estado})
                retorno = VisitaBuscaPorProfundidade(situacaoEstado, d, ds, pi, dictAdjacencias, v, estados, memoria)
                d = retorno[0]
                ds = retorno[1]
                pi = retorno[2]
                situacaoEstado = retorno[3]
                memoria = retorno[4]
                # print(retorno)
        if situacaoEstado.get(estado) == 1 and memoria.count(estado) == 1:
            situacaoEstado.update({estado: 2})
            d += 1
            ds.update({estado: [ds.get(estado), d]})
            del (memoria[-1])
        elif situacaoEstado.get(estado) == 1 and memoria.count(estado) > 1:
            if memoria.count(estado) == len(memoria):
                situacaoEstado.update({estado: 2})
                d += 1
                ds.update({estado: [ds.get(estado), d]})
                del (memoria[-1])

    else:
        situacaoEstado.update({estado: 2})
        d += 1
        ds.update({estado: [ds.get(estado), d]})
        del (memoria[-1])

    cont = 0
    while cont < len(memoria):
        contLimpa = len(memoria)
        finalizaEstado = memoria[contLimpa - 1]
        if situacaoEstado.get(estado) == 1:
            if memoria.count(finalizaEstado) == 1:
                situacaoEstado.update({estado: 2})
                d += 1
                ds.update({estado: [ds.get(estado), d]})
            else:
                del (memoria[-1])
        cont += 1
    return ([d, ds, pi, situacaoEstado, memoria])


def BuscaPorProfundidadeCompleta(dictAdjacencias={}, estado="", estados=[]):
    retorno = BuscaPorProfundidade(dictAdjacencias, estado, estados)
    for est in estados:
        if retorno[1].get(est) == 0:
            retorno = BuscaPorProfundidade(dictAdjacencias, est, estados, retorno[2], retorno[3], retorno[4],
                                           retorno[1])
    return (retorno)


def OrdenacaoTopologica(dictAdjacencias={}, estado="", estados=[]):
    retorno = BuscaPorProfundidadeCompleta(dictAdjacencias, estado, estados)
    estFinal = {}
    for v in retorno[3]:
        estFinal.update({v: retorno[3].get(v)[1]})
    # print(estFinal)
    ordenados = {}
    ord2 = []
    maximo = len(estFinal)
    while len(ord2) < maximo:
        aux = 0
        e = ""
        for est in estFinal:
            if estFinal.get(est) > aux:
                e = est
                aux = estFinal.get(est)
                # print(aux)
        ord2.append(e)
        ordenados.update({e: aux})
        estFinal.pop(e)
    # print(ord2)
    # print(ordenados)


def ParteAcessivel(Automato1):
    adj1 = {}
    estadosAlcancados = []
    adj1 = MontaDictAdjacencias(Automato1.estados, Automato1.eventos, Automato1.EeE)
    # print(adj1)
    estadosAlcancados = BuscaPorLargura(adj1, Automato1.estadoInicial[0], Automato1.estados)
    # print(estadosAlcancados)
    eventos = Automato1.eventos
    estInicial = Automato1.estadoInicial[0:1]
    EeEalcancados = []
    marcadosAlcancados = []
    acessivel = []
    for alc in estadosAlcancados:
        if estadosAlcancados.get(alc) != ["nulo"]:
            acessivel.append(alc)
    for EeE in Automato1.EeE:
        if EeE[0] in acessivel:
            EeEalcancados.append(EeE)
    for marc in Automato1.estadosMarcados:
        if marc in acessivel:
            if marc not in marcadosAlcancados:
                marcadosAlcancados.append(marc)
    autAcessivel = Automato(acessivel, eventos, estInicial, marcadosAlcancados, EeEalcancados, {})
    return (autAcessivel)


def ParteCoacessivelErrada(automato):
    adj1 = {}
    adj1.clear()
    adj1 = MontaDictAdjacencias(automato.estados, automato.eventos, automato.EeE)
    # print(automato.EeE)
    # print(adj1)
    jaPesquisei = []
    EeEalcancados = []
    estadosCoacessivel = []
    marcadosCoacessivel = []
    coacessivel = []
    for est in automato.EeE:
        # print(est[0])
        if est[0] not in jaPesquisei:
            busca = BuscaPorLargura(adj1, est[0], automato.estados)
            # print(est[0])
            # print(busca)

            for alc in busca:
                if busca.get(alc) != ["nulo"] and alc in automato.estadosMarcados and est[0] not in coacessivel:
                    # print(est)
                    # print(alc)
                    coacessivel.append(est[0])
                    # print(coacessivel)
    for EeE in automato.EeE:
        if EeE[2] in coacessivel:
            EeEalcancados.append(EeE)
    for marc in automato.estadosMarcados:
        if marc in coacessivel:
            if marc not in marcadosCoacessivel:
                marcadosCoacessivel.append(marc)
    # print(EeEalcancados)
    autCoacessivel = Automato(coacessivel, automato.eventos, automato.estadoInicial, marcadosCoacessivel, EeEalcancados,
                              {})
    return (autCoacessivel)


def Verificador(automato, eventosOi, eventosFalha):
    eventos = automato.eventos
    eventosRenomeados = []
    autGNis = []

    estadosLabel = ["N", "Y"]
    eventosLabel = ["sf"]
    EeELabel = [["N", "sf", "Y"], ["Y", "sf", "Y"]]
    estadoInicialLabel = ["N"]
    autLabel = Automato(estadosLabel, eventosLabel, estadoInicialLabel, [], EeELabel, {})

    estadosNormal = ["N"]
    eventosNormal = ["a", "b", "c", "sf", "su"]
    EeENormal = [["N", "a", "N"], ["N", "b", "N"], ["N", "c", "N"], ["N", "su", "N"]]
    estadoInicialNormal = ["N"]
    autNormal = Automato(estadosNormal, eventosNormal, estadoInicialNormal, [], EeENormal, {})

    autGL = ComposicaoParalela(automato, autLabel)
    autGN = ComposicaoParalela(automato, autNormal)
    listaEventosNovos = []
    for evF in eventosFalha:
        for evN in autGN.eventos:
            if evF == evN:
                autGN.eventos.remove(evF)
    eventos = autGN.eventos
    autGL.estadosMarcados = ["3|Y", "4|Y", "5|Y", "6|Y"]
    autGF = ParteCoacessivel(autGL)

    EeE = autGN.EeE
    autGV = autGF
    dEventos = {}
    aux = {0: {}}
    i = 1
    for evOi in eventosOi:
        EeENi = []
        for ev in eventos:
            if ev not in evOi:
                eventosOi[i - 1].append(ev + str(i))
                eventosRenomeados.append(ev + str(i))
                dEventos.update({ev + str(i): ev})
        for ee in EeE:
            if ee[1] not in eventosOi[i - 1]:
                EeENi.append([ee[0], ee[1] + str(i), ee[2]])
            else:
                EeENi.append(ee)
        autGNi = Automato(autGN.estados, eventosOi[i - 1], autGN.estadoInicial, [], EeENi, {})
        i += 1
        autGV = ComposicaoParalela(autGNi, autGV)
    autGV = ParteAcessivel(autGV)
    return ([autGV, eventosRenomeados])


def VerificadorDiagnosticabilidade(automato, eventosRenomeados):
    adj1 = MontaDictAdjacencias(automato.estados, automato.eventos, automato.EeE, {})
    # print(adj1)
    # resposta = ""
    resposta = []
    ciclo = []
    isAutolaco = False
    for elemento in adj1:

        if "Y" in elemento:
            # print(elemento)
            if elemento in adj1.get(elemento):
                # print(adj1.get(elemento))
                for ee in automato.EeE:
                    if ee[0] == elemento and ee[2] == elemento and ee[1] not in eventosRenomeados:
                        isAutolaco = True
                        resposta.append(
                            "Linguagem gerada não é diagnosticável, o estado " + elemento + " possui um autolaço por evento próprio no comportamento pós falha e evento proprios (" +
                            ee[1] + ") entre eles")
                        ciclo.append(ee[1])
    isCFC = False
    isEvento = False
    eventosProblema = ""
    for estado1 in automato.estados:
        for estado2 in automato.estados:
            if estado1 != estado2:
                isCFC = False
                if isCFC == False and "Y" in estado1 and "Y" in estado2:
                    ret = ComponenteFortementeConexo(adj1, estado1, estado2, automato.estados)
                    isCFC = ret[0]
                    # print(ret)
                    ####REVER ESTA PARTE

                    caminho1 = ret[1][::-1]
                    caminhoEventos1 = []
                    contador = 0
                    # print((estado1))
                    # print((caminho1))
                    while contador < len(caminho1) - 1:
                        for ee in automato.EeE:
                            # print(ee[0])
                            # print( caminho1[contador] )
                            # print(ee[2])
                            # print( caminho1[contador+1] )
                            if ee[0] == caminho1[contador] and ee[2] == caminho1[contador + 1]:
                                caminhoEventos1.append(ee[1])
                        contador += 1
                    for ev in caminhoEventos1:
                        if ev not in eventosRenomeados:
                            isEvento = True
                            if eventosProblema == "":
                                eventosProblema = ev
                            else:
                                eventosProblema += ", " + ev
                    caminho2 = ret[2][::-1]
                    # print((caminho2))
                    # print(estado1 + "====>" + estado2 + "====>" + str(isCFC))
                    # print(caminhoEventos1)
                    if isCFC and isEvento:
                        resposta.append(
                            "Linguagem gerada não é diagnosticável estados " + estado1 + " e " + estado2 + " são componentes fortemente conexos com falha e eventos proprios (" + eventosProblema + ") entre eles")
                        ciclo.append(eventosProblema)
    if isCFC == False and isAutolaco == False:
        resposta.append("Linguagem gerada é diagnosticável")

    return ([resposta, ciclo])


def ParteNormal(Automato1, EF):
    eventosNormais = []
    EeENormais = []
    # estadosNormais = []
    for SF in EF:
        for ev in Automato1.eventos:
            if ev != SF:
                eventosNormais.append(ev)
        # print(eventosNormais)
        for EeE in Automato1.EeE:
            if EeE[1] != SF:
                EeENormais.append(EeE)

    autAux = Automato(Automato1.estados, eventosNormais, Automato1.estadoInicial, [], EeENormais, {})
    estadosAlcancados = []
    adj = {}
    adj = MontaDictAdjacencias(autAux.estados, autAux.eventos, autAux.EeE)

    estadosAlcancados = BuscaPorLargura(adj, autAux.estadoInicial[0], autAux.estados)
    # print(estadosAlcancados)
    eventos = autAux.eventos
    estInicial = autAux.estadoInicial[0:1]
    EeEalcancados = []
    acessivel = []
    for alc in estadosAlcancados:
        if estadosAlcancados.get(alc) != ["nulo"]:
            acessivel.append(alc)
    for EeE in autAux.EeE:
        if EeE[0] in acessivel:
            EeEalcancados.append(EeE)
            eventosNormais.append(ev)
    autAcessivel = Automato(acessivel, eventos, estInicial, [], EeEalcancados, {})
    return (autAcessivel)


def Renomear(Automato1, eventos=[], indice="R1"):
    # print(Automato1.eventos)
    estadosR = []
    eventosR = []
    EeER = []

    for ev in eventos:
        for e in Automato1.eventos:
            # print(ev)
            if ev == e:
                if ev + indice not in eventosR:
                    eventosR.append(ev + indice)
            else:
                if e not in eventosR and e not in eventos:
                    eventosR.append(e)

    for ev in eventos:
        for ee in Automato1.EeE:
            if ee[1] == ev:
                EeER.append([ee[0], ev + indice, ee[2]])
            else:
                if ee not in EeER and ee[1] not in eventos:
                    EeER.append(ee)
    autRenomeado = Automato(Automato1.estados, eventosR, Automato1.estadoInicial, [], EeER)

    return (autRenomeado)
    # autNormal = ParteAcessivel(autAux)
    # return(autNormal)


def ComponenteNormal(aut, Gn, SF):
    autN = ParteNormal(aut, SF)
    T1 = ComposicaoParalela(autN, Gn)

    # print("Gn")
    # for ee in Gn.EeE:
    #  print(ee)

    # print("teste1")
    # for ee in T1.EeE:
    #  print(ee)

    # print("Gn1")
    # for ee in aut1n.EeE:
    #  print(ee)

    evO = []
    evUO = []
    for ev in Gn.eventos:
        if ev in autN.eventos:
            evO.append(ev)
        else:
            evUO.append(ev)

    TesteObs = Observador(T1, evO, evUO)

    EeETemp = []
    EeEFinal = []
    estadosTemp = []
    estadosFinal = []
    # print("inicio")
    for ee1 in TesteObs.EeE:
        for ee2 in TesteObs.EeE:
            # partida = False
            # chegada = False
            similar = False
            eeP = ""
            eeC = ""
            if ee1[1] == ee2[1]:
                for estP in ee2[0].split("_"):
                    if estP in ee1[0]:
                        similar = True
                        # print(estP)
                        # print(ee1[0])
                for estC in ee2[2].split("_"):
                    if estC in ee1[2]:
                        similar = True
                        # print(estC)
                        # print(ee1[2])

                if similar == True:
                    # print("similar")
                    # print(ee1)
                    # print(ee2)

                    eeP = ee1[0]
                    eeC = ee1[2]
                    for estP2 in ee2[0].split("_"):
                        if estP2 not in eeP:
                            eeP = eeP + "_" + estP2
                            # print("eeP")
                            # print(eeP)

                    for estC2 in ee2[2].split("_"):
                        if estC2 not in eeC:
                            eeC = eeC + "_" + estC2
                            # print("eeC")
                            # print(eeC)
                    if [eeP, ee1[1], eeC] not in EeETemp:
                        EeETemp.append([eeP, ee1[1], eeC])

                    if eeP not in estadosTemp:
                        estadosTemp.append(eeP)
                    if eeC not in estadosTemp:
                        estadosTemp.append(eeC)

                    # print([eeP, ee1[1], eeC])
                else:
                    EeETemp.append([ee1[0], ee1[1], ee1[2]])
                    EeETemp.append([ee2[0], ee2[1], ee2[2]])
                    if ee1[0] not in estadosTemp:
                        estadosTemp.append(ee1[0])
                    if ee1[2] not in estadosTemp:
                        estadosTemp.append(ee1[2])
                    if ee2[0] not in estadosTemp:
                        estadosTemp.append(ee2[0])
                    if ee2[2] not in estadosTemp:
                        estadosTemp.append(ee2[2])

    for ee in EeETemp:
        if ee not in EeEFinal:
            EeEFinal.append(ee)

    # print("final")
    # for ef in EeEFinal:
    # print(ef)
    # print("end")
    # if
    # limpando EeEFinal
    # addFinal = False
    # maior = 0
    # for est in estadosTemp:
    #  maior = 0
    #  addFinal = False
    #  for temp in estadosTemp:
    #    if est in temp:
    #      if maior < len(temp):
    #        maior = len(temp)
    #  if maior == len(est):
    #    if est not in estadosFinal:
    #      estadosFinal.append(est)

    contador = 0
    estIn = ""
    estOut = ""
    # for ee in TesteObs.EeE:

    # print(TesteObs.estados)

    # for ee in EeETemp:
    #  print(ee)
    # return(TesteObs)


def TesteParteNormalRestrita(aut1, aut2, EF):
    autN = ParteNormal(aut1, EF)

    estados1 = autN.estados
    estados2 = aut2.estados
    # print(aut1.estadoInicial[0])
    # print(aut2.estadoInicial[0])

    paraleloInicial = [autN.estadoInicial[0] + "|" + aut2.estadoInicial[0]]
    paraleloEstados = []
    paraleloEventos = []
    paraleloEeE = []
    estadoAtual = ""
    for est1 in estados1:
        for est2 in estados2:
            estadoAtual = est1 + "|" + est2
            paraleloEstados.append(estadoAtual)
    for ev in autN.eventos:
        if ev not in paraleloEventos:
            paraleloEventos.append(ev)
    for ev in aut2.eventos:
        if ev not in paraleloEventos:
            paraleloEventos.append(ev)
    for ev1 in autN.EeE:
        for ev2 in aut2.EeE:
            adicionar12 = []
            adicionar1 = []
            adicionar2 = []
            adicionarL1 = []
            adicionarL2 = []
            # if ev1[0]=='31' or ev2[0]=='1|4|2|2|Y':
            # print(ev1)
            # print(ev2)
            # print(ev1[0] + "-" + ev2[0] + "-" + ev1[1] + "-" + ev2[1])
            if ev1[1] in aut2.eventos and ev2[1] in autN.eventos and ev1[1] == ev2[1]:
                adicionar12 = [ev1[0] + "|" + ev2[0], ev1[1], ev1[2] + "|" + ev2[2]]
            if ev1[1] not in aut2.eventos:
                adicionar1 = [ev1[0] + "|" + ev2[0], ev1[1], ev1[2] + "|" + ev2[0]]
                adicionarL1 = [ev1[0] + "|" + ev2[2], ev1[1], ev1[2] + "|" + ev2[2]]
            if ev2[1] not in autN.eventos:
                # print(ev2)
                evPulou = PulaPegaProximo(aut2.EeE, ev2, autN.eventos)
                # print(evPulou)
                for evp in evPulou:
                    # print(evp)
                    adicionar2.append([ev1[0] + "|" + evp[0], evp[1], ev1[0] + "|" + evp[2]])
                    adicionarL2.append([ev1[2] + "|" + evp[0], evp[1], ev1[2] + "|" + evp[2]])
                    # print(adicionar2)
                    # print(adicionarL2)
                # oensar nos autolacos
            # if ev1[0] == ev1[2] and ev1[1] not in aut2.eventos:
            #  adicionarL1 = [ev1[0] + "|" + ev2[2], ev1[1], ev1[0] +"|" + ev2[2]]
            # if ev2[0] == ev2[2] and ev2[1] not in aut1.eventos:
            #  adicionarL2 = [ev1[2] + "|" + ev2[0], ev2[1], ev1[2] +"|" + ev2[2]]
            # adicionar e criar o analogo
            if adicionar12 not in paraleloEeE and adicionar12 != []:
                paraleloEeE.append(adicionar12)
            if adicionar1 not in paraleloEeE and adicionar1 != []:
                paraleloEeE.append(adicionar1)
            for ad2 in adicionar2:
                if ad2 not in paraleloEeE and adicionar2 != []:
                    paraleloEeE.append(ad2)
            if adicionarL1 not in paraleloEeE and adicionarL1 != []:
                paraleloEeE.append(adicionarL1)
            for adL2 in adicionarL2:
                if adL2 not in paraleloEeE and adicionarL2 != []:
                    paraleloEeE.append(adL2)
            # print(adicionar)

    autParaleloFull = Automato(paraleloEstados, paraleloEventos, paraleloInicial, [], paraleloEeE, {})
    # print(paraleloEventos)
    # print(paraleloEeE)
    autAcessivel = ParteAcessivel(autParaleloFull)
    return (autAcessivel)


def PulaPegaProximo(EeE, ee, eventos):
    ret = []
    # print(eventos)
    for ev in EeE:
        if ee[1] not in eventos:
            aux = PulaPegaProximo(EeE, [ee[0], ev[1], ev[2]], eventos)
            for e in aux:
                ret.append(e)

        if ev[0] == ee[2] and ee[1] in eventos:
            # print("ee")
            # print(ee)
            # print("ev")
            # print(ev)
            # print(ev[0]+"ev0")
            # print(ee[2]+"ee2")
            # print(ee[1]+"ee1")
            ret.append([ee[0], ev[1], ev[2]])

    return (ret)


def ParteNormalRestrita(aut, Gn, EF):
    autN = aut

    autN = ParteNormal(aut, EF)

    autP = ComposicaoParalela(autN, Gn)
    EeE = autP.EeE

    EeEIntermediario = []

    # remove autolacos de eventos de outros modulos
    # print(EeE)
    for autolaco in EeE:
        # print(autolaco)
        if autolaco[1] not in autN.eventos and autolaco[0] == autolaco[2]:
            LIXO = ""
            # print(autolaco[1])
            # print(autolaco)
            # print("nao")
            # EeE.remove(autolaco)
        else:
            # print(autolaco)
            # print("sim")
            EeEIntermediario.append(autolaco)

    # unifica estados que são acessados por eventos que nao pertencem ao modulo
    # print(EeE)
    # print(EeEIntermediario)
    EeESemAL = EeEIntermediario
    temEventosExtras = True
    # EeEIntermediario = EeE
    contador = 0
    # if temEventosExtras:
    while temEventosExtras:
        EeEAtualizado = []

        for ee1 in EeEIntermediario:
            for ee2 in EeESemAL:
                if ee1[1] in autN.eventos:
                    if ee1 not in EeEAtualizado:
                        EeEAtualizado.append(ee1)
                else:
                    if ee1[2] == ee2[0]:
                        add = [ee1[0], ee2[1], ee2[2]]
                        if add not in EeEAtualizado:
                            EeEAtualizado.append(add)
        # print(EeEIntermediario)
        EeEIntermediario = EeEAtualizado
        # print(EeEIntermediario)
        temEventosExtras = False
        listaTemEventos = []
        # print(listaTemEventos)
        for ee in EeEAtualizado:
            # print(ee)
            if ee[1] not in autN.eventos:
                listaTemEventos.append(True)
            else:
                listaTemEventos.append(False)

        for tem in listaTemEventos:
            if tem == True:
                temEventosExtras = True
        # print(temEventosExtras)
        # print(listaTemEventos)

    autParaleloFull = Automato(autP.estados, autN.eventos, autP.estadoInicial, [], EeEIntermediario, {})
    # print(paraleloEventos)
    # print(paraleloEeE)
    autAcessivel = ParteAcessivel(autParaleloFull)
    return (autAcessivel)


def EliminaEstadosSimilares(aut):
    # verifica se os estados são similares e os substitui
    manter = []
    apagar = []
    similares = []

    manter.append(aut.estadoInicial[0])
    for ee1 in aut.EeE:
        for ee2 in aut.EeE:
            if (ee1[0] == ee2[0]) and (ee1[1] == ee2[1]) and (ee1[2] != ee2[2]):
                similares.append([ee1[2], ee2[2]])
                if (ee1[2] in manter) and (ee2[2] not in manter):
                    if ee2[2] not in apagar:
                        apagar.append(ee2[2])
                elif (ee2[2] in manter) and (ee1[2] not in manter):
                    if ee1[2] not in apagar:
                        apagar.append(ee1[2])
                elif (ee1[2] not in manter) and (ee2[2] not in apagar):
                    manter.append(ee1[2])
                    apagar.append(ee2[2])

    primeiro = []
    for est in aut.estados:
        possuiEvento = False
        for emorto in aut.EeE:
            if emorto[0] == est:
                possuiEvento = True
        if possuiEvento == False:
            if primeiro == []:
                primeiro.append(est)
                manter.append(est)
            else:
                apagar.append(est)
                similares.append([primeiro[0], est])

    primeirolaco = []
    for est in aut.estados:
        possuiExtraLaco = False
        for elaco in aut.EeE:
            if (elaco[0] == est) and elaco[0] != elaco[2]:
                possuiExtraLaco = True
        if possuiExtraLaco == False:
            if primeirolaco == []:
                primeirolaco.append(est)
                manter.append(est)
            else:
                apagar.append(est)
                similares.append([primeirolaco[0], est])

    EeEFinal = []
    for eenovo in aut.EeE:
        if (eenovo[2] not in apagar):
            if eenovo not in EeEFinal:
                EeEFinal.append(eenovo)
    EeEResult = []
    for eenovo in EeEFinal:
        if (eenovo[0] not in apagar):
            if eenovo not in EeEResult:
                EeEResult.append(eenovo)

    EeEAcertos = []
    for eeacertos in aut.EeE:
        for sim in similares:
            if eeacertos[0] in apagar:
                if eeacertos[0] == sim[0]:
                    if [sim[1], eeacertos[1], eeacertos[2]] not in EeEAcertos:
                        EeEAcertos.append([sim[1], eeacertos[1], eeacertos[2]])
                if eeacertos[0] == sim[1]:
                    if [sim[0], eeacertos[1], eeacertos[2]] not in EeEAcertos:
                        EeEAcertos.append([sim[0], eeacertos[1], eeacertos[2]])
            if eeacertos[2] in apagar:
                if eeacertos[2] == sim[0]:
                    if [eeacertos[0], eeacertos[1], sim[1]] not in EeEAcertos:
                        EeEAcertos.append([eeacertos[0], eeacertos[1], sim[1]])
                if eeacertos[2] == sim[1]:
                    if [eeacertos[0], eeacertos[1], sim[0]] not in EeEAcertos:
                        EeEAcertos.append([eeacertos[0], eeacertos[1], sim[0]])

    for eea in EeEAcertos:
        if (eea not in EeEResult) and (eea[0] not in apagar) and (eea[2] not in apagar):
            EeEResult.append(eea)

    # print(similares)
    # print(manter)
    # print(apagar)
    # print("resultado")
    # for e in EeEResult:
    # print(e)

    # print("teste")
    possiveis = {}
    listaPossiveis = []

    for ee1 in EeEResult:
        for ee2 in EeEResult:
            if (ee1[0] != ee2[0]) and (ee1[1] == ee2[1]) and (ee1[2] == ee2[2]):
                if ee1[0] + "_" + ee2[0] in possiveis.keys():
                    aux1 = possiveis[ee1[0] + "_" + ee2[0]]
                    aux1[ee1[1]] = ee1[2]
                    # print(aux1)
                    possiveis[ee1[0] + "_" + ee2[0]] = aux1
                # else:
                # possiveis[ee1  [0] + "_" + ee2[0]] = {ee1[1]:ee1[2]}
                if ee2[0] + "_" + ee1[0] in possiveis.keys():
                    aux2 = possiveis[ee2[0] + "_" + ee1[0]]
                    aux2[ee1[1]] = ee1[2]
                    # print(aux1)
                    possiveis[ee1[0] + "_" + ee2[0]] = aux2
                if (ee1[0] + "_" + ee2[0] not in possiveis.keys()) and (ee2[0] + "_" + ee1[0] not in possiveis.keys()):
                    # else:
                    possiveis[ee1[0] + "_" + ee2[0]] = {ee1[1]: ee1[2]}

                if ee1[0] not in listaPossiveis:
                    listaPossiveis.append(ee1[0])
                if ee2[0] not in listaPossiveis:
                    listaPossiveis.append(ee2[0])

                # print(ee1)
                # print(ee2)
    # print(possiveis)
    # print(listaPossiveis)
    # EeEResult.append(['0|0|0|1|0', 'b', '0|0|0|1|0'])
    # print(EeEResult)
    temEventoAMais = {}
    for key1, value1 in possiveis.items():  # for pos in listaPossiveis:
        pos12 = key1.split("_")
        temEventoAMais[key1] = False
        for ee1 in EeEResult:
            for ee2 in EeEResult:
                # for key1, value1 in possiveis.items():
                if temEventoAMais[key1] == False:
                    # pos12 = pos12[0].split("_")
                    if ee1[0] == pos12[0]:
                        # print(ee1)
                        if ee1[1] not in value1.keys():
                            temEventoAMais[key1] = True
                        else:
                            temEventoAMais[key1] = False
                        # print(ee1[1])
                        # print(value1.keys())
                        # print(temEventoAMais)

    relacao = {}
    for k, v in temEventoAMais.items():
        est = k.split("_")
        if v == False:

            # print(temEventoAMais)
            # print("est")
            # print(est)
            if (est[0] in relacao.keys()) and (est[1] in relacao.keys()):
                if relacao[est[0]] != relacao[est[1]]:
                    temEventoAMais[k] = True
            elif est[0] in relacao.keys():
                relacao[est[1]] = relacao[est[0]]
            elif est[1] in relacao.keys():
                relacao[est[0]] = relacao[est[1]]
            else:
                relacao[est[0]] = est[0]
                relacao[est[1]] = est[0]
        if v == True:
            relacao[est[0]] = est[0]
            relacao[est[1]] = est[1]

    # print(temEventoAMais)

    # print("relacao")
    # print(relacao)

    EeEDefinitivo = []
    for eer in EeEResult:
        # print(eer)
        for evMk, evMv in temEventoAMais.items():

            lp = evMk.split("_")
            if eer[0] not in listaPossiveis:
                if eer not in EeEDefinitivo:
                    EeEDefinitivo.append(eer)
            if eer[0] in listaPossiveis:

                if (eer[0] == lp[0]):
                    # print(lp[0])
                    # print(eer)

                    # print(evMk)
                    if evMv == False:
                        if [relacao[eer[0]], eer[1], eer[2]] not in EeEDefinitivo:
                            EeEDefinitivo.append([relacao[eer[0]], eer[1], eer[2]])
                    if evMv == True:
                        if (eer not in EeEDefinitivo):
                            EeEDefinitivo.append(eer)
                if (eer[0] == lp[1]):
                    if evMv == False:
                        if [relacao[eer[0]], eer[1], eer[2]] not in EeEDefinitivo:
                            EeEDefinitivo.append([relacao[eer[0]], eer[1], eer[2]])
                    if evMv == True:
                        if (eer not in EeEDefinitivo):
                            EeEDefinitivo.append(eer)

    EeELinha = []
    estadosLinha = []
    partida = ""
    chegada = ""
    for d in EeEDefinitivo:
        if d[0] in relacao.keys():
            partida = relacao[d[0]]
        else:
            partida = d[0]
        if d[2] in relacao.keys():
            chegada = relacao[d[2]]
        else:
            chegada = d[2]
        add = [partida, d[1], chegada]
        if add not in EeELinha:
            EeELinha.append(add)
        if partida not in estadosLinha:
            estadosLinha.append(partida)
        if chegada not in estadosLinha:
            estadosLinha.append(chegada)

    # print("transição de eventos")
    # for l in EeELinha:
    #  print(l)
    # print("estados")
    # for eL in estadosLinha:
    #  print(eL)
    # print("eventos")
    # for ev in aut.eventos:
    #  print(ev)
    inicialLinha = aut.estadoInicial
    if inicialLinha[0] in relacao.keys():
        inicialLinha[0] = relacao[inicialLinha[0]]

    # print(estadosLinha)
    # print(EeELinha)
    # print(inicialLinha)
    # print(relacao)
    autLinha = Automato(estadosLinha, aut.eventos, inicialLinha, [], EeELinha, {})
    return (autLinha)


def PartePosFalha(Automato1, EF):
    adj1 = {}
    estadosAlcancados = []
    adj1 = MontaDictAdjacencias(Automato1.estados, Automato1.eventos, Automato1.EeE)
    # print(adj1)

    inicialPosFalha = []
    acessivelPosFalha = []
    # pegando os estados que sao sequencia de eventos de falha

    for SF in EF:
        for ePF in Automato1.EeE:
            if ePF[1] == SF:
                if ePF[2] not in inicialPosFalha:
                    inicialPosFalha.append(ePF[2])

    for iPF in inicialPosFalha:
        estadosAlcancados = BuscaPorLargura(adj1, iPF, Automato1.estados)
        # print(estadosAlcancados)
        eventos = Automato1.eventos
        # estInicial = Automato1.estadoInicial[0:1]
        # EeEalcancados = []
        # acessivel = []
        for alc in estadosAlcancados:
            if estadosAlcancados.get(alc) != ["nulo"] and alc not in acessivelPosFalha:
                acessivelPosFalha.append(alc)
        # for EeE in Automato1.EeE:
        #  if EeE[0] in acessivelPosFalha:
        #    EeEalcancados.append(EeE)
    # autAcessivel = Automato(acessivel, eventos, estInicial, [] , EeEalcancados, {})
    return (acessivelPosFalha)


def automatoGf(aut, EF):
    estadosL = ["N", "Y"]
    eventosL = aut.eventos
    EeEL = []
    for ev in aut.eventos:
        if ev in EF:
            EeEL.append(["N", ev, "Y"])
            EeEL.append(["Y", ev, "Y"])
        else:
            EeEL.append(["N", ev, "N"])
            EeEL.append(["Y", ev, "Y"])
    Al = Automato(estadosL, eventosL, ["N"], ["Y"], EeEL)
    preGf = ComposicaoParalela(aut, Al)
    # print(preGf.estados)
    # print(preGf.eventos)
    # print(preGf.estadosMarcados)
    # print(preGf.estadoInicial)
    # print(preGf.EeE)

    Gf = ParteCoacessivel(preGf)
    return (Gf)


def automatoGn(aut, EF):
    estadosN = ["N"]
    eventosN = aut.eventos
    EeEN = []
    for ev in aut.eventos:
        if ev not in EF:
            EeEN.append(["N", ev, "N"])

    An = Automato(estadosN, eventosN, ["N"], [], EeEN)
    Gn = ComposicaoParalela(aut, An)
    # print(preGf.estados)
    # print(preGf.eventos)
    # print(preGf.estadosMarcados)
    # print(preGf.estadoInicial)
    # print(preGf.EeE)

    # Gf = ParteCoacessivel(preGf)
    return (Gn)


def automatoGni(aut, Gn, EF):
    estadosGni = []
    estadosinicialGni = []
    EeEGni = []
    dictSimilares = {}

    for ee in Gn.EeE:
        if ee[1] not in aut.eventos and ee[0] != ee[2]:
            dictSimilares = ComparaSimilares(ee[0], ee[2], dictSimilares)
            # if ee[0] not in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[2]] = ee[0]
            #     dictSimilares[ee[0]] = ee[0]
            # elif ee[0] in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     dictSimilares[ee[0]] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[0]] = dictSimilares[ee[2]]
            #     dictSimilares[ee[2]] = dictSimilares[ee[2]]
            # elif ee[0] in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     aux = dictSimilares[ee[2]]
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #          if v == aux:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[2]] = ee[0]
            #     dictSimilares[ee[0]] = ee[0]
            # elif ee[0] in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     aux = dictSimilares[ee[0]]
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #          if v == ee[0]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[0]] = dictSimilares[ee[2]]
            # elif ee[0] in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] not in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #          if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[2]] = ee[0]
            #     dictSimilares[ee[0]] = ee[0]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = ee[0]
            # elif ee[0] in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            #           if v == ee[0]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[0]] = dictSimilares[ee[2]]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[2]]
            #           if v == ee[0]:
            #              dictSimilares[k] = dictSimilares[ee[2]]
            # elif ee[0] in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            #           if v == ee[0]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[0]] = ee[2]
            #     dictSimilares[ee[2]] = ee[2]
            # elif ee[0] in dictSimilares.keys() and ee[2] not in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[0]]
            # elif ee[0] not in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[0]] = dictSimilares[ee[2]]
            #     for k, v in dictSimilares.items():
            #           if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[2]]
            # elif ee[0] in dictSimilares.keys() and ee[2] in dictSimilares.keys() and ee[0] not in dictSimilares.values() and ee[2] in dictSimilares.values():
            #     dictSimilares[ee[2]] = dictSimilares[ee[0]]
            #     for k, v in dictSimilares.items():
            #          if v == ee[2]:
            #              dictSimilares[k] = dictSimilares[ee[0]]

    # montando função de transição de estados
    # for ee in Gn.EeE:
    #     partida = ee[0]
    #     chegada = ee[2]

    #     if partida in dictSimilares.keys():
    #         partida = dictSimilares[partida]
    #     if chegada in dictSimilares.keys():
    #         chegada = dictSimilares[chegada]

    #     if ee[1] in aut.eventos:
    #         add = [partida, ee[1], chegada]
    #         if add not in EeEGni:
    #             EeEGni.append(add)

    # #montando estados
    # for eg in EeEGni:
    #     if eg[0] not in estadosGni:
    #         estadosGni.append(eg[0])
    #     if eg[2] not in estadosGni:
    #         estadosGni.append(eg[2])

    # #estado inicial
    # if Gn.estadoInicial[0] in dictSimilares.keys():
    #     estadosinicialGni.append(dictSimilares[Gn.estadoInicial[0]])
    # else:
    #     estadosinicialGni.append(Gn.estadoInicial[0])
    comp = filtraElementosAutomato(aut.estados, aut.eventos, Gn.estadoInicial, aut.estadosMarcados, Gn.EeE,
                                   dictSimilares)
    # [estadosNovo, eventosnovo, estadoInicialNovo, estadoMarcadoNovo, EeENovo]
    # FALTA MARCAR ESTADOS
    # print(listaSimilares)
    Gni = Automato(comp[0], comp[1], comp[2], comp[3], comp[4], {})
    return (Gni)


def filtraElementosAutomato(estados, eventos, estadoInicial, estadosMarcados, EeE, dictSimilares):
    EeENovo = []
    estadosNovo = []
    estadoInicialNovo = []
    estadoMarcadoNovo = []
    eventosNovo = eventos
    for ee in EeE:
        partida = ee[0]
        chegada = ee[2]

        if partida in dictSimilares.keys():
            partida = dictSimilares[partida]
        if chegada in dictSimilares.keys():
            chegada = dictSimilares[chegada]

        if ee[1] in eventos:
            add = [partida, ee[1], chegada]
            if add not in EeENovo:
                EeENovo.append(add)

    # montando estados
    for eg in EeENovo:
        if eg[0] not in estadosNovo:
            estadosNovo.append(eg[0])
        if eg[2] not in estadosNovo:
            estadosNovo.append(eg[2])

    # estado inicial
    if estadoInicial[0] in dictSimilares.keys():
        estadoInicialNovo.append(dictSimilares[estadoInicial[0]])
    else:
        estadoInicialNovo.append(estadoInicial[0])

    return ([estadosNovo, eventosNovo, estadoInicialNovo, estadoMarcadoNovo, EeENovo])


def limpaGni(aut):
    # primeiro vamos unificar os estados que não possuem eventos ativos

    # listando os estados mortos
    dictMorto = {}
    primeiroMorto = []
    for est in aut.estados:
        estadoMorto = []
        estadoAcessivel = []
        for ee in aut.EeE:
            # print(est)
            # print(ee[0])
            # print(ee[2])
            if ee[0] == est:
                estadoMorto.append(False)
            if ee[2] == est:
                estadoAcessivel.append(True)
        if False not in estadoMorto and True in estadoAcessivel:
            if primeiroMorto == []:
                primeiroMorto.append(est)
                dictMorto[est] = est
            else:
                dictMorto[est] = primeiroMorto[0]
    print("morto")
    print(dictMorto)
    # organizando os estados e funcoes de transicao de estados para contemplar os similares mortos

    comp = filtraElementosAutomato(aut.estados, aut.eventos, aut.estadoInicial, aut.estadosMarcados, aut.EeE, dictMorto)
    # return([estadosNovo, eventosNovo, estadoInicialNovo, estadoMarcadoNovo, EeENovo])
    EeELinha = comp[4]
    estadosLinha = comp[0]
    estadoInicialLinha = comp[2]
    # partida = ""
    # chegada = ""
    # for ee in aut.EeE:
    #     partida = ee[0]
    #     chegada = ee[2]

    #     if partida in dictMorto.keys():
    #         partida = dictMorto[partida]
    #     if chegada in dictMorto.keys():
    #         chegada = dictMorto[chegada]

    #     if ee[1] in aut.eventos:
    #         add = [partida, ee[1], chegada]
    #         if add not in EeELinha:
    #             EeELinha.append(add)

    # #montando estados
    # for eg in EeELinha:
    #     if eg[0] not in estadosLinha:
    #         estadosLinha.append(eg[0])
    #     if eg[2] not in estadosLinha:
    #         estadosLinha.append(eg[2])

    # #estado inicial
    # if aut.estadoInicial[0] in dictMorto.keys():
    #     estadoInicialLinha.append(dictMorto[aut.estadoInicial[0]])
    # else:
    #     estadoInicialLinha.append(aut.estadoInicial[0])

    # FALTA MARCAR ESTADOS

    # juntando estados que realizam apenas self loop com os mesmos eventos
    dictAutolaco = {}
    listaEventos = []
    listaEventosEstado = []
    dictEventosEstado = {}
    dictJuntarEstados = {}

    estadosAux = []
    estadoInicialAux = []
    EeEAux = []
    for est in estadosLinha:
        listaEventosEstado = []
        listaEventos = []
        for ee in EeELinha:
            if ee[0] == est:
                listaEventosEstado.append(ee[1])
                if ee[0] == ee[2]:
                    if ee[1] not in listaEventos:
                        listaEventos.append(ee[1])
                    dictAutolaco[est] = listaEventos
        dictEventosEstado[est] = listaEventosEstado
    print("dictAutolaco")
    print(dictAutolaco)
    print("dictEventosEstado")
    print(dictEventosEstado)

    for est1 in estadosLinha:
        for est2 in estadosLinha:
            temEventoSobrando1 = []
            temEventoSobrando2 = []
            for ees in EeELinha:
                if ees[0] == est1:

                    if est1 in dictAutolaco.keys() and est2 in dictAutolaco.keys() and est1 != est2:
                        # print(dictAutolaco.keys())
                        # print(est1)
                        # print(est2)
                        # print(dictAutolaco[est1])
                        # print(dictAutolaco[est2])
                        # print(ees[1])
                        if ees[1] in dictAutolaco[est1] and ees[1] in dictAutolaco[est2]:
                            temEventoSobrando1.append(False)
                        else:
                            temEventoSobrando1.append(True)
                if ees[0] == est2:
                    if est1 in dictAutolaco.keys() and est2 in dictAutolaco.keys():
                        if ees[1] in dictAutolaco[est1] and ees[1] in dictAutolaco[est2]:
                            temEventoSobrando2.append(False)
                        else:
                            temEventoSobrando2.append(True)
            # print("temEventoSobrando1")
            # print(temEventoSobrando1)
            # print("temEventoSobrando2")
            # print(temEventoSobrando2)
            if True not in temEventoSobrando1 and True not in temEventoSobrando2 and temEventoSobrando1 != [] and temEventoSobrando1 != []:
                dictJuntarEstados = ComparaSimilares(est1, est2)
    print("dictJuntarEstados")
    print(dictJuntarEstados)

    comp = filtraElementosAutomato(estadosLinha, aut.eventos, estadoInicialLinha, aut.estadosMarcados, EeELinha,
                                   dictJuntarEstados)
    # return([estadosNovo, eventosNovo, estadoInicialNovo, estadoMarcadoNovo, EeENovo])

    EeELinha = comp[4]
    estadosLinha = comp[0]
    estadoInicialLinha = comp[2]

    # juntando os estados similares, por fazerem os mesmos eventos e chegarem aos mesmos estados

    # separando os eventos ativos em cada estado
    dictEventosAtivos = {}
    for est in estadosLinha:
        listaEventos = []
        for ee in EeELinha:
            if ee[0] == est:
                listaEventos.append(ee[1])
        dictEventosAtivos[est] = listaEventos

    # separando os possiveis similares
    dictTalvez = {}
    for est1 in estadosLinha:
        for est2 in estadosLinha:
            for ee1 in EeELinha:
                for ee2 in EeELinha:
                    if est1 == ee1[0] and est2 == ee2[0] and ee1[1] == ee2[1] and ee1[2] == ee2[2]:
                        if est1 not in dictTalvez.keys() and est2 not in dictTalvez.keys():
                            dictTalvez[est2] = est1
                        elif est1 in dictTalvez.keys() and est2 not in dictTalvez.keys():
                            dictTalvez[est2] = dictTalvez[est1]
                        elif est1 not in dictTalvez.keys() and est2 in dictTalvez.keys():
                            dictTalvez[est1] = dictTalvez[est2]
                        elif est1 in dictTalvez.keys() and est2 in dictTalvez.keys():
                            dictTalvez[est2] = dictTalvez[est1]
                            for k, v in dictTalvez.items():
                                if v == est2:
                                    dictTalvez[k] = dictTalvez[est1]

    # EeELinha = []
    # estadosLinha = []
    # partida = ""
    # chegada = ""
    # inicialLinha = aut.estadoInicial
    # if inicialLinha[0] in relacao.keys():
    #     inicialLinha[0] = relacao[inicialLinha[0]]

    # print(estadosLinha)
    # print(EeELinha)
    # print(inicialLinha)
    # print(relacao)
    autLinha = Automato(estadosLinha, aut.eventos, estadoInicialLinha, [], EeELinha, {})
    return (autLinha)


def ComparaSimilares(estado1, estado2, dicionario={}):
    if estado1 not in dicionario.keys() and estado2 not in dicionario.keys() and estado1 not in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado2] = estado1
        dicionario[estado1] = estado1
    elif estado1 in dicionario.keys() and estado2 not in dicionario.keys() and estado1 not in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        dicionario[estado1] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 in dicionario.keys() and estado1 not in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado1] = dicionario[estado2]
        dicionario[estado2] = dicionario[estado2]
    elif estado1 in dicionario.keys() and estado2 in dicionario.keys() and estado1 not in dicionario.values() and estado2 not in dicionario.values():
        aux = dicionario[estado2]
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == aux:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 not in dicionario.keys() and estado1 in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado2] = estado1
        dicionario[estado1] = estado1
    elif estado1 in dicionario.keys() and estado2 not in dicionario.keys() and estado1 in dicionario.values() and estado2 not in dicionario.values():
        aux = dicionario[estado1]
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado1:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 in dicionario.keys() and estado1 in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado1] = dicionario[estado2]
    elif estado1 in dicionario.keys() and estado2 in dicionario.keys() and estado1 in dicionario.values() and estado2 not in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 not in dicionario.keys() and estado1 in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado2] = estado1
        dicionario[estado1] = estado1
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = estado1
    elif estado1 in dicionario.keys() and estado2 not in dicionario.keys() and estado1 in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado1]
            if v == estado1:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 in dicionario.keys() and estado1 in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado1] = dicionario[estado2]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado2]
            if v == estado1:
                dicionario[k] = dicionario[estado2]
    elif estado1 in dicionario.keys() and estado2 in dicionario.keys() and estado1 in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado1]
            if v == estado1:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 not in dicionario.keys() and estado1 not in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado1] = estado2
        dicionario[estado2] = estado2
    elif estado1 in dicionario.keys() and estado2 not in dicionario.keys() and estado1 not in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado1]
    elif estado1 not in dicionario.keys() and estado2 in dicionario.keys() and estado1 not in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado1] = dicionario[estado2]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado2]
    elif estado1 in dicionario.keys() and estado2 in dicionario.keys() and estado1 not in dicionario.values() and estado2 in dicionario.values():
        dicionario[estado2] = dicionario[estado1]
        for k, v in dicionario.items():
            if v == estado2:
                dicionario[k] = dicionario[estado1]

    return (dicionario)
