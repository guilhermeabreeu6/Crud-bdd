# 📚 CRUD de Disciplinas com BDD

## 📌 Descrição

Este projeto implementa um sistema CRUD (Create, Read, Update, Delete) para gerenciamento de disciplinas de uma instituição de ensino.

Cada disciplina possui os seguintes campos obrigatórios:

* Título
* Data de início
* Data de término
* Número de vagas
* Indicação se é disciplina de verão

A aplicação foi desenvolvida em Python utilizando Flask e organizada em camadas para melhor manutenção.

---

## 🏗️ Estrutura do Projeto

```
crud_disciplinas_bdd/
│
├── app.py
├── models.py
├── repository.py
├── service.py
├── requirements.txt
├── .coveragerc
│
├── features/
│   ├── disciplinas.feature
│   ├── environment.py
│   └── steps/
│       └── disciplina_steps.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🚀 Tecnologias Utilizadas

* Python
* Flask
* Behave (BDD)
* Coverage (cobertura de testes)
* GitHub Actions (CI/CD)

---

## ⚙️ Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 2. Executar a aplicação

```bash
python app.py
```

A API ficará disponível em:

```
http://127.0.0.1:5000
```

---

## 🔥 Endpoints da API

### Criar disciplina

**POST** `/disciplinas`

```json
{
  "titulo": "Banco de Dados",
  "data_inicio": "2026-08-01",
  "data_termino": "2026-12-15",
  "numero_vagas": 30,
  "eh_verao": false
}
```

---

### Listar disciplinas

**GET** `/disciplinas`

---

### Buscar por ID

**GET** `/disciplinas/{id}`

---

### Atualizar disciplina

**PUT** `/disciplinas/{id}`

---

### Remover disciplina

**DELETE** `/disciplinas/{id}`

---

## 🧪 Testes com BDD

Os testes foram implementados utilizando a metodologia Behavior-Driven Development (BDD) com a ferramenta Behave.

### Executar testes

```bash
python -m behave
```

---

## 📊 Cobertura de Testes

Para executar os testes com análise de cobertura:

```bash
python -m coverage run -m behave
python -m coverage report --fail-under=75
```

O projeto exige no mínimo **75% de cobertura**.

---

## ⚙️ Integração Contínua (CI)

O projeto utiliza GitHub Actions para validar automaticamente pull requests para a branch `main`.

A esteira executa:

* Instalação das dependências
* Execução dos testes BDD
* Verificação de cobertura mínima de 75%

Se a cobertura não atingir o mínimo exigido, o processo falha.

---

## 🧠 Arquitetura

O projeto foi dividido em camadas:

* **models.py** → definição da entidade Disciplina
* **repository.py** → armazenamento em memória
* **service.py** → regras de negócio e validações
* **app.py** → rotas da API

Essa separação melhora a organização, manutenção e testabilidade do sistema.

---

## ✅ Funcionalidades Implementadas

* Criar disciplina
* Listar disciplinas
* Buscar disciplina por ID
* Atualizar disciplina
* Remover disciplina
* Validação de dados obrigatórios
* Testes automatizados com BDD
* Verificação de cobertura mínima
* Pipeline automatizado com GitHub Actions

---

## 📌 Considerações Finais

Este projeto atende aos requisitos propostos, garantindo:

* Qualidade através de testes automatizados
* Organização do código em camadas
* Validação contínua via CI/CD

---

## 👨‍💻 Autores

Guilherme de Siqueira Abreu
Samuel Pereira Dias
Guilherme Leão Teles