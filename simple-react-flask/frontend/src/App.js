import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <h1>Personen Tabelle</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Alter</th>
            <th>Beruf</th>
          </tr>
        </thead>
        <tbody>
          {data.map(person => (
            <tr key={person.id}>
              <td>{person.id}</td>
              <td>{person.name}</td>
              <td>{person.alter}</td>
              <td>{person.beruf}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
