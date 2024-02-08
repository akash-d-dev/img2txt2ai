/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';

function Ques({ ques }) {
  return (
    <>
      <Box>
        <Typography variant='h5' color='initial'>
          Questions Collection
        </Typography>
        <br />
        <Box>{ques}</Box>
      </Box>
    </>
  );
}

export default Ques;
