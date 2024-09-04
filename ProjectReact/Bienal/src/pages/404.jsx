import { Link } from "../components/Link";

export default function Page404(){
    return (
        <>
        <div>
            <h1>ERROR 404</h1>
            <img src="https://img.freepik.com/premium-vector/set-cute-robot-ai-character-error-crash-action_99413-154.jpg?w=900" alt="Crashing Robots"/>
            <Link to='/'>Regresar a Inicio</Link>
        </div>
        </>
    )
}