// src/components/SurahList/SurahList.jsx
import React, { useState, useEffect } from 'react';
import SurahItem from '../SurahItem/SurahItem';
import axios from 'axios';
import Header from '../Header/Header';
import './SurahList.css';

const SurahList = () => {
    const [surahs, setSurahs] = useState([]);

    useEffect(() => {
        const fetchSurahs = async () => {
            try {
                const response = await axios.get('https://127.0.0.1:8000/api/surahs/');
                setSurahs(response.data);
            } catch (error) {
                console.error('Error fetching surahs:', error);
            }
        };

        fetchSurahs();
    }, []);

    return (
        <div className="surah-list-container">
            <Header />
            <div className="surah-list" style={{backgroundColor: "#fff"}}>
                {surahs.map((surah) => (
                    <SurahItem key={surah.number} surah={surah} />
                ))}
            </div>
        </div>
    );
};

export default SurahList;