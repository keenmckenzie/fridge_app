import React, { Component } from 'react';
import './App.css';
import FridgeApp from './component/FridgeApp';

class App extends Component {
  render() {
    return (
      <div className="container">
        <FridgeApp />
      </div>
    );
  }
}

export default App;