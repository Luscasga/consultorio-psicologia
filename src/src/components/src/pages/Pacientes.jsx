import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Pacientes = () => {
  const [pacientes, setPacientes] = useState([]);

  useEffect(() => {
    api.get('/pacientes').then((response) => {
      setPacientes(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Pacientes</h1>
      <ul>
        {pacientes.map((paciente) => (
          <li key={paciente.id}>{paciente.nome} - {paciente.email}</li>
        ))}
      </ul>
    </div>
  );
};

export default Pacientes;
