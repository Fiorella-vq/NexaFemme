import React from "react";
import "../../styles/home.css";
import AvatarGemela from "../component/avatarGemela";
import TodayCard from "../component/todayCard";


const Home = () => {
    const fecha = new Date().toLocaleDateString("es-UY", {
        day: "2-digit",
        month: "short",
    });

    return (
        <main className="home-wrapper">

            <header className="home-header">
                <div>
                    <h1 className="nexa-title">NexaFemme</h1>
                    <p className="nexa-subtitle">Tu gemela emocional, todos los días.</p>
                </div>
                <span className="home-date">{fecha}</span>
            </header>

            <section className="avatar-section">
                <AvatarGemela 
                    mood="sensible" 
                    energia={3} 
                    fase="Fase lútea" 
                />
            </section>

            <section className="cards-section">
                <TodayCard
                    title="Fase actual"
                    pill="Fase lútea"
                    text="Hoy podés sentirte más sensible."
                />

                <TodayCard
                    title="Energía estimada"
                    pill="Media"
                    text="Tenés energía moderada."
                />

                <TodayCard
                    title="Alerta emocional"
                    pill="Reflexioná"
                    text="Podés estar más irritable."
                />
            </section>
        </main>
    );
};

export default Home;
