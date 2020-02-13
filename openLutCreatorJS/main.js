const {app, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');

let main;

function App(){
    main = new BrowserWindow({
        width: 600,
        height: 400,
        backgroundColor: '#37474f',
        center: true,
        resizable: false,
        frame: false
    });
    main.loadFile('views/main.html');

}

app.on('ready', App);

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin'){
        app.quit();
    }

});