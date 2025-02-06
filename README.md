# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python, permitindo ao usuário realizar operações básicas como saque, depósito e consulta de extrato.

## Funcionalidades

Sacar

O usuário pode sacar um valor da conta, respeitando as seguintes regras:

O limite diário de saque é de R$ 1500,00.

O usuário não pode sacar um valor maior do que o saldo disponível.

Não é possível sacar valores negativos ou zero.

Após cada saque, uma mensagem de confirmação é exibida.

Depositar

O usuário pode depositar dinheiro na conta, respeitando as regras:

O limite máximo por depósito é de R$ 500,00.

O usuário pode realizar no máximo 3 depósitos por dia.

Não é possível depositar valores negativos ou zero.

Após cada depósito, o saldo atualizado é exibido.

Extrato

O usuário pode visualizar todas as movimentações do dia.

Exibe todos os depósitos e saques realizados.

Mostra o saldo atual da conta.

## Como Utilizar

Execute o script Python.

Escolha uma das opções do menu:

1 para Sacar.

2 para Depositar.

3 para consultar o Extrato.

4 para Sair.

## Insira os valores conforme solicitado pelo sistema.

O sistema validará as regras antes de confirmar a transação.

Estrutura do Código

Classe Banco

Responsável por gerenciar o saldo e transações.

## Métodos:

- sacar(valor): Processa saques e verifica regras.

- depositar(valor): Processa depósitos e verifica regras.

- extrato(): Exibe todas as movimentações do dia.

- menu(): Interface de interação com o usuário.


# Tecnologias Utilizadas

Python 3



