from behave import given, when, then
import json
from app import app
from service import repository


@given('que existe uma disciplina cadastrada com título "{titulo}"')
def step_given_disciplina_existente(context, titulo):
    disciplina = repository.criar(
        titulo=titulo,
        data_inicio="2026-08-01",
        data_termino="2026-12-15",
        numero_vagas=30,
        eh_verao=False
    )
    context.disciplina_id = disciplina.id
    context.disciplina_titulo = disciplina.titulo


@when('eu criar uma disciplina com título "{titulo}"')
def step_when_criar_disciplina(context, titulo):
    client = app.test_client()
    context.response = client.post(
        "/disciplinas",
        json={
            "titulo": titulo,
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-15",
            "numero_vagas": 30,
            "eh_verao": False
        }
    )


@when('eu criar uma disciplina inválida')
def step_when_criar_disciplina_invalida(context):
    client = app.test_client()
    context.response = client.post(
        "/disciplinas",
        json={
            "titulo": "",
            "data_inicio": "2026-12-20",
            "data_termino": "2026-08-01",
            "numero_vagas": 0,
            "eh_verao": "sim"
        }
    )


@when('eu listar as disciplinas')
def step_when_listar(context):
    client = app.test_client()
    context.response = client.get("/disciplinas")


@when('eu buscar a disciplina cadastrada')
def step_when_buscar(context):
    client = app.test_client()
    context.response = client.get(f"/disciplinas/{context.disciplina_id}")


@when('eu atualizar a disciplina para o título "{titulo}"')
def step_when_atualizar(context, titulo):
    client = app.test_client()
    context.response = client.put(
        f"/disciplinas/{context.disciplina_id}",
        json={
            "titulo": titulo,
            "data_inicio": "2026-08-01",
            "data_termino": "2026-12-20",
            "numero_vagas": 35,
            "eh_verao": True
        }
    )


@when('eu excluir a disciplina cadastrada')
def step_when_excluir(context):
    client = app.test_client()
    context.response = client.delete(f"/disciplinas/{context.disciplina_id}")


@then('o status da resposta deve ser {status:d}')
def step_then_status(context, status):
    assert context.response.status_code == status


@then('a resposta deve conter o título "{titulo}"')
def step_then_titulo(context, titulo):
    data = context.response.get_json()
    assert data["titulo"] == titulo


@then('a resposta deve conter erros')
def step_then_erros(context):
    data = context.response.get_json()
    assert "erros" in data
    assert len(data["erros"]) > 0


@then('a lista deve conter {quantidade:d} item')
def step_then_lista(context, quantidade):
    data = context.response.get_json()
    assert len(data) == quantidade


@then('a resposta deve conter o título da disciplina cadastrada')
def step_then_titulo_cadastrado(context):
    data = context.response.get_json()
    assert data["titulo"] == context.disciplina_titulo


@then('ao buscar a disciplina excluída o status deve ser {status:d}')
def step_then_busca_excluida(context, status):
    client = app.test_client()
    response = client.get(f"/disciplinas/{context.disciplina_id}")
    assert response.status_code == status