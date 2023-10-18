drop schema if exists smite;
create schema smite;
use smite;

create table panteon(
panteon varchar(15) not null,
primary key (panteon)
);

create table rol(
rol varchar(20) not null,
primary key (rol)
);

create table personaje(
personaje varchar(15) not null,
panteon varchar(15) not null,
rol varchar(20) not null,
dificultad varchar(10) not null,
primary key (personaje),
foreign key (panteon) references panteon (panteon),
foreign key (rol) references rol (rol)
);

create table habilidad(
habilidad varchar(30) not null,
personaje varchar(15) not null,
descripcion text not null,
primary key (habilidad),
foreign key (personaje) references personaje (personaje)
);

create table articulo(
articulo varchar(30) not null,
costo int(4) not null,
primary key(articulo)
);

create table jugador(
nombre varchar(40) not null,
personaje varchar(15) not null,
primary key(nombre),
foreign key (personaje) references personaje (personaje)
);

create table modo(
modo varchar(15) not null,
descripcion text not null,
cantJugadores int(2) not null,
primary key (modo)
);

create table partida(
ID int(9) not null,
modo varchar(15) not null,
inicioPartida datetime not null,
finPartida datetime not null,
primary key (ID),
foreign key (modo) references modo (modo)
);

create table partida_jugador(
ID int(9) not null,
nombre varchar(40) not null,
primary key (ID, nombre),
foreign key (ID) references partida (ID),
foreign key (nombre) references jugador (nombre)
);

create table jugador_articulo(
nombre varchar(40) not null,
articulo varchar(30) not null,
primary key (nombre, articulo),
foreign key (nombre) references jugador (nombre),
foreign key (articulo) references articulo (articulo)
);
