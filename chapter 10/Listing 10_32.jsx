#Listing 10_32: chat app login screen
        <form onSubmit={handleNameSubmit}>
          <h1>Welcome to the Chat</h1>
         
          <input
            type="text"
            placeholder="Enter your name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        
        <nbsp>  </nbsp>
          <button type="submit">Join</button>
        </form>
