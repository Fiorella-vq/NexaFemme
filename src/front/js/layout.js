import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import Home from "./pages/home";

import injectContext from "./store/appContext";

import BottomNav from "./component/bottomNav";
import { Footer } from "./component/footer";   

import AvatarGemela from "./component/avatarGemela";
import TodayCard from "./component/todayCard";


const Layout = () => {
    const basename = process.env.BASENAME || "";

    if (!process.env.BACKEND_URL || process.env.BACKEND_URL === "") {
        return <BackendURL />;
    }

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>

                    {/* CONTENIDO PRINCIPAL */}
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/demo" element={<Demo />} />
                        <Route path="/avatar" element={<AvatarGemela />} />
                        <Route path="/todaycard" element={<TodayCard />} />
                        <Route path="/single/:theid" element={<Single />} />
                        <Route path="*" element={<h1>Not found!</h1>} />
                    </Routes>

                 
                    <BottomNav />

                    
                    <Footer />

                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
