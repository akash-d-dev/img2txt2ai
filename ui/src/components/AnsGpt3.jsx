/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material';
import ResFormatter from '../utils/ResFormatter';

function AnsGpt3({ ans }) {
  return (
    <>
      <Box>
        <Typography variant='h6'>Answer Collection - GPT-3.5 Turbo</Typography>
        <br />
        <Box>
          <Typography
            variant='body2'
            dangerouslySetInnerHTML={{ __html: ans }}
          />
        </Box>
      </Box>
    </>
  );
}

export default AnsGpt3;
