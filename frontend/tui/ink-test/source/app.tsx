import React, {useState} from 'react';
import {Box, Text, useApp, useInput} from 'ink';

const items = ['查看状态', '部署', '回滚', '退出'];

export default function App() {
  const [selected, setSelected] = useState(0);
  const {exit} = useApp();

  useInput((input, key) => {
    if (key.upArrow) {
      setSelected(prev => (prev - 1 >= 0 ? prev - 1 : prev));
    }
    if (key.downArrow) {
      setSelected(prev => (prev + 1 < items.length ? prev + 1 : prev));
    }
    if (key.return) {
      if (items[selected] == '退出') exit();
    }
    if (input === 'q') exit();
  });

  return (
    <Box borderStyle={'round'} flexDirection="column" width={35}>
      <Text>用 上下 选择，回车确认，q 退出</Text>
      {items.map((item, i) => (
        <Text key={item} color={i == selected ? 'green' : undefined}>
          {i === selected ? '> ' : '  '}
          {item}
        </Text>
      ))}
    </Box>
  );
}
