import {Text, useFocus} from 'ink';
import React from 'react';
import {FC} from 'react';

const Field: FC<{label: string}> = ({label}) => {
  // 调用这个 hook，组件就变成可聚焦的了
  const {isFocused} = useFocus();

  return (
    <Text color={isFocused ? 'green' : undefined}>
      {isFocused ? '> ' : '  '}
      {label}
    </Text>
  );
};

export default Field;
