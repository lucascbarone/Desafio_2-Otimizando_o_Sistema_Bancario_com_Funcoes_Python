# Desafio de Projeto do Curso da DIO: Potência Tech powered by iFood | Ciência de Dados
## Desafio 2: Otimizando o Sistema Bancário com Funções Python
### Objetivo
Otimizar o código, deixando-o mais modularizado. Deve-se criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, serão criadas duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

### Requisitos
 - Função de depósito
   > Deve receber os argumentos apenas por posição (positional only);
   > Sugestão de argumentos: saldo, valor e extrato;
   > Sugestão de retornos: saldo e extrato.
 - Função de saque
   > Deve receber os argumentos apenas por nome (keyword only);
   > Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques;
   > Sugestão de retornos: saldo e extrato.
 - Função de extrato
   > Deve receber os argumentos por posição e nome (positional only and keyword only);
   > Argumentos posicionais: saldo;
   > Argumentos nomeados: extrato.
 - Função criar usuário (cliente)
   > Deve armazenar os usuários em uma lista;
   > Um usuário é composto por: nome, data de nascimento, cpf e endereço;
   > O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado;
   > O CPF é uma string na qual deve-se armazenar somente os números;
   > Não podemos cadastrar mais de um usuário com o mesmo CPF.
 - Função conta corrente
   > Deve armazenar contas em uma lista;
   > Uma conta é composta por: agência, número da conta e usuário;
   > O número da conta é sequencial, iniciando em 1;
   > O número da agência é fixo: "0001";
   > O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.