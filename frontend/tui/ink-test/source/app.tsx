import React, {FC, useState} from 'react';
import {Box, Text, useFocus, useInput} from 'ink';

const TextField: FC<{label: string}> = ({label}) => {
  const {isFocused} = useFocus();
  const [value, setValue] = useState('');

  useInput(
    (input, key) => {
      if (key.backspace || key.delete) {
        setValue(prev => prev.slice(0, -1));
      } else if (input && !key.ctrl && !key.meta) {
        setValue(prev => prev + input);
      }
    },
    {
      isActive: isFocused,
    },
  );

  return (
    <Box>
      <Text color={isFocused ? 'green' : undefined}>
        {label}: {value}
        {isFocused ? '|' : ''}
      </Text>
    </Box>
  );
};

export default function App() {
  return (
    <Box borderStyle={'round'} flexDirection="column" width={35}>
      <Text dimColor>用 Tab 切换输入框。</Text>
      <TextField label="用户名" />
      <TextField label="密码" />
      <TextField label="邮箱" />
    </Box>
  );
}
