#Listing 10_6: Axios object
import axios from 'axios';

const API = axios.create({
    baseURL: 'https://example.com/api/'
});
