/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./main_app/templates/*.html', './main_app/templates/**/*.html', './main_app/templates/pages/**/*.html', './main_app/templates/components/**/*.html'],
  theme: {
    extend: {
      colors: {
        bg: '#1a1a1a',
        prim: '#b3fed5',
        bright: '#f0f0f0',
        bright_grey: '#d0d0d0',
      },
    },
  },
  plugins: [],
}