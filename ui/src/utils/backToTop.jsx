import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import { Button } from '@mui/material';

const BacktoTop = () => {
  const scrollUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  };

  return (
    <Button
      variant='contained'
      size='small'
      sx={{
        borderRadius: '50%',
        minWidth: 0,
        p: 0.75,
        position: 'fixed',
        bottom: '80px',
        left: '50%',
        zIndex: '100',
        opacity: '0.5',
      }}
      onClick={scrollUp}
    >
      <KeyboardArrowUpIcon />
    </Button>
  );
};

export default BacktoTop;
