#Listing 10_33: chat interface
          <h1>Welcome, {name}!</h1>
          <form onSubmit={handleMessageSubmit}>
            <input
              type="text"
              placeholder="Type your message"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              required
            />
            <nbsp>  </nbsp>
            <button type="submit">Send</button>
          </form>
