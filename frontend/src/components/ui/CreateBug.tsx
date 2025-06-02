import {Dialog, Button, Portal, CloseButton, Input, Textarea, Field} from "@chakra-ui/react";
import React, {useState} from "react";


import api from "@/api.ts";
import PrioritySelect from "@/components/ui/PrioritySelect.tsx";
import AssigneeSelect from "@/components/ui/AssigneeSelect.tsx";
import SeveritySelect from "@/components/ui/SeveritySelect.tsx";
import StatusSelect from "@/components/ui/StatusSelect.tsx";
import type {Bug} from "@/types.ts";

function CreateBug() {
    const [newBug, setNewBug] = useState<Partial<Bug>>({});
    const [loading, setLoading] = useState(false);

    const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        const id = e.target.id
        setNewBug({...newBug, [id]: value});

    }

    const handleCreate = () => {
        setLoading(true);
        api.post("/bugs", newBug).then(() => {
            location.reload();
        }).catch(error => {
            console.log(error)
        }).finally(() =>
            setLoading(false)
        )
    }

    return (
        <Dialog.Root size="cover" placement="center" motionPreset="slide-in-bottom">
            <Dialog.Trigger asChild>
                <Button variant="outline" size="sm">
                    Create
                </Button>
            </Dialog.Trigger>
            <Portal>
                <Dialog.Backdrop/>
                <Dialog.Positioner>
                    <Dialog.Content>
                        <Dialog.Header>
                            <Dialog.Title>New bug</Dialog.Title>
                            <Dialog.CloseTrigger asChild>
                                <CloseButton size="sm"/>
                            </Dialog.CloseTrigger>
                        </Dialog.Header>
                        <Dialog.Body onChange={handleOnChange}>
                            <Field.Root>
                                <Field.Label>Title</Field.Label>
                                <Input id="title" required type="text" placeholder="Title..." maxLength={255}></Input>
                            </Field.Root>
                            <Field.Root>
                                <Field.Label>Description</Field.Label>
                                <Textarea id="description" autoresize size="lg" resize="vertical"
                                          placeholder="Description..." maxLength={1000}></Textarea>
                            </Field.Root>

                            <Field.Root>
                                <Field.Label>Steps to reproduce</Field.Label>
                                <Textarea id="steps" placeholder="Steps..." maxLength={255}></Textarea>
                            </Field.Root>

                            <Field.Root>
                                <Field.Label>Expected result</Field.Label>
                                <Textarea id="expected" placeholder="expected" maxLength={255}></Textarea>
                            </Field.Root>

                            <Field.Root>
                                <Field.Label>Actual result</Field.Label>
                                <Textarea id="actual" placeholder="actual" maxLength={255}></Textarea>
                            </Field.Root>
                            <StatusSelect/>
                            <SeveritySelect/>
                            <PrioritySelect/>
                            <AssigneeSelect/>
                        </Dialog.Body>
                        <Dialog.Footer>
                            <Button size="md" colorPalette="green" onClick={handleCreate} disabled={!newBug["title"]}
                                    loading={loading} loadingText="Saving...">Create</Button>
                        </Dialog.Footer>
                    </Dialog.Content>
                </Dialog.Positioner>
            </Portal>
        </Dialog.Root>
    )
}

export default CreateBug;
