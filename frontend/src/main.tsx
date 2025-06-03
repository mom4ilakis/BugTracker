import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import {Provider} from "@/components/ui/provider"
import './index.css'
import App from './App.tsx'
import {RouterProvider} from "react-router/dom";
import {createBrowserRouter} from "react-router";
import {LoginPage} from "@/components/ui/LoginPage.tsx";
import {RegisterPage} from "@/components/ui/RegisterPage.tsx";
import ProtectedRoute from "@/components/ProtectedRoute.tsx";
import {Toaster} from "@/components/ui/toaster.tsx";

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <Provider>
            <Toaster/>
                <RouterProvider router={createBrowserRouter([
                    {
                        element: <ProtectedRoute/>,
                        children: [{
                            path: '/',
                            element: <App/>
                        }]

                    }, {
                        path: '/login',
                        element: <LoginPage/>,
                    }, {
                        path: '/register',
                        element: <RegisterPage/>,
                    }

                ])}/>
        </Provider>
    </StrictMode>,
)
