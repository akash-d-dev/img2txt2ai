/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';
import ResFormatter from '../utils/ResFormatter';

function Ques({ ques }) {
  return (
    <>
      <Box>
        <Typography variant='h6' color='initial'>
          Questions Collection
        </Typography>
        <br />
        <Box>
          <Typography
            variant='body1'
            color='initial'
            dangerouslySetInnerHTML={{ __html: ques }}
          />
        </Box>
      </Box>
    </>
  );
}

export default Ques;
