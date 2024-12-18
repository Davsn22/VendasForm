import time
import pyautogui
import pandas as pd
import subprocess

# Gerar dados fictícios em CSV
data = {
    'Nome': ['Maria Souza', 'Carlos Oliveira'],
    'Email': ['maria@yahoo.com', 'carlos@hotmail.com'],
    'Telefone': ['998877665', '996622441'],
    'CPF': [ '98765432100', '11223344556'],
    'RG': [ '2345678', '3456789'],
    'Orgão Emissor': ['PC', 'SSP'],
    'Data Emissão': ['2005-06-15', '2010-10-30'],
    'Naturalidade': ['Imperatriz', 'Açailândia'],
    'Nacionalidade': [ 'Brasileira', 'Brasileiro'],
    'Estado Civil': ['Casado', 'Divorciado'],
    'Cônjuge': ['José Souza', 'Carla Oliveira'],
    'Rendimento Cônjuge': [ '5000', '4500'],
    'Rendimento Titular': ['6000', '5500'],
    'Atividade': [ 'Advogada', 'Médico'],
    'Mãe': [ 'Joana Souza', 'Fernanda Oliveira'],
    'Pai': [ 'Antônio Souza', 'Paulo Oliveira']
}

df = pd.DataFrame(data)
df.to_csv('dados_ficticios.csv', index=False)

# Abrir o arquivo HTML no navegador
subprocess.Popen(["start", "chrome", "http://localhost:8000/"], shell=True)
time.sleep(3)  # Aguardar o navegador carregar a página

# Função para preencher os campos
def preencher_campos():
    campos = [
        'Maria Souza', 'maria@yahoo.com','998877665','987.654.321-00','15-06-2000', '23456723456788 SSP/PC','15-06-2020','Imperatriz','Brasileiro','Casada','Jose Souza 234.567.234-56 25/06/2020','5000','6000','Advogada','Joana Souza','Antonio Souza'
    ]
    
    # Preencher o formulário com dados fictícios usando pyautogui (pressionando teclas)
    pyautogui.press('tab')
    pyautogui.write(campos[0])  # Nome
    pyautogui.press('tab')
    pyautogui.write(campos[1])  # Email
    pyautogui.press('tab')
    pyautogui.write(campos[2])  # Telefone
    pyautogui.press('tab')
    pyautogui.write(campos[3])  # CPF
    pyautogui.press('tab')
    pyautogui.write(campos[4])  # RG
    pyautogui.press('tab')
    pyautogui.write(campos[5])  # Orgão Emissor
    pyautogui.press('tab')
    pyautogui.write(campos[6])  # Data de Emissão
    pyautogui.press('tab')
    pyautogui.write(campos[7])  # Naturalidade
    pyautogui.press('tab')
    pyautogui.write(campos[8])  # Nacionalidade
    pyautogui.press('tab')
    pyautogui.write(campos[9])  # Estado Civil
    pyautogui.press('tab')
    pyautogui.write(campos[10])  # Nome Cônjuge
    pyautogui.press('tab')
    pyautogui.write(campos[11])  # Rendimento Cônjuge
    pyautogui.press('tab')
    pyautogui.write(campos[12])  # Rendimento Titular
    pyautogui.press('tab')
    pyautogui.write(campos[13])  # Atividade
    pyautogui.press('tab')
    pyautogui.write(campos[14])  # Nome Mãe
    pyautogui.press('tab')
    pyautogui.write(campos[15])  # Nome Pai
    pyautogui.press('tab')
    
    # Enviar o formulário
    pyautogui.press('enter')

# Chamar a função para preencher os campos
preencher_campos()
