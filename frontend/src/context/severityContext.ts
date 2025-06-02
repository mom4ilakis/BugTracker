import {createContext} from "react";
import type {Severity} from "@/types.ts";


const SeverityContext = createContext<Severity[]>([]);

export default SeverityContext;