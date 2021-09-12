import os
import shutil
from multiplos import conv_base


dir_or = '/mnt/sda1/usb'
dir_d = '/home/minux/Public/c'


def ficheiros_duplicados(directorio):
    '''
    Esta funcao faz a pesquisa e listagem de ficheiros duplicados num determinado directorio.
    :param directorio: Directorio no qual pretende-se fazer a busca.
    :return: Duas listas, uma dos caminhos e a outra de tamanhos de cada um...
    '''

    lista = []
    file_link = []
    tamanhos = []
    for root, directories, directory in os.walk(directorio):

        for file in directory:
            arq = os.path.join(root, file)
            tamanho = os.path.getsize(arq)
            lista.append(file)
            file_link.append(arq)
            tamanhos.append(tamanho)

    links = []
    size = []
    for i in range(len(lista)):
        if lista.count(lista[i]) != 1:
            links.append(file_link[i])
            size.append(tamanhos[i])
    
    return links, size


def deletefiles(flink, links):
    '''
    Funcao responsavel por copiar um arquivo de cada arquivo repetido para
    um directorio definido pelo usuario para uma posterior reorganizacao.

    :parm flink: Lista de enderecos de arquivos a serem ignorados na remocao.
    :parm links: Lista de enderecos de todos arquivos repetidos.
    :return: Sem retorno!
    '''

    dest = '/home/minux/Templates'
    count = 0
    try:
        for i in range(len(links)): 
            if links[i] in flink:
                shutil.copy(src=flink[i], dst=dest)

            # os.remove(links[i])
            count += 1

    except OSError:
        pass

    print('{:~^80}\n'.format(' Relatorio '))
    print(links)
    print(f'\nFicheiros removidos: {count - len(flink)}')


def org(links, size):

    '''
    Funcao responsavel por armazenar enderecos de uma copia de cada arquivo duplicado.
    :param links: Lista dos enderecos de cada arquivo duplicado.
    :return: Lista dos enderecos de uma copia de cada arquivo duplicado.
    '''

    forg = []
    flink = []
    sfile = []
    fsize = []
    for i in range(len(links)):
        f = os.path.split(links[i])
        forg.append(f)
        
    for f in range(len(forg)):
        if forg[f][1] not in sfile:
            sfile.append(forg[f][1])
            flink.append(links[f])
            fsize.append(size[f])
            
    return flink, size


def Relatorio(lista, size):
    '''
    Guarda em um documento 'txt', as informacoes resultantes da pesquisa...
    :param lista: Lista dos ficheiros encontrados.
    :param size: Lista dos tamanhos de cada ficheiro.
    :return: Nao ha retorno, apenas permite a visualizacao do conteudo guardado
    '''

    with open('dub.txt', 'w') as doc:
        doc.write('{:~^60}\n\n'.format('Ficheiros duplicados'))
        for l in range(len(lista)):
            doc.write(f'{l+1} - {lista[l]}  -  {conv_base(size[l])}\n')

    d = open('dub.txt')
    print(d.read())
    d.close()
    return


def main():

    links, size = ficheiros_duplicados(r'/home/minux/Desktop/lab/')
    flink, fsize = org(links,size)
    print(Relatorio(flink, fsize))
    return

main()
