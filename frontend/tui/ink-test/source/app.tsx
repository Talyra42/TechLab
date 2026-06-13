import React, {useEffect, useState} from 'react';
import {Box, Text} from 'ink';

export default function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCount(prev => prev + 1);
    }, 100);

    return () => clearInterval(timer);
  }, []);

  return (
    <Box flexDirection="column" borderStyle="round" paddingX={1} width={42}>
      <Box justifyContent="space-between">
        <Text color="magenta">Counter</Text>
        <Text dimColor>{count}</Text>
      </Box>
    </Box>
  );
}
