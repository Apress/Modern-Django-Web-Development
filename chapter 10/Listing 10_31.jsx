#Listing 10_31: App.jsx for Apollo app
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

export default App
