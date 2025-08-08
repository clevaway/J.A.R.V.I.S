import { app, BrowserWindow } from 'electron';
import * as path from 'path';

const isDev = require('electron-is-dev');

let mainWindow: BrowserWindow | null;

function createWindow(): void {
  mainWindow = new BrowserWindow({
    width: 500,
    height: 600,
    minWidth: 500,           // Minimum width - prevents window from being too narrow
    minHeight: 600,          // Minimum height - prevents window from being too short
    maxWidth: 1200,          // Maximum width - prevents window from being too wide
    maxHeight: 900,          // Maximum height - prevents window from being too tall
    frame: false,            // Remove default window frame
    transparent: false,      // Keep opaque background
    titleBarStyle: 'hidden', // Hide title bar
    resizable: true,         // Allow resizing but within the min/max bounds
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  const startURL = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startURL);

  mainWindow.on('closed', () => (mainWindow = null));
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
