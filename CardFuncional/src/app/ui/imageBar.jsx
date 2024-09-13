'use client';

import { Card, CardHeader, CardBody } from "@chakra-ui/react";

export default function ImageBar() {
  return (
    <>
      <Card>
        <CardHeader>
          <h2>Arte</h2>
        </CardHeader>
        <CardBody>
          <p>Creaciones que superan la imaginación</p>
        </CardBody>
      </Card>
      <Card>
        <CardHeader>
          <h2>Escultores</h2>
        </CardHeader>
        <CardBody>
          <p>Escultores de todo el mundo</p>
        </CardBody>
      </Card>
      <Card>
        <CardHeader>
          <h2>Eventos</h2>
        </CardHeader>
        <CardBody>
          <p>La Bienal cuenta con una multitud de eventos</p>
        </CardBody>
      </Card>
    </>
  );
}
