---
layout: post
title: PPR
description: Final Check
type: issues 
comments: true
permalink: /navigation/arya_blog/PPR
---
# 1. List Creation

The list of messages is represented by the ul element with the ID messages. The code grabs this list element with document.getElementById("messages") and assigns it to the messageList variable.   


```python
const messageList = document.getElementById("messages");
```

# 2. List Processing

Each message is dynamically added as a new <li> element inside the message list. This creates a new list item and appends it to messageList.


```python
const newMessage = document.createElement("li");
newMessage.textContent = message;
messageList.appendChild(newMessage);

```

# 3. Function with Parameters (Sequencing, Selection, Iteration)

The function displayMessage(id, message) takes two parameters:
id: Unique identifier for the message.
message: The actual text content.


```python
function displayMessage(id, message) {
    const messageList = document.getElementById("messages");
    const newMessage = document.createElement("li");
    newMessage.textContent = message;
    newMessage.id = id; 
    messageList.appendChild(newMessage);
  }  
```

# Sequencing:
It first selects the message list.
Creates a new message element.
Assigns it an ID.
Appends it to the list.

# Selection (if-else Statement)

It checks if the message is a server message before assigning an id, if the message is from the server, it does not assign an ID>


```python
let isServer = message === "Server: Welcome to the chat!";
if (!isServer) {
  newMessage.id = id;
}
```

# Iteration (Looping through Messages)

The chat messages are displayed by appending each one dynamically. Each message is created and processed in a sequence.


```python
const messageText = document.createElement("span");
messageText.textContent = message;
newMessage.appendChild(messageText);
```

# Function Call

The function is executed whenever a new message is recieved. Calls displayMessage whenever a new chat message is received. Passes the id and message content as arguments.


```python
socket.on("chat_message", (data) => {
  displayMessage(data.id, `${data.user}: ${data.text}`);
});

```
