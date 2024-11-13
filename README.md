# Criptografia e Descriptografia de Mensagens com Imagens como Chave

Este script permite criptografar e descriptografar mensagens utilizando uma imagem como chave de criptografia. A criptografia é realizada utilizando a operação XOR entre os valores binários da mensagem e os valores binários dos pixels da imagem, criando uma cifra simples mas eficaz. O processo de criptografia e descriptografia é feito de forma interativa por meio de um menu no terminal.

## Requisitos

Antes de executar o script, é necessário instalar as bibliotecas adicionais mencionadas abaixo:

- **Pillow**: Biblioteca para manipulação de imagens.
  
  ```bash
  pip install pillow
  ```

- **Numpy**: Biblioteca para manipulação de arrays e dados numéricos.
  
  ```bash
  pip install numpy
  ```

## Como Funciona

1. **Criptografia**:
   - O usuário escolhe uma imagem que será utilizada como chave de criptografia.
   - Em seguida, insere a mensagem que deseja criptografar.
   - A imagem é convertida para uma string binária e a operação XOR é realizada entre os bits da mensagem e os bits da imagem.
   - A mensagem criptografada é salva em um arquivo `.bin`.

2. **Descriptografia**:
   - O usuário escolhe o arquivo criptografado e a imagem chave.
   - O script aplica a operação XOR novamente entre os dados da imagem e do arquivo criptografado para restaurar a mensagem original.

## Funcionalidades

- **Criptografar**: Criptografa a mensagem fornecida utilizando a imagem escolhida como chave.
- **Descriptografar**: Descriptografa uma mensagem previamente criptografada utilizando a mesma imagem chave usada na criptografia.

## Exemplo de Uso

### Criptografando uma Mensagem

1. O usuário escolhe a opção de criptografar no menu:
    ```plaintext
    Escolha uma das opções abaixo:
    1- Criptografar
    2- Descriptografar
    ```

2. Insere a mensagem que deseja criptografar.
3. Escolhe uma imagem para ser a chave de criptografia.
4. Escolhe o local para salvar a mensagem criptografada (o arquivo será salvo com a extensão `.bin`).

### Descriptografando uma Mensagem

1. O usuário escolhe a opção de descriptografar no menu:
    ```plaintext
    Escolha uma das opções abaixo:
    1- Criptografar
    2- Descriptografar
    ```

2. O script solicita que o usuário forneça o arquivo de mensagem criptografada.
3. O usuário escolhe a imagem chave que foi utilizada para criptografar a mensagem.
4. O script exibe a mensagem descriptografada.

## Funções Principais

### `acessar_string_em_loop(string, index)`
- Função auxiliar que permite acessar um índice de forma cíclica em uma string. Usada para garantir que os índices da imagem e da mensagem se alinhem mesmo quando os dados da imagem forem menores que os dados da mensagem.

### `string_para_binario(string)`
- Converte uma string em uma sequência binária (string de 0s e 1s).

### `binario_para_string(binary)`
- Converte uma sequência binária de volta para uma string legível.

### `criptografar_string_xor_binario(imagem, string)`
- Realiza a criptografia XOR entre a imagem (convertida para binário) e a string (também convertida para binário). Retorna a mensagem criptografada em formato binário.

## Observações

- O script utiliza a operação XOR entre os bits da mensagem e da imagem para criptografar e descriptografar. O mesmo processo de criptografia deve ser aplicado para descriptografar a mensagem.
- A imagem usada como chave deve ser escolhida cuidadosamente, já que uma chave de imagem simples pode ser vulnerável a ataques.
  
## Licença

Este projeto é de código aberto. Você pode usá-lo, modificá-lo e distribuí-lo livremente, desde que inclua uma referência ao autor original.

---

Para dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* ou enviar uma *pull request*.

