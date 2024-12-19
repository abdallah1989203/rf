# React Conventions Guide

## 1. Komponenten-Namensgebung
```jsx
// RICHTIG: PascalCase für Komponenten
function UserProfile() { }
const HeaderComponent = () => { }

// FALSCH: camelCase
function userProfile() { }
```

## 2. Props-Namensgebung
```jsx
// RICHTIG: camelCase für Props
<UserProfile userName="Max" userAge={25} />

// FALSCH: andere Schreibweisen
<UserProfile UserName="Max" user_age={25} />
```

## 3. Event Handler Benennung
```jsx
// RICHTIG: handle + Event
const handleClick = () => { }
const handleSubmit = () => { }

// JSX
<button onClick={handleClick}>Klick mich</button>
```

## 4. State Benennung und Updates
```jsx
// RICHTIG: beschreibende Namen und setter mit "set" Prefix
const [isLoading, setIsLoading] = useState(false);
const [userList, setUserList] = useState([]);

// FALSCH
const [l, setL] = useState(false);
```

## 5. Komponenten-Struktur
```jsx
// RICHTIG: Logische Gruppierung und Reihenfolge
function UserProfile({ name, age }) {
  // 1. State
  const [isEditing, setIsEditing] = useState(false);
  
  // 2. Effects
  useEffect(() => {}, []);
  
  // 3. Handler Functions
  const handleEdit = () => {};
  
  // 4. Render
  return (
    <div>
      {/* JSX */}
    </div>
  );
}
```

## 6. Destrukturierung
```jsx
// RICHTIG: Props destrukturieren
function UserCard({ name, age, address }) {
  return <div>{name}</div>;
}

// FALSCH
function UserCard(props) {
  return <div>{props.name}</div>;
}
```

## 7. Bedingte Renderung
```jsx
// RICHTIG: Ternärer Operator für einfache Bedingungen
{isLoggedIn ? <UserProfile /> : <LoginForm />}

// RICHTIG: && für einfache Bedingungen
{isLoading && <Spinner />}

// FALSCH: Komplexe Logik im JSX
{isLoggedIn && isAdmin && hasPermission ? <AdminPanel /> : null}
```

## 8. Key Prop bei Listen
```jsx
// RICHTIG: Eindeutige Keys
{users.map(user => (
  <UserItem key={user.id} user={user} />
))}

// FALSCH: Index als Key
{users.map((user, index) => (
  <UserItem key={index} user={user} />
))}
```

## 9. Prop Types
```jsx
import PropTypes from 'prop-types';

function User({ name, age }) {
  return <div>{name} ist {age} Jahre alt</div>;
}

User.propTypes = {
  name: PropTypes.string.required,
  age: PropTypes.number
};
```

## 10. Custom Hooks
```jsx
// RICHTIG: "use" Prefix für Custom Hooks
const useUserData = () => {
  const [user, setUser] = useState(null);
  return { user, setUser };
};

// FALSCH: ohne "use" Prefix
const getUserData = () => { };
```

## 11. Dateiorganisation
```
src/
  components/
    common/
    features/
  hooks/
  utils/
  services/
  assets/
```

## 12. Imports Ordnung
```jsx
// 1. React und externe Bibliotheken
import React, { useState } from 'react';
import axios from 'axios';

// 2. Components
import Header from './components/Header';

// 3. Hooks, Utils
import useAuth from './hooks/useAuth';
import { formatDate } from './utils';

// 4. Styles, Assets
import './styles.css';
import logo from './assets/logo.png';
```

## Vorteile dieser Conventions
- Konsistenter Code
- Verbesserte Lesbarkeit
- Erhöhte Wartbarkeit
- Erleichterte Teamarbeit
- Fehlerprävention

