document.querySelectorAll(".delete-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    const confirmed = window.confirm("Deseja excluir este endereco?");

    if (!confirmed) {
      event.preventDefault();
    }
  });
});
