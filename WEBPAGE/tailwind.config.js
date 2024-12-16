/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                "gruene-tanne": "#005538",
                "gruene-klee": "#008939",
                "gruene-grashalm": "#8ABD24",
                "gruene-sand": "#F5F1E9",
                "gruene-himmel": "#0BA1DD",
                "gruene-sonne": "#FFF17A"
            },
            fontFamily: {
                "gruene-text": ["GRUENE_TEXT", 'sans-serif'],
            }
        },
    },
    plugins: [],
}

