
#############################################################################
##                                 NOTA                                    ##
## AS DATAS DAS ATIVIDADES DESTE PROGRAMA SÓ PODEM SER ADICIONADAS UMA VEZ ##
## QUE ESTEJAM ENTRE O ANO DE 2017 E O ANO DE 2099.                        ##
#############################################################################


import sys




listaDeEntrada = sys.argv

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'




RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)

#######################################################
#Determinando operações de função de validação de data#
#######################################################

def dataValida(data) :
    #validando tamanho
    if len(data) != 8:
        return False
    #validando caracteres
    if ord(data[0]) < 48 or ord(data[0]) > 51:
        return False
    if ord(data[1]) < 48 or ord(data[1]) > 57:
        return False
    if ord(data[2]) < 48 or ord(data[2]) > 49:
        return False
    if ord(data[3]) < 48 or ord(data[3]) > 57:
        return False
    if ord(data[4]) < 50 or ord(data[4]) > 50:
        return False
    if ord(data[5]) < 48 or ord(data[5]) > 48:
        return False
    if ord(data[6]) < 49 or ord(data[6]) > 57:
        return False
    if ord(data[7]) < 48 or ord(data[7]) > 57:
        return False
      
    #validando casos de mês com 30 ou 31 dias através do codigo ASCII do caractere 
    if ord(data[0]) > 50 and ord(data[1]) == 49 and not(ord(data[3]) == 49 or ord(data[3]) == 51 \
                                                        or ord(data[3]) == 53 or ord(data[3]) == 55 \
                                                        or ord(data[3]) == 56 or ord(data[3]) == 48 \
                                                        or (ord(data[2]) == 49 and ord(data[3]) == 50)):
        return False

    #fevOdiferentao
    if ord(data[0]) > 50 and ord(data[2]) == 48 and ord(data[2]) == 50:
        return False
    else:
        return True
      
#######################################################
#Determinando operações de função de validação da hora#
#######################################################

def horaValida(horaMin):
  #conferindo se há mais ou menos do que 4 caracteres
  if len(horaMin) != 4:
    return False
  #validando se os caracteres representam o formato da hora solicitado
  if ord(horaMin[0]) > 50 or ord(horaMin[0]) < 48:
      return False 
  if ord(horaMin[1]) > 57 or ord(horaMin[1]) < 48:
      return False
  if ord(horaMin[2]) > 53 or ord(horaMin[2]) < 48:
      return False 
  if ord(horaMin[3]) > 57 or ord(horaMin[3]) < 48:
      return False
  else:
    return True

##############################################################
#Determinando operacoes de funcao de validacao de prioridades#
##############################################################

def prioridadeValida(pri):
    #se o tamanho da string for três, sendo o primeiro e último caracteres
    #'(' e ')' e o caractere central variando de uma letra de A-Z, a validacao devolve True
    if len(pri) == 3 and ord(pri[0]) == 40 and ord(pri[2]) == 41 and (ord(pri[1]) < 91 and ord(pri[1]) > 64):
        return True
    else:
        return False

###########################################################
#Determinando operacoes de funcao de validacao de contexto#
###########################################################

def contextoValido(cont):
    #se o tamanho da string contexto for dois ou mais e o primeiro caractere for um @, retorna True
    if len(cont) >= 2 and ord(cont[0]) == 64:
        return True
    else:
        return False

##########################################################
#Determinando operacoes de funcao de validacao de projeto#
##########################################################

def projetoValido(proj):
    #se o tamanho da string projeto for 2 ou mais e o primeiro caractere for um +, retorna True
    if len(proj) >= 2 and ord(proj[0]) == 43:
        return True
    else:
        return False

#################################################
#Determinando operacoes de funcao de organizacao#
#################################################

"""fp = open('C:/Users/Lúcio/Desktop/Estudo/UFPE/Programação 1/Projeto/Partes/todo.txt', 'r')
texto = fp.readlines()
fp.close()
print(texto)"""
def organizar(texto):
    itens = []
    for linha in texto:
        data = ' '
        hora = ' '
        pri = ' '
        desc = ' '
        contexto = ' '
        projeto = ' '
        #print(linha)
        linha = linha.strip() # remove espaços em branco e quebras de linha do começo e do fim
        tokens = linha.split() # quebra o string em palavras
        #adiciona cada Token ao seu respectivo campo na tupla
        #sendo eles ou data ou hora ou descricao,prioridade
        #contexto ou projeto.
        while tokens != []:
            if dataValida(tokens[0]) == True:
                data = tokens[0]
            elif horaValida(tokens[0]) == True:
                hora = tokens[0]  
            elif prioridadeValida(tokens[0]) == True:
                pri = tokens[0]
            elif contextoValido(tokens[0]) == True:
                contexto = tokens[0]              
            elif projetoValido(tokens[0]) == True:
                projeto = tokens[0]
            else:
                desc += (tokens[0]+' ')
            tokens.pop(0)     
        itens.append((desc, (data, hora, pri, contexto, projeto)))
    return itens

###############################################################
#Determinando operacoes de funcao de adicionar elemento p todo#
###############################################################   

def adicionar(descricao, extras): 
  #se a descricao for vazia, retorna false
  if descricao  == '' :
      return False
  
  else:
      #caso contrário, cada trecho da linha vai ser adicionado no seu respectivo
      #campo, a partir da validacao, assim como foi na funcao organizar()
      desc = descricao
      hora = ""
      data = ""
      pri = ""
      contexto = ""
      projeto = ""
      for x in extras:
          if x != '':
              if dataValida(x) == True:
                  data = x 
              elif horaValida(x) == True:
                  hora = x
              elif prioridadeValida(x) == True:
                  pri = x
              elif contextoValido(x) == True:
                  contexto = x
              elif projetoValido(x) == True:
                  projeto = x 

      #cria uma "nova atividade" a partir da junção das strings de cada campo
      novaAtividade = data + " " + hora + " " + desc + " " + pri + " " + contexto + " " + projeto + " "
      #Escreve no TODO_FILE a nova atividade. 
      try: 
        fp = open(TODO_FILE, 'a')
        fp.write(novaAtividade + "\n")
        fp.close()
      except IOError as err:
        print("Não foi possível escrever para o arquivo " + TODO_FILE)
        print(err)
        return False

      return print("Atividade adicionada com sucesso")

##############################################
#Determinando operacoes de funcao de listagem#
##############################################
    
def listar():
    #abre arquivo To do para modo de leitura
    fp = open(TODO_FILE,'r')
    #armazena seu conteudo em formato de lista de strings, para cada string, uma linha
    #arquivo
    conteudo = fp.readlines()
    fp.close()
    #chama a funcao de ordenar por data e hora e ordena o conteudo do arquivo
    OrdenadaPorDataHora = ordenarPorDataHora(conteudo)
    #chama a funcao de ordenar por prioridade e ordenada o conteudo do arquivo que já
    #foi ordenado por data e hora
    OrdenadaPorPriDataHora = ordenarPorPrioridade(OrdenadaPorDataHora)
    #cria uma lista para a manipulacao
    ListarFormatoOrganizar = []
    #cria uma lista para exibicao que será construída em cima do que for manipulado
    #na lista anterior
    ListarFormatoShow = []
    Data = ""
    Hora = ""
    Prioridade = ""
    Descricao = ""
    Contexto = ""
    Projeto = ""
    #funcao enumerate pega como parametro o indice de x e x para cada linha em
    #ordenadas por prioridade, data e adiciona à lista de manipulação uma tupla
    #com o indice+1 de cada linha, dando uma noção de contagem.
    for indice,x in enumerate(OrdenadaPorPriDataHora):
      ListarFormatoOrganizar.append((indice + 1, x))

    #para cada tupla, que representa uma linha, na lista de manipulacao
    #atribuimos sua string ao seu devido campo e, se for uma data, recebe as barras
    #para formato DD/MM/AAAA. Se for uma hora, recebe "h" e "min" para as horas e minutos.
    for x in ListarFormatoOrganizar:
      if dataValida(x[1][1][0]) == True:
        Data = x[1][1][0]
        Data = Data[0:2]+"/"+Data[2:4]+"/"+Data[4:8]
      else:
        Data = ""
      if horaValida(x[1][1][1]) == True:
        Hora = x[1][1][1]
        Hora = Hora[0:2]+"h"+Hora[2:4]+"min"
      else:
        Hora = ""
      if prioridadeValida(x[1][1][2]) == True:
        Prioridade = x[1][1][2]
      else:
        Prioridade = ""
      Descricao = x[1][0]
      if contextoValido(x[1][1][3]) == True:
        Contexto = x[1][1][3]
      else:
        Contexto = ""
      if projetoValido(x[1][1][4]) == True:
        Projeto = x[1][1][4]
      else:
        Projeto = ""
      #constroi uma linha a partir da juncao dos elementos guardados em cada campo + o índice+1
      linha = str(x[0])+" "+Data+" "+Hora+" "+Prioridade+" "+Descricao+" "+Contexto+" "+Projeto+"\n"
      #a linha é adicionada a lista para exibicao
      ListarFormatoShow.append(linha)
    dadosOrganizados = organizar(ListarFormatoShow)
    #para cada linha da lista de tuplas dos dados organizados, confere se uma prioridade é
    #A, B, C ou D para que então, possa ser impressa na tela com a cor específica.
    for linha in dadosOrganizados:
      i = dadosOrganizados.index(linha)
      if linha[1][2] == "(A)":
        printCores(ListarFormatoShow[i],RED+BOLD)
      elif linha[1][2] == "(B)":
              printCores(ListarFormatoShow[i],CYAN)
      elif linha[1][2] == "(C)":
              printCores(ListarFormatoShow[i],GREEN)
      elif linha[1][2] == "(D)":
              printCores(ListarFormatoShow[i],YELLOW)
      else:
        print(ListarFormatoShow[i])

    return
#funcao listar para funcionamento de outras funcoes
def listarParaOutrasFuncoes():
    #abre arquivo To do para modo de leitura
    fp = open(TODO_FILE,'r')
    #armazena seu conteudo em formato de lista de strings, para cada string, uma linha
    #arquivo
    conteudo = fp.readlines()
    fp.close()
    #chama a funcao de ordenar por data e hora e ordena o conteudo do arquivo
    OrdenadaPorDataHora = ordenarPorDataHora(conteudo)
    #chama a funcao de ordenar por prioridade e ordenada o conteudo do arquivo que já
    #foi ordenado por data e hora
    OrdenadaPorPriDataHora = ordenarPorPrioridade(OrdenadaPorDataHora)
    #cria uma lista para a manipulacao
    ListarFormatoOrganizar = []
    #cria uma lista para exibicao que será construída em cima do que for manipulado
    #na lista anterior
    ListarFormatoShow = []
    Data = ""
    Hora = ""
    Prioridade = ""
    Descricao = ""
    Contexto = ""
    Projeto = ""
    #funcao enumerate pega como parametro o indice de x e x para cada linha em
    #ordenadas por prioridade, data e adiciona à lista de manipulação uma tupla
    #com o indice+1 de cada linha, dando uma noção de contagem.
    for indice,x in enumerate(OrdenadaPorPriDataHora):
      ListarFormatoOrganizar.append((indice + 1, x))

    #para cada tupla, que representa uma linha, na lista de manipulacao
    #atribuimos sua string ao seu devido campo.
    for x in ListarFormatoOrganizar:
      if dataValida(x[1][1][0]) == True:
        Data = x[1][1][0]
      else:
        Data = ""
      if horaValida(x[1][1][1]) == True:
        Hora = x[1][1][1]
      else:
        Hora = ""
      if prioridadeValida(x[1][1][2]) == True:
        Prioridade = x[1][1][2]
      else:
        Prioridade = ""
      Descricao = x[1][0]
      if contextoValido(x[1][1][3]) == True:
        Contexto = x[1][1][3]
      else:
        Contexto = ""
      if projetoValido(x[1][1][4]) == True:
        Projeto = x[1][1][4]
      else:
        Projeto = ""
      #constroi uma linha a partir da juncao dos elementos guardados em cada campo + o índice+1
      linha = str(x[0])+" "+Data+" "+Hora+" "+Prioridade+" "+Descricao+" "+Contexto+" "+Projeto+"\n"
      #a linha é adicionada a lista para exibicao
      ListarFormatoShow.append(linha)
    return ListarFormatoShow
  
###############################################################
#Determinando operacoes de funcao de ordenacao por data e hora#
###############################################################   

def ordenarPorDataHora(itens):
    #organiza os dados para avaliacao e manipulacao
    lista_n_ordenada =(organizar(itens))
    #cria uma lista pra armazenar as atividades ordenadas por data e hora
    ordenadaDataHora = []
    #cria uma lista pra armazenar as atividades que nao possuem data e hora
    semDataHora = []
    #cria a lista da qual os elementos das duas listas acima serão adicionados
    ordenadaCompletaDataHora = []
    #para cada componente da lista nao ordenada, primeiramente confere se tem
    #data e hora. Se não tiver, o componente é adicionado a lista semDataHora.
    #caso contrário, adiciona a lista ordenadaDataHora, que ainda não está ordenada.
    #são criadas chaves com nome de "ano","mes","dia","hora" para posteriormente servirem
    #para a funcao sorted()
    for x in lista_n_ordenada:
        if x[1][0] == ' ' and x[1][1] == ' ':
            semDataHora.append(x)
        else:
            ordenadaDataHora.append(x)
            #ano será a chave que corresponde aos dois ultimos dígitos do ano
            ano = lambda ano: ano[1][0][6:] 
            #mes será a chave que corresponde aos dois dígitos do mês "MM"
            mes = lambda mes: mes[1][0][2:4]
            #dia será a chave que corresponde aos dois dígitos do dia "DD"
            dia = lambda dia: dia[1][0][:2]
            #hora será a chave que corresponde aos quatro dígitos da hora "HHMM"
            hora = lambda hora: hora[1][1]
            #ordena por ano a ordenada por mês,
            #que por sua vez está ordenada por dia,
            #que por sua vez está ordenada por hora.
            ordenadaDataHora = sorted(sorted(sorted(sorted(ordenadaDataHora,key=hora),key=dia),key=mes),key=ano)
    #preencho a lista completa de ordenadas para utilização no programa
    for x in ordenadaDataHora:
        ordenadaCompletaDataHora.append(x)
    for x in semDataHora:
        ordenadaCompletaDataHora.append(x)
      
    return ordenadaCompletaDataHora    
"""
data
01 23 4567
DD MM AAAA
01 01 2017
31 12 2099
for x in itens:[1][0] 

hora
0123
HHMM
0000
2359
for x in itens:[1][1]
"""

###############################################################
#Determinando operacoes de funcao de ordenacao por prioridades#
###############################################################      

def ordenarPorPrioridade(itens):
    lista_n_ordenada =itens
    lista_ordenada = []
    semPri = []
    #i é equivalenteo ao número que representa o caractere A na tabela ASCII 
    i = 65
    #enquanto i estiver entre os valores que representam A e Z
    #para cada item da lista não ordenada, confere qual a sua
    #prioridade e, se for igual a i, que a cada iteracao progride
    #numa ordem crescente representando a ordem alfabética, é adicionado
    #à lista ordenada. Se a prioridade for vazia, adiciona à lista "semPri"
    #e logo dps a lista ordenada recebe cada elemento das sem prioridade.
    while i >= 65 and i <= 90:        
        for x in lista_n_ordenada:
            if x[1][2] == "("+ chr(i)+ ")":
                lista_ordenada.append(x)     
        i+=1
    for x in lista_n_ordenada:
        if x[1][2] == chr(32):
                semPri.append(x)
    for x in semPri:
        lista_ordenada.append(x)
    return lista_ordenada

################################################
#Determinando operacoes de funcao de associacao#
################################################
  
#funcao que associa o número escolhido pelo usuário ao índice da atividade referente no
#arquivo
def associacao(num,listada,todo):
      #recebe o número de input(num), a lista resultado de uma das funcoes listar (listada)
      #e o conteúdo presente no arquivo (todo).
      for x in listada:
        if num[0] == "0":
          novoNum = num[1]
          if x[0][1] == novoNum:
            linhaParametro = x
        else:
          if x[0][1:3] == num:
            linhaParametro = x
      for x in todo:
        if x[0][1:].strip() == linhaParametro[0][3:].strip():
          indice = todo.index(x)
      return indice
    
########################################################
#Determinando operacoes de funcao de comando de remocao#
########################################################

def remover(numAtivd):
  #se o tamanho do número da atividade inserido for diferente de dois dígitos,
  # função retorna mensagem para o usuário por um número com dois dígitos.
  if len(numAtivd) != 2:
    return print("Número deve ter dois dígitos. Exemplo: 01 e não 1")
  else:
    #cria lista com formato padrão para exibicao
    listaShow = listarParaOutrasFuncoes()
    #abre o arquivo todo em modo de leitura e atribui a uma variável o seu conteúdo
    fp = open(TODO_FILE,"r+")
    listaToDo = fp.readlines()
    #organiza os dados do conteudo do arquivo em uma outra variável
    listaToDoOrganizada = organizar(listaToDo)
    #organiza os dados da lista com formato padrão para exibicao
    listaShow = organizar(listaShow)
    #cria variável que receberá o parâmetro de comparaçao entre o X da lista
    #e o X do arquivo
    linhaParametro = ''
    #indice do elemento que o usuário deseja remover NO ARQUIVO será atribuído
    #à variável 'indice' através da utilizacao da funcao de associacao.
    indice = associacao(numAtivd,listaShow,listaToDoOrganizada)
    #remove da lista com o conteúdo original do arquivo o item correspondente
    #ao número escolhido pelo usuário
    listaToDo.remove(listaToDo[indice])
    #abre novamente o arquivo, desta vez em modo de escrita e reescreve o conteúdo
    #do arquivo com base nos dados contidos na listaToDo
    fp = open(TODO_FILE,"w")
    fp.writelines(listaToDo)
    fp.close()
       
    return print("Atividade "+numAtivd+" foi removida com sucesso")

#######################################################
#Determinando operacoes de funcao de comando priorizar#
#######################################################

def priorizar(texto):
  numAtivd = texto[0:2]
  priori = texto[3:]
  if (ord(numAtivd[0]) < 48 or ord(numAtivd[0]) > 57) or (ord(numAtivd[1]) < 48 or ord(numAtivd[1]) > 57):
    return print("Você deve informar o número da atividade da qual deseja priorizar com dois dígitos. Exemplo: 'p 01 A'")
  else:
    #mesmo padrao de raciocinio da funcao de remocao
    listaShow = listarParaOutrasFuncoes()    
    fp = open(TODO_FILE,"r+")
    listaToDo = fp.readlines()
    fp.close()
    listaToDoOrganizada = organizar(listaToDo)
    listaShow = organizar(listaShow)
    linhaParametro = ''
    indice = ''
    indice = associacao(numAtivd,listaShow,listaToDoOrganizada)
    #a linha da qual o usuário quis priorizar será encontrada já com a prioridade alterada na
    #variável criada a seguir "linhaPriorizada"
    linhaPriorizada = listaToDoOrganizada[indice][1][0]+" "+listaToDoOrganizada[indice][1][1]+\
                      listaToDoOrganizada[indice][0]+"("+priori+")"+" "+listaToDoOrganizada[indice][1][3]+" "+listaToDoOrganizada[indice][1][4]+"\n"
    #remove a linha com a prioridade antiga
    listaToDo.remove(listaToDo[indice])
    #adiciona a linha com a nova prioridade
    listaToDo.append(linhaPriorizada)
    #abre o arquivo e o reescreve com base nos dados contidos na listaToDo
    fp = open(TODO_FILE,"w")
    fp.writelines(listaToDo)
    fp.close()

    return print("Atividade "+numAtivd+" foi priorizada com sucesso.")

###################################################
#Determinando operacoes de funcao de comando fazer#
###################################################

def fazer(num):
  AbrindoDONE = open(ARCHIVE_FILE,'w')
  AbrindoDONE.close()
  numAtivd = num
  #se o tamanho do número da atividade inserido for diferente de dois dígitos,
  # função retorna mensagem para o usuário por um número com dois dígitos.
  if len(numAtivd) != 2:
    return print("Número deve ter dois dígitos. Exemplo: 01 e não 1")
  else:
    #mesmo raciocinio das funcoes de remocao e priorizacao
    done = open(ARCHIVE_FILE,"r")
    listaDone = done.readlines()
    fp = open(TODO_FILE,"r")
    listaToDo = fp.readlines()
    listaToDoOrganizada = organizar(listaToDo)
    listaShow = listarParaOutrasFuncoes()
    listaShow = organizar(listaShow)
    linhaParametro = ''
    indice = associacao(numAtivd,listaShow,listaToDoOrganizada)
    #reconhece a linha concluida no arquivo
    linhaConcluida = listaToDo[indice]
    #adiciona ela a listaDone
    listaDone.append(linhaConcluida)
    #remove ela da listaToDo
    listaToDo.remove(listaToDo[indice])
    #abre o arquivo para atividades completas em modo de escrita e copia as linhas
    #das atividades já feitas
    done = open(ARCHIVE_FILE,"w")
    for x in listaDone:
      done.writelines(x)
    #abre o arquivo para atividades ainda não feitas em modo de escrita e reescreve
    #o seu conteudo sem as linhas das atividades feitas
    fp = open(TODO_FILE,"w")
    for x in listaToDo:
      fp.writelines(x)
    fp.close()
    done.close()

    return print("Atividade "+numAtivd+" marcada como feita.") 

###############################################################
#Determinando operacoes de funcao de processamento de comandos#
###############################################################    

def processarComandos(listaDeEntrada):
  if listaDeEntrada[1] == ADICIONAR:
    stringDeEntrada = ' '.join(listaDeEntrada)
    stringNova = stringDeEntrada[12:]
    itemParaAdicionar = organizar([(stringNova)])[0]
    #itemParaAdicionar = (descricao, (data, hora, prioridade, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1])

  elif listaDeEntrada[1] == LISTAR:
    return listar()
    
  elif listaDeEntrada[1] == REMOVER:
    stringDeEntrada = ' '.join(listaDeEntrada)
    stringNova = stringDeEntrada[12:]
    remover(stringNova)
    return     

  elif listaDeEntrada[1] == FAZER:
    stringDeEntrada = ' '.join(listaDeEntrada)
    stringNova = stringDeEntrada[12:]
    fazer(stringNova)
    return    

  elif listaDeEntrada[1] == PRIORIZAR:
    stringDeEntrada = ' '.join(listaDeEntrada)
    stringNova = stringDeEntrada[12:]
    priorizar(stringNova)
    return    

  else :
    print("Comando inválido.")

#########
#RODANDO#
#########

print(processarComandos(listaDeEntrada))
