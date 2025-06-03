#Listing 10_34: Handler to send message
  const handleMessageSubmit = (e) => {
    e.preventDefault();
    if (chatSocket && chatSocket.readyState === WebSocket.OPEN) {
      chatSocket.send(JSON.stringify({ message: `${name}: ${message}` }));
      setMessage('');
    } else {
      console.error('WebSocket is not open. Cannot send message.');
    }
  };
