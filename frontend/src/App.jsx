// src/App.jsx
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SurahList from './components/SurahList/SurahList';
import SurahDetail from './components/SurahDetail/SurahDetail';
import './App.css';

const App = () => {
    useEffect(() => {
        if (window.Telegram?.WebApp) {
            const tg = window.Telegram.WebApp;
            tg.ready(); // Подготавливаем Telegram Web App
            console.log("Данные пользователя:", tg.initDataUnsafe?.user);
        }
    }, []);

    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<SurahList />} />
                    <Route path="/surah/:number" element={<SurahDetail />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
