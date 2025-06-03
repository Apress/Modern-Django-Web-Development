#Listing 10_21: ApolloClient object
import { ApolloClient, InMemoryCache } from '@apollo/client';
const client = new ApolloClient({
  uri: "GraphQL API endpoint",   
  cache: new InMemoryCache(),         
});
