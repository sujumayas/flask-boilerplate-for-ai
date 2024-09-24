// frontend/src/services/api.js
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:5000/api';

export const getUsers = () => axios.get(`${API_BASE_URL}/users`);
export const getUser = (id) => axios.get(`${API_BASE_URL}/users/${id}`);
export const createUser = (user) => axios.post(`${API_BASE_URL}/users`, user);
export const deleteUser = (id) => axios.delete(`${API_BASE_URL}/users/${id}`);

// Similarly, add services for other entities like Products
