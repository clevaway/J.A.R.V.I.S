import { render, screen } from '@testing-library/react';
import JarvisHUD from './JarvisHUD';

test('renders JarvisHUD component', () => {
  render(<JarvisHUD />);
  const jarvisText = screen.getByText(/J.A.R.V.I.S/i);
  expect(jarvisText).toBeInTheDocument();
});

test('JarvisHUD renders without crashing', () => {
  render(<JarvisHUD />);
  // Test passes if component renders without throwing an error
  expect(screen.getByText(/J.A.R.V.I.S/i)).toBeInTheDocument();
});
