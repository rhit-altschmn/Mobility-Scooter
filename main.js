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

async function sendCommand(command){
    let response = await fetch(`/api/${command}`);
    let responseText = await response.text();
    console.log(responseText);
    const respArray = responseText.split("?")
    //TODO: Actually show the user on screen
    document.querySelector("#responseText").innerHTML = responseText;
    
    const infoText = "Heading: " + respArray[1] + "  Sensors: " + respArray[2]
    document.querySelector("#scooterInfo").innerHTML = infoText;
}

main();