import React, { useState } from "react";
import axios from "axios";

const Validation = () => {
  const [tableName, setTableName] = useState("");
  const [results, setResults] = useState([]);

  const handleValidate = async () => {
    const response = await axios.get(`http://localhost:8000/validate/${tableName}`);
    setResults(response.data.results);
  };

  return (
    <div>
      <h2>Data Validation</h2>
      <input
        type="text"
        value={tableName}
        onChange={(e) => setTableName(e.target.value)}
        placeholder="Enter table name"
      />
      <button onClick={handleValidate}>Validate</button>
      <ul>
        {results.map((result, index) => (
          <li key={index}>
            {result.check_name}: {result.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Validation;
