
# Wichtige React-Konventionen

Bei der Arbeit mit React gibt es bestimmte **Best Practices** und **Konventionen**, die helfen, sauberen, wartbaren und performanten Code zu schreiben. Hier sind die wichtigsten React-Konventionen:

---

## **1. Dateistruktur und Benennung**
- **Komponenten-Dateien**:
  - Nutze **PascalCase** für Komponenten (z. B. `MyComponent.js`).
  - Eine Komponente pro Datei.
- **Ordnerstruktur**:
  - Organisiere nach Funktionalität, z. B.:
    ```
    src/
      components/
      pages/
      hooks/
      utils/
    ```
  - Gruppiere ähnliche Dateien in Ordnern (z. B. Komponenten mit ihren Styles oder Tests).

---

## **2. Komponenten-Typen**
- **Funktionale Komponenten** bevorzugen:
  - Verwende funktionale Komponenten anstelle von Klassenkomponenten, da sie moderner, leichter und mit Hooks besser sind.
  
  ```jsx
  function MyComponent() {
    return <div>Hello, React!</div>;
  }
  ```

- **Presentational vs. Container Components**:
  - **Presentational Components**: Nur für UI, kein State.
  - **Container Components**: Handhaben Logik und State.

---

## **3. State und Props**
- **Props sind unveränderlich**:
  - Ändere niemals Props direkt. Nutze den State oder Callback-Funktionen zur Datenaktualisierung.
  
- **State minimal halten**:
  - Speichere nur notwendige Daten im State. Berechne abgeleitete Daten direkt in der Komponente.

- **Lifting State Up**:
  - Teile den State, indem du ihn an die nächsthöhere Komponente hebst, die beide Komponenten gemeinsam haben.

---

## **4. Hooks**
- **Hook-Konventionen**:
  - Benenne eigene Hooks mit `use`, z. B. `useFetchData`.
  - Nutze Hooks nur in funktionalen Komponenten.
  
- **React-Hook-Regeln**:
  1. Hooks dürfen nur im obersten Level der Komponente verwendet werden (nicht in Schleifen, Bedingungen oder verschachtelten Funktionen).
  2. Nur in React-Komponenten oder anderen benutzerdefinierten Hooks verwenden.

---

## **5. JSX Konventionen**
- **Self-Closing Tags**:
  - Nutze Self-Closing für leere Tags:
    ```jsx
    <img src="logo.png" />
    ```

- **Einfache und lesbare JSX**:
  - Teile komplexes JSX in kleinere Komponenten auf.

- **Props weitergeben**:
  - Nutze den Spread-Operator nur bewusst:
    ```jsx
    const props = { id: 1, name: 'React' };
    <MyComponent {...props} />;
    ```

- **CSS-Klassen**:
  - Verwende `className` statt `class`:
    ```jsx
    <div className="my-class"></div>
    ```

---

## **6. Event-Handling**
- **Arrow-Funktionen verwenden**:
  - Vermeide Bindings in `render`:
    ```jsx
    <button onClick={() => handleClick()}>Click Me</button>
    ```

- **Passende Namenskonvention**:
  - Benenne Event-Handler mit `handle` oder `on`, z. B. `handleSubmit` oder `onClick`.

---

## **7. Modularisierung und Wiederverwendbarkeit**
- Schreibe **kleine, wiederverwendbare Komponenten**.
- Nutze **Props** für Konfiguration und Anpassung.

---

## **8. Zustand verwalten**
- **Globaler Zustand**:
  - Nutze `Context API` oder Bibliotheken wie **Redux**, **Recoil**, oder **Zustand** für globalen State.
  
- **Lokaler Zustand**:
  - Bevorzuge `useState` und `useReducer` für lokales State-Management.

---

## **9. Fehler und Performance**
- **Prop-Typen validieren**:
  - Nutze **PropTypes** oder **TypeScript**:
    ```jsx
    import PropTypes from 'prop-types';

    MyComponent.propTypes = {
      name: PropTypes.string.isRequired,
    };
    ```

- **Key für Listen**:
  - Nutze eindeutige Keys in Listen:
    ```jsx
    {items.map(item => <li key={item.id}>{item.name}</li>)}
    ```

- **Memoisierung**:
  - Nutze `React.memo` und `useMemo` für Performance-Optimierung bei teuren Berechnungen.

---

## **10. Styling**
- Wähle eine konsistente Methode:
  - **CSS-Module**, **Styled-Components**, oder **TailwindCSS**.
  - Vermeide Inline-Stile außer bei einfachen Ausnahmen.

---

## **11. Versionierung und Abhängigkeiten**
- Halte React und seine Abhängigkeiten stets aktuell.
- Überprüfe Breaking Changes bei Versionswechseln.

---

## **12. Tests**
- Schreibe Tests für Komponenten:
  - **Unit-Tests**: Teste einzelne Komponenten mit **Jest** oder **React Testing Library**.
  - **End-to-End-Tests**: Nutze **Cypress** oder **Playwright**.

---

## **Zusammenfassung**
- **Strukturierter Code**: Organisiere Dateien und Komponenten sinnvoll.
- **Konsistente Namenskonventionen**: Verwende PascalCase, camelCase usw.
- **Hooks und State effizient nutzen**: Vermeide unnötigen globalen State.
- **JSX und Styling optimieren**: Halte JSX einfach und modular.
- **Performance-Optimierungen**: Nutze Memoisierung und eindeutige Keys.

Diese Konventionen helfen dir dabei, saubere und skalierbare React-Anwendungen zu entwickeln. 😊
