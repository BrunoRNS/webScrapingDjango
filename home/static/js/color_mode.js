function chooseColorMode() {

  const root = document.documentElement;

  if (root.classList.contains("dark_mode")) {

    root.classList.remove("dark_mode");
    root.classList.add("white_mode");

    localStorage.setItem("color-mode", "white_mode");

  } else {

    root.classList.remove("white_mode");
    root.classList.add("dark_mode");

    localStorage.setItem("color-mode", "dark_mode");

  }

}

window.addEventListener("DOMContentLoaded", () => {

  const savedMode = localStorage.getItem("color-mode");
  const root = document.documentElement;

  if (savedMode === "dark_mode" || savedMode === "white_mode") {

    root.classList.add(savedMode);

  } else {

    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    root.classList.add(prefersDark ? "dark_mode" : "white_mode");

  }
  
});