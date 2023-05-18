/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        Primary: {
          1: "#F6FCFF",
          2: "#F1FAF1",
          3: "#ECF5EC",
          4: "#E7F0E7",
          5: "#E2EBE2",
          6: "#DDE6DD",
        },
        Secondary: {
          1: "#FF8800",
          2: "#FAA200",
          3: "#F59E00",
          4: "#F09B00",
          5: "#EB9800",
          6: "#E69500",
        },
        Accent: {
          1: "#000000",
          2: "#2B2B2B",
          3: "#555555",
          4: "#808080",
          5: "#AAAAAA",
          6: "#CCCCCC",
        },
        CustomBlue: {
          1: "#EBF5FF",
          2: "#00203F",
          3: "#20486D",
        },
      },
      boxShadow: {
        NavBarboxShadow: "0px 2px 12px 0px #00203F29",
      },
    },
  },
  plugins: [],
};
