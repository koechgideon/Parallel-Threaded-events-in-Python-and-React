import './App.css';
import Header from './components/Header'
import ReportDisplay from './components/ReportDisplay'
import Clock from './components/Clock';
import DisplayArea from './components/DisplayArea'


function App() {
  return (
    <div className="App">
      <div className='grid-item'><Header/></div>
      <div className='grid-item'><Clock /></div>
        <div className='grid-item'><DisplayArea /></div>
        <div className='grid-item'><ReportDisplay /></div>
          
    </div>
  );
}

export default App;
