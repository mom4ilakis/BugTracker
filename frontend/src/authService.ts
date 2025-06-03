import {loginApi} from "@/api.ts";

export const login = async (creds: FormData) => {
    const {data} = await loginApi.post('/login', creds, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    });
    const token = data.access_token;
    localStorage.setItem('token', token);
};

export const register = async (creds: { password: string, email: string, username: string }) => {
    const {data} = await loginApi.post('/register', creds);
    const token = data.access_token;
    localStorage.setItem('token', token);
}


export const logout = () => {
    localStorage.removeItem('token');
}