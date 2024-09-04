import { ROUTES } from "./utils/const.js";
import { Router } from "./components/Router.jsx";
import Page404 from "./pages/404.jsx";

export default function App(){
    
    return(
        <main>
            <Router routes={ROUTES} defaultComponent={Page404}/>
        </main>
        )
}