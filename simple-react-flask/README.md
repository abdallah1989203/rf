# Simple React-Flask App

Eine einfache Webanwendung zur Anzeige von Personendaten aus einer SQLite-Datenbank.

## Technologien

- Frontend: React
- Backend: Flask
- Datenbank: SQLite
- ORM: SQLAlchemy
- CORS: Flask-CORS

## Projektstruktur

```
simple-react-flask/
├── backend/
│   ├── app.py             # Flask Backend-Server
│   └── requirements.txt   # Python-Abhängigkeiten
└── frontend/
    ├── src/
    │   ├── App.js        # React-Hauptkomponente
    │   └── App.css       # Styling
    └── package.json      # Node.js-Abhängigkeiten
```

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
yarn install
yarn start
```

## Features

- Anzeige von Personendaten in einer formatierten Tabelle
- Automatische Datenbankinitialisierung
- Responsive Design
- REST-API-Endpunkt
- Cross-Origin Resource Sharing (CORS) aktiviert
