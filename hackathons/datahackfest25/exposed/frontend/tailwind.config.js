/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
      colors: {
        background: {
          dark: "#181824",
          accent: "#23243a",
        },
        primary: {
          DEFAULT: "#fff",
          dark: "#181824",
        },
        accent: {
          pink: "#ec4899",
          purple: "#a855f7",
          blue: "#38bdf8",
        },
      },
      boxShadow: {
        card: "0 4px 32px 0 rgba(0,0,0,0.12)",
      },
      borderRadius: {
        xl: "1.25rem",
        '2xl': "2rem",
      },
      animation: {
        fadeIn: 'fadeIn 1s ease-in-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
      },
    },
  },
  plugins: [],
};
