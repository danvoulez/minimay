/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      colors: {
        primary: "#0e0e10",
        secondary: "#1e1e22",
        accent: "#ff4181",
        success: "#22c55e",
        warning: "#facc15",
        error: "#ef4444"
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"]
      },
      borderRadius: {
        'md': "8px",
        'lg': "16px"
      }
    }
  },
  plugins: []
}