from anfitrioes.models import Anfitriao
from hospedes.models import Hospede


TIPO_ANFITRIAO = "anfitriao"
TIPO_HOSPEDE = "hospede"
TIPOS_LOGIN = {TIPO_ANFITRIAO, TIPO_HOSPEDE}


def email_do_usuario(usuario):
    return usuario.email or f"{usuario.username}@email.local"


def criar_hospede(usuario):
    return Hospede.objects.create(
        nome=usuario.username,
        email=email_do_usuario(usuario),
        telefone="Nao informado",
        documento=f"user-{usuario.id}",
        nacionalidade="Nao informada",
        data_nascimento="2000-01-01",
    )


def criar_anfitriao(usuario):
    return Anfitriao.objects.create(
        nome=usuario.username,
        email=email_do_usuario(usuario),
        telefone="Nao informado",
        documento=f"user-{usuario.id}",
        bio="",
    )


def perfil_por_tipo(usuario, tipo_login):
    email = email_do_usuario(usuario)

    if tipo_login == TIPO_ANFITRIAO:
        anfitriao = Anfitriao.objects.filter(email=email).first()
        if not anfitriao:
            anfitriao = criar_anfitriao(usuario)
        return {
            "tipo_login": TIPO_ANFITRIAO,
            "hospede_id": None,
            "anfitriao_id": anfitriao.id,
        }

    hospede = Hospede.objects.filter(email=email).first()
    if not hospede:
        hospede = criar_hospede(usuario)
    return {
        "tipo_login": TIPO_HOSPEDE,
        "hospede_id": hospede.id,
        "anfitriao_id": None,
    }


def perfil_login(usuario):
    email = email_do_usuario(usuario)
    anfitriao = Anfitriao.objects.filter(email=email).first()

    if anfitriao:
        return {
            "tipo_login": TIPO_ANFITRIAO,
            "hospede_id": None,
            "anfitriao_id": anfitriao.id,
        }

    hospede = Hospede.objects.filter(email=email).first()

    if hospede:
        return {
            "tipo_login": TIPO_HOSPEDE,
            "hospede_id": hospede.id,
            "anfitriao_id": None,
        }

    return perfil_por_tipo(usuario, TIPO_HOSPEDE)
