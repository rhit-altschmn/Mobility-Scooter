function main(){    

    document.querySelector("#FC").onclick = () => {
        setCamera("pi");     // Front = Pi camera
    };

    document.querySelector("#BC").onclick = () => {
        setCamera("usb2");   // Back = USB camera 2
    };

    document.querySelector("#SC").onclick = () => {
        setCamera("usb0"); 
    
    };
    
    document.querySelector("#F").onclick = () => {
        sendCommand("FORWARD");
    };
    document.querySelector("#B").onclick = () => {
        sendCommand("BACKWARD");
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
async function setCamera(camName){
    try {
        let response = await fetch(`/set_camera/${camName}`, {
            method: "POST"
        });

        if (!response.ok) {
            throw new Error("Failed to switch camera");
        }

        document.querySelector("#responseText").innerHTML =
            "Active Camera: " + camName;

    } catch (err) {
        console.error(err);
        document.querySelector("#responseText").innerHTML =
            "Camera switch failed";
    }
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
