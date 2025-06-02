export type Priority = {
    displayName: string,
    name: string,
}

export type Severity = {
    displayName: string,
    name: string,
}

export type Status = {
    displayName: string,
    name: string,
}

export type User = {
    username: string,
    uuid: string,
    is_superuser: boolean,
}

export type CurrentUser = {
    username: string,
    uuid: string,
    is_superuser: boolean,
}

export type Bug = {
    uuid: string,
    title: string,
    description: string | null,
    status: string,
    priority: string,
    severity: string,
    steps: string | null,
    expected: string | null,
    actual: string | null,
    assignee: User | null,
    reporter: User | null
}
