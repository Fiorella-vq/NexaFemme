import React from "react";
import { NavLink } from "react-router-dom";
import "../../styles/nexafemme-nav.css";


export default function BottomNav() {
    return (
        <nav className="nexa-bottom-nav">
            <NavLink to="/" className="nexa-item">Inicio</NavLink>
            <NavLink to="/daily-log" className="nexa-item">Registro</NavLink>
            <NavLink to="/emotional-map" className="nexa-item">Mapa</NavLink>
            <NavLink to="/relationships" className="nexa-item">Relaciones</NavLink>
            <NavLink to="/profile" className="nexa-item">Perfil</NavLink>
        </nav>
    );
}
