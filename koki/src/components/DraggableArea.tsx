import React from 'react';

interface DraggableAreaProps {
  className?: string;
  children?: React.ReactNode;
}

export default function DraggableArea({ className = '', children }: DraggableAreaProps) {
  return (
    <div 
      className={`fixed top-0 left-0 w-full h-12 z-40 ${className}`}
      style={{ WebkitAppRegion: 'drag' } as any}
    >
      {children}
    </div>
  );
}
