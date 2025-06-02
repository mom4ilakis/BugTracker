import {createContext} from "react";
import type {CurrentUser} from "@/types.ts";


const CurrentUserContext = createContext<CurrentUser | null>(null);

export default CurrentUserContext;