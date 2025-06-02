import {useEffect, useState} from 'react'

import './App.css'
import {Box, Button, Center, Flex, Grid, GridItem, Heading, Separator, Stack} from "@chakra-ui/react";
import {BugCard} from "@/components/ui/BugCard.tsx";
import CreateBug from "@/components/ui/CreateBug.tsx";

import api from './api';
import {ColorModeButton} from "@/components/ui/color-mode.tsx";
import SeverityContext from "@/context/severityContext.ts";
import PriorityContext from "@/context/priorityContext.ts";
import StatusContext from "@/context/statusContext.ts";
import UsersContext from "@/context/usersContext.ts";
import CurrentUserContext from "@/context/currentUserContext.ts";
import type {Bug, CurrentUser, Priority, Severity, Status, User} from "@/types.ts";


const status2display: { [key: string]: string } = {
    "NEW": "New",
    "IN_PROGRESS": "In Progress",
    "DONE": "Done",
    "WONT_DO": "Won't do",
    "CLOSED": "Closed",
    "REOPENED": "Reopened"
}

const priority2display: { [key: string]: string } = {
    "LOW": "Low",
    "MEDIUM": "Medium",
    "HIGH": "High"
}

const severity2display: { [key: string]: string } = {
    "CRITICAL": "Critical",
    "HIGH": "High",
    "MEDIUM": "Medium",
    "LOW": "Low"
}

type SortedBugsByStatus = {
    [key: string]: Bug[]
}

function App() {
    const [status, setStatus] = useState<Status[]>([]);
    const [priority, setPriority] = useState<Priority[]>([]);
    const [severity, setSeverity] = useState<Severity[]>([]);
    const [bugs, setBugs] = useState<SortedBugsByStatus>({});
    const [users, setUsers] = useState<User[]>([]);
    const [currentUser, setCurrentUser] = useState<CurrentUser | null>(null);
    const [showMineOnly, setShowMineOnly] = useState<boolean>(false);


    useEffect(() => {
        api.get("/bugs/metadata").then(({data}) => {
            const status = data.status.map((s: string) =>
                ({displayName: status2display[s], name: s}));
            const prio = data.priority.map((p: string) =>
                ({displayName: priority2display[p], name: p}));
            const severity = data.severity.map((s: string) =>
                ({displayName: severity2display[s], name: s}));
            setStatus(status);
            setPriority(prio);
            setSeverity(severity);
        })
        api.get("/users/me").then((response) => {
            const user: CurrentUser = response.data;
            setCurrentUser(user);

            api.get(`/bugs`).then(response => {
                const new_bugs: SortedBugsByStatus = response.data.reduce((acc: SortedBugsByStatus, bug: Bug) => {
                    acc[bug.status] = [...(acc[bug.status] || []), bug]
                    return acc;
                }, {})
                setBugs(new_bugs)
            });
        });
        api.get("/users").then(response => {
            setUsers(response.data)
        });
    }, []);

    const colRepeat = `repeat(${status.length}, 1fr)`

    return (
        <Box w="100%" h="100%">
            <CurrentUserContext.Provider value={currentUser}>
                <StatusContext.Provider value={status}>
                    <PriorityContext.Provider value={priority}>
                        <SeverityContext.Provider value={severity}>
                            <UsersContext.Provider value={users}>
                                <Center>
                                    <Heading>Bug Tracker</Heading>
                                    <ColorModeButton/>
                                </Center>
                                <Separator/>
                                <Flex justify="space-between" align="center" w="100%" p="2">
                                    <CreateBug/>
                                    <Button size="sm" colorPalette="gray"
                                            onClick={() => setShowMineOnly(!showMineOnly)}>{showMineOnly ? "Show all" : "Assigned to me"}</Button>
                                </Flex>
                                <Grid templateColumns={colRepeat} gap={4} pt={4}>
                                    {status.map(({displayName, name}) =>
                                        <GridItem>
                                            <Stack>
                                                <Heading>{displayName}</Heading>
                                                {bugs[name]?.map((bug) =>
                                                    showMineOnly ? bug.assignee?.uuid === currentUser?.uuid &&
                                                        <BugCard key={bug.uuid} {...bug}/> :
                                                        <BugCard key={bug.uuid} {...bug}/>
                                                )
                                                }
                                            </Stack>
                                        </GridItem>
                                    )}
                                </Grid>
                            </UsersContext.Provider>
                        </SeverityContext.Provider>
                    </PriorityContext.Provider>
                </StatusContext.Provider>
            </CurrentUserContext.Provider>
        </Box>
    )
}

export default App
