#!/usr/bin/env node
import React from 'react';
import {render} from 'ink';
import App from './app.js';

const {waitUntilExit} = render(<App />);

try {
  await waitUntilExit();
} catch (err) {
  console.error(err);
  process.exitCode = 1;
}
