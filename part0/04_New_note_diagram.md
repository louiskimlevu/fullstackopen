![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/louiskimlevu/fullstackopen/main/part0/04_new_note_diagram.puml)

```mermaid
sequenceDiagram
    actor user
    participant browser
    participant studies.cs.helsinki.fi server as server

    # User creates a notes in the browser
    #note over browser: 
    user ->> browser: submits form
    activate browser
    browser ->> server: sends form data
    server -->> browser: ok
    deactivate browser



    browser->>server: GET https://studies.cs.helsinki.fi/exampleapp/notes
    activate server
    server-->>browser: HTML document
    deactivate server

    browser->>server: GET https://studies.cs.helsinki.fi/exampleapp/main.css
    activate server
    server-->>browser: the css file
    deactivate server

    browser->>server: GET https://studies.cs.helsinki.fi/exampleapp/main.js
    activate server
    server-->>browser: the JavaScript file
    deactivate server

    Note right of browser: The browser starts executing the JavaScript code that fetches the JSON from the server

    browser->>server: GET https://studies.cs.helsinki.fi/exampleapp/data.json
    activate server
    server-->>browser: [{ "content": "HTML is easy", "date": "2023-1-1" }, ... ]
    deactivate server

    Note right of browser: The browser executes the callback function that renders the notes
```