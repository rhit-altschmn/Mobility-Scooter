
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
        const infoText = "~Heading: " + headingVal.slice(1) + "deg Right     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }
    else if (headingVal == "0"){
        const infoText = "~Heading: Straight Ahead     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }
    else{
        const infoText = "~Heading: " + headingVal + "deg Left     Sensors: " + senseStrVal
        document.querySelector("#scooterInfo").innerHTML = infoText;
    }

    //document.querySelector("#scooterInfo").innerHTML = infoText;
}

main();

/*
// main.js

// Helper: update text on page
function setResponseText(msg) {
    const p = document.getElementById('responseText');
    if (p) p.textContent = msg;
}

function setScooterInfo(heading, dists) {
    const p = document.getElementById('scooterInfo');
    if (p) p.textContent = `Heading: ${heading}  Sensors: ${dists}`;
}

// ---- CAMERA CONTROL ----

// Call the Flask /set_camera/<cam> endpoint
function setCamera(camName) {
    fetch(`/set_camera/${camName}`, {
        method: 'POST'
    })
    .then(res => {
        if (!res.ok) {
            throw new Error('Failed to set camera');
        }
        setResponseText(`Active camera: ${camName}`);
    })
    .catch(err => {
        console.error(err);
        setResponseText('Error switching camera');
    });
}

// ---- SCOOTER DRIVE CONTROL ----

// Call the Flask /api/<command> endpoint
function sendDriveCommand(command) {
    fetch(`/api/${command}`)
        .then(res => res.text())
        .then(text => {
            // Expected format: resp_cmd?heading?dists
            setResponseText(`Drive response: ${text}`);

            const parts = text.split('?');
            if (parts.length >= 3) {
                const heading = parts[1];
                const dists = parts[2];
                setScooterInfo(heading, dists);
            }
        })
        .catch(err => {
            console.error(err);
            setResponseText('Error sending drive command');
        });
}

// ---- WIRE UP BUTTONS AFTER DOM IS READY ----
document.addEventListener('DOMContentLoaded', () => {

    // Camera buttons
    const btnFront = document.getElementById('FC');
    const btnBack  = document.getElementById('BC');
    const btnSide  = document.getElementById('SC');

    if (btnFront) btnFront.addEventListener('click', () => setCamera('pi'));    // front = Pi cam
    if (btnBack)  btnBack.addEventListener('click', () => setCamera('usb2'));  // back = USB2
    if (btnSide)  btnSide.addEventListener('click', () => setCamera('usb0'));  // side = USB0

    // Drive buttons
    const btnF = document.getElementById('F');
    const btnB = document.getElementById('B');
    const btnL = document.getElementById('L');
    const btnR = document.getElementById('R');
    const btnC = document.getElementById('C');

    // Here "F", "B", etc must match what scooterController.controlCommand() expects
    if (btnF) btnF.addEventListener('click', () => sendDriveCommand('F'));
    if (btnB) btnB.addEventListener('click', () => sendDriveCommand('B'));
    if (btnL) btnL.addEventListener('click', () => sendDriveCommand('L'));
    if (btnR) btnR.addEventListener('click', () => sendDriveCommand('R'));
    if (btnC) btnC.addEventListener('click', () => sendDriveCommand('C'));
});
*/
