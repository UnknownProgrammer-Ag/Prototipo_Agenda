import { EVENTS } from "../utils/const";

export function navigation(href){
    //Esto permite manipular el historial de sesión del navegador
    //(páginas visitadas en el tab o marco de la pagina actual cargada).
    window.history.pushState({},'',href)
    const navigationEvent = new Event(EVENTS.PUSHSTATE)
    window.dispatchEvent(navigationEvent)   
}

export function Link ({target, to, ...props}){
    const handleClick = (event) => {
        // Agregando manejo de comandos de teclado xD

        const isMainEvent = event.button === 0 // Click principal
        const isModifiedEvent = event.metaKey || event.ctrlKey || event.altKey || event.shiftKey
        const isManageableEvent = target === undefined || target === '_self'

        if (isMainEvent && isManageableEvent && !isModifiedEvent)
            event.preventDefault()
            navigation(to)
        
    }

    return <a onClick={handleClick} href={to} target={target} {...props}/>
}