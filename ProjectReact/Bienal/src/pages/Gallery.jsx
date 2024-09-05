import { ESCULTURAS } from "../utils/DataEsculturas.js"
import {getImageUrl} from "../utils/getImageUrl.js"
import { Link } from "../components/Link.jsx"

function Sculpture({item}){
    return(
        <>
        <h2>{item.name}</h2>
        <img src={getImageUrl(item)} alt={item.name}/>
        </>
    )
}

export default function GalleryPage(){
const listItems = ESCULTURAS.map(sculp =>
    <Sculpture key={sculp.id} item = {sculp}/>
);
return (
    <>
        <h1>Esculturas</h1>
        <div><Link to='/'>Volver a Inicio</Link></div>
        <div>
            {listItems} 
        </div>
       
    </>
)
}
