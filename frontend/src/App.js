
import React, { useState, useEffect } from 'react';

const API_BASE = 'http://127.0.0.1:8000';

function App() {
  const [task, setTask] = useState('');
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const response = await fetch(`${API_BASE}/tasks`);
      const data = await response.json();
      setHistory(data);
    } catch (error) {
      console.log(error);
    }
  };

  const submitTask = async (e) => {
    e.preventDefault();

    if (!task.trim()) {
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_BASE}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task: task
        })
      });

      const data = await response.json();

      setResult(data);
      setTask('');

      loadHistory();
    } catch (error) {
      alert('Backend server not running');
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        padding: '20px',
        fontFamily: 'Arial',
        maxWidth: '800px',
        margin: '0 auto'
      }}
    >
      <h1>Simple Agent Task App</h1>

      <form onSubmit={submitTask}>
        <textarea
          rows='4'
          placeholder='Enter task here'
          value={task}
          onChange={(e) => setTask(e.target.value)}
          style={{
            width: '100%',
            padding: '10px',
            marginBottom: '10px'
          }}
        />

        <button
          type='submit'
          style={{
            padding: '10px 20px'
          }}
        >
          {loading ? 'Processing...' : 'Submit Task'}
        </button>
      </form>

      <div style={{ marginTop: '20px' }}>
        <h3>Example Tasks</h3>

        <ul>
          <li>uppercase hello world</li>
          <li>lowercase HELLO</li>
          <li>5 + 7 * 2</li>
          <li>weather in Toronto</li>
        </ul>
      </div>

      {result && (
        <div
          style={{
            border: '1px solid gray',
            padding: '15px',
            marginTop: '20px'
          }}
        >
          <h2>Result</h2>

          <p>
            <strong>Tool Used:</strong> {result.tool_used}
          </p>

          <p>
            <strong>Output:</strong> {result.output_text}
          </p>

          <h3>Execution Steps</h3>

          <ul>
            {result.steps &&
              result.steps.map((step, index) => (
                <li key={index}>{step}</li>
              ))}
          </ul>
        </div>
      )}

      <div style={{ marginTop: '30px' }}>
        <h2>Task History</h2>

        {history.length === 0 && <p>No history found</p>}

        {history.map((item) => (
          <div
            key={item.id}
            style={{
              border: '1px solid lightgray',
              padding: '10px',
              marginBottom: '10px'
            }}
          >
            <p>
              <strong>Task:</strong> {item.input_text}
            </p>

            <p>
              <strong>Tool:</strong> {item.tool_used}
            </p>

            <p>
              <strong>Result:</strong> {item.output_text}
            </p>

            <details>
              <summary>View Steps</summary>

              <ul>
                {item.steps &&
                  item.steps.map((step, index) => (
                    <li key={index}>{step}</li>
                  ))}
              </ul>
            </details>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;