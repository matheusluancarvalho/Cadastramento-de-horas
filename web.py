from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urls import endereco, chave_token
from arquivo import Dados
import time


# isd = Arquivo(3)
# print(isd.retornaId()) Capitan medi

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome()
actions = ActionChains(navegador)
navegador.get(endereco)

# Entra na Url e insere a chave token

navegador.find_element('xpath', '//*[@id="root"]/div[1]/form/div[2]/div/div/input').send_keys(chave_token)
time.sleep(2)

# Clica em entrar

navegador.find_element('xpath', '//*[@id="root"]/div[1]/form/div[3]/button').click()
time.sleep(5)

# Clica na opção de colocar a hora manualmente

navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[1]/button[2]').click()

# Instância a classe Dados para chamar as funções

teste = Dados()
tamanho = teste.tamanho()


for i in range(tamanho):

    hora_inicial = int(teste.horaInicial(i))
    hora_final = int(teste.horaFinal(i))
    tarefa = int(teste.tarefa(i))
    atividade = str(teste.atividade(i))
    comentario = str(teste.comentario(i))

   # Hora inicial

    navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/input').send_keys(hora_inicial)
    time.sleep(3)

    # Hora final

    navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys(hora_final)
    time.sleep(3)

     # Tarefa

    navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/form/div[1]/div[1]/div/input').send_keys(tarefa)
    time.sleep(3)

    # Atividade

    category_atividade = navegador.find_element('xpath', '//*[@id="activity"]/div/div[1]/div[2]')
    category_atividade.click()
    actions.send_keys(atividade).send_keys(Keys.ENTER).perform()
    time.sleep(3)

    # Comentário

    navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/form/div[2]/div[1]/input').send_keys(comentario)
    time.sleep(3)


    # Adicionar Atividade

    navegador.find_element('xpath', '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/form/div[2]/div[2]/button[2]').click()
    time.sleep(4)
 

input()
