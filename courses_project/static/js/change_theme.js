document.addEventListener("DOMContentLoaded", function () {

    const html = document.documentElement;
    const button = document.getElementById("themeToggle");

    // 1. Загружаем сохранённую тему
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }

    // 2. Переключение по кнопке
    button.addEventListener("click", function () {

        const currentTheme = html.getAttribute("data-bs-theme");

        const newTheme = currentTheme === "dark" ? "light" : "dark";

        html.setAttribute("data-bs-theme", newTheme);

        localStorage.setItem("theme", newTheme);

        button.textContent = newTheme === "dark" ? "☀️" : "🌙";
    });

});