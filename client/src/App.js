import React, { useState, useEffect } from 'react';
import axios from 'axios';

const serverUrl = 'https://touchstoneserve.onrender.com';
// const serverUrl = 'http://127.0.0.1:8000';

const App = () => {
  const [form, setForm] = useState({ firstname: '', lastname: '', email: '', phone: '' });
  const [users, setUsers] = useState([]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post(`${serverUrl}/users`, form);
    fetchUsers();
    setForm({ firstname: '', lastname: '', email: '', phone: '' });
  };

  const fetchUsers = async () => {
    const res = await axios.get(`${serverUrl}/users`);
    setUsers(res.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>User Registration</h1>
      <form onSubmit={handleSubmit}>
        <input name="firstname" value={form.firstname} onChange={handleChange} placeholder="First Name" required /><br />
        <input name="lastname" value={form.lastname} onChange={handleChange} placeholder="Last Name" required /><br />
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" required /><br />
        <input name="phone" value={form.phone} onChange={handleChange} placeholder="Phone" required /><br />
        <button type="submit">Submit</button>
      </form>

      <h2>User List</h2>
      <ul>
        {users.map((u) => (
          <li key={u.id}>{u.firstname} {u.lastname} - {u.email}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;