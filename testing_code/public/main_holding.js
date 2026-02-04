function main_holding(){    

    document.querySelector("#FC").onclick = () => {
        setCamera("pi");     // Front = Pi camera
    };

    document.querySelector("#BC").onclick = () => {
        setCamera("usb0");   // Back = USB camera 0
    };

    document.querySelector("#SC").onclick = () => {
        setCamera("usb2"); // Side = USB cam 2
    
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

    const forwardBtn = document.querySelector("#F");
    const reverseBtn = document.querySelector("#B");
    let intervalId;

    // .onclick = () => {
    //     sendCommand("FORWARD");
    // };
    // document.querySelector("#B").onclick = () => {
    //     sendCommand("REVERSE");
    // };

    forwardBtn.addEventListener('mousedown', function(){
        sendCommand("FORWARD");
        intervalId = setInterval(sendCommand("FORWARD"),500); //call forward every 500ms
    });
    forwardBtn.addEventListener('mouseup', function() {
        clearInterval(intervalId); //stops the call loop when button released
        #sendCommand("STOP");
    });

    reverseBtn.addEventListener('mousedown', function(){
        sendCommand("REVERSE");
        intervalId = setInterval(sendCommand("REVERSE"),500); //call reverse every 500ms
    });
    reverseBtn.addEventListener('mouseup', function() {
        clearInterval(intervalId); //stops the call loop when button released
        #sendCommand("STOP");
    });


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

    let infoText;

    if (headingVal.includes("-")){
        infoText = "--Heading: " + headingVal.slice(1) + "deg Right     Sensors: " + senseStrVal   
    }
    else if (headingVal == "0"){
        infoText = "--Heading: Straight Ahead     Sensors: " + senseStrVal  
    }
    else{
        infoText = "--Heading: " + headingVal + "deg Left     Sensors: " + senseStrVal    
    }

    document.querySelector("#scooterInfo").innerHTML = infoText;
}

main_holding();
