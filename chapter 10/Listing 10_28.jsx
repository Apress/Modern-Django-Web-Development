#Listing 10_28: Root component for Apollo app
import { ApolloClient, InMemoryCache, ApolloProvider } from "@apollo/client";


import BookList from "./BookList";

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/", 
  cache: new InMemoryCache(),
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <h1>React with Django GraphQL</h1>
      </div>
    </ApolloProvider>
  );
}

export default App
