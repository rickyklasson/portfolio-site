/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./main_app/templates/*.html', './main_app/templates/**/*.html', './main_app/templates/pages/**/*.html', './main_app/templates/components/**/*.html', './main_app/templates/sections/**/*.html'],
  theme: {
    extend: {
      colors: {
        bg: '#121212',
        prim: '#b3fed5',
        bright: '#f0f0f0',
        bright_grey: '#d0d0d0',
      },
      keyframes: {
        bounce_left: {
          '0%, 100%': { transform: 'translateX(0px)' },
          '50%': { transform: 'translateX(-10px)' },
        },
      },
      animation: {
        'bounce-left': 'bounce_left 2s linear infinite',
      },
    },
  },
  plugins: [],
}