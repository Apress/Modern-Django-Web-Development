#Listing 10_18: ticketList.jsx
function TicketList() {
  const [userData, setData] = useState([]);

  useEffect(() => {
    API.get("tickets/")
      .then((response) => {
        console.log(response.data); // Check the structure of the data
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div>
      <h2>Ticket List</h2>
      {userData.map((item, index) => (
        <div key={index} style={{border: "1px solid", margin: "10px", padding: "10px"}}>
          <p><b>Name:</b> {item.passenger_name} <b>Flight No:</b> {item.flight_number} 
          <b>Seat No:</b> {item.seat_number}</p>
        </div>
      ))}
    </div>
  );
}
