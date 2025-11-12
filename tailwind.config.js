/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/templates/core/*.{js,jsx,ts,tsx,html}"],
  theme: {
    extend: {
      keyframes: {
        float: {
          '0%': { transform: 'translateY(30)' },
          '100%': { transform: 'translateY(0px)' },
        },
      },
      animation: {
        float: 'float 3s ease-in-out'
      },
    },
  },
  plugins: [],
}

