import { Card, CardHeader, CardBody, CardFooter } from "@chakra-ui/react";
import ImageArt from "./imageArt";
import ImageEvent from "./imageEvent";
import ImageEscult from "./imageEscult";
import Link from "next/link";

export default function ThreeCards() {
  return (
    <>
      <Card>
        <CardHeader>
          <h2>Arte</h2>
        </CardHeader>
        <CardBody>
          <ImageArt />
          <p>Creaciones que superan la imaginación</p>
        </CardBody>
        <CardFooter>
          <Link href="/art">Ver más</Link>
        </CardFooter>
      </Card>
      <Card>
        <CardHeader>
          <h2>Escultores</h2>
        </CardHeader>
        <CardBody>
          <ImageEscult />
          <p>Escultores de todo el mundo</p>
        </CardBody>
      </Card>
      <Card>
        <CardHeader>
          <h2>Eventos</h2>
        </CardHeader>
        <CardBody>
          <ImageEvent />
          <p>La Bienal cuenta con una multitud de eventos</p>
        </CardBody>
        <CardFooter>
          <Link href="/events">Ver más</Link>
        </CardFooter>
      </Card>
    </>
  );
}
