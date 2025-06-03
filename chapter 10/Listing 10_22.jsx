#Listing 10_22: ApolloProvider component
import { ApolloProvider } from "@apollo/client";
function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <h1>React with Django GraphQL</h1>
        <BookList />
      </div>
    </ApolloProvider>
  );
}
