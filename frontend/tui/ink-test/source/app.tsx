import React, {useEffect, useState} from 'react';
import {Box, Spacer, Text, useApp} from 'ink';

export default function App() {
  const [counter, setCounter] = useState(0);

  // 获取退出方法
  const {exit} = useApp();

  useEffect(() => {
    const timer = setInterval(() => setCounter(prev => prev + 1), 100);
    return () => clearInterval(timer);
  }, []);

  // 监听 到达一个数字就退出程序
  useEffect(() => {
    if (counter >= 10) exit();
  }, [counter, exit]);

  return (
    <Box borderStyle={'round'} marginX={2} flexDirection="column">
      <Box width={'100%'}>
        <Text>Counter</Text>
        <Spacer />
        <Text>{counter}</Text>
      </Box>
      {counter >= 10 && <Text color={'green'}>Done !</Text>}
    </Box>
  );
}
