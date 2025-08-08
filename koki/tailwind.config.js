/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      colors: {
        'jarvis-cyan': '#19E3FF',
        'jarvis-blue': '#0BC2E6', 
        'jarvis-dim': '#0AAFD1',
        'jarvis-bg': '#051824',
        'jarvis-light': '#CFF8FF',
      },
      animation: {
        'jarvis-pulse': 'jarvis-pulse 2.2s ease-in-out infinite',
      },
      keyframes: {
        'jarvis-pulse': {
          '0%, 100%': { opacity: '0.25' },
          '50%': { opacity: '0.9' },
        }
      }
    },
  },
  plugins: [],
}
