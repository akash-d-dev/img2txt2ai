import { Box, Button, IconButton } from '@mui/material';
import axios from 'axios';
import { useEffect, useState } from 'react';
import Ques from '../components/Ques';
import AnsGpt3 from '../components/AnsGpt3';
import AnsBard from '../components/AnsBard';
import ContentPasteGoIcon from '@mui/icons-material/ContentPasteGo';
import AutorenewIcon from '@mui/icons-material/Autorenew';
import InputBox from '../components/Input';
// import AddIcon from '@mui/icons-material/Add';
// import {Button} from '@mui/material';

function Home() {
  //  const urlNetwork = 'http://192.168.56.1:8000';
  // const urlNetwork = 'http://192.168.19.66:8000';
  const urlNetwork = 'http://localhost:8008';
  // const urlNetwork = 'https://lucid-wave-72717.pktriot.net';

  const [active, setActive] = useState(0);
  const [quesFile, setQuesFile] = useState('');
  const [ansFile, setAnsFile] = useState({
    ans_gpt: '',
    ans_gemini: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [inputBox, setInputBox] = useState(false);

  const buttonContainerStyle = {
    position: 'absolute',
    top: '12px',
    transform: 'translateX(-0%)',
    display: 'flex',
    gap: '10px',
  };

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await axios.get(urlNetwork);
      setQuesFile(response.data.qna_content);
      setAnsFile({
        ans_gpt: response.data.ans_content_gpt,
        ans_gemini: response.data.ans_content_gemini,
      });
    } catch (error) {
      console.error(error);
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  const sendTexttoServer = async (text) => {
    try {
      setLoading(true);
      await axios.post(urlNetwork, {
        text,
      });
    } catch (error) {
      console.error(error);
      setError(error);
    } finally {
      setLoading(false);
      setInputBox(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <IconButton
        disabled={loading}
        color='primary'
        onClick={fetchData}
        sx={{
          mx: 2,
          mt: 2,
          width: 30,
          height: 30,
        }}
      >
        <AutorenewIcon />
      </IconButton>
      <IconButton
        disabled={loading}
        color='primary'
        onClick={() => setInputBox(!inputBox)}
        sx={{
          mx: 0,
          mt: 2,
          width: 30,
          height: 30,
        }}
      >
        <ContentPasteGoIcon />
      </IconButton>

      <Button
        variant='contained'
        color={active === 0 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 150 }}
        onClick={() => setActive(0)}
      >
        Ques
      </Button>
      <Button
        variant='contained'
        color={active === 1 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 230 }}
        onClick={() => setActive(1)}
      >
        Gpt3
      </Button>
      <Button
        variant='contained'
        color={active === 2 ? 'secondary' : 'primary'}
        disableElevation
        disableTouchRipple
        sx={{ ...buttonContainerStyle, left: 310 }}
        onClick={() => setActive(2)}
      >
        Bard
      </Button>
      {inputBox && (
        <InputBox sendTexttoServer={sendTexttoServer} loading={loading} />
      )}

      <Box display={'flex'} mt={2} mb={12} mx={1}>
        {loading ? 'Loading...' : error && `Someting went wrong:${error}`}
        {!loading && !error && active === 0 && <Ques ques={quesFile} />}
        <br />
        {!loading && !error && active === 1 && (
          <AnsGpt3 ans={ansFile.ans_gpt} />
        )}
        <br />
        {!loading && !error && active === 2 && (
          <AnsBard ans={ansFile.ans_gemini} />
        )}
      </Box>
    </>
  );
}

export default Home;
