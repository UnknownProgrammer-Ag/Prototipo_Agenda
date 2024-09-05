import { useState } from 'react';
import {ESCULTURAS} from '../utils/DataEsculturas';
import {Link} from '../components/Link';


export default function FormPage(){

    const [escultura, setEscultura]=useState(ESCULTURAS);
    const [name, setName] = useState('');
    const [imageId, setImageId] = useState('');

		const handleSubmit = (e) => {
        e.preventDefault();
        const newEscultura = {
            id: escultura.length,
            name: name,
            imageId: imageId
        };
        // Usando propagacion de array, actualizamos de manera recomendada el array y agregamos el nuevo elemento
       setEscultura((prevEscultura) =>
        [...prevEscultura,
        newEscultura
       ]);

       // El hook es una forma de modificar partes de los componentes de react, aqui indicamos que se borra el contenido
       setName('');
       setImageId('');
    };
	
	return(
        <>
            <h1>Nueva Escultura</h1>
            <p>A continuación podrá introducir los datos necesarios para cargar una nueva escultura.</p>
            <form onSubmit={handleSubmit}>
                <div>                
                    <label>Nombre de la escultura
                        <input
                        type="text"
                        value={name}
                        onChange={(e)=>setName(e.target.value)}
                        required //Atributo del componente que vuelve obligatorio el campo
                        />
                    </label>
                </div>
                <div>                
                    <label>ID de la imagen
                        <input
                        type="text"
                        value={imageId}
                        onChange={(e)=>setImageId(e.target.value)}
                        required //Atributo del componente que vuelve obligatorio el campo
                        />
                    </label>
                </div>
                <button type="submit">Agregar Escultura</button>
            </form>
            <Link to='/'>Volver a Inicio</Link>
        </>
    )
	}
