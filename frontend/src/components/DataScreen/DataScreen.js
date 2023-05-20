import React from 'react';
import useStyles from "./styles";
import {Button} from "@mui/material";
import iconBack from "../../images/IconBack.svg"

const DataScreen = (props) => {

    const classes = useStyles();

    function goToBack(){
        props.setStateScreen(0)
    }

    return (
        <div className={classes.container}>
            <div style={{display: "flex", flexDirection: "row", justifyContent: "center", alignItems: "center"}}>
                <img onClick={goToBack} style={{
                    marginTop: 20,
                    marginBottom: 20,
                    width: 30,
                    height: 60,
                }} src={iconBack}/>
                <Button style={downloadButton}>
                    Скачать обработанный датасет
                </Button>
            </div>
        </div>
    );
};

export default DataScreen;

let downloadButton = {
    marginTop: 20,
    marginBottom: 20,
    background: "#00F43A",
    borderRadius: "20px",
    fontFamily: 'Nunito',
    fontStyle: "normal",
    fontWeight: 600,
    fontSize: "16px",
    lineHeight: "33px",
    color: "#181818",
    marginLeft: "10px",
    height: "5vh"
}
