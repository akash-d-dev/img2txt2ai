/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';
import ResFormatter from '../utils/ResFormatter';

function AnsBard({ ans }) {
  return (
    <>
      <Box>
        <Typography variant='h6'>
          Answer Collection - Bard Gemini Pro
        </Typography>
        <br />
        <Box>
          {/* <Typography
            variant='body1'
            dangerouslySetInnerHTML={{ __html: ans }}
          /> */}
          Comming soon...
        </Box>
      </Box>
    </>
  );
}

export default AnsBard;
