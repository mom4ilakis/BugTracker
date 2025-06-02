import {Field, NativeSelect} from "@chakra-ui/react";
import {useContext} from "react";
import SeverityContext from "@/context/severityContext.ts";

type Props = {
    selected?: string;
};

function SeveritySelect({selected = "MEDIUM"}: Props) {
    const severity = useContext(SeverityContext);
    return (
        <Field.Root>
            <Field.Label>Severity</Field.Label>
            <NativeSelect.Root>
                <NativeSelect.Field id="severity" defaultValue={selected}>
                    {severity.map(({displayName, name}) =>
                        <option key={name} value={name}>
                            {displayName}
                        </option>
                    )}
                </NativeSelect.Field>
                <NativeSelect.Indicator/>
            </NativeSelect.Root>

        </Field.Root>
    )
}

export default SeveritySelect;
