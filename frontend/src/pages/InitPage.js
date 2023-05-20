import React from 'react';
import {Button} from "@mui/material";
import useStyles from "./styles";
import FileUpload from "../components/FileUpload/FileUpload";

const InitPage = () => {

    const classes = useStyles();

    return (
        <div style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}}>
            <FileUpload/>
        </div>
    );
};

export default InitPage;
