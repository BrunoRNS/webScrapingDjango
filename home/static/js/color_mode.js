function chooseColorMode() {
  
  const root = document.documentElement;

  if (root.classList.contains("dark_mode")) {

      root.classList.remove("dark_mode");
      root.classList.add("white_mode");

  } else {

      root.classList.remove("white_mode");
      root.classList.add("dark_mode");

  }

}

window.addEventListener("DOMContentLoaded", () => {

    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    document.documentElement.classList.add(prefersDark ? "dark_mode" : "white_mode");


});