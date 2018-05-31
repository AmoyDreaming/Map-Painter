const { app, BrowserWindow, Menu } = require('electron');

let win;

app.on('ready', () => {
    // init window
    Menu.setApplicationMenu(null);
    win = new BrowserWindow({
        width: 1920,
        height: 1080,
    });
    win.loadURL('file://' + __dirname + '/index.html');
    win.webContents.openDevTools();
});