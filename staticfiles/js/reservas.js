document.querySelectorAll(".delete-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    const confirmed = window.confirm("Deseja excluir esta reserva?");

    if (!confirmed) {
      event.preventDefault();
    }
  });
});
