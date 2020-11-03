import './App.css';
import StepBtn from './StepBtn';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

function App() {
  return (
    <div className="App">
      <Container>
        <Row className="d-flex justify-content-center align-items-center mt-5">
          <StepBtn/>
        </Row>
      </Container>
    </div>
  );
}

export default App;