import { Button, Center, Field, Fieldset, Flex, Heading, Input, Stack} from "@chakra-ui/react";
import {register} from '@/authService.ts';
import {PasswordInput} from "@/components/ui/password-input.tsx";
import {useState} from "react";
import {useNavigate} from "react-router";
import {ColorModeButton} from "@/components/ui/color-mode.tsx";

export const RegisterPage = () => {
    const navigate = useNavigate()
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');

    const onSubmit = async () => {
        if (password === "" || password !== repeatPassword || email === "" || username === "") {
            return;
        }
        await register({email, password, username});
        navigate('/login');
    };

    return (
        <Flex direction="column" align="center" justify="center">
            <Flex justify="space-between" align="center" w="100%" p="2">
                <Heading>Bug Tracker</Heading>
                <ColorModeButton/>
            </Flex>
            <Center mt="5%">
                <Fieldset.Root size="lg" width="350px">
                    <Stack>
                        <Fieldset.Legend>
                            Registration form
                        </Fieldset.Legend>
                    </Stack>
                    <Fieldset.Content>
                        <Field.Root required>
                            <Field.Label>Email</Field.Label>
                            <Input type="text" placeholder="Email" onChange={(e) => setEmail(e.target.value)}/>
                        </Field.Root>
                        <Field.Root>
                            <Field.Label>Username</Field.Label>
                            <Input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)}/>
                        </Field.Root>
                        <Field.Root required>
                            <Field.Label>Password</Field.Label>
                            <PasswordInput onChange={(e) => setPassword(e.target.value)}/>
                        </Field.Root>
                        <Field.Root required>
                            <Field.Label>Repeat password</Field.Label>
                            <PasswordInput onChange={(e) => setRepeatPassword(e.target.value)}/>
                        </Field.Root>
                    </Fieldset.Content>
                    <Button type="submit" onClick={onSubmit} colorPalette="green">Register</Button>
                    <Button type="submit" onClick={() => navigate("/login")} colorPalette="gray" variant="subtle">Already have an account? Click here to login</Button>
                </Fieldset.Root>
            </Center>
        </Flex>
    );
};