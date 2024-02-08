/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';
import ResFormatter from '../utils/ResFormatter';

function AnsBard({ ans }) {
  return (
    <>
      <Box>
        <Typography variant='h6'>Answer Collection</Typography>
        <br />
        <Box>
          {/* <Typography
            variant='body2'
            dangerouslySetInnerHTML={{ __html: ans }}
          /> */}
          Comming soon...
        </Box>
      </Box>
    </>
  );
}

export default AnsBard;
