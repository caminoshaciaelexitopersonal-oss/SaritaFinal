# SARITA Shared UI Documentation

## Overview
`@sarita/shared-ui` is the unified component library for the SARITA platform. It ensures visual and functional parity across Web (Next.js), Mobile (Expo), and Desktop (Electron).

## Component Architecture
We follow the Atomic Design methodology:
- **Atoms:** Foundational components (Button, Input, Text).
- **Molecules:** Composite components (StatCard, FormField).
- **Organisms:** Complex UI sections (Navbar, Sidebar).
- **Layouts:** Standardized page structures.

## Installation
In your frontend application:
```bash
npm install @sarita/shared-ui
```

## Usage
```tsx
import { Button, ThemeProvider } from '@sarita/shared-ui';

const App = () => (
  <ThemeProvider>
    <Button label="Click Me" onPress={() => console.log('Action')} />
  </ThemeProvider>
);
```

## Theme Customization
The library supports `light`, `dark`, and `institutional` modes via the `ThemeProvider`.

## Storybook
To visualize components during development:
```bash
cd packages/shared-ui
npm run storybook
```
