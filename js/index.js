const axios = require('axios');

const baseURL = 'http://127.0.0.1:5000';
const api = axios.create({
  baseURL,
});

api.get(`/bulas/amoxicilina`).then(response => {
  console.log(response.data);
});