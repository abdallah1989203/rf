from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app)

# SQLite Datenbank (keine Installation erforderlich)
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Modell für die Tabelle
class Person(Base):
    __tablename__ = 'personen'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    alter = Column(Integer)
    beruf = Column(String(100))

# Datenbank und Tabelle erstellen
Base.metadata.create_all(engine)

# Session erstellen
Session = sessionmaker(bind=engine)

@app.route('/api/data', methods=['GET'])
def get_data():
    session = Session()
    try:
        # Überprüfen, ob Daten vorhanden sind
        count = session.query(Person).count()
        if count == 0:
            # Beispieldaten einfügen
            example_data = [
                Person(name="John Doe", alter=30, beruf="Entwickler"),
                Person(name="Jane Smith", alter=25, beruf="Designer")
            ]
            session.add_all(example_data)
            session.commit()
        
        # Daten abrufen
        personen = session.query(Person).all()
        data = [{
            'id': person.id,
            'name': person.name,
            'alter': person.alter,
            'beruf': person.beruf
        } for person in personen]
        return jsonify(data)
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
