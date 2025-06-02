import {Field, NativeSelect} from "@chakra-ui/react";
import {useContext} from "react";
import StatusContext from "@/context/statusContext.ts";

type Props = {
    selected?: string;
};


function StatusSelect({selected = "NEW"}: Props) {
    const status = useContext(StatusContext);
    return (
        <Field.Root>
            <Field.Label>Status</Field.Label>
            <NativeSelect.Root>
                <NativeSelect.Field id="status" defaultValue={selected}>
                    {status.map(({displayName, name}) =>
                        <option key={name} value={name}>
                            {displayName}
                        </option>)}
                </NativeSelect.Field>
                <NativeSelect.Indicator/>
            </NativeSelect.Root>
        </Field.Root>
    )
}

export default StatusSelect;