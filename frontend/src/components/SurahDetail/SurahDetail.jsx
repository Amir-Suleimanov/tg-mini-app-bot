// src/components/SurahDetail/SurahDetail.jsx
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import AyahItem from '../AyahItem/AyahItem';
import axios from 'axios';
import Header from '../Header/Header';

const SurahDetail = () => {
    const { number } = useParams();
    const [surah, setSurah] = useState(null);

    useEffect(() => {
        const fetchSurah = async () => {
            try {
                const response = await axios.get(`https://127.0.0.1:8000/api/surahs/${number}/`);
                setSurah(response.data);
            } catch (error) {
                console.error('Error fetching surah:', error);
            }
        };

        fetchSurah();
    }, [number]);

    if (!surah) {
        return <div>Loading...</div>;
    }

    return (
        <div className="surah-detail" style={{backgroundColor: "#fff"}}>
            <Header surahName={surah.name} />
            <div className="ayah-list">
                {surah.ayahs.map((ayah) => (
                    <AyahItem key={ayah.number} ayah={ayah} />
                ))}
            </div>
        </div>
    );
};

export default SurahDetail;
