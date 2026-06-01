document.querySelectorAll(".delete-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    const confirmed = window.confirm("Deseja excluir esta avaliacao?");

    if (!confirmed) {
      event.preventDefault();
    }
  });
});
