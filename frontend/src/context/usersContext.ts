import {createContext} from "react";
import type {User} from "@/types.ts";


const UsersContext = createContext<User[]>([]);

export default UsersContext;