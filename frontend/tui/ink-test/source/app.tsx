import React from 'react';
import {Text, Box} from 'ink';

type Props = {};

export default function App({}: Props) {
  return (
    <>
      <Box
        justifyContent="center"
        borderStyle="single"
        borderBottom={false}
        borderTopColor={'green'}
      >
        <Text>普通单线</Text>
      </Box>
      <Box
        justifyContent="center"
        borderStyle="double"
        borderTop={false}
        borderBottomColor={'blue'}
      >
        <Text>双线</Text>
      </Box>
    </>
  );
}
