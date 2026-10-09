const pass = document.getElementById("password");
const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
    if (pass.value.length < 9) {
        e.preventDefault();
        alert("La contraseña debe tener al menos 9 caracteres.");
    }
});