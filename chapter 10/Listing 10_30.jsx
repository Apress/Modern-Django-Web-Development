#Listing 10_30: BookList component
import { useQuery} from "@apollo/client";
function BookList() {
    const { loading, error, data } = useQuery(GET_BOOKS);

  console.log("Query Response:", { loading, error, data });

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;  
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;
  
    return (
        <ul>
          {data.allBooks.map((book) => (
            <li key={book.id}>
              {book.title} by {book.author}
            </li>
          ))}
        </ul>
      );
  }

export default BookList;
