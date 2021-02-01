import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

const pessoas_list = [
  {
    "nome": "pessoa 1",
    "cpf": "12345678901",
    "salario": "100.00",
    "enderecos": []
  },
  {
      "nome": "pessoa 2",
      "cpf": "12345678902",
      "salario": "200.00",
      "enderecos": []
  },
  {
      "nome": "pessoa 3",
      "cpf": "12345678903",
      "salario": "300.00",
      "enderecos": []
  }
]

class App extends Component {
  state = {
    pessoas: []
  }

  async componentDidMount(){
    try{
      const res = await fetch('http://localhost:8000/api/pessoas/');
      const pessoas = await res.json();
      this.setState({
        pessoas
      });
    } catch(e){
      console.log(e);
    }
  }

  render(){
    return(
      <div>
        {this.state.pessoas.map(item =>
          <div>
            <h1>{item.nome}</h1>
            <h2>{item.cpf}</h2>
            <h3>{item.salario}</h3>
          </div>
        )}
      </div>
    );
  }
}

export default App;


/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Aprenda React. Aprendeu?
        </a>
      </header>
    </div>
  );
}

export default App;
*/