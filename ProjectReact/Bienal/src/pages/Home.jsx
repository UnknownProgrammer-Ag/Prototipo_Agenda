import { Link } from "../components/Link.jsx"

export default function HomePage(){
    return (
        <>
            <h1>Bienal</h1>
            <h2>Feria Internacional de Arte</h2>
            <p>Placeholder texto de presentación</p>
            <ul><b>To do</b>
            <li>Diferenciar elementos en el CSS entre secciones
            </li>
            <li>
                Crear seccion de formularios de carga de datos
            </li>
            </ul>
            <div><Link to='/about'>Sobre Nosotros</Link></div>
            <div><Link to='/esculturas'>Galeria de Esculturas</Link></div>
        </>
    )
    }