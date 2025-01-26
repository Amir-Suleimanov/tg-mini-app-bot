// src/components/SurahItem.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './SurahItem.css';

const SurahItem = ({ surah }) => {
    return (
        <Link to={`/surah/${surah.number}`} className="surah-item-link">
            <div className="surah-item">
                <div className="number">{surah.number}</div>
                <div className="name">{surah.name}</div>
                <div className="ayats-count">{surah.ayats_count}</div>
            </div>
        </Link>
    );
};

export default SurahItem;