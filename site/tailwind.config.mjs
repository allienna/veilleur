/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#f59f0a',
        'navy-custom': '#162d60',
        'background-light': '#f8f7f5',
        'background-dark': '#221c10',
      },
      fontFamily: {
        display: ['"Work Sans"', 'sans-serif'],
        sans: ['"Work Sans"', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
