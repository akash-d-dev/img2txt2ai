import { Box, Button } from '@mui/material';
import axios from 'axios';
import { useEffect, useState } from 'react';
import Ques from '../components/Ques';
import AnsGpt3 from '../components/AnsGpt3';
import AnsBard from '../components/AnsBard';
// import {Button} from '@mui/material';

function Home() {
  const [active, setActive] = useState(0);
  const [quesFile, setQuesFile] = useState('');
  const [ansFile, setAnsFile] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const buttonContainerStyle = {
    position: 'fixed',
    bottom: '20px',
    transform: 'translateX(-50%)',
    display: 'flex',
    gap: '10px',
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://127.0.0.1:8000');
        setQuesFile(response.data.qna_content);
        setAnsFile(response.data.ans_content);
      } catch (error) {
        console.error(error);
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <>
      <Box display={'flex'} my={2} mx={1}>
        {loading ? 'Loading...' : error && `Someting went wrong:${error}`}
        {!loading && !error && active === 0 && <Ques ques={quesFile} />}
        <br />
        {!loading && !error && active === 1 && <AnsGpt3 ans={ansFile} />}
        <br />
        {!loading && !error && active === 2 && <AnsBard ans={quesFile} />}
      </Box>

      <Button
        variant='contained'
        color={active === 0 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 100 }}
        onClick={() => setActive(0)}
      >
        Ques
      </Button>
      <Button
        variant='contained'
        color={active === 1 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 200 }}
        onClick={() => setActive(1)}
      >
        Gpt3
      </Button>
      <Button
        variant='contained'
        color={active === 2 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 300 }}
        onClick={() => setActive(2)}
      >
        Bard
      </Button>
    </>
  );
}

export default Home;
