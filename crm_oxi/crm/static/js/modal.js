document.addEventListener("DOMContentLoaded", function () {
  const myModal = document.getElementById("taskModal");
  const myInput = document.getElementById("myInput");

  myModal.addEventListener("shown.bs.modal", () => {
    if (myInput) {
      myInput.focus();
    }
  });
});