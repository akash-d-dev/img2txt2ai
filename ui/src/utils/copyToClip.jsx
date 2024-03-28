import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import DoneIcon from "@mui/icons-material/Done";
import { IconButton } from "@mui/material";
import { useState } from "react";

const CopyToClipBtn = ({ active, quesFile, ansFile }) => {
  const [copying, setCopying] = useState(false);

  const copyToClipboard = (text) => {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
  };

  const handleCopy = () => {
    setCopying(true);
    setTimeout(() => {
      setCopying(false);
    }, 500);
    if (active === 0) copyToClipboard(quesFile.qna_prompt);
    if (active === 1) copyToClipboard(ansFile.ans_gpt);
    if (active === 2) copyToClipboard(ansFile.ans_gemini);
    if (active === 3) copyToClipboard(ansFile.ans_gemini_img);
    if (active === 4) copyToClipboard(quesFile.qna);
  };

  return (
    <IconButton
      onClick={handleCopy}
      sx={{
        position: "fixed",
        bottom: "70px",
        left: "80%",
        zIndex: "100",
        bgcolor: "#585858",
        p: 2.5,
        mx: 0.5,
        mt: 2,
        width: 30,
        height: 30,
      }}
    >
      {copying ? <DoneIcon /> : <ContentCopyIcon />}
    </IconButton>
  );
};

export default CopyToClipBtn;
