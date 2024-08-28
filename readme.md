# Teste de Desempenho de Protocolos TCP e UDP

Este projeto consiste em comparar o desempenho dos protocolos de comunicação TCP e UDP, avaliando o tempo de resposta e a confiabilidade das mensagens enviadas entre um cliente e um servidor.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/ProtocolBenchmark.git
```


### Instalação das Dependências

Todas as bibliotecas usadas são padrão do python.
### Executando o Projeto

1. **Iniciar o Servidor**

   Primeiro, inicie o servidor TCP e UDP. Execute o script `server.py` para iniciar ambos os servidores em threads diferentes:
   
    ```bash 
    python3 server.py 
    ```
    

Este comando iniciará dois servidores:
- Servidor TCP escutando na porta 65432
- Servidor UDP escutando na porta 65433

2. **Executar o Cliente**

    Em seguida, execute o script `client.py` para iniciar os testes de desempenho:

    ```bash 
    python3 client.py 
    ```
O cliente realizará 100.000 requisições para ambos os protocolos e imprimirá as estatísticas de desempenho ao final dos testes.
<div align="center">
<img src=print.png >
</div>


## Protocolos de Comunicação

### TCP (Transmission Control Protocol)

**Características:**
- **Orientado a Conexão:** Estabelece uma conexão entre o cliente e o servidor antes da transmissão de dados.
- **Confiável:** Garante a entrega das mensagens na ordem correta e realiza retransmissões em caso de perda de pacotes.
- **Controle de Fluxo:** Gerencia o ritmo de envio dos dados para evitar a sobrecarga do receptor.
- **Sobrehead:** Devido ao controle de fluxo e garantia de entrega, TCP pode ter mais latência em comparação ao UDP.

### UDP (User Datagram Protocol)

**Características:**
- **Não Orientado a Conexão:** Não estabelece uma conexão prévia entre o cliente e o servidor.
- **Menos Confiável:** Não garante a entrega das mensagens, nem a ordem correta, nem retransmite pacotes perdidos.
- **Menos Sobrehead:** Tem menos latência e overhead em comparação ao TCP, pois não realiza controle de fluxo ou verificação de erros.

## Parâmetros do Programa

- **Tamanho dos Pacotes:** TCP e UDP: 32 KB (32 * 1024 bytes) para mensagens enviadas entre o cliente e o servidor.
- **Buffer:** TCP e UDP: O buffer para recepção de dados é configurado para 32 KB, o que corresponde ao tamanho das mensagens.
- **Quantidade de Requisições:** Número de Requisições: 100.000 requisições para cada protocolo durante os testes.