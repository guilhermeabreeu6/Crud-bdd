Funcionalidade: CRUD de disciplinas
  Como usuário do sistema
  Quero gerenciar disciplinas
  Para cadastrar, listar, buscar, atualizar e excluir disciplinas

  Cenário: Criar disciplina com dados válidos
    Quando eu criar uma disciplina com título "Banco de Dados"
    Então o status da resposta deve ser 201
    E a resposta deve conter o título "Banco de Dados"

  Cenário: Não criar disciplina com dados inválidos
    Quando eu criar uma disciplina inválida
    Então o status da resposta deve ser 400
    E a resposta deve conter erros

  Cenário: Listar disciplinas
    Dado que existe uma disciplina cadastrada com título "Engenharia de Software"
    Quando eu listar as disciplinas
    Então o status da resposta deve ser 200
    E a lista deve conter 1 item

  Cenário: Buscar disciplina por id
    Dado que existe uma disciplina cadastrada com título "Redes"
    Quando eu buscar a disciplina cadastrada
    Então o status da resposta deve ser 200
    E a resposta deve conter o título da disciplina cadastrada

  Cenário: Atualizar disciplina
    Dado que existe uma disciplina cadastrada com título "POO"
    Quando eu atualizar a disciplina para o título "POO Avançada"
    Então o status da resposta deve ser 200
    E a resposta deve conter o título "POO Avançada"

  Cenário: Excluir disciplina
    Dado que existe uma disciplina cadastrada com título "Algoritmos"
    Quando eu excluir a disciplina cadastrada
    Então o status da resposta deve ser 204
    E ao buscar a disciplina excluída o status deve ser 404