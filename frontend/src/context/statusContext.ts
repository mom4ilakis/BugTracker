import {createContext} from "react";
import type {Status} from "@/types.ts";


const StatusContext = createContext<Status[]>([]);

export default StatusContext;