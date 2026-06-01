document.querySelectorAll(".delete-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    const confirmed = window.confirm("Deseja excluir esta hospedagem?");

    if (!confirmed) {
      event.preventDefault();
    }
  });
});
