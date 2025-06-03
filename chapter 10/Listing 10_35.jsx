#Listing 10_35: Handler to receive messages
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'chat') {
        setMessages((prevMessages) => [...prevMessages, data.message]);
      }
    };
