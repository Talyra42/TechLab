import React from 'react';
import {Text, Box} from 'ink';

type Props = {};

export default function App({}: Props) {
  return (
    <>
      <Box width={7} flexDirection="column">
        {/* 后面省略号 */}
        <Text wrap="truncate-end">Hello World</Text>
        {/* 前面省略号 */}
        <Text wrap="truncate-start">Hello World</Text>
        {/* 中间省略号 */}
        <Text wrap="truncate-middle">Hello World</Text>
      </Box>
    </>
  );
}
