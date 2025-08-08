import { render, screen } from '@testing-library/react';
import JarvisHUD from './JarvisHUD';

test('renders JarvisHUD component with default props', () => {
  render(<JarvisHUD mode="idle" />);
  const jarvisText = screen.getByText(/J.A.R.V.I.S/i);
  expect(jarvisText).toBeInTheDocument();
});

test('JarvisHUD renders without crashing', () => {
  render(<JarvisHUD mode="idle" />);
  // Test passes if component renders without throwing an error
  expect(screen.getByText(/J.A.R.V.I.S/i)).toBeInTheDocument();
});

test('renders with different modes', () => {
  const modes = ['idle', 'listening', 'speaking', 'thinking'] as const;
  
  modes.forEach(mode => {
    const { unmount } = render(<JarvisHUD mode={mode} />);
    expect(screen.getByText(/J.A.R.V.I.S/i)).toBeInTheDocument();
    unmount();
  });
});

test('renders with custom label', () => {
  render(<JarvisHUD mode="idle" label="FRIDAY" />);
  expect(screen.getByText(/FRIDAY/i)).toBeInTheDocument();
});

test('renders with volume prop', () => {
  render(<JarvisHUD mode="speaking" volume={0.5} />);
  expect(screen.getByText(/J.A.R.V.I.S/i)).toBeInTheDocument();
});

test('renders with custom size', () => {
  render(<JarvisHUD mode="idle" size={400} />);
  // Just test that the component renders successfully with custom size
  expect(screen.getByText(/J.A.R.V.I.S/i)).toBeInTheDocument();
});
