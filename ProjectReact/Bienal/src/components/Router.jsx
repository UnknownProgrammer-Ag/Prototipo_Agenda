import { useEffect, useState } from "react"
import { EVENTS } from "../utils/const"

export function Router({routes = [], defaultComponent: DefaultComponet = () => <h1><b>ERROR 404</b></h1>}){
    const [currentPath, setCurrentPath] = useState(window.location.pathname)
    
    useEffect(() =>{
        const onLocationChange = () =>{
            setCurrentPath(window.location.pathname)
        }
        
        window.addEventListener(EVENTS.PUSHSTATE, onLocationChange)
        window.addEventListener(EVENTS.POPSTATE, onLocationChange)

        return() => {
            window.removeEventListener(EVENTS.PUSHSTATE, onLocationChange)
            window.removeEventListener(EVENTS.POPSTATE, onLocationChange)
        }

    },[])

    const Page = routes.find(({path}) => path === currentPath)?.Component
    return Page ? <Page />: <DefaultComponet/>
}