function atualizarCamposPerfil() {
  const tipo = document.querySelector("#id_tipo_usuario")?.value;
  const nacionalidade = document.querySelector(".field-nacionalidade");
  const bio = document.querySelector(".field-bio");

  if (nacionalidade) {
    nacionalidade.style.display = tipo === "hospede" ? "grid" : "none";
  }

  if (bio) {
    bio.style.display = tipo === "anfitriao" ? "grid" : "none";
  }
}

document
  .querySelector("#id_tipo_usuario")
  ?.addEventListener("change", atualizarCamposPerfil);

atualizarCamposPerfil();
