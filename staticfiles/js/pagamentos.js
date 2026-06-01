document.querySelectorAll(".delete-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    const confirmed = window.confirm("Deseja excluir este pagamento?");

    if (!confirmed) {
      event.preventDefault();
    }
  });
});
