import api from "@/api.ts";

export const login = async (creds: FormData) => {
    const {data} = await api.post('/login', creds, {
        headers: {
            'Content-Type': 'pplication/x-www-form-urlencoded',
        },
    });
    const token = data.access_token;
    localStorage.setItem('token', token);
};

export const register = async (creds: { password: string, email: string, username: string }) => {
    const {data} = await api.post('/register', creds);
    const token = data.access_token;
    localStorage.setItem('token', token);
}


export const logout = () => {
    localStorage.removeItem('token');
}