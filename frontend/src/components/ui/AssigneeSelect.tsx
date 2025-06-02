import {Field, NativeSelect} from "@chakra-ui/react";
import {useContext} from "react";
import UsersContext from "@/context/usersContext.ts";

type Props = {
    selected?: string;
};

function AssigneeSelect({selected}: Props) {
    const users = useContext(UsersContext);
    return (<Field.Root>
        <Field.Label>Assignee</Field.Label>
        <NativeSelect.Root>
            <NativeSelect.Field id="assigned_to" placeholder="Unasigned" defaultValue={selected}>
                {users.map(({username, uuid}) =>
                    <option key={uuid} value={uuid}>
                        {username}
                    </option>)}
            </NativeSelect.Field>
            <NativeSelect.Indicator/>
        </NativeSelect.Root>
    </Field.Root>)
}

export default AssigneeSelect;