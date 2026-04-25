import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';
import { spawn } from 'child_process';

const isDev = require('electron-is-dev');

let mainWindow: BrowserWindow | null;

function createWindow(): void {
  mainWindow = new BrowserWindow({
    width: 500,
    height: 750,
    minWidth: 500,           // Minimum width - prevents window from being too narrow
    minHeight: 750,          // Minimum height - prevents window from being too short
    maxWidth: 1200,          // Maximum width - prevents window from being too wide
    maxHeight: 900,          // Maximum height - prevents window from being too tall
    frame: false,            // Remove default window frame
    transparent: false,      // Keep opaque background
    titleBarStyle: 'hidden', // Hide title bar
    resizable: true,         // Allow resizing but within the min/max bounds
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: false,
    },
  });

  const startURL = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startURL);

  // Get the absolute paths - go up two levels: one from dist/ to koki/, and one from koki/ to project root
  const rootDir = path.join(__dirname, '..', '..');
  const pythonScriptPath = path.join(rootDir, 'main.py');
  console.log('Root directory:', rootDir);
  console.log('Python script path:', pythonScriptPath);

  // Spawn Python process with correct working directory
  const pythonProcess = spawn('python', [pythonScriptPath], {
    stdio: ['inherit', 'pipe', 'pipe'],
    cwd: rootDir, // Set working directory to the root of the project
    env: {
      ...process.env,
      PYTHONUNBUFFERED: '1' // This ensures Python output isn't buffered
    }
  });

  // Forward Python logs to renderer
  pythonProcess.stdout.on('data', (data) => {
    const message = data.toString();
    console.log('Python stdout:', message);
    if (mainWindow) {
      mainWindow.webContents.send('python-log', message);
    }
  });

  pythonProcess.stderr.on('data', (data) => {
    const message = data.toString();
    console.error('Python stderr:', message);
    if (mainWindow) {
      mainWindow.webContents.send('python-error', message);
    }
  });

  pythonProcess.on('error', (error) => {
    console.error('Failed to start Python process:', error);
  });

  pythonProcess.on('exit', (code, signal) => {
    console.log(`Python process exited with code ${code} and signal ${signal}`);
    if (mainWindow) {
      mainWindow.webContents.send('python-error', `Python process exited with code ${code}`);
    }
  });

  // Send a test message to verify IPC is working
  setTimeout(() => {
    if (mainWindow) {
      mainWindow.webContents.send('python-log', 'Test message from Electron');
    }
  }, 2000);

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
