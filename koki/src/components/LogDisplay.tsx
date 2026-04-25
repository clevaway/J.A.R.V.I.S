import React, { useEffect, useState } from 'react';

// Safe electron import
const electron = window.require ? window.require('electron') : null;
const ipcRenderer = electron ? electron.ipcRenderer : null;

interface IpcEvent {
  sender: unknown;
  senderId: number;
}

export function LogDisplay() {
  const [logs, setLogs] = useState<string[]>([]);
  const logsContainerRef = React.useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when logs change
  useEffect(() => {
    if (logsContainerRef.current) {
      logsContainerRef.current.scrollTop = logsContainerRef.current.scrollHeight;
    }
  }, [logs]);

  useEffect(() => {
    if (!ipcRenderer) {
      console.error('IPC Renderer not available');
      return;
    }

    // Debug message to confirm component mount
    console.log('LogDisplay mounted, setting up IPC listeners');

    // Listen for Python logs
    ipcRenderer.on('python-log', (_event: IpcEvent, message: string) => {
      console.log('Received python-log:', message);
      
      // Filter out audio-related logs
      if (!message.includes('Saying:') && 
          !message.includes('Playing audio') && 
          !message.includes('Generated audio')) {
        setLogs(prev => [...prev, message].slice(-100)); // Keep last 100 logs
      }
    });

    // Listen for Python errors
    ipcRenderer.on('python-error', (_event: IpcEvent, message: string) => {
      console.log('Received python-error:', message);
      setLogs(prev => [...prev, `Error: ${message}`].slice(-100));
    });

    return () => {
      ipcRenderer.removeAllListeners('python-log');
      ipcRenderer.removeAllListeners('python-error');
    };
  }, []);

  return (
    <div 
      ref={logsContainerRef}
      className="mt-4 w-full max-h-36 overflow-y-auto bg-black/20 rounded-lg p-2 text-xs font-mono scroll-smooth"
    >
      {logs.map((log, index) => (
        <div key={index} className="text-gray-300 whitespace-pre-wrap">
          {log}
        </div>
      ))}
    </div>
  );
}
