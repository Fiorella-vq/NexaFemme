import React from "react";
import "../../styles/global.css";


const AvatarGemela = ({ mood, energia, fase }) => {
    return (
        <div className="avatar-card">
            <div className="avatar-circle">
                <div className="avatar-glow"></div>
                <span className="avatar-emoji">💜</span>
            </div>

            <div className="avatar-info">
                <p className="avatar-mood">Tu gemela hoy está: {mood}</p>
                <p className="avatar-phase">{fase}</p>
                <p className="avatar-energy">Energía: {energia}/5</p>
            </div>
        </div>
    );
};

export default AvatarGemela;
