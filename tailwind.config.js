module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/**/*.{css, js}",
        "./apps/**/*.py",
        "./venv/lib/site-packages/crispy_tailwind/**/*.{css, js, py}"
    ],
    theme: {
        extend: {
            container: {
                center: true,
            }
        },
    },
    plugins: [],
}

