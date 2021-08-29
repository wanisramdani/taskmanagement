import './home.css';
import Navbar from '../navbar/navbar';
import { BrowserRouter as Router,Route, Switch } from 'react-router-dom';

function App() {

  return (
    <Router>
      <div className="container">
        <Navbar/>
        <Switch>
          <Route exact path='/'>
            
          </Route>
          <Route path='clients'>

          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
