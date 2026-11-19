import os
import unicodedata

PASTA_PERSONAGENS = os.path.join('.','Personagens')
PASTA_CORPOS = os.path.join('.','Corpos')

# Cada personagem tem uma pasta em Personagens/ com pelo menos retrato.png e
# corpo.txt. corpo.txt diz qual pasta de Corpos/ fornece as animacoes, sons e
# frases. Qualquer arquivo colocado na pasta do personagem (por exemplo
# frases.txt ou vs.png) tem prioridade sobre o arquivo do corpo.

def _chave(nome):
    """ Ordena ignorando acentos e maiusculas """
    return unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode().lower()

def listar():
    """ Lista os personagens disponiveis em ordem alfabetica """
    nomes = [n for n in os.listdir(PASTA_PERSONAGENS)
             if not n.startswith(".") and os.path.isdir(os.path.join(PASTA_PERSONAGENS, n))]
    return sorted(nomes, key=_chave)

def pastas(nome):
    """ Pastas onde procurar arquivos do personagem, em ordem de prioridade """
    lista = [os.path.join(PASTA_PERSONAGENS, nome)]
    arqcorpo = os.path.join(PASTA_PERSONAGENS, nome, "corpo.txt")
    if os.path.exists(arqcorpo):
        with open(arqcorpo, encoding="utf-8") as f:
            corpo = f.read().strip()
        if corpo:
            lista.append(os.path.join(PASTA_CORPOS, corpo))
    return lista

def arquivo(nome, arq):
    """ Caminho de um arquivo do personagem (na pasta dele ou no corpo) """
    for pasta in pastas(nome):
        caminho = os.path.join(pasta, arq)
        if os.path.exists(caminho):
            return caminho
    raise FileNotFoundError("Personagem %s: arquivo %s nao encontrado em %s" % (nome, arq, pastas(nome)))

def sons(nome, prefixo):
    """ Lista os .wav que comecam com prefixo, da primeira pasta que tiver algum """
    for pasta in pastas(nome):
        if os.path.isdir(pasta):
            lista = sorted(i for i in os.listdir(pasta) if i.startswith(prefixo) and i.endswith('.wav'))
            if lista:
                return [os.path.join(pasta, i) for i in lista]
    raise FileNotFoundError("Personagem %s: nenhum som %s*.wav em %s" % (nome, prefixo, pastas(nome)))
