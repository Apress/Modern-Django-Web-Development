#Listing 10_29: GET_BOOKS query
import { gql } from "@apollo/client";
const GET_BOOKS = gql`
  query {
  allBooks {
    id
    title
    author
    publisher
    price
  }
}
`;
