#Listing 10_16: routing in App.jsx
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import TicketList from './TicketList';
import AddTicket from './AddTicket';
import Home from './Home';
<Router>
              <div>  
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/list" element={<TicketList />} />  
                    <Route path="/add" element={<AddTicket />} />
            </Routes>
        </div>
        </Router>
