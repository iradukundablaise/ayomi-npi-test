import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const calculate = () => {
    const exprEncoded = encodeURIComponent(expression);
    
    setError('');
    setResult('');

    fetch(`http://localhost:8000/evaluate?expr=${exprEncoded}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.results){
        setResult(data.results);
      }else if (data.error){
        setError(data.error);
      }
    })
    .catch((error) => {
      setError("Erreur lors de l'évaluation de l'expression");
    });
  }

  return (
    <div className='my-10'>
      <h1 className='text-3xl text-center'>Calculatrice en notation polonaise inverse</h1>
      <div className='w-80 bg-gray-100 p-4 mx-auto mt-10 rounded'>
        <label className='block mb-4 font-bold'>Expression en NPI</label>
        <input 
          type='text' 
          className='border border-gray-300 p-2 w-full mb-4'
          placeholder='expresssion en NPI' 
          onChange={ (e) => {
            setExpression(e.target.value)
          }} 
        />

        {
        result && 
        <div className='bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative' role='alert'>
          <strong className='font-bold'>Résultat: </strong>
          <span className='block sm:inline'>{result}</span>
        </div> 
        }

        {
        error &&
        <div className='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative' role='alert'>
          <strong className='font-bold'>Erreur: </strong>
          <span className='block sm:inline'>{error}</span>
        </div>
        }
        
        <button 
          className='bg-blue-500 text-white p-2 rounded mt-2'
          onClick={() => { calculate() }}
          >Evaluer</button>

        <a
          href='http://localhost:8000/export-csv'
          className='bg-green-500 text-white p-2 rounded mt-2'
          >Exporter les données en csv</a>
      </div>
    </div>
  );
}

export default App
