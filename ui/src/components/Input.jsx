import React, { useRef } from 'react';
import { IconButton, TextField } from '@mui/material';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
const InputBox = ({ sendTexttoServer, loading }) => {
  const inputStyles = {
    position: 'fixed',
    bottom: '10px',
    transform: 'translateX(-50%)',
    display: 'flex',
    gap: '10px',
    left: '171px',
  };
  const inputRef = useRef('');

  return (
    <>
      <TextField
        aria-label='input'
        multiline
        inputRef={inputRef}
        disabled={loading}
        placeholder='Paste to transfer'
        sx={{
          ...inputStyles,
          width: '333px',
          zIndex: 10,
          bgcolor: 'white',
        }}
        maxRows={22}
      />
      <IconButton
        size='medium'
        disabled={loading}
        onClick={() => sendTexttoServer(inputRef.current.value)}
        sx={{
          ...inputStyles,
          left: 363,
          bottom: 16,
          padding: 1.25,
          borderRadius: '20%',
          color: 'white',
          bgcolor: 'primary.main',
        }}
      >
        <ArrowUpwardIcon />
      </IconButton>
    </>
  );
};

export default InputBox;
