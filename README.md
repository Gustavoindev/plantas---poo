Classificando Tipos de Plantas

Este projeto representa a classificação das plantas utilizando conceitos fundamentais de Programação Orientada a Objetos (POO) com Python, esses são os conceitos:herança, polimorfismo, encapsulamento e modularização.

O sistema pede para que a gente responda a um formulário interativo no terminal, informando características básicas de uma planta, e no final recebe a classificação correta da planta.

Estrutura do Projeto
O código é organizado em vários arquivos, cada um representa uma classe ou funcionalidade específica:
`plantas.py` – Classe base `Planta`
`briofitas.py` – Classe `Briofita`
`pteridofitas.py` – Classe `Pteridofita`
`gimnospermas.py` – Classe `Gimnosperma`
`angiospermas.py` – Classe `Angiosperma`
`formulario.py` – Função de interação com o usuário
`main.py` (ou arquivo principal) – Execução do programa

Todos os conteúdo utilizados:
 Classificação das plantas:
  Briofitas
  Pteridofitas
  Gimnospermas
  Angiospermas (Monocotiledôneas e Dicotiledôneas)
  Utilizando conceitos de Programação Orientada a Objetos

Quais os Conceitos de POO utilizados:

Encapsulamento
Exemplo: O atributo `_nome` da classe `Planta` é protegido, garantindo controle sobre os dados.

Herança
Exemplo: Todas as classes específicas (`Briofita`, `Pteridofita`, `Gimnosperma` e `Angiosperma`) herdam da classe base `Planta`, que pode ser considerada a classe principal.

Polimorfismo
Exemplo: O método `caracteristicas()` é feito em cada classe, apresentando características diferentes de acordo o tipo da planta.

Classes do Sistema:

Classe `Planta`
Classe base do sistema.
Atributos:
`_nome`
Métodos:
`caracteristicas()`

Classe `Briofita`
Herda de `Planta`.
Métodos:
`caracteristicas()`

Classe `Pteridofita`
Herda de `Planta`.
Métodos:
`caracteristicas()`

Classe `Gimnosperma`
Herda de `Planta`.
Métodos:
`caracteristicas()`

Classe `Angiosperma`
Herda de `Planta`.
Atributos:
`tipo`
Métodos:
`__init__(nome, tipo)`
`caracteristicas()`












