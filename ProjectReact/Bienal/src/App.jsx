import { esculturas } from "./DataEsculturas.js"
import {getImageUrl} from "./utils.js"

function Sculpture({item}){
    return(
        <>
        <h2 className="titleSculp">{item.name}</h2>
        <img className="showcase" src={getImageUrl(item)} alt={item.name}/>
        </>
    )
}

export default function Galeria(){
    const listItems = esculturas.map(sculp =>
        <Sculpture key={sculp.id} item = {sculp}/>
    );
    return (
        <>
            <h1 className="titleGallery">Esculturas</h1>
            <div classname="container">
                {listItems} 
            </div>
        </>
    )
}