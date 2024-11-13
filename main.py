#Bibliotecas Adicionais Necessárias:
# Pillow - pip install pillow
# Numpy - pip install numpy

from PIL import Image
import numpy as np
from tkinter import filedialog

def acessar_string_em_loop(string, index):
    return string[index % len(string)]

def string_para_binario(string):
    return ''.join(format(ord(i), '08b') for i in string)

def binario_para_string(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))

def criptografar_string_xor_binario(imagem, string):
    # Converte a imagem em um array numpy e depois em uma string binária
    array_pixels_sem_formatar = np.array(imagem)
    array_pixels = str(array_pixels_sem_formatar).replace('[', '').replace(']', '').replace(' ', '').replace('\n', '')
    binario_imagem = string_para_binario(str(array_pixels))

    # Converte a string a ser criptografada em binário
    binario_string = string_para_binario(string)
    binario_criptografado = []

    # Realiza a operação XOR
    for i in range(len(binario_string)):
        caracter_string = int(acessar_string_em_loop(binario_string, i))
        caracter_imagem = int(acessar_string_em_loop(binario_imagem, (i % len(binario_imagem))))
        binario_criptografado.append(caracter_string ^ caracter_imagem)
    return ''.join(map(str, binario_criptografado))

# Menu Usuario
while True:
    opcao = int(input("Escolhas umas das opções abaixo: \n1- Criptografar\n2- Descriptografar\n"))
    if opcao == 1:
        # Mensagem a ser criptografada
        mensagem = input("Digite a Mensagem a ser Criptografada: \n")

        # Abre a imagem Chave
        print("Escolha a Imagem para ser a Chave da Criptografia: ")
        imagem_caminho = filedialog.askopenfilename()
        imagem_chave = Image.open(imagem_caminho)
        print(imagem_caminho)

        # Salvar a mensagem criptografada
        print("Escolha uma Pasta para Salvar a Mensagem Criptografada: ")
        save = filedialog.askdirectory()+"/Mensagem_Criptografada.bin"
        print(save)

        # Criptografa a mensagem
        mensagem_criptografada = criptografar_string_xor_binario(imagem_chave, mensagem)
        mensagem_criptografada_em_string = binario_para_string(mensagem_criptografada)

        # Salva a mensagem criptografada em um arquivo
        with open(save, "w", encoding="utf-8") as arquivo:
            arquivo.write(mensagem_criptografada_em_string)

        # Exibe A Mensagem Criptografada
        with open(save, "r", encoding="utf-8") as arquivo:
            print("Mensagem Criptografada: \n")
            print(arquivo.read())
            print("Mensagem Criptografada com Sucesso!")

    if opcao == 2:
        # Abre o Arquivo
        print("Abra o Arquivo Para ser Descriptografado: ")
        arquivo_mensagem = filedialog.askopenfilename()
        print(arquivo_mensagem)

        # Abre a imagem Chave
        print("Selecione a Imagem Chave da Criptografia: ")
        imagem_descriptografia_caminho = filedialog.askopenfilename()
        imagem_descriptografia = Image.open(imagem_descriptografia_caminho)
        print(imagem_descriptografia_caminho)

        # Exibe A Mensagem Desdescriptografada
        with open(arquivo_mensagem, "r", encoding="utf-8") as arquivo_descriptografia:
            mensagem_descriptografada_arquivo2 = criptografar_string_xor_binario(imagem_descriptografia, arquivo_descriptografia.read())
            mensagem_descriptografada_em_string_arquivo2 = binario_para_string(mensagem_descriptografada_arquivo2)
            print("Mensagem Desdescriptografada: \n")
            print(mensagem_descriptografada_em_string_arquivo2)