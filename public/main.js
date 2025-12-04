function main(){    

    document.querySelector("#FC").onclick = () => {
        sendCommand("FRONT CAM");
    };
    document.querySelector("#BC").onclick = () => {
        sendCommand("BACK CAM");
    };
    document.querySelector("#SC").onclick = () => {
        sendCommand("SIDE CAM");
    };
    
    document.querySelector("#F").onclick = () => {
        sendCommand("FORWARD");
    };
    document.querySelector("#B").onclick = () => {
        sendCommand("REVERSE");
    };
    document.querySelector("#L").onclick = () => {
        sendCommand("LEFT");
    };
    document.querySelector("#C").onclick = () => {
        sendCommand("CENTER");
    };
    document.querySelector("#R").onclick = () => {
        sendCommand("RIGHT");
    };
   
}

async function sendCommand(command){
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);
    const respArray = responseText.split("?")
    //TODO: Actually show the user on screen
    document.querySelector("#responseText").innerHTML = responseText;

    let headingVal = respArray[1];

    let senseStrVal = respArray[2];

    if (headingVal.includes("-")){
        const infoText = "Heading: " + headingVal.slice(1) + "deg Right     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }
    else if (headingVal == "0"){
        const infoText = "Heading: Straight Ahead     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }
    else{
        const infoText = "Heading: " + headingVal + "deg Left     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }

    //document.querySelector("#scooterInfo").innerHTML = infoText;
}

main();
