// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById('toggle-college').addEventListener('change', function () {
    let collegeDiv = document.querySelector('#elementCollege');
    var docDIv = document.querySelector('#elementDoc');
    collegeDiv.style.display = this.checked ? 'block' : 'none';
    docDIv.style.display = this.checked ? 'block' : 'none';
  });
});
