import React, {useRef, useState} from 'react';
import {Button, Typography} from "@mui/material";
import useStyles from "./styles";

let openButton = {
        background: "#00F43A",
        borderRadius: "20px",
        fontFamily: 'Nunito',
        fontStyle: "normal",
        fontWeight: 400,
        fontSize: "24px",
        lineHeight: "33px",
        color: "#181818"
}
const FileUpload = () => {

    const classes = useStyles();
    const fileInputRef = useRef(null)
    const [filename, setFilename] = useState(null)

    function handleClick(){
        console.log(fileInputRef.current.files[0])
    }

    return (
        <div className={classes.container}>
            <p className={classes.title}>Классификация обращений</p>
            <div className={classes.sendContainer}>
                <div className={classes.fileNameContainer}>{filename || "выберите файл для отправки"}</div>
                <Button
                    className={classes.openButton}
                >
                    Выбрать файл
                    <input type="file" hidden onChange={(e) => {
                        if (!!e.target.files[0]) {
                            setFilename(e.target.files[0].name)
                        }
                    }}
                    />
                </Button>
            </div>
        </div>
    );
};

export default FileUpload;
