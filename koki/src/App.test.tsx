import { render, screen } from '@testing-library/react';
import App from './App';

// Mock the MicVAD component since it likely uses browser APIs not available in tests
jest.mock('./components/MicVAD', () => ({
  MicVAD: ({ onUpdate }: any) => <div data-testid="mic-vad">MicVAD Component</div>
}));

test('renders HUD Container with JARVIS', () => {
  render(<App />);
  const jarvisElement = screen.getByText(/J.A.R.V.I.S/i);
  expect(jarvisElement).toBeInTheDocument();
});

test('renders controls', () => {
  render(<App />);
  const muteButton = screen.getByRole('button', { name: /mute/i });
  expect(muteButton).toBeInTheDocument();
});
