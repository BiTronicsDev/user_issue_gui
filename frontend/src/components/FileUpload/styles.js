import { makeStyles } from "@mui/styles";


export default makeStyles(theme => ({

    textFileName: {
        fontSize: 18,
        fontWeight: 400,
        fontFamily: "Roboto",
        lineHeight: 1,
    },

    checkButtonWt: {
        cursor: "pointer",
        appearance: "none",
        borderRadius: "4px",
        background: "#ffffff",
        float: "left",
        color: "#1565C0",
        width: "200px",
        height: "44px",
        fontSize: "16px",
        border: "1px solid #1564c0",
        textTransform: "uppercase",
        fontWeight: 400,
        fontFamily: "Roboto",
    },


    testButtonSubmit: {
        cursor: "pointer",
        appearance: "none",
        borderRadius: "4px",
        background: "#1665c1",
        color: "#ffffff",
        width: "200px",
        height: "44px",
        fontSize: "16px",
        border: "1px solid #1665c1",
        textTransform: "uppercase",
        fontWeight: 400,
        fontFamily: "Roboto",
        "&:hover":{
            background: "#115eb6",
            borderColor: "#115eb6",
            color: "#ffffff",
        },
        "&:disabled":{
            background: "#ebebeb",
            borderColor: "#98999d",
            color: "#98999d",
        },
    },

    container: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-start",
        alignItems: "center",
        marginTop: "10vh",
        borderRadius: "50px",
        background: "#181818",
        width: "50vw",
        height: "50vh",
        marginBottom: "10vh",
    },

    title: {
        fontStyle: "normal",
        fontWeight: 400,
        fontSize: 40,
        color: "#00F43A",
        fontFamily: "Nunito",
    },

    sendContainer: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center"
    },

    fileNameContainer: {
        width: "30vw",
        height: "8vh",
        background: "#39393A",
        borderRadius: 20,
        display:"flex",
        flexDirection:"row",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: 'Nunito',
        fontStyle: "normal",
        fontWeight: 400,
        fontSize: "24px",
        lineHeight: "33px",
        color: "#E6E6E6"
    },

    openButton: {
        background: "#00F43A",
        borderRadius: "20px",
        fontFamily: 'Nunito',
        fontStyle: "normal",
        fontWeight: 400,
        fontSize: "24px",
        lineHeight: "33px",
        color: "#181818"
    }
}))

