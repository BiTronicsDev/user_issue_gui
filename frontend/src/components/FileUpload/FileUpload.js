import React, {useRef, useState} from 'react';
import {Button, Typography} from "@mui/material";
import useStyles from "./styles";

const FileUpload = (props) => {

    const classes = useStyles();
    const fileInputRef = useRef(null)
    const [filename, setFilename] = useState(null)

    function handleClick(){
        console.log(fileInputRef.current.files[0])
        props.setStateScreen(1)
    }

    return (
        <div className={classes.container}>
            <p className={classes.title}>Классификация обращений</p>
            <div className={classes.sendContainer}>
                <div className={classes.fileNameContainer}>{filename || "выберите файл для отправки"}</div>
                <Button
                    component="label"
                    style={openButton}
                >
                    Обзор
                    <input type="file" ref={fileInputRef} hidden onChange={(e) => {
                        if (!!e.target.files[0]) {
                            setFilename(e.target.files[0].name)
                        }
                    }}
                    />
                </Button>
            </div>
            <Button onClick={handleClick} style={sendButton}>
                Обработать датасет
            </Button>
        </div>
    );
};

export default FileUpload;


let openButton = {
    background: "#00F43A",
    borderRadius: "20px",
    fontFamily: 'Nunito',
    fontStyle: "normal",
    fontWeight: 600,
    fontSize: "16px",
    lineHeight: "33px",
    color: "#181818",
    marginLeft: "10px",
    height: "8vh"
}

let sendButton = {
    marginTop: "10vh",
    background: "#39393A",
    borderRadius: "20px",
    fontFamily: 'Nunito',
    fontsStyle: "normal",
    fontWeight: "600",
    fontSize: "16px",
    lineHeight: "33px",
    color: "#00F43A",
}
