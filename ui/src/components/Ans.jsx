/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';

function Ans({ ans }) {
  return (
    <>
      <Box>
        <Typography variant='h5' color='initial'>
          Answer Collection
        </Typography>
        <br />
        <Box>{ans}</Box>
      </Box>
    </>
  );
}

export default Ans;
