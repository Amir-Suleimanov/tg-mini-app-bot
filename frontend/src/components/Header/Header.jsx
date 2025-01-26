// src/components/Header/Header.jsx
import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './Header.css';

const Header = ({ surahName, onSearch }) => {
    const location = useLocation();
    const navigate = useNavigate();
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        if (window.Telegram?.WebApp) {
            const webApp = window.Telegram.WebApp;
            webApp.ready();
            webApp.setHeaderColor('#7fbdd4');
            webApp.setBackgroundColor('#f8f9fa');
        }
    }, []);

    const handleSearchChange = (e) => {
        const query = e.target.value;
        setSearchQuery(query);
        onSearch(query); // Передаем поисковый запрос в родительский компонент
    };

    const closeWebApp = () => {
        if (window.Telegram?.WebApp) {
            window.Telegram.WebApp.close();
        }
    };

    const goBack = () => {
        navigate(-1);
    };

    if (location.pathname === '/') {
        return (
            <header className="header" style={{ backgroundColor: '#7fbdd4' }}>
                <div className="tabs">
                    <span>Суры</span>
                    <span>Джузы</span>
                </div>
                <input 
                    type="text" 
                    placeholder="Поиск по сурам" 
                    value={searchQuery}
                    onChange={handleSearchChange}
                />
                <button onClick={closeWebApp} className="close-button">Закрыть</button>
            </header>
        );
    }

    return (
        <header className="detail-header" style={{ backgroundColor: '#7fbdd4' }}>
            <button onClick={goBack} className="back-button">Назад</button>
            <span className="header-title">{surahName}</span>
            <button onClick={closeWebApp} className="close-button">Закрыть</button>
        </header>
    );
};

export default Header;