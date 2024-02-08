import { Box, Button } from '@mui/material';
import axios from 'axios';
import { useEffect, useState } from 'react';
import Ques from '../components/Ques';
import Ans from '../components/Ans';
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
    // left: '50%',
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

  const handleClick = (v) => {
    // console.log(e);
    setActive(v);
    console.log(v);
  };

  return (
    <>
      <Box>
        {loading ? 'Loading...' : error && `Someting went wrong:${error}`}
        {!loading && !error && active === 0 && <Ques ques={quesFile} />}
        <br />
        {!loading && !error && active === 1 && <Ans ans={ansFile} />}
        <br />
        {/* {!loading && !error && active === 0 && <Ques ques={quesFile} />} */}
      </Box>

      <Button
        variant='contained'
        sx={{ ...buttonContainerStyle, left: 100 }}
        onClick={() => handleClick(0)}
      >
        Ques
      </Button>
      <Button
        variant='contained'
        sx={{ ...buttonContainerStyle, left: 200 }}
        onClick={() => handleClick(1)}
      >
        Ans
      </Button>
      <Button
        variant='contained'
        sx={{ ...buttonContainerStyle, left: 300 }}
        onClick={() => handleClick(2)}
      >
        Raw
      </Button>
    </>
  );
}

export default Home;
