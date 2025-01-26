// src/components/AyahItem/AyahItem.jsx
import React from 'react';
import './AyahItem.css';

const AyahItem = ({ ayah }) => {
    return (
        <div className="ayah-item">
            <div className="number">{ayah.number}</div>
            <div className="content">
                <div className="text-arabic" dir="rtl">{ayah.text_arabic}</div>
                <div className="translation">{ayah.translation}</div>
            </div>
        </div>
    );
};

export default AyahItem;