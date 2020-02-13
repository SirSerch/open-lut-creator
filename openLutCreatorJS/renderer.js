const remote = require('electron').remote;

// When document has loaded, initialise
document.onreadystatechange = () => {
    if (document.readyState == "complete") {
        handleWindowControls();
    }
};

function handleWindowControls() {

    let win = remote.getCurrentWindow();
    // Make minimise/maximise/restore/close buttons work when they are clicked
    document.getElementById('min').addEventListener("click", event => {
        win.minimize();
    });

    document.getElementById('close').addEventListener("click", event => {
        win.close();
    });

}