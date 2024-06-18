/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html', './**/*.js'],
  theme: {
    extend: {
      screens: {
        sm: '640px',
        'lg-md': '992px',
      },
    },
  },
  plugins: [],
};
