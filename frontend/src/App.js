import './App.css';
import InitPage from "./pages/InitPage";
import shishka from "./images/ShishkaClassificator.svg"
import image1 from "./images/image1.svg"
import image2 from "./images/image2.svg"
import image3 from "./images/image3.svg"


function App() {
    return (
        <div className="App">
            <img style={{width: "400px", marginTop: "80px"}} src={shishka}/>
            <InitPage/>
            <footer className="App-footer">
                <img className={"image"} src={image1}/>
                <img className={"image"} src={image2}/>
                <img className={"image"} src={image3}/>
            </footer>
        </div>
    );
}

export default App;
