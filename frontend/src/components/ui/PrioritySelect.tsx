import {Field, NativeSelect} from "@chakra-ui/react";
import {useContext} from "react";
import PriorityContext from "@/context/priorityContext.ts";

type Props = {
    selected?: string;
};

function PrioritySelect({selected ="MEDIUM"}: Props) {
    const priority = useContext(PriorityContext);
    return (
        <Field.Root>
            <Field.Label>Priority</Field.Label>
            <NativeSelect.Root>
                <NativeSelect.Field id="priority" defaultValue={selected}>
                    {priority.map(({displayName, name}) =>
                        <option key={name} value={name}>
                            {displayName}
                        </option>)}
                </NativeSelect.Field>
                <NativeSelect.Indicator/>
            </NativeSelect.Root>
        </Field.Root>
    )
}

export default PrioritySelect;
