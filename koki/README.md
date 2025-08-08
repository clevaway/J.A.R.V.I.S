# Jarvis UI - Electron + React TypeScript

> **Status: 🚧 Still working on this, will perfect it before integrating**

This is the **ui directory** for this Jarvis repository. Built with Electron and React using TypeScript for a modern, type-safe desktop application experience.

## Preview
(Not final, I'm open to suggestions)

<img width="1431" height="743" alt="image" src="https://github.com/user-attachments/assets/cc7965bc-60e5-455e-8df6-cd98b7d94551" />

## 🚀 Quick Start

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Setup & Run

```bash
# Install dependencies
npm install

# Start development mode (React dev server + Electron)
npm run electron:dev
```

## 📋 Available Commands

```bash
# Development
npm run electron:dev    # Start React dev server + Electron
npm start              # Just React development server
npm run electron       # Just Electron (after building)

# Building
npm run build          # Build React app for production
npm run build:electron # Compile Electron TypeScript
npm run electron:pack  # Package for distribution

# Testing
npm test               # Run all tests
npm test -- --coverage # Run with coverage report
```

## 🧪 Testing

- Component tests use `.test.tsx` extension
- Uses React Testing Library
- Run `npm test` to execute all tests

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with TypeScript
4. Add/update tests
5. Run `npm test` to ensure tests pass
6. Submit a pull request

### Code Guidelines

- Use TypeScript for all components
- Write tests for new features
- Follow React functional component patterns

## 🐛 Troubleshooting

**TypeScript errors:** `npm install` and check `npm ls typescript`
**Electron won't start:** Run `npm run build:electron` first
**Test failures:** Try `npm run test -- --clearCache`
