#Listing 10_20: AddTicket component
const AddTicket = () => {
    const [ticket, setTicket] = useState({
        flight_number: '',
        passenger_name: '',
        departure_time: '',
        seat_number: '',
    });

    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    // Handle form input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setTicket({ ...ticket, [name]: value });
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        setSuccessMessage('');
        setErrorMessage('');

        axios.post('tickets/', ticket)
            .then((response) => {
                setSuccessMessage('Ticket added successfully!');
                setTicket({ flight_number: '', passenger_name: '', departure_time: '', seat_number: '' }); // Clear form
                console.log(response.data);
            })
            .catch((error) => {
                setErrorMessage('Failed to add ticket. Please try again.');
                console.error(error);
            });
    };

    return (
        <div>
            <h2>Book New Ticket</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    //input component for flight_number
                </div>
                <div>
                    //input component for passenger_name
                </div>
                <div>
                    //input component for departure_time
                </div>
                <div>
                    //input component for seat_number
                </div>
                <button type="submit">Submit</button>
            </form>
            {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
        </div>
    );
};

export default AddTicket;
