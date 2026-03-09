/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            'blockquote p:first-of-type::before': { content: 'none' },
            'blockquote p:last-of-type::after': { content: 'none' },
            'blockquote p': { marginTop: '0', marginBottom: '0' },
          },
        },
      },
      colors: {
        primary: '#f59f0a',
        'navy-custom': '#162d60',
        'background-light': '#f8f7f5',
        'background-dark': '#221c10',
      },
      fontFamily: {
        display: ['"Poppins"', 'sans-serif'],
        sans: ['"Work Sans"', 'sans-serif'],
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
