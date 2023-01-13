import pandas as pd
import os


class Dados:
    def __init__(self):
        self.df = pd.read_csv(os.getcwd() + '/registro.csv')

    def tamanho(self):
        return len(self.df)

    def horaInicial(self, i):
        return self.df.iloc[i]['hora_inicial']

    def horaFinal(self, i):
        return self.df.iloc[i]['hora_final']

    def tarefa(self, i):
        return self.df.iloc[i]['tarefa']
    
    def atividade(self, i):
        return self.df.iloc[i]['atividade']
    
    def comentario(self, i):
        return self.df.iloc[i]['comentario']




