import {
    Button, Center,
    Field,
    Fieldset,
    Flex,
    Heading,
    Input,
    Stack
} from "@chakra-ui/react";
import {login} from '@/authService.ts';
import {PasswordInput} from "@/components/ui/password-input.tsx";
import {useNavigate} from "react-router";
import {useState} from "react";
import {ColorModeButton} from "@/components/ui/color-mode.tsx";

export const LoginPage = () => {
    const navigate = useNavigate()
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const onSubmit = async () => {
        if (username === "" || password === "") {
            return;
        }

        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);
        await login(formData);
        navigate('/');
    };

    return (
        <Flex direction="column" align="center" justify="center">
            <Flex justify="space-between" align="center" w="100%" p="2">
                <Heading>Bug Tracker</Heading>
                <ColorModeButton/>
            </Flex>
            <Center mt="10%">
                <Fieldset.Root size="lg" width="350px">
                    <Stack>
                        <Fieldset.Legend>
                            You are not logged in
                        </Fieldset.Legend>
                        <Fieldset.HelperText>Please login</Fieldset.HelperText>
                    </Stack>
                    <Fieldset.Content>
                        <Field.Root>
                            <Field.Label>Username</Field.Label>
                            <Input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)}/>
                        </Field.Root>
                        <Field.Root>
                            <Field.Label>Password</Field.Label>
                            <PasswordInput onChange={(e) => setPassword(e.target.value)}/>
                        </Field.Root>
                    </Fieldset.Content>
                    <Button type="submit" onClick={onSubmit} colorPalette="green" >Login</Button>
                    <Button type="submit" onClick={() => navigate("/register")} variant="subtle" colorPalette="gray">
                        Don't have an account? Click to register!
                    </Button>
                </Fieldset.Root>
            </Center>
        </Flex>
    );
};