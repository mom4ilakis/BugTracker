import {createContext} from "react";
import type {Priority} from "@/types.ts";


const PriorityContext = createContext<Priority[]>([]);

export default PriorityContext;