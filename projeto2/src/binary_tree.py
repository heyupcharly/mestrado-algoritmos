#!/usr/bin/env python3

import csv
from anytree import NodeMixin, RenderTree
from anytree.exporter import DotExporter
from anytree.dotexport import RenderTreeGraph
import datetime



class BuscaTree():
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None




    def inserir(self, v):
        novo = No(v, None, None)  # cria um novo Nó
        if self.root == None:
            self.root = novo
        else:  # se nao for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.name:  # ir para esquerda
                    if atual.name == v:
                        atual.count += 1
                        return
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = No(v, None, None, parent=anterior)
                        return
                # fim da condição ir a esquerda
                else:  # ir para direita
                    if atual.name == v:
                        atual.count += 1
                        return
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = No(v, None, None, parent=anterior)
                        return
                # fim da condição ir a direita

    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return 1 + self.altura(atual.esq)
            else:
                return 1 + self.altura(atual.dir)

    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return 1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

    def buscar(self, key):
        if self.root == None:
            return None  # se arvore vazia
        atual = self.root  # começa a procurar desde raiz
        chave = str(key)
        while atual.name != chave:  # enquanto nao encontrou
            if chave < atual.name:
                atual = atual.esq  # caminha para esquerda
            else:
                atual = atual.dir  # caminha para direita
            if atual == None:
                return None  # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item

    def tempoBusca(self, key):
        start = datetime.datetime.now()

        if self.root == None:
            return None  # se arvore vazia
        atual = self.root  # começa a procurar desde raiz
        chave = str(key)
        while atual.name != chave:  # enquanto nao encontrou
            if chave < atual.name:
                atual = atual.esq  # caminha para esquerda
            else:
                atual = atual.dir  # caminha para direita
            if atual == None:
                delta = datetime.datetime.now() - start
                return delta
        delta = datetime.datetime.now().microsecond - start.microsecond
        return delta.real # terminou o laço while e chegou aqui é pq encontrou item

class No(NodeMixin):
    def __init__(self, key, dir, esq, parent=None, args=""):
        super(No, self).__init__()
        self.name = key
        self.dir = dir
        self.esq = esq
        self.parent = parent
        self.count = 1
        self.args = []
        self.args.append(args)

if __name__ == '__main__':
    jsonArray = []
    # read csv file and converts into a array
    with open('../hr-employee-attrition.csv') as f:
        reader = csv.reader(f)
        next(reader)
        lst = list(reader)

    #ordering by id counts the equals.
    print("Indexing by Age")
    eTree = BuscaTree()

    for line in lst:
        value = line[0]
        eTree.inserir(value)

    #exports Picture of the tree
    DotExporter(eTree.root).to_dotfile("../files/BynaryTree.dot")
    RenderTreeGraph(eTree.root).to_picture("../files/BinaryTree.png")

    # print the Age and the count of people with same age.
    for pre, _, node in RenderTree(eTree.root):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.count)

    # altura da arvore
    print(eTree.altura(eTree.root))

    # busca na arvore
    print("buscando: ", dir(eTree.buscar(40)))

    # busca tempo
    print("tempo buscando em mil : ",eTree.tempoBusca(40))