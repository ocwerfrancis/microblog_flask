# Grace Community Church Website (Flask + Bootstrap)

A modern, responsive church website built with **Flask**, **Python**, **HTML5**, **Bootstrap 5**, and a small amount of custom CSS.

## Features

- Bootstrap-based responsive layout and components
- Hero section with call-to-action buttons
- About section and scripture highlight
- Sunday and daily mass schedules rendered from Flask data
- Thursday program section (Mass, Adoration, Benediction, Catechesis)
- Ministry cards rendered from Flask data
- Plan-a-visit section with a simple form layout
- Mobile-friendly navigation using Bootstrap navbar collapse

## Project structure

```text
microblog_flask/
├── app.py
├── requirements.txt
├── static/
│   ├── css/style.css
│   └── js/main.js
└── templates/
    ├── base.html
    └── index.html
```

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
python app.py
```

4. Open your browser at `http://127.0.0.1:5000`.

## Customize

- Update church name/contact details in `templates/base.html`.
- Update schedule/ministry cards in `app.py`.
- Adjust styles in `static/css/style.css`.
