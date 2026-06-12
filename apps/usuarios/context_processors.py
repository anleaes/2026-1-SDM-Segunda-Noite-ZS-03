def perfil_template(request):
    tipo_usuario = request.session.get("tipo_usuario")

    return {
        "tipo_usuario": tipo_usuario,
        "is_hospede": tipo_usuario == "hospede",
        "is_anfitriao": tipo_usuario == "anfitriao",
    }
