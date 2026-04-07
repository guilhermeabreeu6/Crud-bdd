from service import repository


def before_scenario(context, scenario):
    repository.resetar()