#Listing 10_19: input element in React
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Flight Number:</label>
                    <input
                        type="text"
                        name="flight_number"
                        value={ticket.flight_number}
                        onChange={handleChange}
                        required
                    />
                </div>
