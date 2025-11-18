# Sistema de Gestão de Campi e Cursos  
Projeto da disciplina de Programação Orientada a Objetos (POO) – UFC

Este repositório contém um sistema simples desenvolvido em Python para gerenciar **Campi** e **Cursos**, aplicando conceitos fundamentais de Programação Orientada a Objetos.

---

#  1. Objetivo do Projeto
O objetivo é implementar um sistema modularizado que permita:
- Criar e gerenciar Campi.
- Criar e gerenciar Cursos dentro de cada Campus.
- Aplicar conceitos de **classes, objetos, encapsulamento e modularização**.

O sistema funciona totalmente pelo terminal.

---

#  2. Estrutura do Projeto

A estrutura de diretórios é a seguinte:

/campus
│ ├── init.py # Permite que a pasta funcione como módulo
│ ├── campus.py # Classe Campus e suas funcionalidades
│ └── curso.py # Classe Curso
│
├── main.py # Arquivo principal que executa o menu do sistema
└── README.md 


### ✔ campus.py
Contém a classe `Campus`, responsável por:
- Armazenar nome e lista de cursos.
- Adicionar cursos.
- Listar cursos.
- Remover cursos.
- Editar informações de cursos.

### ✔ curso.py
Contém a classe `Curso`, responsável por:
- Armazenar nome do curso.
- Armazenar código identificador.
- Armazenar coordenador.

### ✔ main.py
É o arquivo que executa o sistema.  
Contém:
- Menu de Campi.
- Menu de Cursos.
- Funções de entrada e saída.
- Controle do fluxo do programa.

---

#  3. Funcionamento do Sistema

Quando o programa inicia, o usuário vê o menu:

1. Criar Campus  
2. Listar Campi  
3. Selecionar Campus  
4. Sair  

Após selecionar um campus, abre-se o menu interno:

1. Adicionar curso  
2. Listar cursos  
3. Editar curso  
4. Remover curso  
5. Voltar  

O sistema realiza operações armazenando objetos em listas durante a execução.

---

# 4. Conceitos de POO Aplicados

### ✔ Classes
Cada entidade (Campus e Curso) é um blueprint para objetos.

### ✔ Objetos
Cada campus ou curso criado é um objeto independente em memória.

### ✔ Encapsulamento
Atributos são manipulados por métodos, evitando acesso direto.

### ✔ Modularização
Código organizado em vários arquivos para melhor manutenção.

### ✔ Composição
Um "Campus" possui vários "Cursos".

---

# 5. Requisitos

- Python 3.8+  
- Nenhuma biblioteca externa é necessária

---

# 6. Autor
Diego  
Universidade Federal do Ceará  
Disciplina: Programação Orientada a Objetos

