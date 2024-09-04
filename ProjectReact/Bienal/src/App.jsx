import { ROUTES } from "./utils/const.js";
import { Router } from "./components/Router.jsx";

export default function App(){
    
    return(
        <main>
            <Router routes={ROUTES}/>
        </main>
        )
}