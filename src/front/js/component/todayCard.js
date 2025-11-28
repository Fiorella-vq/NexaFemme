import React from 'react';
import "../../styles/global.css";


const TodayCard = ({ title, text, pill }) => {
    return (
        <article className="today-card">
            <div className="today-card-header">
                <h3>{title}</h3>
                {pill && <span className="pill">{pill}</span>}
            </div>
            <p className="today-card-text">{text}</p>
        </article>
    );
};

export default TodayCard;
