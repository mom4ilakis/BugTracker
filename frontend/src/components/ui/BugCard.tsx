import {
    Avatar,
    Box,
    Button,
    Card,
    CloseButton,
    Dialog,
    Field,
    Flex,
    Heading,
    Input,
    Portal, Separator, Status,
    Tag,
    Textarea
} from "@chakra-ui/react"
import SeveritySelect from "@/components/ui/SeveritySelect.tsx";
import PrioritySelect from "@/components/ui/PrioritySelect.tsx";
import AssigneeSelect from "@/components/ui/AssigneeSelect.tsx";
import StatusSelect from "./StatusSelect";
import React, {useState} from "react";
import api from "@/api.ts";
import type {Bug} from "@/types.ts";
import {toaster} from "@/components/ui/toaster.tsx";

type BugCardProps = Bug

const colorPalette = ["red", "blue", "green", "yellow", "purple", "orange"]

const pickPriorityPalette = (priority: string) => {
    switch (priority) {
        case "LOW":
            return "green";
        case "MEDIUM":
            return "yellow";
        case "HIGH":
            return "red";
        default:
            return "blue";
    }
}

const pickSeverityPalette = (severity: string) => {
    switch (severity) {
        case "CRITICAL":
            return "red";
        case "HIGH":
            return "orange";
        case "MEDIUM":
            return "yellow";
        case "LOW":
            return "green";
        default:
            return "blue";
    }
}

const pickAssignPalette = (name: string) => {
    if (name === "Unassigned") {
        return "gray";
    }
    const index = name.charCodeAt(0) % colorPalette.length
    return colorPalette[index]
}

function DetailedBug(bug: BugCardProps) {
    const [updatedBug, setUpdatedBug] = useState({});
    const [loading, setLoading] = useState(false);
    const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        const id = e.target.id
        setUpdatedBug({...updatedBug, [id]: value});

    }

    const handleUpdate = () => {
        if (Object.keys(updatedBug).length === 0) {
            return;
        }
        setLoading(true);
        api.patch(`/bugs/${bug.uuid}`, updatedBug).then(() => {
            window.location.reload();
        }).catch(error => {
            toaster.error({
                title: "Update failed",
                description: error.response.data.detail,
            });
            console.log(error);
        }).finally(() => {
                setUpdatedBug({});
                setLoading(false);
            }
        )
    };

    const handleDelete = () => {
        setLoading(true);
        api.delete(`/bugs/${bug.uuid}`).then(() => {
            window.location.reload();
        }).catch(error => {
            toaster.error({
                title: "Could not delete bug",
                description: error.response.data.detail,
            });
        }).finally(
            () => setLoading(false)
        );
    }

    return (
        <Dialog.Root
            placement="center"
            size="cover"
            motionPreset="slide-in-bottom"
        >
            <Dialog.Trigger asChild>
                <Button variant="outline">View</Button>
            </Dialog.Trigger>
            <Portal>
                <Dialog.Backdrop/>
                <Dialog.Positioner>
                    <Dialog.Content onChange={handleOnChange}>
                        <Dialog.Header>
                            <Dialog.Title>
                                <Tag.Root>
                                    <Tag.Label>{bug.uuid}</Tag.Label>
                                </Tag.Root>
                                <Field.Root>
                                    <Field.Label>Title</Field.Label>
                                    <Input id="title" type="text" defaultValue={bug.title} maxLength={255}/>
                                </Field.Root>
                            </Dialog.Title>
                        </Dialog.Header>
                        <Dialog.Body>
                            <Field.Root>
                                <Field.Label>Description</Field.Label>
                                <Textarea id="description" defaultValue={bug.description ?? undefined}
                                          placeholder="Description"
                                          maxLength={1000}/>
                            </Field.Root>
                            <SeveritySelect selected={bug.severity}/>
                            <PrioritySelect selected={bug.priority}/>
                            <StatusSelect selected={bug.status}/>
                            <AssigneeSelect selected={bug.assignee?.uuid}/>
                            <Field.Root>
                                <Field.Label>Steps to reproduce</Field.Label>
                                <Textarea id="steps" defaultValue={bug.steps ?? undefined}
                                          placeholder="Steps to reproduce"
                                          maxLength={255}></Textarea>
                            </Field.Root>
                            <Field.Root>
                                <Field.Label>Expected result</Field.Label>
                                <Textarea id="expected" defaultValue={bug.expected ?? undefined}
                                          placeholder="Expected result"
                                          maxLength={255}></Textarea>
                            </Field.Root>
                            <Field.Root>
                                <Field.Label>Actual result</Field.Label>
                                <Textarea id="actual" defaultValue={bug.actual ?? undefined} placeholder="Actual result"
                                          maxLength={255}></Textarea>
                            </Field.Root>

                        </Dialog.Body>
                        <Dialog.Footer>
                            <Dialog.ActionTrigger asChild>
                                <Button variant="outline">Close</Button>
                            </Dialog.ActionTrigger>
                            <Button size="md" colorPalette="green" onClick={handleUpdate}
                                    loading={loading} loadingText="Saving...">Save</Button>
                            <Button size="sm" colorPalette="red" loading={loading} onClick={handleDelete}>Delete this
                                bug!</Button>
                        </Dialog.Footer>
                        <Dialog.CloseTrigger asChild>
                            <CloseButton size="sm"/>
                        </Dialog.CloseTrigger>
                    </Dialog.Content>
                </Dialog.Positioner>
            </Portal>
        </Dialog.Root>
    );
}


export function BugCard({title, description, assignee, ...rest}: BugCardProps) {
    const name = assignee?.username || "Unassigned";
    return (
        <Card.Root size="sm" colorPalette="teal" variant="elevated" shadowColor="teal" maxW="2xs" maxH="2xs">
            <Card.Body gap="2">
                <Card.Title mt="2" gap="2">
                    <Flex justify="space-between" align="center" gap="2" direction="row" wrap="wrap">
                        <Heading>{title}</Heading>
                        <Avatar.Root colorPalette={pickAssignPalette(name)} shape="rounded" size="sm">
                            <Avatar.Fallback name={name}/>
                        </Avatar.Root>
                    </Flex>
                </Card.Title>
                <Card.Description overflow="hidden" maxH="100px">
                    <Box>
                        <Flex justify="space-between" align="center" gap="2" direction="row" wrap="wrap" mt="2">
                            <Status.Root colorPalette={pickPriorityPalette(rest.priority)} size="sm">
                                <Status.Indicator/>
                                {rest.priority}
                            </Status.Root>
                            <Status.Root colorPalette={pickSeverityPalette(rest.severity)} size="sm">
                                <Status.Indicator/>
                                {rest.severity}
                            </Status.Root>
                        </Flex>
                        <Separator/>
                        {description}
                    </Box>
                </Card.Description>
                <DetailedBug {...{title, description, assignee, ...rest}}/>
            </Card.Body>
        </Card.Root>
    )
}
