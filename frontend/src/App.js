import './App.css';
import Header from './components/Header'

import Clock from './components/Clock';
import DisplayArea from './components/DisplayArea'


function App() {
  return (
    <div className="App">
      <div className='grid-item'><Header/></div>
      <div className='grid-item'><Clock /></div>
        <div className='grid-item'><DisplayArea /></div>
          
    </div>
  );
}

export default App;
