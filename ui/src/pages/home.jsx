import { Box, Button, IconButton } from '@mui/material';
import axios from 'axios';
import { useEffect, useState, useRef } from 'react';
import Ques from '../components/Ques';
import AnsGpt3 from '../components/AnsGpt3';
import AnsBard from '../components/AnsBard';
import ContentPasteGoIcon from '@mui/icons-material/ContentPasteGo';
import AutorenewIcon from '@mui/icons-material/Autorenew';
import InputBox from "../components/Input";
import useScrollTrigger from "@mui/material/useScrollTrigger";
import BacktoTop from "../utils/backToTop";
import CopyToClipBtn from "../utils/copyToClip";

function Home() {
  // const url = "http://localhost:8888";
  const url = "https://bjn18spw-8888.inc1.devtunnels.ms";
  // const url = process.env.REACT_APP_API_URL;
  const trigger = useScrollTrigger();
  const [active, setActive] = useState(0);
  const [quesFile, setQuesFile] = useState({
    qna: "",
    qna_prompt: "",
  });
  const [ansFile, setAnsFile] = useState({
    ans_gpt: "",
    ans_gemini: "",
    ans_gemini_img: "",
  });
  const [copying, setCopying] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [inputBox, setInputBox] = useState(false);

  const buttonContainerStyle = {
    position: "absolute",
    top: "12px",
    transform: "translateX(-0%)",
    display: "flex",
    gap: "10px",
    width: "55px !important",
    minWidth: "55px !important",
  };

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await axios.get(url);
      setQuesFile({
        qna: response.data.paste_content,
        qna_prompt: response.data.qna_content,
      });
      setAnsFile({
        ans_gpt: response.data.ans_content_gpt,
        ans_gemini: response.data.ans_content_gemini,
        ans_gemini_img: response.data.ans_content_gemini_img,
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
      await axios.post(url, {
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
    <Box className='wrapper'>
      {trigger && <BacktoTop />}
      <CopyToClipBtn active={active} quesFile={quesFile} ansFile={ansFile} />
      <Box
        display={"flex"}
        position={"sticky"}
        top={0}
        zIndex={100}
        bgcolor={"#000"}
        pb={1.5}
        width={"100%"}
      >
        <IconButton
          disabled={loading}
          color='primary'
          onClick={fetchData}
          sx={{
            mx: 0.5,
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
          color={active === 0 ? "secondary" : "primary"}
          disableElevation
          disableTouchRipple
          sx={{ ...buttonContainerStyle, left: 82 }}
          onClick={() => setActive(0)}
        >
          Ques
        </Button>
        <Button
          variant='contained'
          color={active === 1 ? "secondary" : "primary"}
          disableElevation
          disableTouchRipple
          sx={{ ...buttonContainerStyle, left: 142 }}
          onClick={() => setActive(1)}
        >
          Gpt3
        </Button>
        <Button
          variant='contained'
          color={active === 2 ? "secondary" : "primary"}
          disableElevation
          disableTouchRipple
          sx={{ ...buttonContainerStyle, left: 202 }}
          onClick={() => setActive(2)}
        >
          Bard
        </Button>
        <Button
          variant='contained'
          color={active === 3 ? "secondary" : "primary"}
          disableElevation
          disableTouchRipple
          sx={{ ...buttonContainerStyle, left: 262 }}
          onClick={() => setActive(3)}
        >
          Img
        </Button>
        <Button
          variant='contained'
          color={active === 4 ? "secondary" : "primary"}
          disableElevation
          disableTouchRipple
          sx={{ ...buttonContainerStyle, left: 322 }}
          onClick={() => setActive(4)}
        >
          Raw
        </Button>
      </Box>
      {inputBox && (
        <InputBox sendTexttoServer={sendTexttoServer} loading={loading} />
      )}

      <Box display={"flex"} mt={2} mb={12} mx={1}>
        {loading ? "Loading..." : error && `Someting went wrong:${error}`}
        {!loading && !error && active === 0 && (
          <Ques ques={quesFile.qna_prompt} />
        )}
        <br />
        {!loading && !error && active === 1 && (
          <AnsGpt3 ans={ansFile.ans_gpt} />
        )}
        <br />
        {!loading && !error && active === 2 && (
          <AnsBard ans={ansFile.ans_gemini} />
        )}
        <br />
        {!loading && !error && active === 3 && (
          <AnsBard ans={ansFile.ans_gemini_img} />
        )}
        <br />
        {!loading && !error && active === 4 && <Ques ques={quesFile.qna} />}
      </Box>
    </Box>
  );
}

export default Home;
